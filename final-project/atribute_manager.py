def add_attribute(records: list, field: str, compute) -> list:
    """Добавляет каждой записи поле field со значением compute

    Параметры:
        records -- список плоских словарей
        field -- название нового поля
        compute -- функция, которая принимает одну запись
            и возвращает значение нового поля

    На выходе:
        Новый список копий записей с добавленным полем field
    """
    add_list = []
    for dictionary in records:
        temp = dictionary.copy()
        temp[field] = compute(dictionary)
        add_list.append(temp)
    return add_list


def remove_attribute(records: list, field: str) -> list:
    """Удаляет поле field у всех записей, где оно есть

    Параметры:
        records -- список плоских словарей
        field -- название поля, которое нужно удалит

    На выходе:
        Новый список копий записей без поля field
    """
    remove_list = []
    for dictionary in records:
        temp = dictionary.copy()
        if field in dictionary:
            del temp[field]
        remove_list.append(temp)
    return remove_list


if __name__ == '__main__':
    pass
