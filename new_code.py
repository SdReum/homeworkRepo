import pandas as pd
df = pd.DataFrame([
  ["g", "g0"],
  ["g", "g1"],
  ["g", "g2"],
  ["g", "g3"],
  ["h", "h0"],
  ["h", "h1"]
], columns=["A", "B"])
print(df.groupby("A").nth[1:-1])


# sum = 0
# def f(sum):
#     for y in range(10000000):
#         sum += 1 / (1 + y) ** 2
#         if y == 9999:
#             print(sum)
#             return
#         if sum >= 1.644:
#             print(sum,y)

# f(sum)
# s = 'aahАhff Амhsshsrм'
# print(s[:s.index('h')]+s[s.rindex('h')+1:])