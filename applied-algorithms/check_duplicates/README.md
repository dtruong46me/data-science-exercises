## Description
Given the integer series: $A_1, A_2,...A_n$. For each the number $A_i$, you have to check if the number $A_j$ in the series that if $A_i=A_j$ for $j<i$

**Input**
- The first line: `n` $1 \leq n \leq 100,000 $
- The second line: `n` integers: $A_1 A_2 ...A_n$ $1 \leq A_i \leq 1,000,000,000$

**Output**
- Print `n` lines, the $i^{th}$ line print `1` if exist $A_j=A_i$ for $j<i$, otherwise print `0`

## Example
**Input**

5

1 4 3 1 4

**Output**

0

0

0

0

1