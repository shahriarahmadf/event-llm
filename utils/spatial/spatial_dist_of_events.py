from utils.spatial.extract_geometry import extract_geometry
import geopandas as gpd 
import contextily as ctx 
import matplotlib.pyplot as plt 
def spatial_dist_of_events(df, events_dataframe_name='events'):
    df['geometry'] = df['GEO'].apply(extract_geometry)

    # Filter out rows with missing or invalid geometries
    valid_locations = df.dropna(subset=['geometry'])

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(valid_locations, geometry='geometry')

    # Set the original CRS (WGS84 - EPSG:4326)
    gdf.set_crs(epsg=4326, inplace=True)

    # Convert to Web Mercator (EPSG:3857) for compatibility with contextily basemaps
    gdf = gdf.to_crs(epsg=3857)

    # Plot the points and multipolygons with different colors based on the 'CATEGORY' column
    ax = gdf.plot(column='CATEGORY', cmap='Set1', legend=True, figsize=(20, 14), markersize=3, alpha=0.6)

    # Add a basemap from contextily
    ctx.add_basemap(ax, crs=gdf.crs)

    # Title
    plt.title(f"Spatial distribution of {events_dataframe_name}")

    # Save the figure before displaying it
    plt.savefig(f'../../results/1.2_spatial_distribution/{events_dataframe_name}.PNG', bbox_inches='tight', dpi=300)
    plt.show()