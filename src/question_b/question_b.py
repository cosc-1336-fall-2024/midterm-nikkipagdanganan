#write functions here, don't add input('') statements here!

def test_config():
    return True

def get_person_category(age):
    cat = ''
    if age <= 1:
        cat = 'infant'
    elif age > 1 and age < 13:
        cat = 'child'
    elif age >= 13 and age < 20:
        cat = 'teenager'
    elif age >= 20:
        cat = 'adult'
    elif age < 0 or age > 125:
        cat = 'Invalid number'
    return cat
