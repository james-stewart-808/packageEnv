import numpy as np

def haversine(lon_0, lat_0, lon_1, lat_1):

    lon_0_rad = np.deg2rad(lon_0)
    lat_0_rad = np.deg2rad(lat_0)
    lon_1_rad = np.deg2rad(lon_1)
    lat_1_rad = np.deg2rad(lat_1)
    dif_lon_1_rad = lon_1_rad - lon_0_rad
    dif_lat_1_rad = lat_1_rad - lat_0_rad
    _AVG_EARTH_RADIUS_KM, _NM_CONVERSION = 6371.0088, 0.539956803

    d = np.sin(dif_lat_1_rad * 0.5) ** 2 + np.cos(lat_0_rad) * np.cos(lat_1_rad) * np.sin(dif_lon_1_rad * 0.5) ** 2
    return 2 * _AVG_EARTH_RADIUS_KM * _NM_CONVERSION * np.arcsin(np.sqrt(d))
