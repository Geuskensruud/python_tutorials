#imports
import pandas as pd
from variables import path, path2

#read the dataframe
df= pd.read_csv(path)

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

schema_df= pd.read_csv(path2)

print(schema_df)