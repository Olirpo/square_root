import functions

def main():
    ciclo= True
    while ciclo:
        print("""
        Welcome to the square root calculator
        Here you will able to use three different methods for the square root
        """)
        option = input("""Please type your choose:
        1. Brute force search
        2. Approach search
        3. Binary search
        Your choose:
        """)

        if option < 1 or option > 3:
            print('Please choose a correct option')








if __name__ == '__main__':
    main()