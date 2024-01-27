import random
import string
import os
import csv
from datetime import datetime, timedelta
import pandas as pd


# Function to generate random new customer data
def generate_random_user():
    first_names = ["Rupa", "Pawan", "Priyanka", "Arun"]
    last_names = ["Singh", "Yadav", "Sharma", "Pandey"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    random_number = str(random.randint(100, 999))
    email = f"{first_name.lower()}_{last_name.lower()}{random_number}@gmail.com"

    password_length = 8
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters) for i in range(password_length))

    gender = "Female" if first_name in ['Rupa', 'Priyanka'] else "Male"

    today = datetime.now()
    birth_date = today - timedelta(
        days=random.randint(18 * 365, 60 * 365))  # Assuming a person can be between 18 and 60 years old
    formatted_birth_date = birth_date.strftime('%m-%d-%Y')

    comment = "Random comment for user " + first_name + " " + last_name

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "gender": gender,
        "birth_date": formatted_birth_date,
        "company_name": random.choice(['TCS', 'Walmart', 'Wipro', 'HCL']),
        "comment": comment,
        "tax_exempt": random.choice([True, False]),
        "manager_vendor": random.choice(['1', '2']),
        "account_status": random.choice([True, False]),
        "newsletter": [random.choice(["Your store name", "Test store 2"])],
        "customer_role": [random.choice(["Registered", "Guests", "Administrators"])]
    }


def saveNewCustomerData2CSV(data, filename):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

