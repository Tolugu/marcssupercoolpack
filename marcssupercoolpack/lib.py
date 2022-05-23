def try_me(faces = 6):
    from random import sample

    if (not type(faces) == int) or (faces <1):
        return print('Non-euklidean dices are not supported, please contact your local Great Old One.')
    if faces == 1:
        return print("I don't think you understand how dice work...")
    roller = range(1,faces+1)
    roll = sample(roller, 1)
    return print(f'You rolled a {roll[0]}, use faces = x to pick your die.')

try_me(-3)
