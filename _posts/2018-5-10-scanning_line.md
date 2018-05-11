---
layout: post
title: Scanning Line
---

This section presents how to use scanning line to solve the problem.

- #### The Skyline Problem
    - [Original Problem](https://www.lintcode.com/problem/the-skyline-problem/description)
    - Solutions
        - scanning line
            1. recording each edge information: use tuple or class to store the (x, height, index), since the change happened at each edge.
            2. storing them based on x and traverse them one by one.
            3. maintaining the highest height at each edge.