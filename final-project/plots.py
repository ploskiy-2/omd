import matplotlib.pyplot as plt
from aggregations import top_n


def plot_bar(metrics: dict, title: str, ylabel: str):
    """Строит столбчатую диаграмму по убыванию значений

    Параметры:
        metrics -- словарь {(группа,): число}
        title -- заголовок графика
        ylabel -- подпись оси Y

    На выходе:
        Показывает график
    """
    labels = []
    values = []
    for key, value in top_n(metrics, len(metrics)):
        labels.append(str(key[0]))
        values.append(value)

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_line(metrics: dict, title: str, ylabel: str):
    """Строит линейный график по десятилетиям

    Параметры:
        metrics -- словарь {(десятилетие,): число}
        title -- заголовок графика
        ylabel -- подпись оси Y

    На выходе:
        Показывает график
    """
    decades = []
    values = []
    for key in sorted(metrics):
        decades.append(key[0])
        values.append(metrics[key])

    plt.figure(figsize=(10, 5))
    plt.plot(decades, values, marker='o')
    plt.title(title)
    plt.xlabel('Десятилетие')
    plt.ylabel(ylabel)
    plt.xticks(decades, rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    pass
