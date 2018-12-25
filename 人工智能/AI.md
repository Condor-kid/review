[TOC]

# Search

## formalization（形式化）

1. Formulate a **state space** (形式化状态空间)

   抽象真实问题

2. Formulate **actions** （形式化动作）

   allow one to move between different states

3. Identify the **initial state** （确定初始状态）

4. Identify the **goal** or **desired condition** （确定目标）

5. Formulate heuristic （形式化启发式）

Example：

![1545749255236](assets/1545749255236.png)

# Property of Search 搜索的属性

- **Completeness 完备性**: will the search always find a solution if a solution exists?
- **Optimality 最优性** : will the search always find the least cost solution? (when actions have costs)
- **Time complexity 时间复杂度**: what is the maximum number of nodes than can be expanded or generated?
- **Space complexity 空间复杂度**: what is the maximum number of nodes that have to be stored in memory?

# Uninformed Search 无信息搜索

## Breadth first 宽度优先

将继承者放置到边界末端

example:

![1545751783080](assets/1545751783080.png)

从小到大寻求方案，直到找到答案为止

最大继承数：b

最小解决方案步数：d

时间复杂度：$1 + b + b^2 + \cdots + b^d + b(b^d - 1) = O(b^{d+1})$

空间复杂度：$b(b^d-1) = O(b^{d+1})$

## Depth first 深度优先

将继承者放置到边界前端

example:

![1545753323707](assets/1545753323707.png)

完备性：![1545753543414](assets/1545753543414.png)

最优性：No

最大继承数：b

最小解决方案步数：d

时间复杂度：$O(b^m)$ m是状态空间中最长的路径；若m远远大于d则非常糟糕，但若有多个解往往会比较快

空间复杂度：$O(bm)$ 线性，每次仅探索一条路径