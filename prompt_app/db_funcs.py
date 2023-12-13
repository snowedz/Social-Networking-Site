import sqlite3


# Create Tables
# def create_table():
#     try:
#         connection = sqlite3.connect('fb.db')
#         cursor = connection.cursor()
#         print('DB Iniciada')

#         query = '''CREATE TABLE IF NOT EXISTS chat (
#             chatid INTEGER PRIMARY KEY AUTOINCREMENT,
#             chat_users TEXT NOT NULL,
#             content TEXT NOT NULL);'''
#         cursor.execute(query)
#         cursor.close()

#     except sqlite3.Error as error:
#         print(f'Error ocurred - {error}')

#     finally:

#         if connection:
#                 connection.close()
#                 print('DB connection closed')
# create_table()

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


# def delete():
#      conn = sqlite3.connect('fb.db')
#      cursor = conn.cursor()

#      query = '''DROP TABLE posts'''
#      cursor = cursor.execute(query)
#      conn.close()
# delete()


# conn = sqlite3.connect('fb.db')
# cursor = conn.cursor()
# # query = '''ALTER TABLE users
# # ADD COLUMN is_active INTEGER'''

# # cursor = cursor.execute(query)
# # conn.commit()
# # conn.close()

# query = '''UPDATE users
# SET is_active = ?'''
# cursor = cursor.execute(query,(1,))
# conn.commit()
# conn.close()