# YYH property属性装饰器
class Animal(object):

    def __init__(self):
        self._animals = dict()
        self._dog_name = None

    def __getitem__(self, item):
        return self._animals[item]

    def __setitem__(self, key, value):
        self._animals[key] = value

    def __delitem__(self, key):
        self._animals.pop(key)
        # del self._animals[key]

    @property
    def dog(self):
        """dog doc"""
        # if not hasattr(self, "_dog_name"):
        #     setattr(self, "_dog_name", None)
        return self._dog_name

    @dog.setter
    def dog(self, value):
        self._dog_name = value

    @dog.deleter
    def dog(self):
        del self._dog_name


if __name__ == '__main__':
    animal = Animal()
    print(animal.dog)
    animal.dog = "Sword Hero"
    animal[animal.dog] = 2
    print(animal[animal.dog])
    del animal[animal.dog]
