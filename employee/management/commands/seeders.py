from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from employee.models import (
    Bill, Country, Document, EmployeeDocument, Cycle, EmployeeCycle, EmplpoyeeLog,
    TimeSheet, EmployeeTimeSheet, EmployeeTimeSheetVerification, Position,
    EmployeePosition, EmployeeProfile
)
from user.models import Role
import random
from datetime import timedelta
from client.models import Client, CasualOrder, Contract


User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Create Countries
        countries = [
            Country.objects.create(name='United States', code='US'),
            Country.objects.create(name='United Kingdom', code='UK'),
            Country.objects.create(name='Canada', code='CA'),
        ]

        # Create Roles
        roles = [
            Role.objects.create(name='Manager'),
            Role.objects.create(name='Team Leader'),
            Role.objects.create(name='Employee'),
        ]

        # Create Users
        users = []
        for i in range(10):
            user = User.objects.create(
                IID=f'EMP{i+1:03d}',
                username=f'user{i+1}',
                email=f'user{i+1}@example.com',
                first_name=f'First{i+1}',
                last_name=f'Last{i+1}',
                mobile_number=f'+1234567890{i}',
            )
            users.append(user)

        # Create Bills
        for i in range(5):
            Bill.objects.create(number=f'BILL{i+1:05d}')

        # Create Documents
        documents = [
            Document.objects.create(name='Passport', required=True),
            Document.objects.create(name='Visa', required=True),
            Document.objects.create(name='Driver License', required=False),
        ]

        # Create Employee Documents
        for user in users:
            for doc in documents:
                EmployeeDocument.objects.create(
                    document_type=doc,
                    employee=user,
                    file=f'path/to/{doc.name.lower().replace(" ", "_")}.pdf',
                    issued_date=timezone.now().date() - timedelta(days=random.randint(1, 365)),
                    expiry_date=timezone.now().date() + timedelta(days=random.randint(1, 365)),
                )

        # Create Cycles
        cycles = [
            Cycle.objects.create(order=1, name='Training', description='Initial training period'),
            Cycle.objects.create(order=2, name='Probation', description='Probation period'),
            Cycle.objects.create(order=3, name='Regular', description='Regular employment'),
        ]

        # Create Employee Cycles
        for user in users:
            EmployeeCycle.objects.create(employee=user, cycle=random.choice(cycles))

        # Create Employee Logs
        for user in users:
            EmplpoyeeLog.objects.create(employee=user, info='Joined the company')

        # Create Clients
        clients = []
        for i in range(5):
            client = Client.objects.create(
                name=f'Client {i+1}',
                location=f'Location {i+1}',
                contact_manager_name=f'Manager {i+1}',
                contact_manager_email=f'manager{i+1}@client{i+1}.com',
                contact_manager_number=f'123456789{i}',
                email=f'info@client{i+1}.com',
                number=f'987654321{i}'
            )
            clients.append(client)

        # Create CasualOrders
        for client in clients:
            for _ in range(3):
                CasualOrder.objects.create(
                    client=client,
                    by=random.choice(['Phone', 'Email', 'In-person']),
                    medium=random.choice(['Phone', 'Email', 'In-person']),
                    rate=random.uniform(50, 200),
                    is_hourly=random.choice([True, False])
                )

        # Create Contracts
        for client in clients:
            Contract.objects.create(
                client=client,
                expiry_date=timezone.now().date() + timedelta(days=random.randint(30, 365)),
                is_terminated=random.choice([True, False]),
                is_terminate_date=timezone.now().date() if random.choice([True, False]) else None,
                termination_reason='Sample termination reason' if random.choice([True, False]) else None,
                rate=random.uniform(100, 500),
                is_hourly=random.choice([True, False]),
                document='path/to/contract_document.pdf'
            )




        # Create TimeSheets
        timesheets = []
        for _ in range(20):
            timesheet = TimeSheet.objects.create(
                drop_time=timezone.now() - timedelta(hours=random.randint(1, 24)),
                drop_driver=random.choice(users),
                pickup_time=timezone.now(),
                pickup_driver=random.choice(users),
                working_hours=random.randint(4, 12),
                client=random.choice(clients),
                department='IT',
                duty_time=timezone.now() - timedelta(hours=random.randint(1, 24)),
                duty_date=timezone.now().date() - timedelta(days=random.randint(0, 30)),
                is_invoiced=random.choice([True, False]),
            )
            timesheets.append(timesheet)

        # Create Employee TimeSheets
        for user in users:
            for timesheet in random.sample(timesheets, k=random.randint(1, 5)):
                EmployeeTimeSheet.objects.create(
                    employee=user,
                    timesheet=timesheet,
                    duty_start_time=timesheet.duty_time,
                    total_duty_hours=timesheet.working_hours,
                    rate=random.uniform(10, 50),
                    is_absent=random.choice([True, False]),
                    remark='Sample remark',
                    is_verified=random.choice([True, False]),
                )

        # Create Employee TimeSheet Verifications
        for timesheet in EmployeeTimeSheet.objects.all():
            EmployeeTimeSheetVerification.objects.create(
                timesheet=timesheet,
                verified_by=random.choice(users),
            )

        # Create Positions
        positions = [
            Position.objects.create(name='Software Developer', job_description='Develops software'),
            Position.objects.create(name='Project Manager', job_description='Manages projects'),
            Position.objects.create(name='HR Specialist', job_description='Handles human resources'),
        ]

        # Create Employee Positions
        for user in users:
            EmployeePosition.objects.create(
                position=random.choice(positions),
                employee=user,
            )

        # Create Employee Profiles
        for user in users:
            EmployeeProfile.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                country=random.choice(countries),
                contact_number=user.mobile_number,
                passport_size_photo='path/to/photo.jpg',
                status=random.choice(EmployeeProfile.Status.choices)[0],
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))