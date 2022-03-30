def prime_checker(number):
    is_prime = True
    for num in range(1, number + 1):
        if (number % num == 0) and (num != 1) and (num != number):
            is_prime = False

    if number == 1:
        is_prime = False

    if is_prime:
        return print("It's a prime number.")
    else:
        return print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
