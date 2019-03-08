import os
import csv

MY_DIR = os.path.realpath(os.path.dirname(__file__))

if_name = 'robot.map.10x10.map'
of_name = 'robot.moves'

def read_map(ifname):
    my_map = []

    with open(ifname, 'r') as inf:
        reader = csv.reader(inf)
        for row in reader:
            # read the rows into the map
