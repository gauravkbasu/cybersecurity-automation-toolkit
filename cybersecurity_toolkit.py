import hashlib
import secrets
import string

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    ratings = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return ratings.get(score, "Very Weak")

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

password = generate_password()

print("Generated Password:")
print(password)

print("\nPassword Strength:")
print(password_strength(password))

print("\nSHA-256 Hash Example:")
print(sha256_hash("CyberSecurity"))
