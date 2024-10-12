#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_assessment_value(value):
    assess = value * .60
    return assess

def get_tax_assessed(value):
    tax = (value / 100) * .72
    return round(tax,2)
