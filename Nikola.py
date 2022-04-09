
class Nikola:
    """
    Exceptional person's class
    """

    __slots__ = ["name", "age"]
    
    def __init__(self, name, age):
        """Constructor"""
        super(Nikola, self).__setattr__("age", age)
        if name == "Николай":
            super(Nikola, self).__setattr__("name", name)
        else:
            line = f"Я не {name}, а Николай"
            super(Nikola, self).__setattr__("name", line)


person_1 = Nikola("Николай", 89)
print(person_1.name, person_1.age)
