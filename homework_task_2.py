#!/usr/bin/env python3
# Math for mid wipe

odd_range = range(1, 1001, 2)

for i in odd_range:
    odd_list = list(odd_range)
    power_of = [i ** 3 for i in odd_list]

sums_for_division = []

for j in power_of:
    summation = 0
    for digit in str(j):
        summation += int(digit)
    sums_for_division.append(summation)

for h in sums_for_division:


""" my_list = [11, 23, 41, 62, 89, 0, 10]
print("The list is : ")
print(my_list)
my_result = []
for elem in my_list:
   sum_val = 0
   for digit in str(elem):
      sum_val += int(digit)
   my_result.append(sum_val)
print ("The result after adding the digits is : " )
print(my_result) """
