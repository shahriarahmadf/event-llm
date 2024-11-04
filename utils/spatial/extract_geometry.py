import json
from shapely.geometry import Point, MultiPolygon, Polygon
import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt

# Define a function to safely extract coordinates or create geometry
def extract_geometry(geo_json_str):
    try:
        geo_dict = json.loads(geo_json_str)
        if 'coordinates' in geo_dict:
            coords = geo_dict['coordinates']
            if geo_dict['type'] == 'Point' and len(coords) == 2:
                return Point(coords)  # Return Point geometry
            elif geo_dict['type'] == 'MultiPolygon':
                # Convert to MultiPolygon
                polygons = [Polygon(polygon[0]) for polygon in coords if len(polygon) > 0]
                return MultiPolygon(polygons) if polygons else None
        return None  # Invalid geometry type
    except (json.JSONDecodeError, TypeError, ValueError):
        return None  # Handle parsing errors