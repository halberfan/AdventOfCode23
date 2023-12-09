import time

def part_one():
    sum = 0
    for line in lines:
        steps = [line.copy()]
        while not all(value == 0 for value in steps[-1]):
            l = steps[-1]
            new = []
            for i in range(len(l)-1):
                new.append(l[i+1] - l[i])
            steps.append(new)
        steps[-1].append(0)
        for i in range(len(steps)-2,-1,-1):
            s = steps[i]
            s.append(steps[i+1][-1] + s[-1])
        sum += steps[0][-1]
    return sum

def part_two():
    sum = 0
    for line in lines:
        steps = [line.copy()]
        while not all(value == 0 for value in steps[-1]):
            l = steps[-1]
            new = []
            for i in range(len(l)-1):
                new.append(l[i+1] - l[i])
            steps.append(new)
        steps[-1].insert(0, 0)
        for i in range(len(steps)-2,-1,-1):
            s = steps[i]
            s.insert(0, s[0] - steps[i+1][0])
        sum += steps[0][0]
    return sum

with open("day09/input.txt", 'r') as f:
    lines = f.read().split("\n")
    lines = [list(map(int, i)) for i in [n.split(" ") for n in lines]]

start_time = time.time()

print("Part One :", part_one())
print("Part Two :", part_two())
print("Runtime  :", time.time() - start_time, "ms")
