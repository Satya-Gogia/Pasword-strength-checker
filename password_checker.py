import re
import numpy as np
import pandas as pd
import os

LOG_FILE = "password_log.csv"


def check_password(password):
    checks = np.array([
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    ])

    score = int(np.sum(checks))

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Fair"
    elif score == 4:
        strength = "Good"
    else:
        strength = "Strong"

    return checks, score, strength


def save_log(length, score, strength):
    data = pd.DataFrame({
        "Password Length": [length],
        "Score": [score],
        "Strength": [strength]
    })

    if os.path.exists(LOG_FILE):
        data.to_csv(LOG_FILE, mode="a", header=False, index=False)
    else:
        data.to_csv(LOG_FILE, index=False)


def main():
    print("=" * 45)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = input("Enter your password: ")

    checks, score, strength = check_password(password)

    print("\n------ RESULT ------")
    print(f"Score: {score}/5")
    print(f"Strength: {strength}\n")

    labels = [
        "Minimum 8 characters",
        "Contains uppercase letter",
        "Contains lowercase letter",
        "Contains number",
        "Contains special character"
    ]

    for label, passed in zip(labels, checks):
        print(f"{'✓' if passed else '✗'} {label}")

    save_log(len(password), score, strength)

    print("\nResult saved to password_log.csv")


if __name__ == "__main__":
    main()
