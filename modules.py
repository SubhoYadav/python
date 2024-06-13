import math
print(math.pi)
from kansas_module import random_fun_fact, capital as kansas_capital
import kansas_module as knsmd

# View the contents of the module
# for item in dir(math):
#     print(item)

print(__name__)
print(kansas_capital)
random_fun_fact()
print(knsmd.__name__)

