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

# plot roads
drive_net = osm.get_network(network_type="driving")

for road in drive_net.itertuples(index=True, name='Roads'):
    print(road.name) # Road Name 16

