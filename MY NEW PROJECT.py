import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('')
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns.to_list)
print(df.describe())
print(df.describe(include='all'))

print(df.duplicated().sum())
print(df.isnull().sum())