from pickle import TRUE
from marcssupercoolpack.lib import try_me

def test_dice_min_max():
    out = []
    for i in range(1000):
        out.append(try_me(faces = 6, return_int=True))
    assert min(out) == 1
    assert max(out) == 6

def test_dice_non_int():
    assert try_me(-3) == print('Non-euklidean dices are not supported, please contact your local Elder Deity.')
    assert try_me('snakes') == print('Non-euklidean dices are not supported, please contact your local Elder Deity.')
    assert try_me('4.5') == print('Non-euklidean dices are not supported, please contact your local Elder Deity.')
    assert try_me(range(4)) == print('Non-euklidean dices are not supported, please contact your local Elder Deity.')

def test_dice_is_one():
    assert try_me(1) == print("I don't think you understand how dice work...")
