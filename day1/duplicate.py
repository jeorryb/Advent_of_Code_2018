import itertools as it

def calcdup(inputfile):
    with open(inputfile, 'r') as f:
        inputs = [int(line) for line in f if line.strip()]
        accum = it.accumulate(it.cycle(inputs))
        dupset = set()
        while True:
            for num in accum:
                if num in dupset:
                    return num
                    break
                dupset.add(num)




firstdup = calcdup('input.txt')

print(f'The first duplicate frequecy is {firstdup}')