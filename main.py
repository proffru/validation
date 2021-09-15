from data import *

def validateBik(bik):
    result = False
    if not bik:
        # raise ValidationError('БИК не заполнен')
        print('БИК не заполнен')
    elif not bik.isdigit():
        print('БИК может состоять только из цифры')
        # raise ValidationError('БИК может состоять только из цифры')
    elif not len(bik) == 9:
        print('БИК может состоять только из 9 цифр')
        # raise ValidationError('БИК может состоять только из 9 цифр')
    else:
        result = True
    return result


ints3 = [2, 4, 10, 3, 5, 9, 4, 6, 8]
ints = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
ints2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]

def check_digits(inn, coefficients):
    n = 0
    # for i in list(coefficients):
    for idx, i in enumerate(coefficients):
        n += i * int(inn[idx])
    return n % 11 % 10


def validateInn(inn):
    result = False
    if not inn:
        # raise ValidationError('ИНН не заполнен')
        print('ИНН не заполнен')
    elif not inn.isdigit():
        print('ИНН может состоять только из цифры')
        # raise ValidationError('ИНН может состоять только из цифры')
    elif not len(inn) in [10, 12]:
        print('ИНН может состоять только из 10 или 12 цифр')
        # raise ValidationError('ИНН может состоять только из 10 или 12 цифр')
    else:
        if len(inn) == 10:
            inn10 = check_digits(inn, [2, 4, 10, 3, 5, 9, 4, 6, 8])
            if inn10 == int(inn[9]):
                result = True
        if len(inn) == 12:
            n11 = check_digits(inn, [7, 2, 4, 10, 3, 5, 9, 4, 6, 8])
            n12 = check_digits(inn, [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8])
            if n11 == int(inn[10]) and n12 == int(inn[11]):
                result = True
        if not result:
            print('Неправильное контрольное число')
            # raise ValidationError('ИНН указан не верно')
    return result
