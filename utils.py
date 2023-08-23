def _parsing_members_by_lists(obj):
    all_members = dir(obj)  # Получить все члены класса. Члены - общее название для атрибутов и методов

    obj_methods = []
    obj_attributes = []

    for member in all_members:
        member_obj = getattr(obj, member)  # Поверяет, является ли член атрибутом
        if callable(member_obj):  # Проверяем, является ли член вызываемым объектом. Атрибуты ими не являются
            obj_methods.append(member)
        else:
            obj_attributes.append(member)

    return obj_attributes, obj_methods


class ToolGetAllPropertyObj:
    """Разбирает атрибуты и методы объекта по спискам"""

    def __init__(self, obj):
        self.obj = obj

        self.obj_attributes, self.obj_methods = _parsing_members_by_lists(obj)

    def print_all_attributes(self):
        print(f'аттрибуты объекта {self.obj}')
        for attr in self.obj_attributes:
            print(attr)
        print()

    def print_all_methods(self):
        print(f'методы объекта {self.obj}')
        for method in self.obj_methods:
            print(method)
        print()

    def print_attributes(self):
        print(f'аттрибуты объекта {self.obj}')
        for attr in self.obj_attributes:
            if attr.startswith('__'):
                continue
            print(attr)
        print()

    def print_methods(self):
        print(f'аттрибуты объекта {self.obj}')
        for attr in self.obj_attributes:
            if attr.startswith('__'):
                continue
            print(attr)
        print()


if __name__ == '__main__':
    print(f'module utils подключен!')
