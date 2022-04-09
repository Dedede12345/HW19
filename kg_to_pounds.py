
class KgToPounds:

    def __init__(self, kg):
        self.kg = kg

    @property
    def kg(self):
        return self.__kg


    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError("Only digits")

    @classmethod
    def to_pounds(cls, kg):
        return kg * 2.205

    def get_kg(self):
        return self.kg

weight = KgToPounds(34)
print(weight.to_pounds(weight.kg))