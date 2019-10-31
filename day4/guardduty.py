import collections
import re
from datetime import datetime

date_re = re.compile(r'\[(?P<date>.+)\] '
                     r'(?P<entry>.+)')
minute_re = re.compile(r'\[.+\:(?P<minute>[0-9]+).+')
guard_re = re.compile(r'.+#(?P<guard_id>[0-9]+).+')
times = collections.defaultdict(int)

format = "%Y-%m-%d %H:%M"
# print(date_re.match('[1518-05-11 00:47] wakes up').group('date'))

def sortdate(input):
    with open(input) as fh:
        mixdates = fh.readlines()
        sorted_entries = sorted(mixdates, key = lambda line: datetime.strptime(date_re.match(line).group('date'), format))
        return sorted_entries

sorted_entries = sortdate('/Users/jeorryb/Dropbox/Advent_of_Code_2018/day4/input.txt')

def parse_entries(entries):
    guards = collections.defaultdict(lambda: collections.defaultdict(int))
    for entry in entries:
        if 'Guard' in entry:
            guard = guard_re.match(entry).group('guard_id')
        elif 'falls' in entry:
            start = int(minute_re.match(entry).group('minute'))
        elif 'wakes' in entry:
            end = int(minute_re.match(entry).group('minute'))
            for x in range(start, end):
                guards[guard][x] += 1
    return guards

 
guards = parse_entries(sorted_entries)

# def max_minutes(guards):
#     for guard, minutes in guards.items():
#         guards[guard]['total'] = sum(minutes.values())
#     max_sleeper = max(g['total'] for g in guards.values())
#     # for guard, minutes in guards.items():
#     #     if guards[guard]['total'] == max_sleeper:
#     #         print(guard, '->', max_sleeper)

# max_minutes(guards)

def max_minute(guards, guard_id):
    most_asleep = max(m for m in guards[guard_id].values())
    for m, t in guards[guard_id].items():
        if t == most_asleep:
            print('most asleep minute ->', m)

max_minute(guards, '2593')

print(f'The answer to day 4 Part 1 puzzle is {2593*40}')

def freq_minute(guards):
    frequent = {}
    for guard, minutes in guards.items():
        high_min = max(m for m in minutes.values())
        for k, v in minutes.items():
            if high_min == v:
                frequent[guard] = (k, v)
    
    itemmax = max(frequent.items(), key=lambda x: x[1][1])
    print(f'Minute most asleep is {itemmax[1][0]}')
    print(f'Guard ID is {itemmax[0]}')
    print(f'Day 4 part 2 solution = {(itemmax[1][0]) * int(itemmax[0])}')

freq_minute(guards)


        