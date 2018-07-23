import re

# defined exception class
class InputException(Exception):
    pass

# settings
SIDE_LENGTH_MIN = 1 # allow side's min length
SIDE_LENGTH_MAX = 10000 # allow side's max length
SIDES_NUMBER = 3 # max sides number (triangle is 3.)

# get user inputs
sides = []
while True:
    input_data = input('Please input {} sides\' numbers [{}-{}] of a triangle.'.format(SIDES_NUMBER, SIDE_LENGTH_MIN, SIDE_LENGTH_MAX)\
    + 'Delimiter must be only comma.'\
    + 'If you feed more than {}, this programm choices the top three numbers. \n'.format(SIDES_NUMBER))
    sides = []
    try:
        input_datas = input_data.split(",")
        if len(input_datas) < SIDES_NUMBER:
            raise InputException('must input three numbers.')
        for i, s in enumerate(input_datas):
            if SIDES_NUMBER == i:
                break
            if not re.match('^[0-9]{1,}$', s):
                print(s)
                raise InputException('must input number.')
            if SIDE_LENGTH_MIN > int(s) or int(s) > SIDE_LENGTH_MAX:
                raise InputException('number\'s range is [{}-{}].'.format(SIDE_LENGTH_MIN, SIDE_LENGTH_MAX))
            sides.append(int(s))
    except InputException as e: 
        print(e)
        continue
    break    
        
print('Your input numbers are "{}".'.format(','.join([str(n) for n in sides])))

# evaluate type of triangle