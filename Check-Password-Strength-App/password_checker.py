import re
import sqlite3

class PasswordChecker:
    def __init__(self, db_path='common_passwords.db'):
        self.common_passwords = set()
        self.load_common_passwords(db_path)

    def load_common_passwords(self, db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS passwords (password TEXT)")
        cursor.execute("SELECT password FROM passwords")
        self.common_passwords = {row[0] for row in cursor.fetchall()}
        conn.close()

    def check_length(self, password):
        return len(password)

    def check_complexity(self, password):
        has_upper = re.search(r'[A-Z]', password) is not None
        has_lower = re.search(r'[a-z]', password) is not None
        has_digit = re.search(r'\d', password) is not None
        has_special = re.search(r'[@$!%*?&#]', password) is not None
        return has_upper, has_lower, has_digit, has_special

    def check_common_password(self, password):
        return password.lower() in self.common_passwords

    def grade_password(self, password, personal_info=[]):
        length = self.check_length(password)
        has_upper, has_lower, has_digit, has_special = self.check_complexity(password)
        is_common = self.check_common_password(password)


        if is_common:
            return "Very Weak"
        elif length >= 12 and all([has_upper, has_lower, has_digit, has_special]):
            return "Very Strong"
        elif length >= 10 and sum([has_upper, has_lower, has_digit, has_special]) >= 3:
            return "Strong"
        elif length >= 8 and sum([has_upper, has_lower, has_digit, has_special]) >= 2:
            return "Moderate"
        elif length >= 6 and (has_upper or has_lower or has_digit) and not (has_upper and has_lower and has_digit):
            return "Weak"
        else:
            return "Very Weak"
