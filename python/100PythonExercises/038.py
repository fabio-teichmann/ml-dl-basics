# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the
# first half values in one line and the last half values in one line.

data = (2,3,4,5,6,7,8,9,10)
if len(data) % 2 == 0:
    mid = int(len(data) / 2)
else:
    mid = int((len(data) + 1) / 2)
# print(mid)
print(data[:mid])
print(data[mid:])