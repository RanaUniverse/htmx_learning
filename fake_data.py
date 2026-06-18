"""
fake_data.py

Here i will generate the fake data there
"""

from faker import Faker

fake = Faker()


def generate_fake_name() -> str:
    name = fake.name_male()
    return name
