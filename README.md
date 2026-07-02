# Password Strength Checker

A simple command-line Password Strength Checker built using Python, NumPy, and Pandas.

## Features

- Checks password length
- Checks uppercase letters
- Checks lowercase letters
- Checks numbers
- Checks special characters
- Gives a score out of 5
- Classifies passwords as Weak, Fair, Good, or Strong
- Saves results to a CSV log

## Technologies Used

- Python
- NumPy
- Pandas

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python password_checker.py
```

## Example

```
Enter your password: Hello@123

Score: 5/5
Strength: Strong

✓ Minimum 8 characters
✓ Contains uppercase letter
✓ Contains lowercase letter
✓ Contains number
✓ Contains special character
```

## Example Output
```
=============================================
      PASSWORD STRENGTH CHECKER
=============================================
Enter your password: hello123

------ RESULT ------
Score: 3/5
Strength: Fair

✓ Minimum 8 characters
✗ Contains uppercase letter
✓ Contains lowercase letter
✓ Contains number
✗ Contains special character

Result saved to password_log.csv
```
