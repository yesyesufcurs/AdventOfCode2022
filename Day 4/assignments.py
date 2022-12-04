number_of_pairs_contained = 0
number_of_pairs_overlap = 0

f = open("input.txt", "r")

for line in f.readlines():
    range1, range2 = [[int(y) for y in x.split("-")] for x in line.strip().split(",")]
    
    # When a range is contained in the other, either range2 is contained in range1 resulting in range1[0] <= range2[0] and range1[1] >= range2[1]
    # Or range1 is contained in range2 resulting in range1[0] >= range2[0] and range1[1] <= range2[1]
    if range1[0] <= range2[0] and range1[1] >= range2[1] or range1[0] >= range2[0] and range1[1] <= range2[1]:
        number_of_pairs_contained += 1
    
    # We look at the range that that has the lowest starting index.
    # Then this range overlaps with the next one if the end index of the first starting range is higher than the
    # starting index of the second range.
    if range1[0] <= range2[0] and range1[1] >= range2[0] or range1[0] > range2[0] and range2[1] >= range1[0]:
        number_of_pairs_overlap += 1
    

print(number_of_pairs_contained)
print(number_of_pairs_overlap)