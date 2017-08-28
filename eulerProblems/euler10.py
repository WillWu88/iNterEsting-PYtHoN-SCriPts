#find the prijme summation of 2 million


def prime_generator(upper_limit, lower_limit=2):
    """generate all prime numbers under the upper_limit given by brute force"""
    a = [2]
    sum = 2
    for n in range(lower_limit, upper_limit):
        for m in a:
            if n % m == 0:
                break
        else:
            a.append(n)
            sum += n
    return sum

print(prime_generator(200000))

#since the upper limit is very large, the program drains off memories quickly
#decided each time the upper limit for caculation is 200000
#
