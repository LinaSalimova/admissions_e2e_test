import dataclasses


@dataclasses.dataclassinstal
class Data:
    name: str
    last_name: str
    email: str
    gender: str
    number: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects: list
    hobbies: list
    address: str
    state: str
    city: str


test_data = Data(
    name="test_name",
    last_name="test_last_name",
    email="test@gmail.com",
    gender="Female",
    number="0123456789",
    day_of_birth="1",
    month_of_birth="January",
    year_of_birth="1942",
    subjects=["History", "Maths"],
    hobbies=["Reading", "Music"],
    address="Some-street, Some-house, Some-apartment",
    state="Haryana",
    city="Panipat"
)