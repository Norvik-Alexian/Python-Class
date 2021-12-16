# Create a class for representing employee with some attributes (name, position, salary, workdays (weekdays), completed
# tasks names) and behavior (change position, check if salary is higher than some threshold, find how many days salary
# works per week, find if employee works on some specific weekday), create several employees and perform actions,
# check how many employees are defined.

class Employee:
    def __init__(self, name: str, position: str, salary: int, workdays: list, completed_tasks: list):
        self.name = name
        self.position = position
        self.salary = salary
        self.workdays = workdays
        self.completed_tasks = completed_tasks

    def change_position(self, new_position: str):
        self.position = new_position
        print(f'{self.position} is the new position of employee')

    def salary_amount(self, treshhold: int):
        if self.salary > treshhold:
            print(f'Salary which is {self.salary} is more than treshold')
        else:
            print(f'Salary which is {self.salary} is less than treshold')

    def workdays_checkup(self, specific_workdays: list):
        days = []
        for day in self.workdays:
            if day in specific_workdays:
                days.append(day)
        print(f'Employee works on {days}')


employee = Employee('Norvik', 'Software Developer', 1000, ['monday, friday, tuesday'], ['crawler, content generator'])
employee.change_position('NLP developer')
employee.salary_amount(800)
employee.workdays_checkup(['friday', 'wednesday', 'sunday'])
