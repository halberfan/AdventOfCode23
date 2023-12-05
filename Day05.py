f = open("sonstiges\\adventofcode\\Task04_2\\input.txt", "r")
lines = f.read().split("\n")

def part_one():
    maps = []
    seeds = [eval(i) for i in lines[0][7:].split(" ")]
    current_map = None
    for l in lines[2:]:
        if "map" in l:
            if current_map != None:
                maps.append(current_map)
            current_map = Map(l[:-1])
        else: 
            if l != "":
                a = l.split(" ")
                current_map.ranges.append(Range(eval(a[0]), eval(a[1]), eval(a[2])))
    maps.append(current_map)
    lowest_loc = 99999999999
    for seed in seeds:
        before = seed
        for map in maps:
            before = map.get_corresponding_number(before)
            if "location" in map.name:
                if lowest_loc > before:
                    lowest_loc = before
    print(lowest_loc)

class Map:

    def __init__(self, name):
        self.name = name
        self.ranges = []
    
    def get_corresponding_number(self, seed):
        frange = None
        for range in self.ranges:
            if seed >= range.source_start and (range.source_start + range.range_length) >= seed:
                frange = range
        if frange == None:
            return seed
        else: 
            return frange.range_start + (seed - frange.source_start)

class Range:
    def __init__(self, range_start, source_start, range_length):
        self.range_start = range_start
        self.source_start = source_start
        self.range_length = range_length

    def __str__(self) -> str:
        return f"Range Start: {self.range_start} Source Start: {self.source_start} Range Length: {self.range_length}"

part_one()
