from models.dog import Dog
from models.cat import Cat
from models.rabbit import Rabbit
from models.hamster import Hamster

# Colors for console output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

class PetManager:
    def __init__(self, db_handler, user_id):
        """Initialize the PetManager with a database handler and the current user's ID."""
        self.db = db_handler
        self.user_id = user_id

    def add_pet(self, name, age, pet_type):
        """Add a new pet to the database."""
        sql = "INSERT INTO pets (user_id, name, age, pet_type) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(sql, (self.user_id, name, age, pet_type))
        self.db.commit()
        print(f"{Colors.GREEN}{Colors.BOLD}✔ Pet '{name}' added successfully!{Colors.END}")

    def display_pets(self):
        """Display all pets for the current user along with their care tips."""
        sql = "SELECT * FROM pets WHERE user_id = %s"
        self.db.cursor.execute(sql, (self.user_id,))
        pets = self.db.cursor.fetchall()

        if not pets:
            print(f"{Colors.YELLOW}{Colors.BOLD}⚠ No pets found.{Colors.END}\n")
            return

        print(f"{Colors.HEADER}{Colors.BOLD}=== Your Pets ==={Colors.END}\n")
        for p in pets:
            # Create pet object based on pet_type
            if p["pet_type"] == "Dog":
                pet = Dog(p["name"], p["age"])
            elif p["pet_type"] == "Cat":
                pet = Cat(p["name"], p["age"])
            elif p["pet_type"] == "Rabbit":
                pet = Rabbit(p["name"], p["age"])
            else:
                pet = Hamster(p["name"], p["age"])

            # Display pet info and care tips
            print(f"{Colors.CYAN}{Colors.BOLD}{pet}{Colors.END}")
            print(f"{Colors.YELLOW}Care Tips:{Colors.END} {pet.get_care_tips()}\n")

    def remove_pet(self, pet_name):
        """Remove a pet by name from the database for the current user."""
        sql = "DELETE FROM pets WHERE user_id = %s AND name = %s"
        self.db.cursor.execute(sql, (self.user_id, pet_name))
        self.db.commit()
        print(f"{Colors.RED}{Colors.BOLD}✖ Pet '{pet_name}' removed.{Colors.END}")

    def get_pets(self):
        """Return all pets for the current user as a list of pet objects (for GUI display)."""
        sql = "SELECT * FROM pets WHERE user_id = %s"
        self.db.cursor.execute(sql, (self.user_id,))
        pets_data = self.db.cursor.fetchall()
        pets = []
        for p in pets_data:
            if p["pet_type"] == "Dog":
                pet = Dog(p["name"], p["age"])
            elif p["pet_type"] == "Cat":
                pet = Cat(p["name"], p["age"])
            elif p["pet_type"] == "Rabbit":
                pet = Rabbit(p["name"], p["age"])
            else:
                pet = Hamster(p["name"], p["age"])
            pets.append(pet)
        return pets
