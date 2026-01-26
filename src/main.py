#!/usr/bin/env python3
# trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled,timepoint
import os
import csv
from enum import IntEnum

ROOT_FILES = "/home/garry/documents/ppt/Time"
OCT_TIMES_CSV = os.path.join(ROOT_FILES, "October_16_2025/stop_times.txt")
JAN_TIMES_CSV = os.path.join(ROOT_FILES, "January_26_2025/stop_times.txt")

class TimeField(IntEnum):
    TRIP_ID = 0
    ARRIVAL_TIME = 1
    DEPARTURE_TIME = 2
    STOP_ID = 3
    STOP_SEQUENCE = 4
    STOP_HEADSIGN = 5
    PICKUP_TYPE = 6
    DROP_OFF_TYPE = 7
    SHAPE_DIST_TRAVELED = 8
    TIMEPOINT = 9

class StopNode:
    def __init__(self):
        self.oldtime = None
        self.newtime = None
        self. = None

def add_to_routes(routes, line, old_or_new):
    time = line[TimeField.ARRIVAL_TIME]
    stop_id = line[TimeField.STOP_ID]
    stop_headsign = line[TimeField.STOP_HEADSIGN]
    stop_sequence = line[TimeField.STOP_SEQUENCE]

    routes[stop_headsign] = routes.get(stop_headsign, {'old':{}, 'new':{}})
    routes[stop_headsign][old_or_new].append(time)

def sort_route(routes, route):


def print_route(routes, route):
    old_sorted = sorted(routes[route]['old'])
    new_sorted = sorted(routes[route]['new'])

    for i in range(min(len(old_sorted), len(new_sorted))):
        print(f"{route}: {old_sorted[i]} - {new_sorted[i]}")
    
    
def main():
    routes = dict()

    with open(OCT_TIMES_CSV, "r") as oct_file:
        oct_reader = csv.reader(oct_file, delimiter=",")
        for row in oct_reader:
            add_to_routes(routes, row, 'old')


    with open(JAN_TIMES_CSV, "r") as jan_file:
        jan_reader = csv.reader(jan_file, delimiter=",")
        for row in jan_reader:
            add_to_routes(routes, row, 'new')


    for route in routes:
        print_route(routes, route)


if __name__ == '__main__':
    main()
