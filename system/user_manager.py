from models.user import User

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

class UserManager:
    def __init__(self, db_handler):
        """
        Initialize UserManager with a database handler.
        """
        self.db = db_handler

    def register(self, username, password):
        """
        Register a new user in the database.
        """
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        self.db.cursor.execute(sql, (username, password))
        self.db.commit()
        print(f"{Colors.GREEN}{Colors.BOLD}✔ Registration successful for user '{username}'!{Colors.END}")

    def login(self, username, password):
        """
        Attempt to log in a user.

        Returns:
        - User object if login is successful
        - None if login fails
        """
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.db.cursor.execute(sql, (username, password))
        result = self.db.cursor.fetchone()
        
        if result:
            print(f"{Colors.BLUE}{Colors.BOLD}✔ Login successful! Welcome, {username}.{Colors.END}")
            return User(result["user_id"], result["username"], result["password"])
        else:
            print(f"{Colors.RED}{Colors.BOLD}✖ Invalid credentials for user '{username}'!{Colors.END}")
            return None
