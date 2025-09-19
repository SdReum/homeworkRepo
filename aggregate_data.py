import pandas as pd

all_data = [1.7, 0.5, None]
data_sum = pd.Series(all_data).sum(skipna=None)
print(data_sum)
count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')