import math
def is_prime(number, prime_list):

    if number < 2:
        return False
    if number == 2:
        return True
    if len(prime_list) == 0:
        prime_list = [2]

    for i in prime_list:
        if number % i == 0:
            return False

    for i in range(max(prime_list), int(math.sqrt(number))+1):
        if number % i == 0:
            return False

    return True


def get_prime_in_range(start, end):
    ans = []
    count = 1
    for i in range(start, end+1):
        if is_prime(i, ans):
            print(i, count)
            count += 1
            ans.append(i)

    return ans

print(get_prime_in_range(1, 100))