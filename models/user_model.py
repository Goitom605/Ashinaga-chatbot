

from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash


# REGISTER USER
def create_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)

    cursor.execute("""
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
    """, (username, email, hashed_password))

    conn.commit()
    conn.close()


# FIND USER BY EMAIL
def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users WHERE email = ?
    """, (email,))

    user = cursor.fetchone()
    conn.close()

    return user


# VERIFY LOGIN
def verify_user(email, password):
    user = get_user_by_email(email)

    if user and check_password_hash(user[3], password):
        return user

    return None