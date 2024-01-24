class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_sorted_data(self, sorting_parameter):
        if sorting_parameter == 1:  # Sort by Age
            sorted_employees = sorted(self.employees, key=lambda x: x.age)
        elif sorting_parameter == 2:  # Sort by Name
            sorted_employees = sorted(self.employees, key=lambda x: x.name)
        elif sorting_parameter == 3:  # Sort by Salary
            sorted_employees = sorted(self.employees, key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter.")
            return

        print("\nSorted Data:")
        print("{:<8} {:<10} {:<5} {:<10}".format("Emp ID", "Name", "Age", "Salary (PM)"))
        for employee in sorted_employees:
            print("{:<8} {:<10} {:<5} {:<10}".format(
                employee.emp_id, employee.name, employee.age, employee.salary))

database = EmployeeDatabase()
database.add_employee(Employee("161E90", "Ramu", 35, 59000))
database.add_employee(Employee("171E22", "Tejas", 30, 82100))
database.add_employee(Employee("171G55", "Abhi", 25, 100000))
database.add_employee(Employee("152K46", "Jaya", 32, 85000))

sorting_param = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
database.display_sorted_data(sorting_param)
