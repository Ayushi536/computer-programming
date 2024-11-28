"""
ques.1 : Nested Dictionary Access and Manipulation
Update the department to "HR".
"""
employee = {"name": "Ayushi", "details": {"age": 25, "department": "IT"}}
employee["details"]["department"] = "HR"
print(employee)
