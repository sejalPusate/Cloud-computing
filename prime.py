# This function checks if a number is prime
def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False
    # Check for factors
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test the function with a number
number = 29
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
