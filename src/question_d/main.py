#add import
import question_d

def main():
    num = int( input ('Enter a number to check if it is a prime number: '))
    result = question_d.is_prime(num)
    if result == True:
        print(f'{num} is a prime number.')
    else:
        print(f'{num} is not a prime number. ')
    esc = input ('Press q or Q to quit program. Press any other key to try another number. ')
    if esc == 'q' or esc =='Q':
        pass
    else:
        main()
main()