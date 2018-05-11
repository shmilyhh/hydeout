---
layout: post
title: Reduction
---

This section presents how to use reduction algorithm to solve the problem.

- #### Trapping Rain Water
    - [Original Problem](https://www.lintcode.com/problem/trapping-rain-water/description)
    - Solutions
        1. left and right scan
            - notes: traverse the list three times.
                1. from left to right, record the highest at each index.
                2. from right to left, record the highest at each index.
                3. from left to right, calculate the trapped water at the index based on the condition: 
                ```python
                total = total + height[index] - min(leftHeight[index], rightHeight[index]) ? height[index] - min(leftHeight[index], rightHeight[index]) : 0
                ```
        2. reduction:
            - notes: from n -> n-1.
                1. using two pointers to implement it.
                2. maintaining the final height at each index, final height = original height + trapped water height. The leftmost and rightmost final height are already known.
                3. starting first from lower side, since the higher side can hold water for lower side. Then update the adjacent final height.
                4. calculating the trapped water based on the condition: 
                ```java
                total = total + height[index] - height[index+1] ? height[index] - height[index+1] : 0
                ````

- #### Trapping Rain Water II
    - [Original Problem](https://www.lintcode.com/problem/trapping-rain-water-ii/)
    - Solutions
        - reduction: from n -> n-1
            1. maintain the minimum heap to store the height of visited index
            2. 4 boundaries' final height are known
            3. starting from minimum height index 