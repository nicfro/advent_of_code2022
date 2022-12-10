with open('day_4_Camp_Cleanup/input.txt') as f:
    lines = f.readlines()

def range_contains(x_start, x_stop, y_start, y_stop):
    return (x_start <= y_start and y_stop <= x_stop) or (y_start <= x_start and x_stop <= y_stop)

def range_overlapping(x_start, x_stop, y_start, y_stop):
    return x_start <= y_stop and y_start <= x_stop

lines = [x.strip() for x in lines]

contains_counter = 0
overlap_counter = 0
for line in lines:
    x, y = line.split(",")
    x_start, x_stop = map(int, x.split("-"))
    y_start, y_stop = map(int, y.split("-"))
    
    contains_counter += range_contains(x_start, x_stop, y_start, y_stop)
    overlap_counter += range_overlapping(x_start, x_stop, y_start, y_stop)

print(overlap_counter)
print(contains_counter)

