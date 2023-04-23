# Problem 1: Multiples of 3 or 5
# We are to find the sum of the multiples of 3 or 5

# Based on my skill level I will use the linear method


def multiplesOf3or5(number):
    sum_of_multiples = 0
    for item in range(1, number):
        if item % 3 == 0 or item % 5 == 0:
            sum_of_multiples += item
    return sum_of_multiples

print(multiplesOf3or5(10))
print(multiplesOf3or5(49))
print(multiplesOf3or5(1000))
print(multiplesOf3or5(8456))
print(multiplesOf3or5(19564))
