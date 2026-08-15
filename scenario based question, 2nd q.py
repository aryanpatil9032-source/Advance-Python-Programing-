class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        return "Low Salary"


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display(self):
        for employee in self.employees:
            print(employee.employee_id, employee.name, employee.salary, employee.category())


company = Company()

company.add_employee(Employee(101, "Aryan", 75000))
company.add_employee(Employee(102, "Rahul", 50000))
company.add_employee(Employee(103, "Amit", 30000))

company.display()
