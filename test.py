# ########################################################################
# class Immutable(object):
#     """
#     An immutable class
#     """
#     __slots__ = ["one", "two", "three"]
#
#     #----------------------------------------------------------------------
#     def __init__(self, one, two, three):
#         """Constructor"""
#         super(Immutable, self).__setattr__("one", one)
#         super(Immutable, self).__setattr__("two", two)
#         super(Immutable, self).__setattr__("three", three)
#
#     #----------------------------------------------------------------------
#     def __setattr__(self, name, value):
#         """"""
#         msg = "'%s' has no attribute %s" % (self.__class__,
#                                             name)
#         raise AttributeError(msg)
#
# i = Immutable(1, 2, 3)
# print(i.three)
#
# from Nikola import Nikola
#
# person_1 = Nikola("Николай", 89)
# print(person_1.name, person_1.age)

# создаем класс Car
class Car:

    # создаем конструктор класса Car
    def __init__(self, model):
        # Инициализация свойств.
        self.model = model

    # создаем свойство модели.
    @property
    def model(self):
        return self.__model

    # Сеттер для создания свойств.
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)


carA = Car(2088)
print(carA.getCarModel())