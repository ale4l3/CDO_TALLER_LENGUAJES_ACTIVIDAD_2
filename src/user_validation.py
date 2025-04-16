def user_validation(username):
    if len(username) < 5:
        return False
    has_numer = any(c.isdigit() for c in username)
    has_mayus = any(c.isupper() for c in username)
    is_alphanumeric = username.isalnum()

    return has_numer and has_mayus and is_alphanumeric