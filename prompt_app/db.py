import sqlite3
from classes import *

def connect_database():
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()
    return conn, cursor

def close_database(conn):
    conn.close()

######### Insert Functions #########
        
def insert_user():
     username = input('Digite o nome do usuário: ')
     if general_search('username','username',username,'users') !=0:
         print('\n-> Usuário já existe\n')
         return 
     first_name = input('Primeiro nome: ')
     second_name = input('Segundo nome: ')
     password = input('Senha: ')
     bday = input('Data de Nascimento: ')
     email = input('Digite seu email: ')
     gender = input('Genero: ')
     if general_search('username','email',email,'users'):
         print('Usuário já existe')
         return
     conn,cursor = connect_database()
     query = '''INSERT INTO users (username, fname, lname, pword, bday, email, gender, is_active) VALUES (?,?,?,?,?,?,?,?)'''
     cursor = cursor.execute(query,(username,first_name,second_name,password,bday,email,gender,1))
     if cursor.rowcount > 0:
        print(f"User '{username}' criado com sucesso.")
        conn.commit()
        conn.close()
     else:
        print("Erro")

def insert_post(Posts,Profile):
     userid = general_search('userid','username',Profile.username,'users')
     conn,cursor = connect_database()
     query = '''INSERT INTO posts (userid, content,image,like_count,comments) VALUES (?,?,?,?,?)'''
     cursor = cursor.execute(query,(userid,Posts.content,Posts.image,Posts.like_count,Posts.comments))
     if cursor.rowcount > 0:
        print(f"Post criado com sucesso.")
        Profile.notify_observers(Posts)
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
            conn,cursor = connect_database()
            
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

def insert_event(Events):
     conn,cursor = connect_database()
     query = '''INSERT INTO events (event_name, event_desc, event_location,event_date,event_time, event_owner, event_members) VALUES (?,?,?,?,?,?,?)'''
     cursor = cursor.execute(query,(Events.name,Events.description, Events.location, Events.date, Events.time, Events.owner, Events.owner))
     if cursor.rowcount > 0:
        print(f"Evento criado com sucesso.")
        conn.commit()
        conn.close()
     else:
        print("Erro")

def insert_groups(Groups):
     conn,cursor = connect_database()
     query = '''INSERT INTO groups (group_name, group_desc, creation_date, group_owner, group_members) VALUES (?,?,?,?,?)'''
     cursor = cursor.execute(query,(Groups.name,Groups.description, Groups.date, Groups.owner, Groups.owner))
     if cursor.rowcount > 0:
        print(f"Grupo criado com sucesso.")
        conn.commit()
        conn.close()
     else:
        print("Erro")

######### ------ ######### 

######### Search Functions #########

def general_search(type,param,search,table):
    conn,cursor = connect_database()

    query = f'''SELECT {type} FROM {table} WHERE {param} = ?'''

    cursor = cursor.execute(query,[search])
    result = cursor.fetchone()
          
    if result:
        # print(f'{type} encontrado : {(result[0])}')
        return result[0]
        conn.close()
    else:
        return 0

def search_user(username):
    conn,cursor = connect_database()

    query = '''SELECT username FROM users WHERE username = ?'''

    cursor = cursor.execute(query,[username])
    result = cursor.fetchone()
          
    if result:
        print(f'Usuário encontrado : {username}')
        conn.close()
        
    else:
        print(f'Usuário não encontrado')
        conn.close()

def my_events(username):
    conn,cursor = connect_database()

    query = '''SELECT * FROM events WHERE event_owner = ?'''

    cursor = cursor.execute(query,[username])
    result = cursor.fetchall()
          
    if len(result) != 0:
        for row in result:
            eventid,event_name,event_desc,event_location,event_date,event_time,event_owner,event_members = row
            print(f'ID do Evento: {eventid}\n{event_name}\n{event_desc}\nLocal: {event_location}\nData: {event_date} as {event_time}')
    else:
        print("Não há eventos no momento")

def my_groups(username):
    conn,cursor = connect_database()

    query = '''SELECT * FROM groups WHERE group_owner IN (?) OR group_member IN (?);'''

    cursor = cursor.execute(query,(username,username))
    result = cursor.fetchall()
          
    if len(result) != 0:
        for row in result:
            groupid,group_name,group_desc,creation_date,group_owner,group_members = row
            print(f'ID do Grupo: {groupid}\n{group_name}\n{group_desc}\nCriado em: {creation_date}\n')
    else:
        print("Você não participa de nenhum grupo no momento\n")

def get_following(username):
    conn,cursor = connect_database()

    query = f''' SELECT username FROM users WHERE followers LIKE ?'''
    cursor = cursor.execute(query,('%' + username + '%',))
    result = cursor.fetchall()
    if result:
        following_users = [user[0] for user in result]
        print(f"Você segue esses perfis: {', '.join(following_users)}\n")
        return conn.close()
    else:
        print(f'Você não segue ninguém\n')
        return conn.close()

def get_followers(username):
    conn,cursor = connect_database()

    query = '''SELECT followers FROM users WHERE username = ?'''

    cursor = cursor.execute(query,[username])
    result = cursor.fetchall()
          
    if None not in result[0]:
        user_followers = [user[0] for user in result]
        print(f"Estes perfis seguem você: {', '.join(user_followers)}\n")
    else:
        print(f'Você não é seguido por ninguém\n')

def show_profile(username):
    conn,cursor = connect_database()

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
        print('\n')

    # if result:
    #     print(f'Usuário encontrado : {username}')
    #     conn.close()
        
    # else:
    #     print(f'Usuário não encontrado')
    #     conn.close()

def view_posts():
    conn,cursor = connect_database()

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
    print('\n')
def view_groups():
    conn,cursor = connect_database()

    query = f'''SELECT * FROM groups'''
    cursor = cursor.execute(query)
    result = cursor.fetchall()
    if len(result) != 0:
        for row in result:
            groupid,group_name,group_desc,creation_date,group_owner,group_members = row
            print(f'ID do Grupo: {groupid}\n{group_name}\n{group_desc}\nCriado em: {creation_date}')
        print('\n')
    else:
        print("Não há grupos no momento\n")


def my_posts(userid):
    conn,cursor = connect_database()

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
    print('\n')
    return 1

def view_events():
    conn,cursor = connect_database()

    query = f'''SELECT * FROM events'''
    cursor = cursor.execute(query)
    result = cursor.fetchall()
    if len(result) != 0:
        for row in result:
            eventid,event_name,event_desc,event_location,event_date,event_time,event_owner,event_members = row
            print(f'ID do Evento: {eventid}\n{event_name}\n{event_desc}\nLocal: {event_location}\nData: {event_date} as {event_time}')
        print('\n')
    else:
        print("Não há eventos no momento\n")

######### ------ ######### 

######### Delete Functions #########

def delete_user(userid):
    conn,cursor = connect_database()
    query = '''DELETE FROM users
        WHERE userid = ?'''
    try:
        cursor = cursor.execute(query,(userid,))
        print(f"Usuário deletado com sucesso.\n")
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)

def delete_event(eventid,username):
    conn,cursor = connect_database()
    query = '''DELETE FROM events
        WHERE eventid = ?
        AND event_owner = ?'''
    try:
        cursor = cursor.execute(query,(eventid,username))
        print(f"Evento excluido com sucesso.\n")
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)

def delete_group(groupid,username):
    conn,cursor = connect_database()
    query = '''DELETE FROM groups
        WHERE groupid = ?
        AND group_owner = ?'''
    try:
        cursor = cursor.execute(query,(groupid,username))
        print(f"Grupo excluido com sucesso.\n")
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
        print("Você não segue essa pessoa\n")

######### ------ ######### 

######### Edit Functions #########

def edit_profile(username,param,value):
    conn,cursor = connect_database()

    query = f''' UPDATE users
        SET {param} = ?
        WHERE username = ?;'''
    cursor = cursor.execute(query,(value,username))
    conn.commit()
    conn.close()
    print('Campo alterado com sucesso\n')
    return

def edit_post(postid,userid,param,value):
    conn,cursor = connect_database()

    query = f''' UPDATE posts
        SET {param} = ?
        WHERE postid = ?
        AND userid = ?;'''
    cursor = cursor.execute(query,(value,postid,userid))
    conn.commit()
    conn.close()
    print('Post alterado com sucesso\n')
    return

def edit_event(eventid,username,param,value):
    conn,cursor = connect_database()

    query = f''' UPDATE events
        SET {param} = ?
        WHERE eventid = ?
        AND event_owner = ?;'''
    
    cursor = cursor.execute(query,(value,eventid,username))
    conn.commit()
    conn.close()
    print('Evento alterado com sucesso\n')
    return

def edit_group(groupid,username,param,value):
    conn,cursor = connect_database()

    query = f''' UPDATE groups
        SET {param} = ?
        WHERE groupid = ?
        AND group_owner = ?;'''
    
    cursor = cursor.execute(query,(value,groupid,username))
    conn.commit()
    conn.close()
    print('group alterado com sucesso\n')
    return

def deactivate_user(username):
    conn,cursor = connect_database()
    query = '''UPDATE users
        SET is_active = ?
        WHERE username = ?;'''
    cursor = cursor.execute(query,(0,username))
    conn.commit()
    conn.close()
    print('Usuário desativado')
    return

def activate_user(username):
    conn,cursor = connect_database()
    query = '''UPDATE users
        SET is_active = ?
        WHERE username = ?;'''
    cursor = cursor.execute(query,(1,username))
    conn.commit()
    conn.close()
    print('Usuário ativado\n')
    return

######### ------ #########

######### Misc Functions #########

def login_user():
    username = input('Usuário: ')
    password = input('Senha: ')
    conn,cursor = connect_database()

    query = '''SELECT * FROM users WHERE username = ?'''

    cursor = cursor.execute(query,[username])
    result = cursor.fetchall()
          
    if result:
        for row in result:
            userid,username,fname,lname,pword,bday,email,gender,followers,friends,is_active = row
        if password == pword and is_active == 1:
            print('\n')
            print(f'-> Usuário logado\n')
            user = Profile(username,fname,lname,pword,bday,email,gender)
            return user
        elif is_active == 0:
            print('\n')
            print('Usuário desativado\n')
            print('\n')
            return False
        conn.close()
        
    else:
        print('\n')
        print(f'Usuário não encontrado\n')
        print('\n')
        conn.close()
        return login_user()

def list_users():
    userlist = []
    conn,cursor = connect_database()
    query = '''SELECT username FROM users '''

    cursor = cursor.execute(query)
    result = cursor.fetchall()
    for user in result:
        print(*user)
        userlist.append(*user)
    conn.close()
    return userlist

######### ------ #########

######### Chat Function #########

def see_messages(username):
     conn = sqlite3.connect('fb.db')
     cursor = conn.cursor()
    ### Check if is there a chat
     query = '''SELECT * FROM chat
     WHERE chat_users LIKE  ?'''
     cursor = conn.execute(query,('%' + username + '%',))
     result = cursor.fetchall()
     if result:
         for row in result:
             chatid,chat_users,content = row
             user,target = chat_users.split(',')
             if user == username:
                content = f'Chat de {target}: {content}'
                print(content)
             if target == username:
                content = f'Chat de {user}: {content}'
                print(content)
         print('\n')

def send_message(username,target,message):
     conn = sqlite3.connect('fb.db')
     cursor = conn.cursor()

     query_1 = '''SELECT fname,lname FROM users
     WHERE username = ?'''
     cursor = conn.execute(query_1,(username,))
     user_fname = cursor.fetchone()
     user_fname = (' '.join(user_fname))
    ## Check if is there a chat
     query_2 = '''SELECT * FROM chat
     WHERE chat_users LIKE  ?'''
     cursor = conn.execute(query_2,[f"{username}, {target}"])
     result = cursor.fetchall()
     if len(result) != 0:
         for row in result:
             chatid,chat_users,content = row
             content = f'{content}\n-> {user_fname}: {message}'
         query_3 =  f'''UPDATE chat
         SET content = ?
         WHERE chatid = ?;'''
         
         cursor = conn.execute(query_3,(content,chatid))
         conn.commit()

     elif len(result) == 0:
         content = f'-> {user_fname}: {content}' 
         query = '''INSERT INTO chat (chat_users,content) VALUES (?,?)'''
         cursor = cursor.execute(query,(f"{username}, {target}",content))
         conn.commit()
         conn.close()
    
def edit_messages(username,target):
     conn = sqlite3.connect('fb.db')
     cursor = conn.cursor()
    ### Check if is there a chat
     query = '''UPDATE chat
      SET chat_users = ?
      WHERE chatid = ?;'''
     cursor = conn.execute(query,(f'{username}, {target}','1'))
     result = cursor.fetchall()
     conn.commit()
     