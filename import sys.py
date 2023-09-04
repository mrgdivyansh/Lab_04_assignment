import sys
class Employee:
    def __init__(self, EId, name, age, salary):
        self.EId=EId
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee(EId={self.EId},name={self.name}, age={self.age}, salary={self.salary})"

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
        Employee("161E90","Raman",41,56000),
        Employee("161F91","Raman",41,56000),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)]
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
