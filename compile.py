import json
from pandas import DataFrame, json_normalize
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import os
path = os.path.dirname(os.path.realpath(__file__))


with open('/home/borady/Documents/tagaddod/tagaddod-d8ffe--MsZkGFSCtYxntenMuVF-export.json', 'r') as f:
  data1 = json.load(f)

with open('/home/borady/Documents/tagaddod/tagaddod-d8ffe--MszT9RZtTjcM5PwTCBH-export.json', 'r') as f:
  data2 = json.load(f)
  
with open('/home/borady/Documents/tagaddod/tagaddod-d8ffe--MwWeqpG3yuQD7G2wcp8-export.json', 'r') as f:
  data3 = json.load(f)

with open('/home/borady/Documents/tagaddod/tagaddod-d8ffe--N4SUsENXI1OF1qf8VxT-export.json', 'r') as f:
  data4 = json.load(f)


df1 = DataFrame.from_dict(data4, orient='index')
df1 = df1.astype({"latitude": float, "longitude": float})

df1.dropna(subset=['longitude','latitude'],inplace=True)

# df1.drop('meta-data',inplace=True)
print(df1)

geomtry = [Point(xy) for xy in zip(df1['longitude'], df1['latitude'])]
gdf = GeoDataFrame(df1, geometry=geomtry)
print(gdf)

gdf.to_csv(path+f"/csv/gdf4",index=False)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
egypt = world.loc[world.name=='Egypt']
gdf.plot(ax=egypt.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)

# plt.scatter(x=df1['longitude'], y=df1['latitude'])
plt.show()