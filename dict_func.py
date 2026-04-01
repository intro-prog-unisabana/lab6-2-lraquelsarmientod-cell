# Write your code here!
def employee_print(employee_info):
    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")

    extra_info = employee_info.copy()

    extra_info.pop("Name", None)
    extra_info.pop("Salary", None)
    extra_info.pop("Role", None)

    if len(extra_info) == 0:
        print("No other info!")
    else:
        for key, value in extra_info.items():
            print(f"{key}: {value}")