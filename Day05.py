import time

class SeedRange:
    def __init__(self, range_start, range_end):
        self.start = range_start
        self.end = range_end

    def get_len(self):
        return self.end - self.start

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

class Map:
    def __init__(self, name):
        self.name = name
        self.ranges = []

    def get_corresponding_number(self, seed):
        frange = None
        for r in self.ranges:
            if seed >= r.source_start and (r.source_start + r.range_length) >= seed:
                frange = r
        if frange is None:
            return seed
        else: 
            return frange.range_start + (seed - frange.source_start)

    def get_ranges(self, seed_range: SeedRange):
        ranges = []
        for r in self.ranges:
            part_range = r.get_part_range(seed_range)
            if part_range is None:
                continue
            ranges.append(SeedRange(part_range.start - r.range_source_diff(), part_range.end - r.range_source_diff()))
            if part_range.start != seed_range.start:
                s = SeedRange(seed_range.start, part_range.start - 1)
                ranges.extend(self.get_ranges(s))
            if part_range.end != seed_range.end:
                e = SeedRange(part_range.end + 1, seed_range.end)
                ranges.extend(self.get_ranges(e))
            break
        return [seed_range] if not ranges else ranges

def get_maps(lines):
    maps = []
    current_map = None
    for l in lines[2:]:
        if "map" in l:
            if current_map is not None:
                maps.append(current_map)
            current_map = Map(l[:-1])
        else: 
            if l != "":
                a = l.split(" ")
                current_map.ranges.append(Range(eval(a[0]), eval(a[1]), eval(a[2])))
    maps.append(current_map)
    return maps

def get_seed_ranges(nums):
    ranges = []
    current_start = eval(nums[0])
    for i in range(1, len(nums)):
        if i % 2 == 1:
            ranges.append(SeedRange(current_start, eval(nums[i]) + current_start))
        else:
            current_start = eval(nums[i])
    return ranges

def part_one(maps, seeds):
    lowest_loc = float('inf')
    for seed in seeds:
        before = seed
        for map in maps:
            before = map.get_corresponding_number(before)
            if "location" in map.name and lowest_loc > before:
                lowest_loc = before
    return lowest_loc

def part_two(maps, seed_ranges):
    current_ranges = seed_ranges
    for map in maps:
        updated_ranges = []
        for sr in current_ranges:
            updated_ranges.extend(map.get_ranges(sr))
        current_ranges = updated_ranges
    lowest_start = current_ranges[0].start
    for c in current_ranges[1:]:
        if c.start < lowest_start and c.start != 0:
            lowest_start = c.start
    return lowest_start

with open("day05/input.txt", "r") as f:
    lines = f.read().split("\n")

start_time = time.time()

maps = get_maps(lines)
seeds = [eval(i) for i in lines[0][7:].split(" ")]
seed_ranges = get_seed_ranges(lines[0][7:].split(" "))

print("Part One:", part_one(maps, seeds))
print("Part Two:", part_two(maps, seed_ranges))
print("Runtime:", time.time() - start_time, "ms")
