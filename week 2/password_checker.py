import re
import getpass

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    print("\n--- Password Evaluation ---")
    if score == 5:
        print("[+] Strong Password! Great job.")
    elif score >= 3:
        print("[!] Moderate Password. Could be better.")
    else:
        print("[-] Weak Password. Please improve it based on the feedback below:")

    for issue in feedback:
        print(f"  - {issue}")

if __name__ == "__main__":
    print("Welcome to the Offline Password Strength Checker")
    user_pass = getpass.getpass("Enter a password to test (input is hidden): ")
    check_password_strength(user_pass)
