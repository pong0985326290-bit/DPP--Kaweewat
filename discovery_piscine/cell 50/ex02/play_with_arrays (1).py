#!/usr/bin/env python3

array = [2,8,9,48,8,22,-12,2]

print(array)

newarray = []
for i in range(len(array)):
    array[i] += 2
    if array[i] > 5:
     newarray.append(array[i])



print(newarray)