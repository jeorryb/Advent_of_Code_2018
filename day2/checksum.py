import collections

def calcchecksum(inputfile):
    with open(inputfile, 'r') as f:
        inputs = [line.strip() for line in f]
        twochar = set()
        threechar = set()
        for input in inputs:
            for letter in input:
                if input.count(letter) == 2:
                    twochar.add(input)
                if input.count(letter) == 3:
                    threechar.add(input)
        
        x = (len(twochar))
        y = (len(threechar))
        checksum = x*y
        return checksum



checksum = calcchecksum('input.txt')

print(f'The checksum is {checksum}')