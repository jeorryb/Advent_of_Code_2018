def parse_input(input):
    with open(input, 'r') as fh:
        data = [int(x) for x in fh.readline().split(' ')]
        return data

data = parse_input('/Users/jeorryb/Dropbox/Advent_of_Code_2018/day8/input.txt')

def parse_data(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, data = parse_data(data)
        totals += total
        scores.append(score)
    
    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:]
        )

total, value, remaining = parse_data(data)

print('part 1:', total)
print('part 2:', value)