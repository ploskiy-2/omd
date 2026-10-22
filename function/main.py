import csv 

INPUT_FILE = "Corp_Summary.csv"
HEADERS = ["FIO", "Department", "Team", "Position", "Mark", "Salary"]
OUTPUT_FILE = "Output.csv"

def read_file() -> list[dict]:
    """
    Считываем информацию о сотрудниках из файла. Каждый сотрудник - это словарь
    с ключами из HEADERS. Возвращаем список таких словарей
    """
    with open(INPUT_FILE, mode="r", encoding="UTF-8") as file:
        reader = csv.DictReader(file, 
                                delimiter=";",
                                fieldnames=HEADERS)
        next(reader)
        employees = []
        for row in reader:
            row["Salary"] = int(row["Salary"])
            row["Mark"] = float(row["Mark"])
            employees.append(row)
        return employees

def get_department_info(employee_data: list[dict]) -> dict:
    departments = {}
    for employee in employee_data:
        department_name = employee["Department"]
        salary = employee["Salary"]
        if department_name not in departments:
            departments[department_name] = {
                "Team_unique": set(),
                "Employee_count": 0,
                "Min_salary": salary,
                "Max_salary": salary,
                "Sum_salary": 0}
        department = departments[department_name]
        department["Team_unique"].add(employee["Team"])
        department["Employee_count"] += 1
        department["Min_salary"] = min(department["Min_salary"], salary)
        department["Max_salary"] = max(department["Max_salary"], salary)
        department["Sum_salary"] += salary
              
    return departments

def report_1(employee_data: list[dict]) -> None:

    departments = get_department_info(employee_data)
    print("Департамент --- Команды")
    for department_name, department_info in departments.items():
        teams = ", ".join(department_info["Team_unique"])
        print(f"{department_name}: {teams}")

def report_2(employee_data: list[dict]) -> None:

    departments = get_department_info(employee_data)
    for department_name, department_info in departments.items():
        print(f"Департамент: {department_name}")
        print(f"Количество сотрудников = {department_info["Employee_count"]}")
        print(f"Минимальная зарплата = {department_info["Min_salary"]}")
        print(f"Максимальная зарплата = {department_info["Max_salary"]}")
        print(f"Средняя зарплата = {round(department_info["Sum_salary"] / department_info["Employee_count"], 2)}")

        print()

def report_3(employee_data: list[dict]) -> None:
    report_headers = ["Department", "Employee Сount", 
                       "Min Salary", "Max Salary", "Avg Salary"]
    departments = get_department_info(employee_data)
    with open(OUTPUT_FILE, mode="w", encoding="UTF-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=report_headers)
        writer.writeheader()
        
        for department_name, department_info in departments.items():
            avg_salary = round(department_info["Sum_salary"] / department_info["Employee_count"], 2)
            writer.writerow({
                "Department": department_name,
                "Employee Count": department_info["Employee_count"],
                "Min Salary": department_info["Min_salary"],
                "Max Salary": department_info["Max_salary"],
                "Avg Salary": avg_salary
            })

def main(report_number: int) -> None:
    employee_data = read_file()

    if report_number == 1:
        report_1(employee_data)
    elif report_number == 2:
        report_2(employee_data)
    elif report_number == 3:
        report_3(employee_data)
    else:
        raise ValueError('Введен неверный номер для создания отчета')

if __name__ == "__main__":
    report_number = int(input("Введите номер отчета: "))
    main(report_number)
     