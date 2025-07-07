import geopandas as gpd

shapefile = "/home/disk/rocinante/vickyye/data/raw/reference_gauges/gagesII_9322_sept30_2011.shp"
gdf = gpd.read_file(shapefile)

# Filter to Washington reference gages
reference_WA = gdf[(gdf['STATE'] == 'WA') & (gdf['CLASS'] == 'Ref')]

# Extract unique station IDs
station_ids = reference_WA['STAID'].unique()

print(station_ids)

with open('../data/raw_data/processed_data/site_codes_ref.txt', 'w') as f:
    for sid in station_ids:
        f.write(f"{sid}\n")