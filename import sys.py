import sys
class Employee:
    def __init__(self, EId, name, age, salary):
        self.EId=EId
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee(EId={self.EId},name={self.name}, age={self.age}, salary={self.salary})"

def age(employees):
    return sorted(employees, key=lambda x: x.age)

def name(employees):
    return sorted(employees, key=lambda x: x.name)

def salary(employees):
    return sorted(employees, key=lambda x: x.salary)

def printemp(employees):
    for employee in employees:
        print(employee)

def main():
    employees = [ 
        Employee("161E90","Raman",41,56000),
        Employee("161F91","Raman",41,56000),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)]
    ch="y" 
    while ch=="y" or ch=="Y":
        print("Choose a sorting parameter:")
        print("1. Age")
        print("2. Name")
        print("3. Salary")

        choice = input()

        if choice == "1":
            employees = age(employees)
        elif choice == "2":
            employees = name(employees)
        elif choice == "3":
            employees = salary(employees)
        else:
            print("Invalid choice")
            sys.exit(1)

        printemp(employees)
        print()
        print()
        ch=input("Continue(Y/N)?")

if __name__ == "__main__":
    main()
