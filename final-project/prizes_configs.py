import json_dict_processing

CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], int),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus']
}


def prize_processor():
    """Создает обработчик для списка призов

    На выходе:
        Функция, которая принимает список сырых призов из json
        и возвращает список плоских словарей по CONFIG_PRIZE
    """
    return json_dict_processing.create_processor(CONFIG_PRIZE, True)


if __name__ == '__main__':
    pass
