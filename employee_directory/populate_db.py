from faker import Faker
from employees.models import Department, Employee
import random

fake = Faker()

# Создаем подразделения
for _ in range(25):
    Department.objects.create(name=fake.company())

# Создаем сотрудников
for _ in range(50000):
    Employee.objects.create(
        full_name=fake.name(),
        position=fake.job(),
        hire_date=fake.date_between(start_date='-10y', end_date='today'),
        salary=random.uniform(30000, 150000),
        department=Department.objects.order_by('?').first(),
    )