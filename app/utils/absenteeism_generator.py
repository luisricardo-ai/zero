import random
import pandas as pd
from faker import Faker


def generate_absenteeism_data() -> pd.DataFrame:
    """
    Generate absenteeism data.

    Returns:
        pd.DataFrame: Absenteeism dataframe.
    """
    faker = Faker("en")

    departments = [
        "Human Resources",
        "Finance",
        "Marketing",
        "IT",
        "Sales",
        "Operations",
        "Legal",
        "Engineering",
        "Customer Service",
        "R&D",
    ]
    
    reasons = [
        "Illness",
        "Personal issues",
        "Medical appointment",
        "Business trip",
        "Others",
    ]


    data = data = {
        "employee_id": [faker.unique.random_number(digits=5) for _ in range(10)],
        "employee_name": [faker.name() for _ in range(10)],
        "department": [faker.random_element(elements=departments) for _ in range(10)],
        "absence_reason": [faker.random_element(elements=reasons) for _ in range(10)],
        "absence_hours": [faker.random_int(min=1, max=8) for _ in range(10)],
        "absence_date": [
            faker.date_between_dates(
                date_start=pd.to_datetime("2023-06-01"),
                date_end=pd.to_datetime("2023-06-30"),
            )
            for _ in range(10)
        ],
        "salary": [round(random.uniform(2500, 12500), 2) for _ in range(10)],
    }

    df = pd.DataFrame(data)
    df["absence_date"] = pd.to_datetime(df["absence_date"])

    return df