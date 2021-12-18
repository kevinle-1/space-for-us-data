# print(drive_net.head(2))

# with open('roads.txt', 'w') as o:
#     o.writelines(drive_net.to_string())

# print(drive_net.to_string())

#plot = drive_net.plot(color="k", figsize=(24, 24), lw=0.2, alpha=0.6)

# boundaries = osm.get_boundaries()
# plot = boundaries.plot(facecolor="none", edgecolor="blue")

# save output
#fig = plot.get_figure()
#fig.savefig("output-can.png")


# buildings = osm.get_buildings()
# buildings.plot()

# draw boundaries
# bound = osm.get_boundaries(boundary_type='administrative')
# bound.plot()

# # get shapely geometry
# geo_bound = bound['geometry'].values[0]

# # init new OSM parser object with boundary
# osm = OSM(fp, bounding_box=geo_bound)
# osm.bounding_box