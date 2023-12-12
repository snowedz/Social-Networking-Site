import sqlite3
from classes import *

# def user_table():
#     try:
#         connection = sqlite3.connect('fb.db')
#         cursor = connection.cursor()
#         print('DB Iniciada')

#         query = '''CREATE TABLE IF NOT EXISTS users (
#             userid INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL,
#             fname TEXT NOT NULL,
#             lname TEXT NOT NULL,
#             pword TEXT NOT NULL,
#             bday TEXT NOT NULL,
#             email TEXT NOT NULL,
#             gender TEXT,
#             followers TEXT,
#             friends TEXT );'''
#         cursor.execute(query)
#         cursor.close()

#     except sqlite3.Error as error:
#         print(f'Error ocurred - {error}')

#     finally:

#         if connection:
#                 connection.close()
#                 print('DB connection closed')


# def posts_table():
#     try:
#         connection = sqlite3.connect('fb.db')
#         cursor = connection.cursor()
#         print('DB Iniciada')

#         query = '''CREATE TABLE IF NOT EXISTS posts (
#             postid INTEGER PRIMARY KEY AUTOINCREMENT,
#             userid INTEGER,
#             content TEXT NOT NULL,
#             image TEXT,
#             comments TEXT,
#             like_count INTEGER );'''
#         cursor.execute(query)
#         cursor.close()

#     except sqlite3.Error as error:
#         print(f'Error ocurred - {error}')

#     finally:

#         if connection:
#                 connection.close()
#                 print('DB connection closed')
# posts_table()

# delete_table()

def search_user(username):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = '''SELECT username FROM users WHERE username = ?'''

    cursor = cursor.execute(query,[username])
    result = cursor.fetchone()
          
    if result:
        print(f'Usuário encontrado : {username}')
        conn.close()
        
    else:
        print(f'Usuário não encontrado')
        conn.close()

# def delete():
#      conn = sqlite3.connect('fb.db')
#      cursor = conn.cursor()

#      query = '''DROP TABLE posts'''
#      cursor = cursor.execute(query)
#      conn.close()
# delete()
     
        
def insert_user(Profile):
     conn = sqlite3.connect('fb.db')
     cursor = conn.cursor()

     query = '''INSERT INTO users (username, fname, lname, pword, bday, email, gender) VALUES (?,?,?,?,?,?,?)'''
     cursor = cursor.execute(query,(Profile.username,Profile.first_name,Profile.second_name,Profile.password,Profile.bday,Profile.email,Profile.gender))
     if cursor.rowcount > 0:
        print(f"User '{Profile.username}' criado com sucesso.")
        conn.commit()
        conn.close()
     else:
        print("Erro")

# user_table()

def login_user(username,password):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = '''SELECT * FROM users WHERE username = ?'''

    cursor = cursor.execute(query,[username])
    result = cursor.fetchall()
          
    if result:
        for row in result:
            userid,username,fname,lname,pword,bday,email,gender,followers,friends = row
        if password == pword:
            print(f'Usuário logado')
            user = Profile(username,fname,lname,pword,bday,email,gender)
            return user
        conn.close()
        
    else:
        print(f'Usuário não encontrado')
        conn.close()


def list_users():
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = '''SELECT username FROM users '''

    cursor = cursor.execute(query)
    result = cursor.fetchall()
    for user in result:
        print(*user)
    conn.close()

def insert_post(userid,Posts):
     conn = sqlite3.connect('fb.db')
     cursor = conn.cursor()

     query = '''INSERT INTO posts (userid, content,image,like_count,comments) VALUES (?,?,?,?,?)'''
     cursor = cursor.execute(query,(userid,Posts.content,Posts.image,Posts.like_count,Posts.comments))
     if cursor.rowcount > 0:
        print(f"Post criado com sucesso.")
        conn.commit()
        conn.close()
     else:
        print("Erro")

def general_search(type,param,search):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = f'''SELECT {type} FROM users WHERE {param} = ?'''

    cursor = cursor.execute(query,[search])
    result = cursor.fetchone()
          
    if result:
        print(f'{type} encontrado : {(result[0])}')
        return result[0]
        conn.close()

def insert_follower(myuser,target):
     conn = sqlite3.connect('fb.db')
     cursor = conn.cursor()

     query = '''UPDATE users
        SET followers = ?
        WHERE username = ?;'''
     cursor = cursor.execute(query,(myuser,target))
     result = cursor.fetchone()
     if result:
        print(f"{target} seguido com sucesso.")
        conn.commit()
        conn.close()
     else:
        print("Erro")