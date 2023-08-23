def _print_all_list(list_with_obj):
    for obj in list_with_obj:
        print(obj)


def _print_not_all_list(list_with_obj):
    for obj in list_with_obj:
        if obj.startswith('__'):
            continue
        print(obj)


def _parsing_members_by_lists(obj):
    """Возвращает два списка: с атрибутами и методами объекта.
    Атрибуты и методы называются общим словом - "члены" (eng members)"""
    all_members = dir(obj)  # Получить все члены класса. Члены - общее название для атрибутов и методов

    list_with_methods = []
    list_with_attributes = []

    for member in all_members:
        member_obj = getattr(obj, member)  # Поверяет, является ли член атрибутом
        if callable(member_obj):  # Проверяем, является ли член вызываемым объектом. Атрибуты ими не являются
            list_with_methods.append(member)
        else:
            list_with_attributes.append(member)

    return list_with_attributes, list_with_methods


def print_am(obj, print_dunder_methods=False):
    """Выводит два списка: с атрибутами и методами объекта.
    По умолчанию не выводит dunder методы."""
    print_dunder_methods_flag = print_dunder_methods
    list_with_attributes, list_with_methods = _parsing_members_by_lists(obj)
    if print_dunder_methods_flag:
        print(f'Атрибуты: {obj}')
        _print_all_list(list_with_attributes)
        print()
        print(f'Методы: {obj}')
        _print_all_list(list_with_methods)
        print()
    else:
        print(f'Атрибуты: {obj}')
        _print_not_all_list(list_with_attributes)
        print()
        print(f'Методы: {obj}')
        _print_not_all_list(list_with_methods)
        print()


if __name__ == '__main__':
    print(f'module utils подключен!')
