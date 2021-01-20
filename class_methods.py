
class Employee:
    def __init__(self, name='John', num_of_years_exp=11, position='QA Engineer'):
        self.Name = name
        self.num_of_years_exp = num_of_years_exp
        self.position = position
        print(f"{self.Name} employee is created")

    def calculate_salary(self):
        if self.num_of_years_exp > 10:
            print(f"{self.Name}'s salary is 100k")

        elif self.num_of_years_exp == 10:
            print(f"{self.Name}'s salary is 90k")

        else:
            print(f"{self.Name}'s salary is 70k")

    def emp_description(self):
        print(f"This is {self.Name}, and {self.Name} has been working for {self.num_of_years_exp} as a {self.position}")


j = Employee('July', 10, 'Business Analyst')
j.calculate_salary()
j.emp_description()