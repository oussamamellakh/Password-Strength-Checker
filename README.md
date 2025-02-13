### Password Strength Checker
The Password Strength Checker is a Python-based tool designed to evaluate password security using two different approaches:

NIST-Compliant Guidelines – Based on the standards set by the National Institute of Standards and Technology (NIST).
Custom Enhanced Password Security – A more stringent standard designed to ensure stronger password security beyond NIST guidelines.
This repository contains two password strength checking scripts:

1. NIST-Based Password Checker
The NIST Password Checker follows the official NIST SP 800-63B guidelines, ensuring that passwords meet basic security standards. It checks for:

✔ Minimum length of 8 characters (12+ recommended).
✔ Avoidance of common passwords by checking against a known list of compromised passwords.
✔ Breach detection using the Have I Been Pwned (HIBP) API.

While NIST guidelines improve security, they do not guarantee a truly strong password..

While NIST guidelines improve security, they do not guarantee a truly strong password.

## 2. Custom Stronger Password Checker
Since NIST’s guidelines are relatively basic, this tool includes a custom, more robust password security standard that enforces stronger security practices.

This Enhanced Password Checker ensures:
✔ Minimum length of 16 characters (for significantly increased security).
✔ Inclusion of multiple character types (uppercase, lowercase, numbers, and special characters).
✔ Avoidance of dictionary words, common phrases, and predictable patterns (e.g., "12345", "password", "qwerty").
✔ Stricter evaluation criteria than NIST, making passwords much harder to crack.

## Why Use This Password Strength Checker?
🔹 Prevents Weak Passwords – By detecting common, breached, or easy-to-guess passwords.
🔹 Enhanced Security – Goes beyond NIST by implementing stricter rules for real-world security threats.
🔹 Breach Check – Verifies whether the password has been exposed in known data breaches using the Have I Been Pwned API.
🔹 User-Friendly Feedback – Provides clear recommendations to improve weak passwords.

## How It Works
1️⃣ The tool prompts the user to enter a password.
2️⃣ The password is checked against both NIST standards and the custom enhanced security rules.
3️⃣ If the password is weak, feedback is provided with specific suggestions on how to strengthen it.
4️⃣ If the password is strong, the user is notified that it meets modern security standards.
