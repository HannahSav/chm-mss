## 3. Задача Стокса и LBB-условия
Для выполнения задания рекомендуется использование конечно-элементной библиотеки [scikit-fem](https://github.com/kinnala/scikit-fem). Установите эту библиотеку и ознакомьтесь с примерами и документацией.

#### Задание
На основе примера [ex18.py](https://github.com/kinnala/scikit-fem/blob/master/docs/examples/ex18.py) исследуйте поведение различных пар базисных элементов для скорости и давления в задаче Стокса для круглой области $`\Omega = \{(x,y): x^2 + y^2 \le 1\}`$:
```math
- \Delta \mathbf{u} + \nabla p = \mathbf{f} \quad \text{ в } \Omega
```
```math
\nabla \cdot \mathbf{u} = 0 \quad \text{ в } \Omega
```
с граничными условиями $`\mathbf{u} = 0`$ на $`\partial\Omega`$ и правой частью $`\mathbf{f}(x,y) = (0, x)`$.

Исследуйте, какие конечно-элементные пары (не) приводят к возникновению паразитных мод решения в поле давлений (осцилляций), и выделите две "хорошие" (осцилляций нет без регуляризации), одну "очень плохую" (для подавления осцилляций нужен настолько большой коэф-т регуляризации $`\varepsilon`$, что решение регуляризованной задачи значительно отличается от решения исходной), и одну "плохую" (есть осцилляции без регуляризации, для подавления осцилляции нужен $`\varepsilon`$ порядка шага сетки $`h`$).

#### Отчет
Результаты исследований оформите в виде краткого отчета:
- Для каждой "хорошей" пары обьясните, почему данная пара не допускает осцилляций в решении, приведите ссылки на литературу, где доказывается ее устойчивость.
- Для "очень плохой" пары найдите наименьший $`\varepsilon`$, при котором осцилляции не наблюдаются, и покажите, что решение регуляризованной задачи значительно отличается от решения исходной задачи (например, сравнив с решением, полученным с помощью устойчивой конечно-элементной парой).
- Для "плохой" пары исследуйте, достаточно ли брать коэф-т регуляризации, пропорциональный $h^2$, для подавления осцилляций. Для этого сначала найдите наименьший $`\varepsilon`$, для которого осцилляции не наблюдаются, а затем проведите несколько расчетов с одновременным измельчением сетки и уменьшением $`\varepsilon \sim h^2`$.

#### Дополнительное необязательное задание
Проверьте сходимость численного решения к точному решению. Для этого вы можете сами выбрать точное решение в виде некоторого бездивергентного поля $`\mathbf{u}`$ и модифицировать граничные условия и правую часть $`\mathbf{f}`$ в задаче Стокса. При проверке обратите внимание на влияние регуляризации и выбор пар базисных элементов.