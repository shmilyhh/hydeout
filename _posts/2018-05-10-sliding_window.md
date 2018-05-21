---
layout: post
title: Sliding Windows
---

This section includes the tricks that handle the sliding windows.

- #### Sliding Window Maximum

    - [Original Problem](https://www.lintcode.com/problem/sliding-window-maximum/description)
    - Notes
        1. maintain a monotonically decreasing queue: from current to left pop left element that is less than the current element
        2. use deque data structure to implement it, since it supports pop and append left and right functions
        3. store the index of data in queue, since the size of the queue could be less than window size, we need to decide whether the leftmost element is out of window based on the condition: leftmost index <= current index - window size

- #### Sliding Window Matrix Maximum

    - Original Problem
        - Given an array of n * m matrix, and a moving matrix window (size k * k), move the window from top left to bottom right at each iteration, find the maximum sum inside the window at each moving. Return 0 if the answer does not exist.
    - Notes
        1. calculate the sums[i][j] of the matrix, sums[i][j] represents the sum of all elements in matrix with row from 0 to i-1 and row from 0 to j-1. The formula is sums[i][j] = matrix[i-1][j-1] + sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1]. The total size of sums is rows+1 x cols +1
        2. calculate the value of matrix with row from i to i+k and column from j to j+k. The formula is sums[i][j] - sums[i][j-k] - sums[i-k][j] + sums[i-k][j-k].
        3. store the maximum value at each iteration