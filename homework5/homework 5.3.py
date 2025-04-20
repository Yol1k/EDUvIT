import random
import json
import string
from faker import Faker

symbols = string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(12):
    password += random.choice(symbols)

fake=Faker("en_US")

age = random.randint(1,100)

data = {
    "name": fake.name(),
    "age": age,
    "email": fake.email(),
    "password": password
    }
json_string = json.dumps(data)

filename="file.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data,f)
    
with open(filename, 'r', encoding='utf-8') as f:
    a = json.load(f)

print(a)
