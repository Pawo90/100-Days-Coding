from math import *



def calc(a_lat, a_lon, b_lat, b_lo):
    # Radius of earth
    R = 6371.0
    # altitude of ISS (average 412)
    h = 412.0

    b_lat_rad = float(b_lat) * pi / 180
    b_lon_rad = float(b_lo) * pi / 180
    a_lat_rad = a_lat * pi / 180
    a_lon_rad = a_lon * pi / 180

    # Calculate azimut bearing to ISS - b
    x = cos(b_lat_rad) * sin(b_lon_rad - a_lon_rad)
    y = cos(a_lat_rad) * sin(b_lon_rad) - sin(a_lat_rad) * cos(b_lat_rad) * cos(b_lon_rad-a_lon_rad)
    b = atan2(x, y)
    b = b * 180 / pi
    # print(f"Bearing to ISS: {b}°")

    # calculate straight line distance to nadir
    x_a = R * cos(a_lat_rad) * cos(a_lon_rad)
    y_a = R * cos(a_lat_rad) * sin(a_lon_rad)
    z_a = R * sin(b_lon_rad)

    x_b = R * cos(b_lat_rad) * cos(b_lon_rad)
    y_b = R * cos(b_lat_rad) * sin(b_lon_rad)
    z_b = R * sin(b_lon_rad)
    dist_to_nadir = sqrt((x_b - x_a)**2 + (y_b - y_a)**2 + (z_b - z_a)**2)

    # Calculate psi - angle from observer to the ISS
    psi = 2 * asin(dist_to_nadir/(2*R))

    # Calculate distance from observer to ISS
    distance_to_iss = sqrt((h + R)**2 + R**2 - 2*(h + R) * R * cos(psi))

    # Calculate alfa - angle from obsever to ISS
    iss_angle = (180/pi) * asin((h + R)*(sin(psi)/distance_to_iss))

    dist_to_nadir = round(dist_to_nadir, 2)
    print(f"Distance from observer do nadir: {dist_to_nadir}[km]")

    distance_to_iss = round(distance_to_iss, 2)
    print(f"Distance from observer to ISS: {distance_to_iss}[km]")

    iss_angle = round(iss_angle, 2)
    print(f"Angle to ISS: {iss_angle}")

