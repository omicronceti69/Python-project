class Employee:
    def _init_(self, emp_id, name, age, department, tenure, attrition):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.tenure = tenure
        self.attrition = attrition  # True for left, False for stayed

class EmployeeRetentionAnalytics:
    def _init_(self):
        self.employees = []

    def create_employee(self, emp_id, name, age, department, tenure, attrition):
        employee = Employee(emp_id, name, age, department, tenure, attrition)
        self.employees.append(employee)
        print(f"Employee {name} added.")

    def read_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return vars(emp)
        return "Employee not found."

    def update_employee(self, emp_id, **kwargs):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                for key, value in kwargs.items():
                    setattr(emp, key, value)
                print(f"Employee {emp_id} updated.")
                return
        print("Employee not found.")

    def delete_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f"Employee {emp_id} deleted.")
                return
        print("Employee not found.")

    def calculate_tenure(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return f"Employee {emp.name} has a tenure of {emp.tenure} years."
        return "Employee not found."

    def predict_attrition_rate(self):
        total_employees = len(self.employees)
        if total_employees == 0:
            return "No employee data available."
        attrition_count = sum(emp.attrition for emp in self.employees)
        attrition_rate = (attrition_count / total_employees) * 100
        return f"Predicted attrition rate: {attrition_rate:.2f}%"

    def employee_demographics(self):
        demographics = {}
        for emp in self.employees:
            demographics[emp.department] = demographics.get(emp.department, 0) + 1
        return demographics

    def feedback_analysis(self, feedback_list):
        positive_feedback = sum(1 for feedback in feedback_list if "good" in feedback.lower())
        return f"Positive feedback percentage: {positive_feedback / len(feedback_list) * 100:.2f}%" if feedback_list else "No feedback available."

    def identify_retention_factors(self):
        departments = {}
        for emp in self.employees:
            if emp.attrition:
                continue
            departments[emp.department] = departments.get(emp.department, 0) + 1
        return departments

# Sample usage
analytics = EmployeeRetentionAnalytics()
analytics.create_employee(1, "Alice", 30, "Engineering", 5, False)
analytics.create_employee(2, "Bob", 28, "HR", 2, True)
analytics.create_employee(3, "Charlie", 35, "Engineering", 3, False)

print(analytics.read_employee(1))
analytics.update_employee(1, age=31, tenure=6)
print(analytics.calculate_tenure(1))
print(analytics.predict_attrition_rate())
print(analytics.employee_demographics())
feedbacks = ["The work environment is good", "Management is not supportive"]
print(analytics.feedback_analysis(feedbacks))
print(analytics.identify_retention_factors())
