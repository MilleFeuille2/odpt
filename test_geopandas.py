# -*- coding:utf-8 -*-

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shapely

# pandas.DataFrameを継承したgeopandas.GeoDataFrameインスタンスとなる
df = gpd.read_file('../land/tokyo.geojson')

print(df.head())
print(df.columns)

df.to_csv('../csv/tokyo.csv')

# 他に、Toshobuがある
ax = df[(df['area_en'] == 'Tama') |
        (df['area_en'] == 'Tokubu')].plot()

plt.show()
