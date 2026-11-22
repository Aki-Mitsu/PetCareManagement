from models.pet import Pet

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age, "Cat")

    def get_care_tips(self):
        return "Clean litter box, feed twice daily, provide scratching post."
