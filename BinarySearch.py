def binary_search(array, target):

    left = 0

    right = len(array) - 1

    while True:
        if right < left:
            return -1
        midpoint = (left + right) // 2
        if array[midpoint] < target:
            left = midpoint + 1
        elif array[midpoint] > target:
            right = midpoint - 1
        else:
            return midpoint


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

result = binary_search(primes, 97)

if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")
