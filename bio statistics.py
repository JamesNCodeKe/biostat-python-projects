def get_the_mean(data):
    total = 0
    for i in data:

        total += i
    mean = total/ len(data)
    return mean

def get_the_variance(data):
    n = len(data)
    sum_of_squares = 0
    mean = get_the_mean(data)

    for i in data:
        difference = i - mean

        squared_diffence = difference * difference

        sum_of_squares += squared_diffence

    if n<2:
        return 0
    
    variance = sum_of_squares/ (n-1)

    return variance

def get_the_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)


    if n == 0:
        return 0
    
    if n % 2 == 1:
        mid_index = n//2

        median = sorted_data[mid_index]
    else:
        mid2_index = n // 2
        mid1_index = mid2_index - 1
        median = (sorted_data[mid1_index] + sorted_data[mid2_index]) / 2
    return median

data = (14, 15, 12, 7, 8, 14, 10, 9, 17, 10)

import random

total_throws = 1000000
success_counts = 0

for i in range(total_throws):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    if die1 == 6 and die2 == 6:
        success_counts += 1
probability = success_counts/ total_throws

real_unswer = 1/36

import math

S2 = get_the_variance(data)
S = math.sqrt(S2)
mean = get_the_mean(data)
median = get_the_median(data)

print(f"The mediand is {median}")
print(f"The mean is {mean}")
print(f"The variance is {S2}")
print(f"The standard deviation is {S}")
print(f"The probablity is {probability}.%")
print(f"Real probability is {real_unswer}.%")

