from math import sin, cos, sqrt, atan2, radians

def distLatLon(lat1, lon1, lat2, lon2):
# approximate radius of earth in km
    R = 6373.0


    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
if __name__ == "__main__": 
    lat1 = radians(52.2296756)
    lon1 = radians(21.0122287)
    lat2 = radians(52.406374)
    lon2 = radians(16.9251681)
    print(distLatLon(lat1, lon1, lat2, lon2))

