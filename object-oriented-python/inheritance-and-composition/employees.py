# Calculating the payroll for all the employees in the company
from abc import ABC, abstractmethod
class PayrollSystem:

    def calculate_payroll(self, employees):
        print("Calculate Payroll")
        print("=================")

        for employee in employees:
            print(f"Payroll for {employee.id} - {employee.name}")
            print(f"- Check Amount {employee.calculate_payroll()}")
            print("")


class Employee(ABC):
    """
    This is an abstract class, with an abstract method 
    """

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll():
        pass

class SalaryEmployee(Employee):
    
    def __init__(self, id, name, weekly_salary) -> None:
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):

    def __init__(self, id, name, hours_worked, hour_rate) -> None:
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hour_rate * self.hours_worked


class ComissionEmployee(SalaryEmployee):

    def __init__(self, id, name, weekly_salary, comission) -> None:
        super().__init__(id, name, weekly_salary)
        self.comission = comission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return self.weekly_salary + self.comission

class Manager(SalaryEmployee):

    def work(self, hours):
        print(f'{self.name} screams and yells for P {hours} hours.')


class Secretary(SalaryEmployee):

    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing the office paperwork.' )

class SalesPerson(ComissionEmployee):

    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.' )

class FactoryWorker(HourlyEmployee):

    def work(self, hours):
        print(f'{self.name} manufactures goods for {hours} hours.' )
