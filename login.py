import time
user_name = 'kunal pal'
password = 'kunal9810'

user_name_input = input("Enter username: ")
password_input =input("Enter password: ")

if user_name_input==user_name and password_input==password:
    print('Access granted')
    print('Please wait')
    time.sleep(5)
    print('Ok... Loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Alright you have security clearance. Pulling up the secret mainframe.')

elif user_name_input==user_name and password_input!=password:
    print('Password incorrect')
elif user_name_input!=user_name and password_input==password:
    print('Username incorrect')
else:
    print('You might wanna check both fields...')
