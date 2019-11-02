import os
from collections import defaultdict

def parse_input(input):
    with open(input) as fh:
        lines = [line.strip() for line in fh.readlines()]
        return lines

lines = parse_input('/Users/jeorryb/Dropbox/Advent_of_Code_2018/day6/input.txt')

def max_area(lines):
    coords = set()

    for line in lines:
        x, y = line.split(',')
        coords.add((int(x), int(y)))

    max_x = max(coords, key=lambda x: x[0])[0]
    max_y = max(coords, key=lambda x: x[1])[1]

    coord_id_to_point = {coord_id: point for coord_id, point in enumerate(coords, start=1)}
    region_sizes = defaultdict(int)
    infinite_ids = set()

    for i in range(max_x + 1):
        for j in range(max_y +1):
            min_dists = sorted([(abs(x - i) + abs(y - j), coord_id) for coord_id, (x, y) in coord_id_to_point.items()])
            if min_dists[0][0] != min_dists[1][0]:
                coord_id = min_dists[0][1]
                region_sizes[coord_id] += 1

                if i == 0 or i == max_x or j == 0 or j == max_y:
                    infinite_ids.add(coord_id)
    max_ar = max(size for coord_id, size in region_sizes.items() if coord_id not in infinite_ids)
    print(f'The max area is {max_ar}')

def coord_safe(lines, m_limit=10000):
    coords = set()

    for line in lines:
        x, y = line.split(',')
        coords.add((int(x), int(y)))

    max_x = max(coords, key=lambda x: x[0])[0]
    max_y = max(coords, key=lambda x: x[1])[1]
    size_shared_region = 0

    for i in range(max_x + 1):
        for j in range(max_y +1):
            if sum(abs(x - i) + abs(y - j) for x, y in coords) < m_limit:
                size_shared_region += 1
    return size_shared_region

print(coord_safe(lines))






# max_area(lines)

