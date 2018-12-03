import collections
import difflib
from itertools import combinations

def twochar(inputfile):
    with open(inputfile, 'r') as f:
        inputs = [line.strip() for line in f]
        twochar = set()
        for input in inputs:
            for letter in input:
                if input.count(letter) == 2:
                    twochar.add(input)
        return twochar

def threechar(inputfile):
    with open(inputfile, 'r') as f:
        inputs = [line.strip() for line in f]
        threechar = set()
        for input in inputs:
            for letter in input:
                if input.count(letter) == 3:
                    twochar.add(input)
        return threechar

twochar = twochar('input.txt')
threechar = threechar('input.txt')
unique = twochar.union(threechar)
combs = [x for x in combinations(unique, 2)]

def find_id(id_pairs):
    for x, y in id_pairs:
        id1 = list(x)
        id2 = list(y)
        samecount = 0
        commonletters = []
        for char1, char2 in zip(id1, id2):
            if char1 == char2:
                samecount += 1
                commonletters.append(char1)
        if samecount == len(id1) - 1:
            common = ''.join(commonletters)
            return common
            

        

common = find_id(combs)
print(f'The common letters between the box ids is {common}')

