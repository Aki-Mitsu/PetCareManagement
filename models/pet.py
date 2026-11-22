class Pet:
    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type

    def get_type(self):
        return self.pet_type

    def get_care_tips(self):
        return "General care tips."

    def __str__(self):
        return f"{self.pet_type} - {self.name} (Age: {self.age})"
