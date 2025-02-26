import faker
import random

fake = faker.Faker()

def generate_emails():

    first_name = fake.first_name()
    last_name = fake.last_name()
    dm_weights = [0.5, 0.2, 0.05, 0.05, 0.2]
    domain = random.choices(["gmail", "outlook", "hotmail", "yahoo", "icloud"], dm_weights, k = 1)
    extension = "com"
    email = f"{first_name}{last_name}@{domain[0]}.{extension}"

    return [first_name, last_name, email]

# print(generate_emails())