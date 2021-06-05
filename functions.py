def brute_force(goal):
    x = 0

    while x**2<goal:
        x += 1
    if x**2 == goal:
        print(f'The square root of {goal} is {x}')
    else:
        print(f'I couldnt find the root')

def aproximation(goal, epsilon):
    respuesta = epsilon**2
    