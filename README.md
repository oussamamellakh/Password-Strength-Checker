# Password Strength Checker 🔒
The Password Strength Checker is a Python-based tool designed to evaluate password security using two different approaches:

NIST-Compliant Guidelines – Based on the standards set by the National Institute of Standards and Technology (NIST).
Custom Enhanced Password Security – A more stringent standard designed to ensure stronger password security beyond NIST guidelines.
This repository contains two password strength checking scripts:

## 1. NIST-Based Password Checker
The NIST Password Checker follows the official NIST SP 800-63B guidelines (link: https://pages.nist.gov/800-63-4/sp800-63b.html), ensuring that passwords meet basic security standards. It checks for:
- Minimum length of 8 characters (12+ recommended).
- Avoidance of common passwords by checking against a known list of compromised passwords.
- Breach detection using the Have I Been Pwned (HIBP) API.

Screenshot of the execution of the NIST-Based Password Checker.
![image](https://github.com/user-attachments/assets/d1479b52-c612-4ca4-aa74-22fff196a2a1)


While NIST guidelines improve security, they do not guarantee a truly strong password.

## 2. Custom Stronger Password Checker
Since NIST’s guidelines are relatively basic, this tool includes a custom, more robust password security standard that enforces stronger security practices.

This Enhanced Password Checker ensures:
- Minimum length of 16 characters (for significantly increased security).
- Inclusion of multiple character types (uppercase, lowercase, numbers, and special characters).
- Avoidance of dictionary words, common phrases, and predictable patterns (e.g., "12345", "password", "qwerty").
- Stricter evaluation criteria than NIST, making passwords much harder to crack.

Screenshot of the execution of the Custom Password Checker.
![image](https://github.com/user-attachments/assets/e0a4af5e-0087-478c-afb3-614740d29075)


## Why Use This Password Strength Checker?
- Prevents Weak Passwords; By detecting common, breached, or easy-to-guess passwords.
- Enhanced Security; Goes beyond NIST by implementing stricter rules for real-world security threats.
- Breach Check; Verifies whether the password has been exposed in known data breaches using the Have I Been Pwned API.
- User-Friendly Feedback; Provides clear recommendations to improve weak passwords.

## Installing Requirements
pip install -r requirements.txt
