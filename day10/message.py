import matplotlib.pyplot as plt
import re
import time
plt.style.use('seaborn-whitegrid')

coord_re = re.compile(r'position=<(?P<x_coord>(\s|-)\d+), '
                       r'(?P<y_coord>(\s|-)\d+)> '
                       r'velocity=<(?P<x_vel>(\s|-)\d+), '
                       r'(?P<y_vel>(\s|-)\d+)>'
 )

def parse_coord(coord_string):
    m = coord_re.match(coord_string)
    return {k: int(v) for k, v in m.groupdict().items()}

def parse_input(input):
    x_coords = []
    y_coords = []
    x_vels = []
    y_vels = []
    with open(input) as fh:
        for line in fh.readlines():
            coord = parse_coord(line)
            x_coords.append(int(coord['x_coord']))
            y_coords.append(int(coord['y_coord']))
            x_vels.append(int(coord['x_vel']))
            y_vels.append(int(coord['y_vel']))
        return x_coords, y_coords, x_vels, y_vels

x_coords, y_coords, x_vels, y_vels = parse_input('/Users/jeorryb/Dropbox/Advent_of_Code_2018/day10/input.txt')

def step_through(xvels, yvels, xcoords, ycoords):
    for x in range(15000):
        for i in range(len(x_coords)):
            xcoords[i] = xcoords[i] + xvels[i]
            ycoords[i] = ycoords[i] + yvels[i]
    plt.plot(xcoords, ycoords, '.')
    plt.show()
        
        

step_through(x_vels, y_vels, x_coords, y_coords)
