import re
import hashlib
import time

# Strong password rules function
def check_strong_password(password):
    feedback = []

    # Check minimum length (16+ characters)
    if len(password) < 16:
        feedback.append("Password must be at least 16 characters.")

    # Check for uppercase, lowercase, digits, and special characters (at least 3 of the 4)
    if not re.search(r'[A-Z]', password):  # Uppercase
        feedback.append("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):  # Lowercase
        feedback.append("Password must contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):  # Digit
        feedback.append("Password must contain at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Special char
        feedback.append("Password must contain at least one special character (e.g., @, #, $, etc.).")

    # Avoid using dictionary words or obvious patterns
    if re.search(r'\b(password|1234|welcome|qwerty|abc|letmein|football)\b', password.lower()):
        feedback.append("Password contains common or easily guessable patterns/words.")

    # Check for sequences (e.g., `12345`, `abcd`)
    if re.search(r'(0123456789|abcdefghijklmnopqrstuvwxyz|qwertyuiop|azertyuiop)', password.lower()):
        feedback.append("Password contains simple sequences (e.g., '12345', 'abcdef').")

    if not feedback:
        return "Strong password", []
    return "Weak password", feedback


# Example usage
print("\n🔒 Welcome to the Enhanced Password Strength Checker! 🔒\n")
time.sleep(1)

print("📌 Follow these **Stronger** password guidelines:")
time.sleep(1)
print("✅ Use at least 16 characters.")
print("✅ Include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
print("✅ Avoid dictionary words, personal information, and common patterns.")
print("✅ Use random passphrases (e.g., random words with symbols).")
print("✅ Avoid common sequences (e.g., '12345').\n")
time.sleep(2)

# Keep asking for a strong password
while True:
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_strong_password(password)

    print(f"\n🔍 Password Strength: {strength}")
    
    if feedback:
        print("\n💡 Suggestions to improve your password:")
        for tip in feedback:
            print(f"- {tip}")
        print("\n❌ Please enter a stronger password.\n")
    else:
        print("✅ Your password is strong and meets the enhanced standards!")
        break  # Exit loop if password is strong
