from pyrosm import OSM, get_data
from pyrosm.data import sources
import pandas as pd
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

PBF_DIRECTORY_NAME = "cities"

pd.set_option('display.max_colwidth', None)
#print(sources.cities.available)

# download dataset
fp = get_data("Canberra", directory=PBF_DIRECTORY_NAME)

# https://github.com/HTenkanen/pyrosm/issues/153

# init OSM parser object
osm = OSM(fp)

total_roads = 0
roads_with_width = 0

area = 0.0
length = 0.0

# plot roads
drive_net = osm.get_network(network_type="driving")

try:
    for road in drive_net.itertuples(index=True, name='Roads'):
        if(road.width): # for roads with width data
            area += float(road.width) * float(road.length)
            roads_with_width += 1
        length += float(road.length)
        total_roads += 1
except Exception as e:
    print(f"Error: {e}")

print(area)
print(length)
print(total_roads)
print(roads_with_width)
print(total_roads - roads_with_width)

# Output:
# 137540.2
# 4533967.0
# 36962
# 172
# 36790 < Not many roads with width data - will have to rely heavily on estimates 