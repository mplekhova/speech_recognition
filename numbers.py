numbers = {'01': 'первое',
'02': 'второе',
'03': 'третье'}
def number_to_word(x):
    if x in numbers.keys():
        return numbers[str(x)]
    return False
