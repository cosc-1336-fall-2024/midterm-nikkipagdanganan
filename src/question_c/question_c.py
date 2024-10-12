#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_miles_per_hour(km, min):
    conv_ratio = .621371
    hr = min / 60
    final = (km * hr) * conv_ratio
    return final