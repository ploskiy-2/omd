import json_dict_processing
from prizes_configs import prize_processor


def process_year(year_string: str) -> int:
    """Достает год из строки с датой

    Параметры:
        year_string -- дата в формате 'YYYY-MM-DD', например '1943-11-07'

    На выходе:
        Год целым числом, например 1943
    """
    return int(year_string[:4])


CONFIG_PERSON = {
    'id': (['id'], int),
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor())
}


CONFIG_ORG = {
    'id': (['id'], int),
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor()),
}


def person_processor():
    """Создает обработчик для лауреатов-людей

    На выходе:
        Функция, которая принимает сырой словарь человека из json
        и возвращает плоский словарь по CONFIG_PERSON
    """
    return json_dict_processing.create_processor(CONFIG_PERSON)


def org_processor():
    """Создает обработчик для лауреатов-организаций

    На выходе:
        Функция, которая принимает сырой словарь организации из json
        и возвращает плоский словарь по CONFIG_ORG
    """
    return json_dict_processing.create_processor(CONFIG_ORG)


process_persons = person_processor()
process_orgs = org_processor()


if __name__ == '__main__':
    pass
