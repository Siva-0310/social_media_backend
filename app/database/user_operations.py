from app.schemas.schemas import UserRegister
from fastapi.security import OAuth2PasswordRequestForm
from psycopg2.errors import UniqueViolation,CheckViolation
def register_user(conn,user_register:UserRegister):
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users(user_name,user_password,user_email) VALUES(%s,%s,%s) RETURNING *;
        """,(user_register.user_name,user_register.user_password,user_register.user_email))
        conn.commit()
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row
    except UniqueViolation as e:
        return 'UniqueViolation'
    except CheckViolation as e:
        return 'CheckViolation'
def search_user(conn,user:OAuth2PasswordRequestForm):
    cur = conn.cursor()
    cur.execute("""
        SELECT user_id,user_password FROM users WHERE user_name = %s
    """,(user.username,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return row
    return dict(row)