from collections import deque, defaultdict

def parse_input(input):
    with open(input) as fh:
        line = fh.read().strip()
        players = int(line[:3])
        marble_worth = int(line[-12:-7])
        return players, marble_worth

players, marble_worth = parse_input('/Users/jeorryb/Dropbox/Advent_of_Code_2018/day9/input.txt')



def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

x = play_game(players, marble_worth)

print(f'The winning score is {x}')

#PART 2

marble100x = marble_worth * 100
x100 = play_game(players, marble100x)
print(f'Part 2 answer is {x100}')