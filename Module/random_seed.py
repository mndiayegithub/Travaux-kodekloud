import random
#Do not uncomment below, otherwise random.seed() wont work
#from random import seed
#from random import randint
#from random import random

# Write the function random_seed
def random_seed(s):
    random.seed(s)
    value=random.random()
    return value

s = float(input("Enter a value: "))
print(random_seed(s))
