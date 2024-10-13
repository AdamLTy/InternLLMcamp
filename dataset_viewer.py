import pandas as pd
file_path = 'DynamicSnakeConvolution.parquet'
df = pd.read_parquet(file_path)
print(df.columns)