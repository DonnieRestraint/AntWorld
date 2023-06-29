# YYH 类像函数一样调用需要实现__call__方法； property(get, set, del, doc)


class Animal(object):
    """class doc"""
    def __init__(self):
        self._dog_name = None

    def get_name(self):
        """get_name doc"""
        return self._dog_name

    def set_name(self, dog_name):
        self._dog_name = dog_name

    def del_name(self):
        del self._dog_name

    dog_name = property(get_name, set_name, del_name, "AD")

    def __call__(self, name):
        return name, self._dog_name


if __name__ == '__main__':
    animal = Animal()

    animal.dog_name = "Sword Hero"
    print(animal("show"))

    print(animal.dog_name)
    # print(animal.dog_name.__doc__ )

    del animal.dog_name
    print(hasattr(animal, "dog_name"))
