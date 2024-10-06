import pandas as pd
import os

# 假设 df 是你的 DataFrame
# df = ...

# 动态创建路径
base_path = r'E:\python pj\ultralytics-main\runs\detect\CSV'
filename = 'results_class_CSV.csv'
csv_path = os.path.join(base_path, filename)

# 将 DataFrame 保存为 CSV 文件
df.to_csv(csv_path, index=False)
