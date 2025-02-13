import re
import requests
import hashlib
import time

# GitHub raw file URL
GITHUB_RAW_URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt"

# Load common passwords from GitHub
def load_common_passwords_from_github(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return set(line.strip() for line in response.text.split("\n") if line.strip())
    except requests.RequestException as e:
        print(f"⚠️ Failed to fetch password list from GitHub: {e}")
        return set()

COMMON_PASSWORDS = load_common_passwords_from_github(GITHUB_RAW_URL)

# Function to check if password is breached
def check_pwned(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200 and suffix in response.text:
            return True
    except requests.RequestException:
        print("⚠️ Unable to check breach data. Skipping this step.")
    
    return False

def check_nist_password(password):
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters.")
    
    # Check for common patterns
    if re.search(r'(.)\1{3,}', password):  # Repeated characters (e.g., 'aaaa')
        feedback.append("Avoid repeated characters (e.g., 'aaaa').")
    
    if re.search(r'12345|abcdef|qwerty', password.lower()):  # Common sequences
        feedback.append("Avoid sequential characters (e.g., '12345').")

    # Check if password is in the fetched common password list
    if password in COMMON_PASSWORDS:
        feedback.append("This password is too common. Choose a more unique one.")

    # Check if password is breached
    if check_pwned(password):
        feedback.append("This password has been found in a breach. Choose a different one.")

    if not feedback:
        return "Strong password (NIST-compliant)", []
    return "Weak password", feedback

# Welcome message
print("\n🔒 Welcome to the Password Strength Checker! 🔒\n")
time.sleep(1)

print("📌 Follow these NIST-compliant password guidelines:")
time.sleep(1)
print("✅ Use at least 8 characters (12+ recommended).")
print("✅ Avoid common words, repeated, or sequential characters.")
print("✅ Consider using a passphrase instead of a single word.")
print("✅ Never reuse passwords from other sites.")
print("✅ Check if your password has been breached.\n")
time.sleep(2)

# Keep asking for a strong password
while True:
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_nist_password(password)

    print(f"\n🔍 Password Strength: {strength}")
    
    if feedback:
        print("\n💡 Suggestions to improve your password:")
        for tip in feedback:
            print(f"- {tip}")
        print("\n❌ Please enter a stronger password.\n")
    else:
        print("✅ Your password is strong and meets NIST standards!")
        break  # Exit loop if password is strong
