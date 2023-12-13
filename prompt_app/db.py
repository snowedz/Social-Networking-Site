import sqlite3
from classes import *

######### Insert Functions
        
def insert_user(Profile):
     username = input('Digite o nome do usuário: ')
     if general_search('username','username',username) !=0:
         print('\n-> Usuário já existe\n')
         return 
     first_name = input('Primeiro nome: ')
     second_name = input('Segundo nome: ')
     password = input('Senha: ')
     bday = input('Data de Nascimento: ')
     email = input('Digite seu email: ')
     gender = input('Genero: ')
     if general_search('username','email',email):
         print('Usuário já existe')
         return
     conn = sqlite3.connect('fb.db')
     cursor = conn.cursor()

     query = '''INSERT INTO users (username, fname, lname, pword, bday, email, gender, is_active) VALUES (?,?,?,?,?,?,?,?)'''
     cursor = cursor.execute(query,(Profile.username,Profile.first_name,Profile.second_name,Profile.password,Profile.bday,Profile.email,Profile.gender,1))
     if cursor.rowcount > 0:
        print(f"User '{Profile.username}' criado com sucesso.")
        conn.commit()
        conn.close()
     else:
        print("Erro")

def insert_post(Posts,Profile):
     userid = general_search('userid','username',Profile.username)
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

def insert_follower(Profile):
     userlist = list_users()
     myuser = Profile.username
     target = input("Que usuário deseja seguir? ")
     if target in userlist:
        if target != myuser:
            conn = sqlite3.connect('fb.db')
            cursor = conn.cursor()
            
            existing_followers = '''SELECT followers FROM users WHERE username = ? '''
            cursor.execute(existing_followers,(target,))
            existing_followers = cursor.fetchone()

            if existing_followers[0] != None:
                existing_followers = existing_followers[0]
                following_already = existing_followers.split()
                if myuser in following_already:
                    print("Você já está seguindo este perfil")
                    return

                updated_followers = f"{existing_followers}, {myuser}"

                query = '''UPDATE users
                    SET followers = ?
                    WHERE username = ?;'''
                cursor = cursor.execute(query,(updated_followers,target))
                result = cursor.fetchone()
                conn.commit()
                conn.close()
                return
            else:
                query = '''UPDATE users
                    SET followers = ?
                    WHERE username = ?;'''
                cursor = cursor.execute(query,(myuser,target))
                result = cursor.fetchone()
                conn.commit()
                conn.close()
                return
        return
     print('Usuário não encontrado')

#########

######### Search Functions

def general_search(type,param,search):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = f'''SELECT {type} FROM users WHERE {param} = ?'''

    cursor = cursor.execute(query,[search])
    result = cursor.fetchone()
          
    if result:
        # print(f'{type} encontrado : {(result[0])}')
        return result[0]
        conn.close()
    else:
        return 0

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

def get_following(username):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = f''' SELECT username FROM users WHERE followers LIKE ?'''
    cursor = cursor.execute(query,('%' + username + '%',))
    result = cursor.fetchall()
    if result:
        following_users = [user[0] for user in result]
        print(f"Você segue esses perfis: {', '.join(following_users)}")
        return conn.close()
    else:
        print(f'Você não segue ninguém')
        return conn.closer()

def get_followers(username):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = '''SELECT followers FROM users WHERE username = ?'''

    cursor = cursor.execute(query,[username])
    result = cursor.fetchall()
          
    if None not in result[0]:
        user_followers = [user[0] for user in result]
        print(f"Estes perfis seguem você: {', '.join(user_followers)}")
    else:
        print(f'Você não é seguido por ninguém')

def show_profile(username):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = '''SELECT username,fname,lname,bday,email,gender FROM users WHERE username = ?'''

    cursor = cursor.execute(query,[username])
    result = cursor.fetchall()

    if result:
        result = str(result[0])
        username,fname,lname,bday,email,gender = result.split(',')
        print(f'Nome: {fname[+2:-1]} {lname[+2:-1]}')
        print(f'Data de nascimento: {bday[+2:-1]}')
        print(f'Email: {email[+2:-1]}')
        print(f'Gênero: {gender[+2:-2]}')

    # if result:
    #     print(f'Usuário encontrado : {username}')
    #     conn.close()
        
    # else:
    #     print(f'Usuário não encontrado')
    #     conn.close()

def view_posts():
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = f'''SELECT * FROM posts'''
    cursor = cursor.execute(query)
    result = cursor.fetchall()
    if result:
        for row in result:
            postid,userid,content,image,comments,like_count = row
            query_2 = f''' SELECT fname,lname FROM users WHERE userid = ?'''
            cursor_2 = cursor.execute(query_2,(userid,))
            result_2 = cursor.fetchall()
            for row_2 in result_2:
                fname,lname = row_2
            print(f'{fname} {lname} postou :   {content}')
    # print(result)
def my_posts(userid):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = f'''SELECT postid,content FROM posts 
        WHERE userid = ?'''
    cursor = cursor.execute(query,(userid,))
    result = cursor.fetchall()
    if len(result) == 0:
        print('Você não tem nenhum post')
        return 0;
    for row in result:
        postid,content = row
        print(f'ID do Post: {postid} - {content}')
    return 1
#########
######### Delete Functions

def delete_user(userid):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()
    query = '''DELETE FROM users
        WHERE userid = ?'''
    try:
        cursor = cursor.execute(query,(userid,))
        print(f"Usuário deletado com sucesso.")
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)


def remove_follower(myuser,target):
     conn = sqlite3.connect('fb.db')
     cursor = conn.cursor()
     
     existing_followers = '''SELECT followers FROM users WHERE username = ? '''
     cursor.execute(existing_followers,(target,))
     existing_followers = cursor.fetchone()

     if existing_followers[0] != 'None':
        existing_followers = existing_followers[0]
        updated_followers = existing_followers.replace(f', {myuser}','')

        query = '''UPDATE users
            SET followers = ?
            WHERE username = ?;'''
        try:
            cursor = cursor.execute(query,(updated_followers,target))
            result = cursor.fetchone()
            conn.commit()
        except sqlite3.Error as e:
            print(e)
     else:
        print("Você não segue essa pessoa")

#########
######### Edit
def edit_profile(username,param,value):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = f''' UPDATE users
        SET {param} = ?
        WHERE username = ?;'''
    cursor = cursor.execute(query,(value,username))
    conn.commit()
    conn.close()
    print('Campo alterado com sucesso')
    return

def edit_post(postid,userid,param,value):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = f''' UPDATE posts
        SET {param} = ?
        WHERE postid = ?
        AND userid = ?;'''
    cursor = cursor.execute(query,(value,postid,userid))
    conn.commit()
    conn.close()
    print('Post alterado com sucesso')
    return

def deactivate_user(username):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()
    query = '''UPDATE users
        SET is_active = ?
        WHERE username = ?;'''
    cursor = cursor.execute(query,(0,username))
    conn.commit()
    conn.close()
    print('Usuário desativado')
    return

def activate_user(username):
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()
    query = '''UPDATE users
        SET is_active = ?
        WHERE username = ?;'''
    cursor = cursor.execute(query,(1,username))
    conn.commit()
    conn.close()
    print('Usuário ativado')
    return
######### Misc

def login_user():
    username = input('Usuário: ')
    password = input('Senha: ')
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()

    query = '''SELECT * FROM users WHERE username = ?'''

    cursor = cursor.execute(query,[username])
    result = cursor.fetchall()
          
    if result:
        for row in result:
            userid,username,fname,lname,pword,bday,email,gender,followers,friends,is_active = row
        if password == pword and is_active == 1:
            print('\n')
            print(f'-> Usuário logado')
            user = Profile(username,fname,lname,pword,bday,email,gender)
            return user
        elif is_active == 0:
            print('\n')
            print('Usuário desativado')
            print('\n')
            return False
        conn.close()
        
    else:
        print('\n')
        print(f'Usuário não encontrado')
        print('\n')
        conn.close()
        return login_user()


def list_users():
    userlist = []
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()
    query = '''SELECT username FROM users '''

    cursor = cursor.execute(query)
    result = cursor.fetchall()
    for user in result:
        print(*user)
        userlist.append(*user)
    conn.close()
    return userlist
