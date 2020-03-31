from typing import List


class Solution:

  def generate(self, currentPath: str, open: str, close: str,
               ans: List[str]) -> List[str]:
    if len(open) == 0 and len(close) == 0:
      return ans + [str(currentPath)]

    ans1 = []
    ans2 = []
    if len(open) >= len(close):
      ans1 = self.generate(currentPath + '(', open[1:], close[:], ans)
    if len(open) < len(close):
      if len(open) > 0:
        ans1 = self.generate(currentPath + '(', open[1:], close[:], ans)
      if len(close) > 0:
        ans2 = self.generate(currentPath + ')', open[:], close[1:], ans)

    return ans1 + ans2

  def generateParenthesis(self, n: int) -> List[str]:
    open = '(' * n
    close = ')' * n

    return self.generate('', open, close, [])


my = Solution()
n = 7
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
