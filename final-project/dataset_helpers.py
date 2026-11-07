def filter_records(records: list, condition) -> list:
    """Оставляет записи, для которых condition возвращает True

    Параметры:
        records -- список плоских словарей
        condition -- функция, которая принимает одну запись

    На выходе:
        Список только тех записей, для которых condition вернула True
    """
    filter_list = []
    for dictionary in records:
        if condition(dictionary):
            filter_list.append(dictionary)
    return filter_list


def group_by_attributes(records: list, fields: list) -> dict:
    """Группирует записи по значениям полей

    Параметры:
        records -- список плоских словарей
        fields -- список названий полей, по которым группируем

    На выходе:
        Словарь, где ключ - кортеж значений полей fields,
        а значение - список записей с такими значениями
    """
    groups_dict = {}
    for dictionary in records:
        temp = []
        for field in fields:
            temp.append(dictionary.get(field))
        key = tuple(temp)

        if key not in groups_dict:
            groups_dict[key] = []
        groups_dict[key].append(dictionary)
    return groups_dict


def apply_aggregation(groups: dict, aggregation, field: str) -> dict:
    """Применяет aggregation к каждой группе: {ключ: число}

    Параметры:
        groups -- словарь групп
        aggregation -- функция из aggregations.py,
            которая принимает список записей и название поля
        field -- название поля, по которому считаем агрегацию

    На выходе:
        Словарь с теми же ключами, что в groups,
        и результатом агрегации для каждой группы
    """
    aggregation_dict = {}
    for key in groups:
        aggregation_dict[key] = aggregation(groups[key], field)
    return aggregation_dict


if __name__ == '__main__':
    pass
