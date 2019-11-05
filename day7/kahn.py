from collections import defaultdict
import bisect

def parse_input(input):
    with open(input) as fh:
        lines = [line.strip() for line in fh.readlines()]
        return lines

lines = parse_input('/Users/jeorryb/Dropbox/Advent_of_Code_2018/day7/input.txt')

def gen_graph(lines):
    graph = defaultdict(list)
    in_degrees = defaultdict(int)
    for line in lines:
        graph[line[5]].append(line[36])
    sorted_graph = {}
    for k, v in graph.items():
        sorted_graph[k] = sorted(v)
    for k in sorted_graph:
        for v in sorted_graph[k]:
            in_degrees[v] += 1
    return sorted_graph, in_degrees

sorted_graph, in_degrees = gen_graph(lines)

def part1():
    L = []
    Q = sorted([k for k in sorted_graph if in_degrees[k] == 0])
    while Q:
        start = Q.pop(0)
        L.append(start)
        if not start in sorted_graph:
            break
        for v in sorted_graph[start]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                bisect.insort(Q, v)

    return L

L = part1()
print(''.join(i for i in L))

# PART 2
deps = defaultdict(set) #deps maps tasks to a set of prereq tasks
tasks = set() #Set of all task names A-Z
done = set()
seconds = 0     #total seconds elapsed
counts = [0] * 5    #seconds remaining for worker `i` to finish its current task
work = [''] * 5    # which task worker `i` is performing

def gendeps(lines):
    for line in lines:
        k = line[36]
        v = line[5]
        deps[k].add(v)
        tasks.add(k)
        tasks.add(v)

gendeps(lines)
while True:
    # decrement each workers remaining time
    # if a worker finishes, mark its task as completed
    for i, count in enumerate(counts):
        if count == 1:
            done.add(work[i])
        counts[i] = max(0, count - 1)
    while 0 in counts:
        i = counts.index(0)
        candidates = [x for x in tasks if deps[x] <= done]
        if not candidates:
            break
        task = min(candidates)
        tasks.remove(task)
        counts[i] = ord(task) - ord('A') + 61
        work[i] = task
    if sum(counts) == 0:
        break
    seconds += 1
print(seconds)



