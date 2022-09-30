class ProductivitySystem:


    def track(self, employees, hours):
        print("tracking employee productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
        print(" ")