def extract_nested_value(obj, keys):
    """Достаёт значение из вложенных словарей по цепочке ключей.

    Аргументы:
        obj: словарь, возможно с вложенными словарями.
        keys: список ключей - путь к нужному значению.

    На выходе:
        Значение в конце пути как есть или None, если по пути
        не нашёлся ключ или встретился не словарь
    """

    value = obj
    for key in keys:
        if not isinstance(value, dict):
            return None
        if key not in value:
            return None
        value = value[key]
    return value


def process_dictionary_with_config(dictionary: dict, config) -> dict:
    """Превращает вложенный словарь в плоский по конфигу

    Аргументы:
        dictionary -- исходный вложенный словарь
        config -- словарь вида {атрибут: путь или (путь, функция)}

    На выходе:
        Плоский словарь с теми же ключами, что в config
    """
    output = {}
    for attribute, rule in config.items():
        if isinstance(rule, list):
            output[attribute] = extract_nested_value(dictionary, rule)
        elif isinstance(rule, tuple):
            temp_rule = extract_nested_value(dictionary, rule[0])
            if temp_rule is None:
                output[attribute] = None
                continue
            output[attribute] = rule[1](temp_rule)

    return output


def process_list_of_dicts_with_config(list_of_dicts: list, config) -> list:
    """Применяет process_dictionary_with_config к каждому словарю списка

    Аргументы:
        list_of_dicts -- список вложенных словарей (например, призов)
        config -- словарь вида {атрибут: путь или (путь, функция)}

    На выходе:
        Список плоских словарей
    """
    output = []
    for dictionary in list_of_dicts:
        if isinstance(dictionary, dict):
            output.append(process_dictionary_with_config(dictionary, config))
    return output


def create_processor(config, list_processor=False):
    """Создает функцию-обработчик с уже заданным конфигом

    Аргументы:
        config -- словарь вида {атрибут: путь или (путь, функция)}
        list_processor -- True - обработчик принимает список словарей,
            False - один словарь

    На выходе:
        Функция, которая принимает данные и возвращает плоский
        словарь (или список плоских словарей)
    """
    def processor(data):
        if list_processor:
            return process_list_of_dicts_with_config(data, config)
        return process_dictionary_with_config(data, config)
    return processor


if __name__ == '__main__':
    pass
