#add import
import question_c

def main():
    print('PROGRAM: MPH Converter')
    km = int( input ('Enter the kilometers: '))
    min = int( input ('Enter the minutes: '))
    if km < 0 or min < 0:
        print('Invalid arguments.')
        main()
    else:
        mph = question_c.get_miles_per_hour(km, min)
        print (f'Conversion = {mph} MPH')
main()