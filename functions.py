def brute_force(goal):
    x = 0

    while x**2 < goal:
        x += 1
    if x**2 == goal:
        print(f'The square root of {goal} is {x}')
    else:
        print(f'I couldnt find the root')


def approach_search(goal, epsilon):
    step = epsilon**2
    answer = 0.0

    while abs(answer**2 - goal) >= epsilon and answer <= goal:
        answer += step
    if abs(answer**2 - goal) >= epsilon:
        print(f'I couldnt find the square root of {goal}')
    else:
        print(f'The square root of {goal} is {answer}')


def binary_search(goal, epsilon):
    lower = 0.0
    top = max(1.0, goal)
    answer = (lower + top) / 2

    while abs(answer**2 - goal) >= epsilon:
        if answer**2 > goal:
            top = answer
        else:
            lower = answer
        answer = (lower + top) / 2

    print(f'The square root of {goal} is {answer}')

