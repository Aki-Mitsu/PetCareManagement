from models.pet import Pet

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age, "Dog")

    def get_care_tips(self):
        return "Feed twice a day, weekly bath, daily exercise."
