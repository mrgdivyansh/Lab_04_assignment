import sys
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age}, salary={self.salary})"

def sort_by_age(employees):
    return sorted(employees, key=lambda x: x.age)

def sort_by_name(employees):
    return sorted(employees, key=lambda x: x.name)

def sort_by_salary(employees):
    return sorted(employees, key=lambda x: x.salary)

def print_employees(employees):
    for employee in employees:
        print(employee)

def main():
    employees = [
        Employee("John", 30, 50000),
        Employee("Jane", 25, 40000),
        Employee("Jack", 35, 60000),
        Employee("Jill", 28, 45000)
    ]

    print("Choose a sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = input()

    if choice == "1":
        employees = sort_by_age(employees)
    elif choice == "2":
        employees = sort_by_name(employees)
    elif choice == "3":
        employees = sort_by_salary(employees)
    else:
        print("Invalid choice")
        sys.exit(1)

    print_employees(employees)

if __name__ == "__main__":
    main()