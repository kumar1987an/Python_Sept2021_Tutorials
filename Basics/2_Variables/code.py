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

print("\n")
print(name)
print(NAME)
print(employee_1)
print(ELEMENT_465)

college_passed_out_year = 2009  # Snake Case # Variables and Functions
College_Passed_Out_Year = 2009  # Pascal Case # Classes
College_passed_out_year = 2009  # Pascal Case # Classes
college_Passed_Out_Year = 2009  # Camel Case
college_Passed_out_year = 2009  # Camel Case

_length = 5
print(_length)

__length__ = 5
print(__length__)

_length_ = 5
print(_length_)

x, y, z = 45, 55, 65
print(x, y, z)

x = y = z = 10
print(x, y, z)
