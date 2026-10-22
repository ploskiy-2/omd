import csv

INPUT_FILE = "Corp_Summary.csv"
HEADERS = ["FIO", "Department", "Team", "Position", "Mark", "Salary"]
OUTPUT_FILE = "Output.csv"


def read_file() -> list[dict]:
    """Прочитать CSV-файл с сотрудниками.

    Ключи словарей берутся из HEADERS, Salary и Mark конвертируются
    в числа.

    Возвращает список сотрудников, где информация о сотруднике в виде словаря.
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
    """Собрать статистику по департаментам.

    Для каждого департамента находим все команды, число сотрудников,
    минимальный, максимальный и суммарный оклад

    Аргументы:
    employee_data -- список сотрудников из read_file()

    Возвращает словарь: название департамента -> его статистика
    """
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
    """Вывести департаменты и входящие в них команды."""
    departments = get_department_info(employee_data)
    print("Департамент --- Команды")
    for department_name, department_info in departments.items():
        teams = ", ".join(department_info["Team_unique"])
        print(f"{department_name}: {teams}")


def report_2(employee_data: list[dict]) -> None:
    """Вывести сводку по департаментам.

    Для каждого департамента: число сотрудников, минимальная,
    максимальная и средняя зарплата
    """
    departments = get_department_info(employee_data)
    for department_name, department_info in departments.items():
        print(f"Департамент: {department_name}")
        print(f"Количество сотрудников = {department_info["Employee_count"]}")
        print(f"Минимальная зарплата = {department_info["Min_salary"]}")
        print(f"Максимальная зарплата = {department_info["Max_salary"]}")
        sum_salary = department_info["Sum_salary"]
        employee_count = department_info["Employee_count"]
        avg_salary = round(sum_salary / employee_count, 2)
        print(f"Средняя зарплата = {avg_salary}")
        print()


def report_3(employee_data: list[dict]) -> None:
    """Сохранить сводку аналогичную report_2() в файл OUTPUT_FILE."""
    report_headers = ["Department", "Employee Count",
                      "Min Salary", "Max Salary", "Avg Salary"]
    departments = get_department_info(employee_data)
    with open(OUTPUT_FILE, mode="w", encoding="UTF-8",
              newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=report_headers)
        writer.writeheader()

        for department_name, department_info in departments.items():
            avg_salary = round(
                department_info["Sum_salary"]
                / department_info["Employee_count"], 2)
            writer.writerow({
                "Department": department_name,
                "Employee Count": department_info["Employee_count"],
                "Min Salary": department_info["Min_salary"],
                "Max Salary": department_info["Max_salary"],
                "Avg Salary": avg_salary
            })


def main(report_number: int) -> None:
    """Прочитать файл и запустить отчет с выбранным номером.

    Аргументы:
    report_number -- номер отчета: 1, 2 или 3

    Выбрасывает ValueError, если номер не 1, 2 или 3
    """
    employee_data = read_file()

    if report_number == 1:
        report_1(employee_data)
    elif report_number == 2:
        report_2(employee_data)
    elif report_number == 3:
        report_3(employee_data)
    else:
        raise ValueError("Введен неверный номер для создания отчета")


if __name__ == "__main__":
    report_number = int(input("Введите номер отчета: "))
    main(report_number)
