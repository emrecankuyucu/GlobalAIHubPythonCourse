#Question 1

# userName="emre"
# password="1234"

# inputUserName=input("Please enter your username")
# inputPassword=input("Please enter your password")

# if (userName==inputUserName and password==inputPassword):
#     print("login succeeded")
# elif  (userName!=inputUserName and password==inputPassword):
#     print("wrong username")
# elif( userName==inputUserName and password!=inputPassword):
#     print("wrong passwornd")
# else:
#     print("login failes")
    

#Extra

user={
    "userName":"can",
    "password":"12345"
}

inputUserName=input("Please enter your username")
inputPassword=input("Please enter your password")

if (user["userName"]==inputUserName and user["password"]==inputPassword):
    print("login succeeded")
elif  (user["userName"]!=inputUserName and user["password"]==inputPassword):
    print("wrong username")
elif( user["userName"]==inputUserName and user["password"]!=inputPassword):
    print("wrong passwornd")
else:
    print("login failes")