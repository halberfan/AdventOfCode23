f = open("input.txt", "r")
lines = f.read().split("\n")

times = [eval(i) for i in lines[0][6:].split(" ")]
distances = [eval(i) for i in lines[1][10:].split(" ")]

result = 1

for i in range(0,len(times)):
    ways_to_beat = 0
    distance_to_beat = distances[i]
    time = times[i]
    for speed in range(1,time):
        remaining_time = time - speed
        if remaining_time * speed > distance_to_beat:
            ways_to_beat += 1
    if ways_to_beat != 0:
        result *= ways_to_beat


print(result)
