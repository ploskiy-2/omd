import csv 

INPUT_FILE = "Corp_Summary.csv"
HEADERS = ["FIO", "Department", "Team", "Position", "Mark", "Salary"]

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

def get_departmet_info(employee_data: list[dict]) -> dict:
    departments = {}
    for employee in employee_data:
        department_name = employee["Department"]
        salary = employee["Salary"]
        if employee["Department"] not in departments:
            departments[employee["Department"]] = {
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

    departments = get_departmet_info(employee_data)
    print("Департамент --- Команды")
    for key, value in departments.items():
        print(f"{key}: {value["Team_unique"]}")

def report_2() -> None:
    return

def report_3() -> None:
    return

if __name__ == "__main__":
    report_number = int(input("Введите номер отчета: "))
    employee_data = read_file()

    if report_number == 1:
        report_1()
    elif report_number == 2:
        report_2()
    elif report_number == 3:
        report_3()
    else:
        raise ValueError('Введен неверный номер для создания отчета')
     