
## Description

Given the n x m rectangle which divided into 1 x 1 square with 2 colors: **black** and **white**. The rectangle is represented by the matrix A(n,m) where A(i,j) = 1 if the square at $i^{th}$ row, $j^{th}$ column is black, and A(i,j) = 0 show that the square is white.

Find the sub-rectangle of the given rectangle which its cell is black having the maximum area.

**Input**
- The first line: 2 integers `n` and `m` $(1 \leq n,m \leq 1000) $
- The $i+1$ line $(i=1,..n)$: include the $i^{th}$ of the matrix A

**Output**
- Print the maximum area of the sub-rectangle

## Example:
**Input**

4 4

0 1 1 1

1 1 1 0

1 1 0 0

1 1 1 0

**Output**

6