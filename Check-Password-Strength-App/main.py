# Core Logic: Create a class to check the strength of a password.
# Database Setup: Store common passwords in a database.
# Main Program: Loop to run the program, ask for input, display history and strengths.
# Code Quality: Ensure high score on pylint.
# Unit Tests: Create tests for core logic.
# Optional: Create a Flask app for a simple website.
                        
from password_checker import PasswordChecker

def main():
    checker = PasswordChecker()

    while True:
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break

        # personal_info = ['alice', 'bob', 'charlie', 'david', 'eva'] # check this for eelvancy
        strength = checker.grade_password(password)#, personal_info)

        print(f"Password Strength: {strength}")

if __name__ == '__main__':
    main()


