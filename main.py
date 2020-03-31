from typing import List


class Solution:

  def generate(self, currentPath: str, open: int, close: int,
               ans: List[str]) -> List[str]:
    if open == 0 and close == 0:
      return ans + [str(currentPath)]

    ans1, ans2 = [], []
    if open >= close:
      ans1 = self.generate(currentPath + '(', open - 1, close, ans)
    else:  #if open < close:
      if open > 0:
        ans1 = self.generate(currentPath + '(', open - 1, close, ans)
      if close > 0:
        ans2 = self.generate(currentPath + ')', open, close - 1, ans)

    return ans1 + ans2

  def generateParenthesis(self, n: int) -> List[str]:

    return self.generate('', n, n, [])


my = Solution()
n = 3
ans = my.generateParenthesis(n)
print("ans", ans)

# n = 3

# (((

# 0 -> 1 -> 2
# 0 <- 1 <- 2
# ((()))

# 0 -> 1
# 0 <- 1
# (())
# 0 -> 2
# 0 <- 2
# (()())

# 0 -> 1
# 0 <- 1

# (())

# ((()))
# 111000
# (()())
# 110100
# (())()
# 110010

# ((
# 2,0
# (())
# 2,2

# SHOULD WORK =))))
# (((  )))  path = ''
#   ((  )))  path = '('
#     ((  ))  path = '()'
#     (  )))  path = '(('
#       _  )))  path = '((('
#       (  ))   path = '(()'
#         _  )))  path = '(()('
#         (  )    path = '(())'
#           _  )  path = '(())('
#             _  _  path = '(())()'
