from string import digit
from itertools import product

for passcode in product( digits , repeat=4):
    print("".join(passcode))