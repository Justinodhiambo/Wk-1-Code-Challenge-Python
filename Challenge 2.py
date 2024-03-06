def digit_sum(number):
    return sum(int(digit) for digit in str(number))

def solution2(A):
    max_sum = -1
    sums = {}
    for number in A:
        ds = digit_sum(number)
        if ds in sums:
            max_sum = max(max_sum, sums[ds] + number)
            sums[ds] = max(sums[ds], number)
        else:
            sums[ds] = number
    return max_sum
