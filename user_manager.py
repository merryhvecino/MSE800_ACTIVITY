from database import get_connection

def add_user(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    conn.close()

def view_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute()
    users = cursor.fetchall()
    conn.close()
    return users

def search_user(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute()
    results = cursor.fetchall()
    conn.close()
    return results

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    conn.close()

def advanced_search_user(user_id, name):   # ADDED OPTION
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute()
    results = cursor.fetchall()
    conn.close()
    return results
