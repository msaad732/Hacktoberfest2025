import random
import string

# Define the character sets for the password
# It includes letters (upper/lower), digits, and punctuation for security
LOWERCASE_CHARS = string.ascii_lowercase
UPPERCASE_CHARS = string.ascii_uppercase
DIGITS = string.digits
PUNCTUATION = string.punctuation

def generate_password(length=12):
    """
    Generates a strong, random password of a specified length.

    The password is guaranteed to contain at least one character from
    each required set (lowercase, uppercase, digit, punctuation) to
    ensure high entropy and security.

    Args:
        length (int): The desired length of the password. Must be 4 or greater.

    Returns:
        str: The generated password.
    """
    if length < 4:
        # A password must be at least 4 characters to guarantee one of each type
        print("Warning: Password length must be at least 4. Defaulting to 12.")
        length = 12

    # 1. Ensure at least one of each required character type is present
    required_chars = [
        random.choice(LOWERCASE_CHARS),
        random.choice(UPPERCASE_CHARS),
        random.choice(DIGITS),
        random.choice(PUNCTUATION)
    ]

    # 2. Combine all character sets for the remaining characters
    all_chars = LOWERCASE_CHARS + UPPERCASE_CHARS + DIGITS + PUNCTUATION

    # 3. Generate the remaining characters randomly
    remaining_length = length - len(required_chars)
    remaining_chars = [random.choice(all_chars) for _ in range(remaining_length)]

    # 4. Combine required and remaining characters
    password_list = required_chars + remaining_chars

    # 5. Shuffle the entire list to randomize the position of the required characters
    random.shuffle(password_list)

    # 6. Join the list into the final string
    return "".join(password_list)

# --- Runnable Example ---
if __name__ == "__main__":
    print("--- Secure Password Generator ---")

    # Generate a default 12-character password
    p1 = generate_password()
    print(f"Generated 12-char Password: {p1}")

    # Generate a longer, custom-length password
    custom_length = 20
    p2 = generate_password(custom_length)
    print(f"Generated {custom_length}-char Password: {p2}")
