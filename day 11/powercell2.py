import numpy
serial = int(3628)

def power(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += serial
    power *= rack
    return (power // 100 % 10) - 5

grid = numpy.fromfunction(power, (9, 9))

# for width in range(3, 300):
#     windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
#     maximum = int(windows.max())
#     location = numpy.where(windows == maximum)
#     print(width, maximum, location[0][0] + 1, location[1][0] + 1)

windows = sum(grid[x:x-3+1 or None, y:y-3+1 or None] for x in range(3) for y in range(3))
print(windows)
maximum = int(windows.max())
location = numpy.where(windows == maximum)

print(maximum, location)
