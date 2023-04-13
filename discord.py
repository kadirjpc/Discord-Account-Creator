import requests
import random
import string

# function to generate a random string of specified length
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# function to generate a random email address
def random_email():
    domain = ["gmail.com", "yahoo.com", "hotmail.com"]
    return random_string(8) + "@" + random.choice(domain)

# function to generate a random password
def random_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

# main function to create discord account with random email and password
def create_discord_account():
    email = random_email()
    password = random_password(12)

    data = {
        'email': email,
        'password': password,
        'username': 'RandomUser',
        'invite': None,
        'fingerprint': None,
        'consent': True,
        'date_of_birth': '1990-01-01',
        'gift_code_sku_id': None
    }

    response = requests.post('https://discord.com/api/v9/auth/register', json=data)

    if response.status_code == 200:
        print("Account created successfully!")
        with open('tokens.txt', 'a') as f:
            f.write(email + ":" + password + ":" + response.json()['token'] + "\n")
    else:
        print("Failed to create account")

create_discord_account()
