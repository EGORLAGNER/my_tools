class ToolGetAllPropertyObj:
    """Разбирает атрибуты и методы объекта по спискам"""

    def __init__(self, obj):
        self.obj = obj
        self.obj_attributes = []
        self.obj_methods = []

        all_members = dir(obj)  # Получить все члены класса. Члены - общее название для атрибутов и методов

        for member in all_members:
            member_obj = getattr(obj, member)  # Поверяет, является ли член атрибутом
            if callable(member_obj):  # Проверяем, является ли член вызываемым объектом. Атрибуты ими не являются
                self.obj_methods.append(member)
            else:
                self.obj_attributes.append(member)

    def print_attributes(self):
        print(f'аттрибуты объекта {self.obj}')
        for attr in self.obj_attributes:
            print(attr)
        print()

    def print_methods(self):
        print(f'методы объекта {self.obj}')
        for method in self.obj_methods:
            print(method)
        print()


if __name__ == '__main__':
    print(f'module utils подключен!')
