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
        return list(reader)


def report_1(employee_data: list[dict]) -> None:
    """
    На вход будем получать информацию о всех сотрудниках
    Создать словарь: Департамент - Команда 
    """
    departments = {}
    for employee in employee_data:
        if employee["Department"] not in departments:
            departments[employee["Department"]] = (employee["Team"])
        else:
            departments[employee["Department"]].add(employee["Team"])
    print("Департамент --- Команды")
    for key, value in departments.items():
        print(f"{key}: {value}")

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
     