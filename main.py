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


def validateInn(inn):
    def check_digits(inn, coefficients):
        n = 0
        for idx, i in enumerate(coefficients):
            n += i * int(inn[idx])
        return n % 11 % 10

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
            inn11 = check_digits(inn, [7, 2, 4, 10, 3, 5, 9, 4, 6, 8])
            inn12 = check_digits(inn, [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8])
            if inn11 == int(inn[10]) and inn12 == int(inn[11]):
                result = True
        if not result:
            print('Неправильное контрольное число')
            # raise ValidationError('ИНН указан не верно')
    return result


def validationCardNumber(number):
    result = False
    odd_digits = number[-1::-2]
    even_digits = number[-2::-2]
    total = 0

    total += sum(map(int, str(odd_digits)))

    for digit in even_digits:
        digit = int(digit)
        if (digit * 2) > 9:
            total += ((digit * 2) - 9)
        else:
            total += (digit * 2)
    if (total % 10) == 0:
        result = True
        print('valid')
    else:
        print('Номер карты указан не верно')
        # raise ValidationError('Номер карты указан не верно')
    return result


def validateRs(bik, rs):
    result = False
    if not rs:
        # raise ValidationError('Расчетный счет не заполнен')
        print('Расчетный счет не заполнен')
    elif not rs.isdigit():
        print('Расчетный счет может состоять только из цифры')
        # raise ValidationError('Расчетный счет может состоять только из цифры')
    elif not len(rs) == 20:
        print('Расчетный счет может состоять только из 20 цифр')
        # raise ValidationError('Расчетный счет может состоять только из 20 цифр')
    else:
        bank_rs = bik[-3::] + rs
        checksum = 0
        check_digits = [7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1]
        for idx, digit in enumerate(check_digits):
            checksum += digit * (int(bank_rs[idx]) % 10)

        if checksum % 10 == 0:
            result = True
            print('Верно')
        else:
            print('Неправильное контрольное число')
            # raise ValidationError('Расчетный счет не соответствует БИКу банка')
    return result


validateRs(bik, rs)