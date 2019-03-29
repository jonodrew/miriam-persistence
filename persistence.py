from typing import List

def multiply(digits: List[int]):
    product = 1
    for x in digits:
        product *= x
    return product


def persistence(number: int):
    """
    persistence takes a number of x digits and returns the number of times you have to multiply the digits within it to
    get to a single digit number
    :param number:
    :type number:
    :return:
    :rtype:
    """
    number_of_multiplications = 0
    if length_number(number) == 1:
        return number_of_multiplications
    while length_number(number) > 1:
        number = multiply(listifier(number))
        number_of_multiplications += 1
    return number_of_multiplications


def length_number(number_to_measure):
    """
    Returns the number of digits in the inputted number
    :param number:
    :type number:
    :return:
    :rtype:
    """
    return len(str(number_to_measure))


def listifier(number_to_be_listified: int):
    return [int(digit) for digit in str(number_to_be_listified) if digit != '-']
