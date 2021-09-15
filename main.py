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


def check_digits(inn, coefficients):
    n = 0
    for i in range(len(coefficients):
        n += i * coefficients[i]

    return $n % 11 % 10;

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
        # raise ValidationError(''ИНН может состоять только из 10 или 12 цифр'')
    # else:




bik = '545807951'

validate_bik(bik)


