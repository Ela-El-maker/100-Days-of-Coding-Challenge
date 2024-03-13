password = 'cskdnjcasa#!'

if len(password) >=11:
    if '!' in password:
        print("Password correct")
    else:
        print('Invalid characters!')
else:
    print('Password too short!')