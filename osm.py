from pyrosm import OSM, get_data
from pyrosm.data import sources 

PBF_DIRECTORY_NAME = "cities"

#print(sources.cities.available)

# download dataset 
fp = get_data("perth", directory=PBF_DIRECTORY_NAME)

# https://github.com/HTenkanen/pyrosm/issues/153

# init OSM parser object
osm = OSM(fp)

# plot roads 
drive_net = osm.get_network(network_type="driving")
plot = drive_net.plot(color="k", figsize=(24, 24), lw=0.2, alpha=0.6)

# boundaries = osm.get_boundaries()
# plot = boundaries.plot(facecolor="none", edgecolor="blue")

# save output 
fig = plot.get_figure()
fig.savefig("output.png")


# buildings = osm.get_buildings()
# buildings.plot()

# print(osm)

# faulthandler.enable()
# routes = ["bus", "ferry", "railway", "subway", "train", "tram", "trolleybus"]
# rails = ["tramway", "light_rail", "rail", "subway", "tram"]
# bus = ['yes']

# transit = osm.get_data_by_custom_criteria(custom_filter={
#                                         'route': routes,
#                                         'railway': rails,
#                                         'bus': bus,
#                                         'public_transport': True},
#                                         # Keep data matching the criteria above
#                                         filter_type="keep",
#                                         # Do not keep nodes (point data)    
#                                         keep_nodes=False, 
#                                         keep_ways=True, 
#                                         keep_relations=True)

#transit.plot()


# draw boundaries 
# bound = osm.get_boundaries(boundary_type='administrative')
# bound.plot()

# # get shapely geometry 
# geo_bound = bound['geometry'].values[0]

# # init new OSM parser object with boundary 
# osm = OSM(fp, bounding_box=geo_bound)
# osm.bounding_box