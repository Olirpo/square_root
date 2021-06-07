import functions

def main():
    ciclo= True
    while ciclo:
        print("""
        Welcome to the square root calculator
        Here you will able to use three different methods for the square root
        """)
        option = int(input("""Please type your choose:
        1. Brute force search
        2. Approach search
        3. Binary search
        
        Your choose:"""))

        if option < 1 or option > 3:
            print('Please choose a correct option')

        elif option == 1:
            print('You choosed the brute force search, please type a number')
            functions.brute_force(int(input('Your number: ')))
        elif option == 2:
            print('You choosed the brute force search, please type a number')
            number = int(input('Your number: '))
            epsilon = float(input('Epsilon *if you dont know what is this just put 0,1* :'))
            functions.approach_search(number, epsilon)
        elif option == 3:
            print('You choosed the binary search, pleas type a number')
            number = int(input('Your number: '))
            epsilon = float(input('Epsilon *if you dont know what is this just put 0,1* :'))
            functions.binary_search(number, epsilon)










if __name__ == '__main__':
    main()