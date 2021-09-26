# String Datatype methods

string_1 = "foo baz bar jazz bazz"
string_2 = "-16273537830"
string_3 = "     {}     ".format(string_1)
string_4 = "{}.6789".format(string_2)
print("These are the methods available for string class under string_1 variable")
print(
    "Also these string_1 methods would be the same as dir(str) as string_1 have str data type"
)
print(
    "========================================================================================"
)
print(dir(string_1))
print()
print(string_1.upper())
print(string_1.lower())
print(string_1.title())
print(string_1.capitalize())
print(string_1.startswith("foo ba"))
print(string_1.endswith("az"))
print(string_1.count("ba"))
print(string_1 + " {}".format("baaz"))
print(string_1.encode())
print(string_1.split())
print(string_3.strip())
print(string_1.isalpha())
print(string_2.isdigit())
print(string_3.isspace())
print(string_4.isdecimal())
