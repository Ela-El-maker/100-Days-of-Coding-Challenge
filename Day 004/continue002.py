def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

count = 0
number = 2
prime_numbers = []

while count < 10:
    if is_prime(number):
        prime_numbers.append(str(number))
        count += 1
    number += 1

print(','.join(prime_numbers))
