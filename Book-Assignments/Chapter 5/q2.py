class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = float(salary)

    @classmethod
    def from_string(cls, employee_str):
        name, emp_id, salary = employee_str.split(",")
        return cls(name, emp_id, salary)
        
    def display_employee_info(self):
        print(f"Employee #{self.employee_id}:", f"\nName: {self.name}", f"\nSalary: {self.salary}")


emp1 = Employee("Osama Ahmed", "OSA1", 6870.58)
emp2Str = "Ahmed Osama,OSA2, 5250.98"
emp2 = Employee.from_string(emp2Str)

emp1.display_employee_info()
print("=====================")
emp2.display_employee_info()