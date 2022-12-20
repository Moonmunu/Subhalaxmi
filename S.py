import pandas as pd
from numpy import empty
import os

file_path='calar.tsv'
if os.stat(file_path).st_size==0:
    print("File is empty")
    df=empty
else:
   df=pd.read_csv('calar.tsv', sep='\t')
   last_col=df.iloc[: ,-1]
   print(last_col.sort_values())