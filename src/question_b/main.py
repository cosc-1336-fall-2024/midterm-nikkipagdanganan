#add import
import question_b

def main():

    num = int (input ('Enter your age to find out what age category you\'re in. '))
    cat = question_b.get_person_category(num)
    print(f'Based on the age you entered, you are a {cat}.')
    esc = input('If this is correct, press Q to quit. Press any other key to try again. ')
    if esc == 'q' or esc =='Q':
        pass
    else:
        main()

main()
