#!/usr/bin/env python3
# trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled,timepoint
import os
import csv
from enum import IntEnum

OCT_TIMES_CSV = os.path.relpath("../October_16_2025/stop_times.txt")
JAN_TIMES_CSV = os.path.relpath("../January_26_2026/stop_times.txt")

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

def add_to_routes(routes, line, old_or_new):
    time = line["arrival_time"]
    stop_id = line["stop_id"]
    stop_headsign = line["stop_headsign"]
    stop_sequence = line["stop_sequence"]

    if stop_headsign not in routes:
        routes[stop_headsign] = dict({'old':list(), 'new':list()})
    routes[stop_headsign][old_or_new].append(time)

def sort_route(routes, route):
    return None

def print_route(routes, route):
    old_sorted = sorted(routes[route]['old'])
    new_sorted = sorted(routes[route]['new'])

    for i in range(min(len(old_sorted), len(new_sorted))):
        if (old_sorted[i] != new_sorted[i]):
            print(f"{route}: {old_sorted[i]} - {new_sorted[i]}")
    
    
def main():
    routes = dict()

    with open(OCT_TIMES_CSV, "r") as oct_file:
        oct_reader = csv.DictReader(oct_file, delimiter=",")
        for row in oct_reader:
            add_to_routes(routes, row, 'old')


    with open(JAN_TIMES_CSV, "r") as jan_file:
        jan_reader = csv.DictReader(jan_file, delimiter=",")
        for row in jan_reader:
            add_to_routes(routes, row, 'new')


    for route in routes:
        print_route(routes, route)


if __name__ == '__main__':
    main()
