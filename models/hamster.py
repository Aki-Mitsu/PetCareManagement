from models.pet import Pet

class Hamster(Pet):
    def __init__(self, name, age):
        super().__init__(name, age, "Hamster")

    def get_care_tips(self):
        return "Fresh water daily, keep wheel clean, avoid loud noises."
