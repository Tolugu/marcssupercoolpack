def try_me(faces = 6, return_int = False):
    from random import sample

    if (not type(faces) == int) or (faces <1):
        return print('Non-euklidean dices are not supported, please contact your local Elder Deity.')
    if faces == 1:
        return print("I don't think you understand how dice work...")
    roller = range(1,faces+1)
    roll = (sample(roller, 1))[0]
    if return_int == True:
        return roll
    return print(f'You rolled a {roll}, use faces = x to pick your die.')

try_me(-3)
