import employees
import productivity

manager = employees.Manager(1, 'John Smith', 1500)
secretary = employees.Secretary(2, 'Jane Doe', 40)
salesperson = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(4, 'Pete Peterson', 40, 15)

employees_list = [manager, secretary, salesperson, factory_worker] 

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees_list, 40)

payroll_system = employees.PayrollSystem()
payroll_system.calculate_payroll(employees_list)