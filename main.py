import numpy as np
import pandas as pd

data_02 = pd.read_csv('東京23区推移0409_2月.csv')
data_03 = pd.read_csv('東京23区推移0409_3月.csv')
data_04 = pd.read_csv('東京23区推移0409_4月.csv')

data_all = pd.concat([data_02, data_03.iloc[:, 2:], data_04.iloc[:, 2:]], axis=1)

data_all.head()