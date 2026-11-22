import mysql.connector

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

class DBHandler:
    def __init__(self):
        """
        Initialize the database connection and create a cursor for executing queries.
        """
        try:
            # Connect to MySQL database
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",       # Replace with your MySQL password
                database="petcare" # Database name
            )
            # Create a cursor that returns results as dictionaries
            self.cursor = self.db.cursor(dictionary=True)
            print(f"{Colors.GREEN}{Colors.BOLD}✔ Database connection successful!{Colors.END}")
        except mysql.connector.Error as err:
            print(f"{Colors.RED}{Colors.BOLD}✖ Database connection failed: {err}{Colors.END}")
            self.db = None
            self.cursor = None

    def commit(self):
        """
        Commit the current transaction to the database.
        """
        if self.db:
            self.db.commit()
            print(f"{Colors.YELLOW}{Colors.BOLD}✔ Changes committed to the database.{Colors.END}")
        else:
            print(f"{Colors.RED}{Colors.BOLD}✖ Cannot commit, no database connection.{Colors.END}")
