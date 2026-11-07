def get_values(records: list, field: str) -> list:
    """Собирает значения поля field из всех записей в список"""
    field_output = []

    for record in records:
        if field in record:
            field_output.append(record[field])

    return field_output


def count_missing(records: list, fields: list) -> dict:
    """Считает пропуски-None по каждому полю"""
    missing_dict = {}

    for record in records:
        for field in fields:
            missing_dict[field] = missing_dict.get(
                field, 0) + (record[field] is None)

    return missing_dict


def missing_share(missing_counts: dict, total: int) -> dict:
    """Переводит количество пропусков в доли от total"""
    missing_share_dict = {}
    for field in missing_counts:
        missing_share_dict[field] = round(missing_counts[field] / total, 5)

    return missing_share_dict


def find_duplicates(values: list) -> set:
    """Находит значения, которые встречаются больше одного раза"""
    duplicates = set()
    for val in values:
        if values.count(val) > 1:
            duplicates.add(val)

    return duplicates


def find_gaps(values: list) -> list[tuple]:
    """Ищет соседние пары отсортированных значений с разницей больше 1"""
    gaps_values = sorted(values)
    gaps_output = []

    for i in range(len(gaps_values) - 1):
        if gaps_values[i+1] - gaps_values[i] > 1:
            gaps_output.append((gaps_values[i], gaps_values[i+1]))
    return gaps_output


if __name__ == '__main__':
    pass
