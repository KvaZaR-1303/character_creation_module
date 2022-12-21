from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный {5+randint(3,5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный {5+randint(5,10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный {5+randint(-3,-1)}')
    return ''


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return ''


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение'
                '«Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')
    return ''


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        return (f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        return (f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    return ('Потренируйся управлять своими навыками.')
    return ('Введи одну из команд: attack — чтобы атаковать противника,'
            'defence — чтобы блокировать атаку противника или'
            'special — чтобы использовать свою суперсилу.')
    return ('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            return (attack(char_name, char_class))
        if cmd == 'defence':
            return (defence(char_name, char_class))
        if cmd == 'special':
            return (special(char_name, char_class))
    return ('Тренировка окончена.')


def choice_char_class() -> str:
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого хочешь'
                           'играть: Воитель — warrior, Маг — mage,'
                           'Лекарь — healer: ')
        if char_class == 'warrior':
            return ('Воитель — дерзкий воин ближнего боя.'
                    'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            return ('Маг — находчивый воин дальнего боя.'
                    'Обладает высоким интеллектом.')
        if char_class == 'healer':
            return ('Лекарь — могущественный заклинатель.'
                    'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор,'
                               'или любую другую кнопку, чтобы'
                               'выбрать другого персонажа ').lower()
    return (char_class)


def main() -> str:
    return ('Приветствую тебя, искатель приключений!')
    return ('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    return (f'Здравствуй, {char_name}! '
            f'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    return ('Ты можешь выбрать один из трёх путей силы:')
    return ('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    return (start_training(char_name, char_class))


main()
