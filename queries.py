from peewee import fn

from cltsalary.model import db, Employee

def main():
     query = Employee.select().where(Employee.name.contains('Lyles'))
     lyles = [employee for employee in query]
     print(f'There are {len(lyles)} employees with last name Lyles.')

     query = Employee.select().where(Employee.job_title == 'Mayor')
     mayors = [employee for employee in query]
     print(f'There is {len(mayors)} mayor employees.')

     max_salary = Employee.select(fn.MAX(Employee.salary)).scalar()
     print(f'The max salary is {max_salary}.')

     query = Employee().select().where(Employee.salary == max_salary)
     max_salary_employee = [employee for employee in query][0]

     print(f'The employee with the highest salary is '
            f'{max_salary_employee.name}, who is the '
            f'{max_salary_employee.job_title}.')

if __name__ == "__main__":
    main()
