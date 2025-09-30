import re

def check_password_strength(password):
    # Conditions
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Collect results
    errors = {
        "Too short (min 8 chars)": length_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing digit": digit_error,
        "Missing special character": special_error
    }

    # Strength Evaluation
    if not any(errors.values()):
        strength = "✅ Strong password"
    elif sum(errors.values()) <= 2:
        strength = "⚠️ Medium password"
    else:
        strength = "❌ Weak password"

    # Print results
    print("\nPassword Check Results:")
    for issue, error in errors.items():
        if error:
            print(f"- {issue}")
    print("Strength:", strength)


# Example usage
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    check_password_strength(pwd)
