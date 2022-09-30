
import sys

input_args = sys.argv

GEO_DATA_FILE = input_args[1]

import csv
from math import sin, cos, sqrt, atan2, radians

def distance_between_two_locations(lat1, lng1, lat2, lng2):
    R = 6373.0

    lat1 = radians(float(lat1))
    lon1 = radians(float(lng1))
    lat2 = radians(float(lat2))
    lon2 = radians(float(lng2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def find_shortest_distance(location, location_list):
    shortest_distance = 100000000000000000
    shortest_location = location
    for loc in location_list:
        distance = distance_between_two_locations(location[0], location[1], loc[0], loc[1])
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_location = loc
    return shortest_distance, shortest_location

with open(GEO_DATA_FILE, 'r') as geo_data_file:
    user_ids = list()
    reader = [i for i in csv.reader(geo_data_file)]
    reader.pop(0)

    all_locations = list()
    sorted_locations = list()
    
    for row in reader:
        row_id = row[0]
        lat = row[1]
        lng = row[2]
        all_locations.append((lat, lng, row_id))

    location_len = len(all_locations)
    current_location = all_locations[0]
    
    
    with open(input_args[2], mode='w') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Adding the first location
        writer.writerow(['lat', 'lng', 'id', 'distance'])
        writer.writerow([current_location[0], current_location[1], current_location[2], 0])

        print("Processing rows - Remaining")
        i = 0
        while i < 10:
            try:
                all_locations.remove(current_location)
                shortest_distance, shortest_location = find_shortest_distance(current_location, all_locations)
                current_location = shortest_location
                # Adding lat, lng
                current_lat = current_location[0]
                current_lng = current_location[1]
                row_id = current_location[2]
                writer.writerow([current_lat, current_lng, row_id, shortest_distance])
                # print(current_location, shortest_location, shortest_distance)
                print(len(all_locations))
                i = i+1
            except ValueError:
                break

    print("Output file", str(input_args[2]))