#Boolean Logic in python(and and or operators)
username = "admin"
password = "key"

#and operator checks upon both conditions to be true
if username == "admin" and password == "key":
    print("Valid User")
else:
    print("Invalid user")

# The or operator will check only one of the conditions
username2 = "user"
password2 = "password"
if username2 == "admin" or password2 == "key":
    print("Valid User")
else:
    print("Invalid user")
