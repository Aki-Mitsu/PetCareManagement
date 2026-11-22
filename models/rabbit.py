from models.pet import Pet

class Rabbit(Pet):
    def __init__(self, name, age):
        super().__init__(name, age, "Rabbit")

    def get_care_tips(self):
        return "Provide hay, trim nails, maintain clean cage."
