import statistics


def field_values(records: list, field: str) -> list:
    """Собирает значения поля field из записей, пропуская None

    Параметры:
        records -- список плоских словарей
        field -- название поля

    На выходе:
        Список заполненных значений поля field
    """
    field_output = []
    for dictionary in records:
        if dictionary.get(field) is not None:
            field_output.append(dictionary[field])
    return field_output


def count_values(records: list, field: str) -> int:
    """Считает записи, у которых поле field заполнено

    Параметры:
        records -- список плоских словарей
        field -- название поля

    На выходе:
        Количество записей с заполненным полем field
    """
    return len(field_values(records, field))


def mean_value(records: list, field: str) -> float:
    """Среднее значение поля field (через statistics.mean)

    Параметры:
        records -- список плоских словарей
        field -- название числового поля

    На выходе:
        Среднее значение или None, если значений нет
    """
    values = field_values(records, field)
    if len(values) == 0:
        return None
    return statistics.mean(values)


def median_value(records: list, field: str) -> float:
    """Медиана поля field (через statistics.median)

    Параметры:
        records -- список плоских словарей
        field -- название числового поля

    На выходе:
        Медиана или None, если значений нет
    """
    values = field_values(records, field)
    if len(values) == 0:
        return None
    return statistics.median(values)


def max_value(records: list, field: str):
    """Максимальное значение поля field

    Параметры:
        records -- список плоских словарей
        field -- название поля

    На выходе:
        Максимальное значение или None, если значений нет
    """
    values = field_values(records, field)
    if len(values) == 0:
        return None
    return max(values)


def min_value(records: list, field: str):
    """Минимальное значение поля field

    Параметры:
        records -- список плоских словарей
        field -- название поля

    На выходе:
        Минимальное значение или None, если значений нет
    """
    values = field_values(records, field)
    if len(values) == 0:
        return None
    return min(values)


def top_n(metrics: dict, n: int) -> list:
    """Возвращает n пар (ключ, значение) с наибольшими значениями

    Параметры:
        metrics -- словарь {ключ: число}, например из apply_aggregation
        n -- сколько пар вернуть

    На выходе:
        Список из n пар (ключ, значение) по убыванию значения
    """
    sorted_keys = sorted(metrics, key=metrics.get, reverse=True)
    top_list = []
    for key in sorted_keys[:n]:
        top_list.append((key, metrics[key]))
    return top_list


if __name__ == '__main__':
    pass
