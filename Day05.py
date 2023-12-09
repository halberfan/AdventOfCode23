import time
f = open("day05/input.txt", "r")
lines = f.read().split("\n")
start_time = time.time()
def get_maps():
    maps = []
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
    return maps

class SeedRange:
    def __init__(self, range_start, range_end):
        self.start = range_start
        self.end = range_end

    def get_len(self):
        return self.end - self.start
    
    def __str__(self) -> str:
        return f"Range Start: {self.start} Range End {self.end}"
    def __repr__(self) -> str:
        return f"Range Start: {self.start} Range End {self.end}"

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
    
    """
    SeedRange wird aufgeteilt in: ALLES DAVOR (REKURSIV) - BEREICH IN MAP - ALLES DANACH (REKURSIV)
    """
    def get_ranges(self, seed_range: SeedRange):
        ranges = []
        for range in self.ranges:
            r = range.get_part_range(seed_range)
            if r == None:
                continue
            ranges.append(SeedRange(r.start - range.range_source_diff(), r.end - range.range_source_diff()))
            if r.start != seed_range.start:
                s = SeedRange(seed_range.start, r.start - 1)
                ranges.extend(self.get_ranges(s))
            if r.end != seed_range.end:
                e = SeedRange(seed_range.start, r.start - 1)
                ranges.extend(self.get_ranges(e))
            break
        if len(ranges) == 0:
            return [seed_range]
        return ranges


class Range:
    def __init__(self, range_start, source_start, range_length):
        self.range_start = range_start
        self.source_start = source_start
        self.range_length = range_length

    def end_source(self):
        return self.source_start + self.range_length
    
    def range_source_diff(self):
        return self.source_start - self.range_start

    def get_part_range(self, seed_range: SeedRange):
        if seed_range.start > self.end_source() or self.source_start > seed_range.end:
            return None
        s = max(self.source_start, seed_range.start)
        e = min(self.end_source(), seed_range.end)
        return SeedRange(s, e)
    

    def __str__(self) -> str:
        return f"Range Start: {self.range_start} Source Start: {self.source_start} Range Length: {self.range_length}"

def part_one():
    maps = get_maps()
    seeds = [eval(i) for i in lines[0][7:].split(" ")]
    lowest_loc = 9999999999999
    for seed in seeds:
        before = seed
        for map in maps:
            before = map.get_corresponding_number(before)
            if "location" in map.name:
                if lowest_loc > before:
                    lowest_loc = before
    return lowest_loc

def get_seed_ranges():
    nums = lines[0][7:].split(" ")
    ranges = []
    current_start = eval(nums[0])
    for i in range(1, len(nums)):
        if i % 2 == 1:
            ranges.append(SeedRange(current_start, eval(nums[i]) + current_start))
        else: current_start = eval(nums[i])
    return ranges

def part_two():
    maps = get_maps()
    seed_ranges = get_seed_ranges()
    for map in maps:
        current_ranges = []
        for range in seed_ranges:
            current_ranges.extend(map.get_ranges(range))
        seed_ranges = current_ranges
    lowest_start = current_ranges[0].start
    for c in current_ranges[1:]:
        if c.start < lowest_start and c.start != 0: # dunno why, but i have to check for 0 
            lowest_start = c.start
    return lowest_start

print("Part One:",part_one())
print("Part Two:",part_two())
print("Runtime: ", time.time() - start_time, "ms")
