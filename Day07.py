from collections import Counter
from functools import cmp_to_key
ranks = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

file = open("day07/input.txt", 'r')
lines = file.read().split("\n")

hands = {}
dupes = []

for line in lines:
    s = line.split(" ")
    if s[0] not in hands:
        hands[s[0]] = eval(s[1])
    else: print(s)

def part_one():
    points = [[],[],[],[],[],[],[],[]]
    
    for hand in hands:
        p = get_hand_type(hand)
        if(points[p] == None):
            points[p] = []
        points[p].append(hand)

    rank = []
    for p_a in points:
        for p in sorted(p_a, key=cmp_to_key(compare_two_hands)):
            rank.insert(0, p)
    r_len = len(rank)
    sum = 0
    rank.reverse()
    for i in (range(0, r_len)):
        sum += (i+1) * hands[rank[i]]
        #print(rank[i], hands[rank[i]], i, get_hand_type(rank[i]))
    return sum

def compare_two_hands(hand1:str, hand2:str):
    for c in range(0,5):
        if hand1[c] != hand2[c]:
            if(ranks[hand1[c]] > ranks[hand2[c]]):
                return 1
            else: return -1
    return 0

def get_hand_type(hand: str):
    amount_of_chars = dict(Counter(hand))
    pair = False
    three_pair = False
    distinct_counter = 0
    for c in amount_of_chars:
        if amount_of_chars[c] == 5:
            return 7
        elif amount_of_chars[c] == 4:
            return 6
        elif amount_of_chars[c] == 3:
            if pair:
                return 5
            else: three_pair = True
        elif amount_of_chars[c] == 2:
            if pair:
                return 3
            else:
                pair = True
        elif amount_of_chars[c] == 1:
            distinct_counter += 1
    if pair:
        if three_pair:
            return 5
        return 2
    elif distinct_counter == 5:
        return 1
    if three_pair:
        return 4
    return 0

print(part_one())
