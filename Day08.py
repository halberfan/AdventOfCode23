from math import gcd
import time
file = open("day8/input.txt")
lines = file.read().split("\n")

t_start = time.time()

network = {}
instruction = []

for i in range(len(lines)):
    if i == 0:
        for a in lines[i]:
            instruction.append(a)
    if i > 1:
        line = lines[i]
        network[line[:3]] = (line[7:10], line[12:15])

def day_one():
    current_instruction = 0
    counter = 0
    current_map = "AAA"
    while True:
        tupl = network[current_map]
        if(instruction[current_instruction] == 'L'):
            current_map = tupl[0]
        else: current_map = tupl[1]
        current_instruction += 1
        if current_instruction == len(instruction):
            current_instruction = 0
        counter += 1
        if current_map == "ZZZ":
            break
    return counter

def all_maps_ending_a():
    maps = []
    for m in network:
        if(m[2:] == "A"):
            maps.append(m)
    return maps

def day_two():
    ending_a = all_maps_ending_a()
    counts = []
    for a in ending_a:
        current_instruction = 0
        counter = 0
        current_map = a
        while True:
            tupl = network[current_map]
            if(instruction[current_instruction] == 'L'):
                current_map = tupl[0]
            else: current_map = tupl[1]
            current_instruction += 1
            if current_instruction == len(instruction):
                current_instruction = 0
            counter += 1
            if current_map[2:] == "Z":
                break
        counts.append(counter)
    counts.sort()
    lcm = 1
    for i in counts:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

print(f"Task One: {day_one()}")
print(f"Task Two: {day_two()}")
print("Runtime for both:", time.time() - t_start, "ms")
