from skfem import *
from skfem.models.elasticity import *
from skfem.visuals.matplotlib import draw, plot
from skfem.helpers import dot
from skfem.io import *
import numpy as np

# Problem description: http://solidmechanics.org/Text/Chapter8_6/Chapter8_6.php
def counter(nu = 0.4995, nr=4, nphi=32):
    def create_mesh(a,b, nr, nphi):
        import meshio
        def roll(arr, axis):
            rolled=np.roll(arr, -1, axis)
            return arr.flatten(), rolled.flatten()
        r, phi = np.meshgrid(np.linspace(a,b,(nr+1)), np.linspace(0,2*np.pi,(nphi+1)))
        x, y = r*np.cos(phi), r*np.sin(phi)
        points = np.array([x.flatten(), y.flatten()]).T[0:(nr+1)*nphi,:]
        off, off2 = roll(np.arange(nphi*(nr+1)).reshape(nphi,nr+1)[:,0:nr], 0)
        cells = np.array([off, off2,  off2+1, off+1]).T
        circ, circ2 = roll(np.vstack(((nr+1)*np.arange(nphi), (nr+1)*np.arange(nphi) + nr)), 1)
        bnds = np.array([circ, circ2]).T
        return meshio.Mesh(points, {"quad": cells, "line": bnds},
                           cell_sets={"inner": [np.arange(0),np.arange(nphi)], "outer": [np.arange(0),np.arange(nphi, 2*nphi)]})

    a,b=1.,4.
    E= 2.5
    lam,mu = lame_parameters(E,nu)
    pa,pb=0.33*E,0.0

    m = from_meshio(create_mesh(a,b, nr, nphi))
    m = m.to_meshtri()
    e = ElementVector(ElementTriP2())

    # e = ElementVector(ElementQuadP(2))
    basis = Basis(m, e)
    # 1-st order quadrature:
    #basis = Basis(m, e, quadrature=(np.array([[0.5],[0.5]]), np.array([1.0])))


    K = asm(linear_elasticity(lam,mu), basis)

    def trac_inner(x,y):
        return pa/a * np.array([x, y])

    @LinearForm
    def loadingIn(v,w):
        return dot(trac_inner(*w.x), v)

    inner_basis=FacetBasis(m,e, facets=m.boundaries['inner'])

    f = asm(loadingIn, inner_basis)

    B=np.zeros((3, basis.N))
    # displacement constraint (restrict rigid body motion):
    # sum(u.x) = sum(u.y) = 0
    B[0, basis.nodal_dofs[0]] = 1
    B[1, basis.nodal_dofs[1]] = 1
    # angular moment constraint:
    # dot(rt,u) = 0, rt = (y,-x)
    B[2, basis.nodal_dofs[0]] = basis.doflocs[1, basis.nodal_dofs[0]]
    B[2, basis.nodal_dofs[1]] = -basis.doflocs[0, basis.nodal_dofs[1]]
    A = bmat([[K,B.T],
                [B, None]], 'csr')
    g = np.concatenate( (f, np.zeros(3) ))

    #u=solve(K,f)
    u=solve(A,g)


    def analytic(x,y):
        r=np.sqrt(np.power(x,2)+np.power(y,2))
        ex,ey = x/r, y/r
        c = (1+nu)*(a*b)**2/(E*(b**2-a**2))
        c2 = c*( (pa-pb)/r + (1-2*nu)*(pa*a**2 - pb*b**2)/((a*b)**2) * r )
        return c2*ex, c2*ey


    def visualize(nu, nr, nphi):
        import matplotlib.pyplot as plt
        axi = plt.subplot()
        axi.set_aspect(1)

        u_ex = analytic(*m.p)
        m1 = m.translated(u[basis.nodal_dofs])
        m2 = m.translated(u_ex)
        axi = draw(m1, ax=axi, color='r')
        axi = draw(m2, ax=axi, color='k')
        axi.plot()
        axi.legend(['Finite element', 'Analytics'])
        error = np.max(np.abs(u_ex-u[basis.nodal_dofs]))
        axi.set_title(f"nu = {nu}, nr = {nr}, nphi = {nphi}\nerror={error:.5f}")
        return axi

    visualize(nu, nr, nphi).show()

k = 2
nr_start = 4
nphi_start = 32

for nu in [0.4995,0.3]:
    for i in range(3):
        counter(nu, nr_start*k**i, nphi_start)

    for i in range(3):
        counter(nu, nr_start, nphi_start*k**i)

    for i in range(3):
        counter(nu, nr_start*k**i, nphi_start*k**i)