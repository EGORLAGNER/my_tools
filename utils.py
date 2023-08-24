def _print_list(label, obj, list_with_members):
    print(f'{label}: {obj}')
    for member in list_with_members:
        print(member)
    print()


def _parsing_members_by_lists(obj, dunder_methods=False):
    """Возвращает два списка: с атрибутами и методами объекта.
    По умолчанию возвращает списки без dunder методов.
    Вернет с dunder методами если dunder_methods примет True.
    Атрибуты и методы называются общим словом - "члены" (eng members)"""
    all_members = dir(obj)  # Получить все члены класса. Члены - общее название для атрибутов и методов

    methods = []
    attributes = []

    for member in all_members:
        member_obj = getattr(obj, member)  # Поверяет, является ли член атрибутом
        if callable(member_obj):  # Проверяем, является ли член вызываемым объектом. Атрибуты ими не являются
            if not dunder_methods and member.startswith('__'):
                continue
            methods.append(member)

        if not callable(member_obj):
            if not dunder_methods and member.startswith('__'):
                continue
            attributes.append(member)

    return attributes, methods


def print_am(obj, print_dunder=False, return_lists=False):
    """Выводит в консоль атрибуты и методы объекта.
    При необходимости возвращает списки с атрибутами и методами.

    Аргумент obj обязательный, принимает объект.
    Аргумент print_dunder отвечает за вывод dunder методов.
    Аргумент return_lists отвечает за возврат списков с атрибутами и методами"""

    list_attributes, list_methods = _parsing_members_by_lists(obj, print_dunder)
    _print_list('Атрибуты', obj, list_attributes)
    _print_list('Методы', obj, list_methods)

    if return_lists:
        return list_attributes, list_methods


if __name__ == '__main__':
    print(f'module utils подключен!')
