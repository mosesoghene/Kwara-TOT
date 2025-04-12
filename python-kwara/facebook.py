user = {
    "username": "@LocalDevv".lower(),
    "password": "password",
    "age": 28,
    "email": "e@ma.il"
}

username = input("Enter username -> ").lower()
password = input("Enter password -> ")

# if username == user['username'] and password == user['password']:
#     print("Welcome, ", user['username'])
# elif username== user['username'] and password != user['password']:
#     print("Incorrect password")
# elif username != user['username']:
#     print("No user with username: ", username)
# else:
#     print("invalid credentials")

if username == user.get('username') and password == user.get('password'):
    print("Welcome, ", user.get('username'), "you are", user.get("age"), "Years old.")
elif username== user.get('username') and password != user.get('password'):
    print("Incorrect password")
elif username != user.get('username'):
    print("No user with username: ", username)
else:
    print("invalid credentials")