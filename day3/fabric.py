import re
from collections import Counter

claim_re = re.compile(r'#(?P<_id>[0-9]+) @ '
                      r'(?P<left>[0-9]+),(?P<top>[0-9]+): '
                      r'(?P<width>[0-9]+)x(?P<height>[0-9]+)'
                     )

# m = claim_re.match('#1 @ 82,901: 26x12')

def parse_claim(claim_string):
    m = claim_re.match(claim_string)
    return {k: int(v) for k, v in m.groupdict().items()}

def claim_area(claim):
    return ((i, j) 
    for i in range(claim['left'], claim['left'] + claim['width'])
    for j in range(claim['top'], claim['top'] + claim['height']))

# claim = parse_claim('#1 @ 82,901: 26x12')

# genex = claim_area(claim)
# print(list(genex))

def parse_input(input):
    with open(input) as fh:
        claims = []
        for line in fh.readlines():
            claim = parse_claim(line)
            claims.append(claim)
        return claims

claims = parse_input('/Users/jeorryb/Dropbox/Advent_of_Code_2018/day3/input.txt')

def calc_fabric(claimlist):
    fabric = Counter(coord for claim in claimlist for coord in claim_area(claim))
    return fabric

fabric = calc_fabric(claims)

def overlap(fabric):
    return sum([1 for claim_count in fabric.values() if claim_count > 1])

print(overlap(fabric))

def no_overlap(claims, fabric):
    for claim in claims:
        if all(fabric[coord] == 1 for coord in claim_area(claim)):
            return claim['_id']

print(no_overlap(claims, fabric))

# def fabric_overlap(claims):
#     fabric = {}
#     for coord in claim