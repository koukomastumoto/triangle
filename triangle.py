import re

# settings
SIDE_LENGTH_MIN = 1 # allow side's min length
SIDE_LENGTH_MAX = 10000 # allow side's max length
SIDES_NUMBER = 3 # max sides number (triangle is 3.)
SIDES_TYPE_NAMES = ["equilateral", "isosceles", "scalene"]

# defined exception class
class InputException(Exception):
    pass

# input validation method
def get_valid_data(input_data):
    input_datas = input_data.split(",")
    sides = []
    if len(input_datas) < SIDES_NUMBER:
        raise InputException('must input {} numbers.'.format(SIDES_NUMBER))
    for i, s in enumerate(input_datas):
        if SIDES_NUMBER == i:
            break
        if not re.match('^[0-9]{1,}$', s):
            raise InputException('must input integer number.')
        if SIDE_LENGTH_MIN > int(s) or int(s) > SIDE_LENGTH_MAX:
            raise InputException('number\'s range is {}-{}.'.format(SIDE_LENGTH_MIN, SIDE_LENGTH_MAX))
        sides.append(int(s))
    return sides

# evaluation method
def evaluate(arr):
    if len(arr) != SIDES_NUMBER:
        raise
    return SIDES_TYPE_NAMES[len(set(arr))-1]

# get user inputs
if __name__ == '__main__':
    sides = []
    while True:
        input_data = input('Please input {} sides\' integer numbers [{}-{}] of a triangle.'.format(SIDES_NUMBER, SIDE_LENGTH_MIN, SIDE_LENGTH_MAX)\
        + 'Delimiter must be only comma.'\
        + 'If you feed more than {}, this programm choices the top three numbers. \n'.format(SIDES_NUMBER)
        + 'i.e. 1,10,5\n')
        try:
            sides = get_valid_data(input_data)
        except InputException as e: 
            print(e)
            continue
        else:    
            break    
        
    print('Your input numbers are [{}].'.format(','.join([str(n) for n in sides])))

    # evaluate type of triangle
    print('This triangle is [{}]'.format(evaluate(sides)))