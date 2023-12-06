import json
from classes import *

JSON_FILE = 'C:/Users/marsh/Desktop/FACULDADE/P3/frostbook/prompt_app/users.json'
user_list_file = open(JSON_FILE)
user_list = json.load(user_list_file)


def welcome():
    print("\n")
    print("Seja bem vindo ao FrostBook \nJá tem uma conta? \n")


        
def create_user(Profile):
    username = input('Digite o nome do usuário: ')
    first_name = input('Primeiro nome: ')
    second_name = input('Segundo nome: ')
    password = input('Senha: ')
    age = int(input('Idade: '))
    posts = []
    follows = []
    user = Profile(username=username,first_name=first_name,second_name=second_name,password=password,age=age,posts=posts,follows=follows)
    save_users(user)
    return user

def create_post(Posts,Profile):
    post = input('O que deseja postar? ')
    post = Posts(Profile,content=post,image=None, like_count = 0 ,comments = None)
    post = vars(post)
    Profile.posts.append(post)
    save_users(Profile)

def view_post(Profile):
    n_post = (len(Profile.posts))
    if n_post == 0:
        print("Você não tem nenhum post")
    else:
        for posts in Profile.posts:
            print(f"{posts['content']} -> Curtidas: {posts['like_count']} -> Comentários: {posts['comments']}\n")
    return

def see_folows(Profile):
    n_follows = len(Profile.follows)
    if n_follows == 0:
        print("Você não segue ninguém")
    else:
        print('Lista de pessoas que você segue ')
        for follows in Profile.follows:
            print(f"- {follows}")

def add_follow(Profile):
    userlist = list_users()
    select = input("Que usuário deseja seguir? ")
    if select in userlist and select != Profile.username:
        Profile.follows.append(select)
        save_users(Profile)
        return
    if select == Profile.username:
        print("Você não pode seguir a si próprio")
    else:
        print('Usuário não encontrado')


def list_users():
    options = []
    if len(user_list) != 0:
        for userlist in user_list['users']:
            options.append(user_list)
            print(f'{userlist}')
        return userlist

def login():
    username = input('Usuário: ')
    password = input('Senha: ')
    if username in user_list['users'] and password == user_list['users'][username]['password']:
        user = user_list['users'][username]
        user = Profile(user['username'],user["first_name"],user["second_name"],user["password"],user['age'],user['posts'],user['follows'])
        return user
    else:
        print('Tente novamente')
        return login()

def menu(Profile):
    menu_options = ['Criar post','Ver posts','Listar Seguindo','Seguir usuários','Sair']
    for n in range(0,5):
        print(f"{n+1} - {menu_options[n]}")
    choice = input("O que deseja fazer? ")
    if choice == '1':
        return create_post(Posts,Profile)
    elif choice == '2':
        return view_post(Profile)
    elif choice == '3':
        return see_folows(Profile)
    elif choice == '4':
        return add_follow(Profile)
    elif choice == '5':
        print('Saindo')
        return
    

def save_users(Profile):
    save = vars(Profile)
    user_list['users'][Profile.username] = save
    with open(JSON_FILE,'w',encoding='utf-8') as save_user:
        json.dump(user_list, save_user)
    return Profile
