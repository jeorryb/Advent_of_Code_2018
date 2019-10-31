from string import *


def string2list(input):
    with open(input) as fh:
        polymer = fh.read().strip()
        polylist = [letter for letter in polymer]
        return polylist

polylist = string2list('/Users/jeorryb/Dropbox/Advent_of_Code_2018/day5/input.txt')

def reaction(l_list):
        p = ['.']
        for u in l_list:
            v = p[-1]
            if v != u and v.lower() == u.lower():
                p.pop()
            else:
                p.append(u)
        return len(p) - 1 

infile = '/Users/jeorryb/Dropbox/Advent_of_Code_2018/day5/input.txt'
print(reaction(polylist))

shortestpoly = min(reaction(c for c in polylist if c.lower() != x) for x in ascii_lowercase)

print(f'The shortest polymer is {shortestpoly}')