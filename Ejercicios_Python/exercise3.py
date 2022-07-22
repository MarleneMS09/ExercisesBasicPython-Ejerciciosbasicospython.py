#PRINT WITH FOR AND IF
def print_square_value(numbers):
    for number in numbers:
        if number != 2:
            square = number*number
            print(square)


numbers = [1, 2, 3, 4]
print_square_value(numbers)
