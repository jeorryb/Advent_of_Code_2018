import re
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

coord_re = re.compile(r'position=<(?P<x_coord>(\s|-)\d+), '
                       r'(?P<y_coord>(\s|-)\d+)> '
                       r'velocity=<(?P<x_vel>(\s|-)\d+), '
                       r'(?P<y_vel>(\s|-)\d+)>'
 )

def parse_coord(coord_string):
    m = coord_re.match(coord_string)
    return {k: int(v) for k, v in m.groupdict().items()}

def parse_input(input):
    positions = []
    velocities = []
    with open(input) as fh:
        for line in fh.readlines():
            coord = parse_coord(line)
            positions.append([int(coord['x_coord']), int(coord['y_coord'])])
            velocities.append([int(coord['x_vel']), int(coord['y_vel'])])
        positions = np.array(positions)
        velocities = np.array(velocities)
        return positions, velocities

# with open("input.txt", "r") as fp:
#     for l in fp.readlines():
#         px, py, vx, vy = parse(fmt_string, l)
#         positions.append([px, py])
#         velocities.append([vx, vy])
# positions = np.array(positions)
# velocities = np.array(velocities)
positions, velocities = parse_input('/Users/jeorryb/Dropbox/Advent_of_Code_2018/day10/input.txt')

def min_func(t):
    global positions
    global velocities
    new_pos = positions + t * velocities
    y_std = np.std(new_pos[:, 1])
    return y_std

pars = (0)
min_results = optimize.minimize(min_func, pars)
time = np.round(min_results['x'])
print(f"Time is {time} steps.")

best_pos = positions + time * velocities
plt.scatter(best_pos[:, 0], best_pos[:, 1])
plt.gca().invert_yaxis()
plt.show()