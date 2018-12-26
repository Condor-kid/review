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

完备性、最优性：Yes

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

## Uniform cost 一致代价搜索

边界顺序由代价(cost)决定，永远扩展代价最小的路径

完备性、最优性：Yes

C*：最优结果的代价  $\epsilon$：每一步的代价

时间、空间复杂度：$O(b^{C^* / \epsilon+1})$

## Depth-limited search 深度受限搜索

设置的深度：L

![1545786261445](assets/1545786261445.png)

## Iterative deepening search 迭代加深搜索

初始令L=0，并逐渐增大L

![1545786514144](assets/1545786514144.png)

时间复杂度：$O(b^d)$

空间复杂度：$O(bd)$

## Bidirectional search 双向搜索

![1545786624521](assets/1545786624521.png)

#### 无信息搜索总结

![1545786732055](assets/1545786732055.png)

(BFS中的空间和时间改为$O(b^{d+1})$)



# path checking / cycle checking 路径检测/环检测

## 路径检测

通向c的路径：$<n_1, \cdots, n_k, c>$

则c不能与$n_i$相同

![1545787614670](assets/1545787614670.png)

## 环检测

在整个探索过程中记录结点，确保扩展的结点c不与之前任何状态中的结点相同

![1545788138297](assets/1545788138297.png)

## 总结

![1545788281615](assets/1545788281615.png)

