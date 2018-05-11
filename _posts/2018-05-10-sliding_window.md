---
layout: post
title: Sliding Windows
---

This section includes the tricks that handle the sliding windows.

- #### Sliding Window Maximum

    - [Original Problem](https://www.lintcode.com/problem/sliding-window-maximum/description)
    - notes
        1. maintain a monotonically decreasing queue: from current to left pop left element that is less than the current element
        2. use deque data structure to implement it, since it supports pop and append left and right functions
        3. store the index of data in queue, since the size of the queue could be less than window size, we need to decide whether the leftmost element is out of window based on the condition: leftmost index <= current index - window size
