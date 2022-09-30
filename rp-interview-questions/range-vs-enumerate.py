

def fizz_buzz(numbers):
    """
    To run the doc test
    python3 -m doctest range-vs-enumerate.py
    
    Given a list of integers 
    1. Replace all the integers that are evenly divisible by 3
    with "fizz"
    2. Replace all the integers divisible by 5 with "buzz"
    3. Replace all the integers divisible by 3 and 5 with "fizzbuzz"

    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers 
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    """
    # with range
    # for i in range(len(numbers)):
    #     num = numbers[i]
    #     if num % 3 == 0 and num % 5 == 0:
    #         numbers[i] = 'fizzbuzz'
    #     elif num % 3 == 0:
    #         numbers[i] = 'fizz'
    #     elif num % 5 == 0:
    #         numbers[i] = 'buzz'

    # with enumerate
    for i, num in enumerate(numbers):
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = 'fizzbuzz'
        elif num % 3 == 0:
            numbers[i] = 'fizz'
        elif num % 5 == 0:
            numbers[i] = 'buzz'

    return numbers


numbers = [45, 22, 14, 65, 97, 72]
print(fizz_buzz(numbers))