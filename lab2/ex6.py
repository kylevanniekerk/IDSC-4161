nums = [47, 36, 71, 63, 12, 80, 90, 42, 25, 92, 45, 42, 5, 74, 77, 25, 0, 30, 91, 71]


def largest_even(nums):
    bigeven = -1
    for num in nums:
        num = int(num)
        if num % 2 == 0 and num > bigeven:
            bigeven = num
    return bigeven
    
print('{0}'.format(largest_even(nums)))
	
def num_two_digits(nums):
    counttwo = int(0)
    for num in nums:
        if len(str(num)) == 2:
            counttwo += 1
    return counttwo
print('{0}'.format(num_two_digits(nums)))

def num_odd(nums):
    countodd = int(0)
    for num in nums:
        if num % 2 == 1: 
            countodd += 1
    return countodd
print('{0}'.format(num_odd(nums)))

