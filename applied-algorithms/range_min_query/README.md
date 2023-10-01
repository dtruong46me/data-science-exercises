
## Description

Given a sequence of n integers $a_0, a_1,...a_n$
. We denote $rmq(i,j)$ the minimum element of the sequence $a_i, a_{i+1}, . . .,a_j$. Given `m` pairs $(i_1, j_1),. . .,(i_m, j_m)$, compute the sum $Q = rmq(i_1,j_1) + . . . + rmq(i_m, j_m)$

**Input**

- Line 1: n $(1 \leq n \leq 10^6)$
- Line 2: $a_0, . . . ,a_{n-1}$ $(1  \leq  a_i \leq 10^6)$
- Line 3: m $(1 \leq m \leq 10^6)$
- Line k+3: $(k=1, . . ., m)$: $i_k, j_k$ $(0 \leq i_k < j_k < n)$

**Output**

Write the value **Q**

## Example

**Input**

16

2 4 6 1 6 8 7 3 3 5 8 9 1 2 6 4
4

1 5

0 9

1 15

6 10

**Output**

6