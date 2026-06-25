# # 1) Fibonacci Number
# # Pattern:

# # 1D DP / simplest recurrence

# # Real-world equivalent:

# # Population growth / repeated financial projection / recurrence-based forecasting.

# # Used in real life:
# # recurrence modeling
# # basic simulation systems
# # teaching memoization and tabulation
# # Problem:
# # LeetCode: Fibonacci Number
# # Learn:
# # overlapping subproblems
# # memoization
# # tabulation
# # space optimization
# Absolutely. **Fibonacci Number** is the best place to start because it teaches the *core DP mindset* with a tiny recurrence.

# ---

# # 1) Problem statement

# The Fibonacci sequence is:

# * **F(0) = 0**
# * **F(1) = 1**
# * **F(2) = 1**
# * **F(3) = 2**
# * **F(4) = 3**
# * **F(5) = 5**
# * **F(6) = 8**

# So every number after the first two is:

# [
# F(n) = F(n-1) + F(n-2)
# ]

# That means:

# * to get **F(5)**, you need **F(4) + F(3)**
# * to get **F(4)**, you need **F(3) + F(2)**

# and so on.

# ---

# # 2) Real-world way to think about it

# Imagine a system where today’s value depends on the **last 2 days**.

# Example:

# * population growth toy model
# * rabbit growth toy model
# * number of ways to reach a stair if you can jump 1 or 2 steps
# * a simple recurrence-based forecast

# The key DP idea is:

# > **A big answer depends on smaller answers.**

# ---

# # 3) Why Fibonacci is a DP problem

# Because the same subproblems repeat.

# Example for **F(5)**:

# [
# F(5)=F(4)+F(3)
# ]

# Then:

# [
# F(4)=F(3)+F(2)
# ]

# So **F(3)** gets computed multiple times.

# That repetition is the whole reason DP exists.

# ---

# # 4) Recursion tree — why brute force is bad

# If you write plain recursion:

# ```python
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)
# ```

# Then for `fib(5)`:

# ```text
# fib(5)
# ├── fib(4)
# │   ├── fib(3)
# │   │   ├── fib(2)
# │   │   └── fib(1)
# │   └── fib(2)
# └── fib(3)
#     ├── fib(2)
#     └── fib(1)
# ```

# Notice:

# * `fib(3)` is repeated
# * `fib(2)` is repeated

# So recursion works, but it repeats work.

# ---

# # 5) DP idea in one line

# ## Store the answer of a subproblem once, then reuse it.

# That’s all DP is doing here.

# ---

# # 6) Step 1 — Brute force recursion

# ```python
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
# ```

# ### Dry run:

# `fib(4)`:

# * `fib(4) = fib(3) + fib(2)`
# * `fib(3) = fib(2) + fib(1)`
# * `fib(2) = fib(1) + fib(0)`

# Works, but too slow.

# ### Time complexity:

# * **O(2^n)** approximately

# ### Why?

# Because every call creates two more calls.

# ---

# # 7) Step 2 — Memoization (Top-Down DP)

# Now we store answers.

# ## Idea:

# If `fib(4)` has already been calculated once, don’t calculate it again.

# ---

# ## Python code — memoization

# ```python
# def fib(n):
#     memo = {}

#     def dp(x):
#         if x <= 1:
#             return x

#         if x in memo:
#             return memo[x]

#         memo[x] = dp(x - 1) + dp(x - 2)
#         return memo[x]

#     return dp(n)
# ```

# ---

# # 8) How this works

# Suppose `n = 5`.

# We compute:

# * `dp(5)` → needs `dp(4)` and `dp(3)`
# * `dp(4)` → needs `dp(3)` and `dp(2)`
# * once `dp(3)` is computed, next time we just fetch it from `memo`

# So repeated work disappears.

# ---

# # 9) Memoization dry run

# For `fib(5)`:

# ### First time:

# * compute `fib(5)`
# * compute `fib(4)`
# * compute `fib(3)`
# * compute `fib(2)`

# Store:

# ```python
# memo[2] = 1
# memo[3] = 2
# memo[4] = 3
# memo[5] = 5
# ```

# Now if `fib(3)` is needed again, it comes directly from the dictionary.

# ---

# # 10) Memoization complexity

# ### Time:

# * **O(n)**

# ### Space:

# * **O(n)** for recursion + memo

# Because each `fib(i)` is solved only once.

# ---

# # 11) Step 3 — Tabulation (Bottom-Up DP)

# Instead of going from top to smaller subproblems, we build from small to big.

# We know:

# * `fib(0) = 0`
# * `fib(1) = 1`

# Then:

# * `fib(2) = fib(1) + fib(0)`
# * `fib(3) = fib(2) + fib(1)`
# * `fib(4) = fib(3) + fib(2)`

# ---

# ## Python code — tabulation

# ```python
# def fib(n):
#     if n <= 1:
#         return n

#     dp = [0] * (n + 1)
#     dp[0] = 0
#     dp[1] = 1

#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]

#     return dp[n]
# ```

# ---

# # 12) Dry run of tabulation for `n = 6`

# Start:

# ```python
# dp = [0, 1, 0, 0, 0, 0, 0]
# ```

# ### i = 2

# ```python
# dp[2] = dp[1] + dp[0] = 1 + 0 = 1
# ```

# Now:

# ```python
# dp = [0, 1, 1, 0, 0, 0, 0]
# ```

# ### i = 3

# ```python
# dp[3] = dp[2] + dp[1] = 1 + 1 = 2
# ```

# ```python
# dp = [0, 1, 1, 2, 0, 0, 0]
# ```

# ### i = 4

# ```python
# dp[4] = dp[3] + dp[2] = 2 + 1 = 3
# ```

# ```python
# dp = [0, 1, 1, 2, 3, 0, 0]
# ```

# ### i = 5

# ```python
# dp[5] = dp[4] + dp[3] = 3 + 2 = 5
# ```

# ```python
# dp = [0, 1, 1, 2, 3, 5, 0]
# ```

# ### i = 6

# ```python
# dp[6] = dp[5] + dp[4] = 5 + 3 = 8
# ```

# Final:

# ```python
# dp = [0, 1, 1, 2, 3, 5, 8]
# ```

# Answer = `8`

# ---

# # 13) DP state here

# For Fibonacci, the state is very simple:

# ## State:

# ```python
# dp[i] = Fibonacci number at index i
# ```

# ---

# # 14) Transition

# ```python
# dp[i] = dp[i - 1] + dp[i - 2]
# ```

# Because Fibonacci at `i` depends on the previous two Fibonacci numbers.

# ---

# # 15) Base cases

# ```python
# dp[0] = 0
# dp[1] = 1
# ```

# ---

# # 16) Final answer

# ```python
# dp[n]
# ```

# ---

# # 17) Step 4 — Space optimization

# Notice something important:

# To compute `dp[i]`, we only need:

# * `dp[i-1]`
# * `dp[i-2]`

# We do **not** need the whole array.

# So we can store just two variables.

# ---

# ## Python code — optimized

# ```python
# def fib(n):
#     if n <= 1:
#         return n

#     prev2 = 0   # fib(0)
#     prev1 = 1   # fib(1)

#     for i in range(2, n + 1):
#         curr = prev1 + prev2
#         prev2 = prev1
#         prev1 = curr

#     return prev1
# ```

# ---

# # 18) Dry run of optimized version for `n = 6`

# Start:

# ```python
# prev2 = 0
# prev1 = 1
# ```

# ### i = 2

# ```python
# curr = 1 + 0 = 1
# prev2 = 1
# prev1 = 1
# ```

# ### i = 3

# ```python
# curr = 1 + 1 = 2
# prev2 = 1
# prev1 = 2
# ```

# ### i = 4

# ```python
# curr = 2 + 1 = 3
# prev2 = 2
# prev1 = 3
# ```

# ### i = 5

# ```python
# curr = 3 + 2 = 5
# prev2 = 3
# prev1 = 5
# ```

# ### i = 6

# ```python
# curr = 5 + 3 = 8
# prev2 = 5
# prev1 = 8
# ```

# Answer = `8`

# ---

# # 19) Complexity comparison

# ## 1. Brute force recursion

# ```python
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)
# ```

# * **Time:** O(2^n)
# * **Space:** O(n)

# ---

# ## 2. Memoization

# ```python
# def fib(n):
#     memo = {}
#     def dp(x):
#         if x <= 1:
#             return x
#         if x in memo:
#             return memo[x]
#         memo[x] = dp(x-1) + dp(x-2)
#         return memo[x]
#     return dp(n)
# ```

# * **Time:** O(n)
# * **Space:** O(n)

# ---

# ## 3. Tabulation

# ```python
# def fib(n):
#     if n <= 1:
#         return n
#     dp = [0]*(n+1)
#     dp[0], dp[1] = 0, 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
# ```

# * **Time:** O(n)
# * **Space:** O(n)

# ---

# ## 4. Space optimized tabulation

# ```python
# def fib(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(2, n+1):
#         a, b = b, a + b
#     return b
# ```

# * **Time:** O(n)
# * **Space:** O(1)

# ---

# # 20) How to identify Fibonacci-style DP

# You should think “Fibonacci-style DP” when:

# * current answer depends on **previous 1 or 2 states**
# * you’re **counting ways**
# * you’re **minimizing cost step by step**
# * you can move by **1 step / 2 step**
# * problem asks for:

#   * number of ways
#   * min cost
#   * max score
#     with transitions from recent states only

# ---

# # 21) Problems that come directly after Fibonacci

# Once Fibonacci makes sense, the next problems should be:

# ## 1. Climbing Stairs

# Why?
# Because it is almost Fibonacci with a story.

# ## 2. Min Cost Climbing Stairs

# Same structure, but now you minimize cost.

# ## 3. House Robber

# Now instead of `i-1` and `i-2` as counts, you do **pick / skip** logic.

# ---

# # 22) Very important DP lesson from Fibonacci

# Every DP problem should be broken into these 5 things:

# ## 1. State

# What does `dp[i]` mean?

# For Fibonacci:

# ```python
# dp[i] = ith Fibonacci number
# ```

# ## 2. Transition

# How is current state formed?

# ```python
# dp[i] = dp[i-1] + dp[i-2]
# ```

# ## 3. Base case

# Known answers:

# ```python
# dp[0] = 0
# dp[1] = 1
# ```

# ## 4. Direction

# * top-down (memoization)
# * bottom-up (tabulation)

# ## 5. Optimization

# Can we reduce space?

# Yes → from array to two variables.

# ---

# # 23) Best Python version to remember in interview

# If they ask Fibonacci, use this:

# ```python
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
        
#         prev2, prev1 = 0, 1
        
#         for _ in range(2, n + 1):
#             curr = prev1 + prev2
#             prev2 = prev1
#             prev1 = curr
        
#         return prev1
# ```

# ---

# # 24) Your practice task now

# Do these in order **right after Fibonacci**:

# 1. **Climbing Stairs**
# 2. **Min Cost Climbing Stairs**
# 3. **House Robber**
# 4. **House Robber II**

# These 4 together will build your first real DP foundation.

# ---

# # 25) What I can do next

# I can continue in the exact same style for the next problem.

# ## Next best step:

# I explain **Climbing Stairs** like this:

# * brute force
# * memoization
# * tabulation
# * space optimization
# * real-world intuition
# * pattern relation with Fibonacci
# * full Python code

# If you want, send **“next: climbing stairs”** and I’ll continue the DP handbook from there.
