# Variables explanation

name = "Python"

NAME = "Python"

employee_1 = "xyz"

ELEMENT_465 = "Iron"


# 23rd_day = "Thursday"  ### Wrong way to use variable name

number_of_kilometer_xyz_athelet_ran = 11  # This is Good
numberofkilometerxyzatheletran = (
    11  # This is programatically correct by wrong based PEP
)
# number-of-kilometer-xyz-athelet-ran = 11 # This is not correct


# This code represent keywords as variables
from keyword import kwlist

for item in kwlist:
    print(item, end=", ")


print(name)
print(NAME)
print(employee_1)
print(ELEMENT_465)
