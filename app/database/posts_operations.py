from psycopg2 import Error
from ..schemas.schemas import Post,TokenDecode,UpdatePosts
def get_posts(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT post_id,post_text,post_date_time,post_votes FROM posts
        """)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    except Error as error:
        return 'error'
def create_posts(conn,post:Post,id:TokenDecode):
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO posts(post_text,post_votes,user_id) VALUES(%s,%s,%s) RETURNING *
        """,(post.post_text,post.post_votes,id.id))
        conn.commit()
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data
    except Error as e:
        print(e)
        return 'Invalid User'
def get_post(conn,post_id : int):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT post_id,user_id,post_text,post_date_time,post_votes FROM posts WHERE post_id = %s
        """,(post_id,))
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data
    except Error as e:
        return 'error'
def delete_post(conn,post_id:int,user_id:int):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM posts WHERE post_id = %s 
        """,(post_id,))
        data = cur.fetchone()
        if not data:
            return 'Not Found'
        data = dict(data)
        if data['user_id'] != user_id:
            return "Not Autherize"
        cur.execute("""
            DELETE FROM posts WHERE post_id = %s AND user_id = %s
        """,(post_id,user_id))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Error as error:
        print(error)
        return False
def update_post(post_id:int,text:UpdatePosts,user_id:int,conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM posts WHERE post_id = %s
        """,(post_id,))
        data = cur.fetchone()
        if not data:
            return 'Post dont exists'
        data = dict(data)
        if data['user_id'] != user_id:
            return 'Not Autherize'
        cur.execute("""
            UPDATE posts SET post_text = %s WHERE post_id = %s AND user_id = %s RETURNING *
        """,(text.text,post_id,user_id))
        conn.commit()
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data
    except Error as e:
        return 'error'
def increment_votes(post_id:int,conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM posts WHERE post_id = %s
        """,(post_id,))
        data = cur.fetchone()
        if not data:
            return 'Post dont exists'
        data = dict(data)
        cur_votes_incrment = data['post_votes']+1
        cur.execute("""
            UPDATE posts SET post_votes = %s WHERE post_id = %s RETURNING *
        """,(cur_votes_incrment,post_id))
        conn.commit()
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data
    except Error as e:
        print(e)
        return 'error'