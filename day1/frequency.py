
def calcfreq(inputfile):
    with open(inputfile, 'r') as f:
        total = sum(int(line) for line in f if line.strip())
    return total

total = calcfreq('input.txt')

print(f'The frequecy is {total}')
