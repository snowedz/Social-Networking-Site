import json
from classes import *

JSON_FILE = 'C:/Users/marsh/Desktop/FACULDADE/P3/frostbook/prompt_app/users.json'
user_list_file = open(JSON_FILE)
user_list = json.load(user_list_file)


def welcome():
    print("Seja bem vindo ao FrostBook \nJá tem uma conta?")

        
def create_user(Profile):
    username = input('Digite o nome do usuário: ')
    first_name = input('Primeiro nome: ')
    second_name = input('Segundo nome: ')
    password = input('Senha: ')
    age = int(input('Idade: '))
    posts = []
    follows = []
    user = Profile(username=username,first_name=first_name,second_name=second_name,password=password,age=age,posts=posts,follows=follows)
    save = vars(user)
    user_list['users'][user.username] = save
    print(user_list)
    with open(JSON_FILE,'w',encoding='utf-8') as save_user:
        json.dump(user_list, save_user)
    return user

def create_post(Posts,Profile):
    post = input('O que deseja postar? ')
    Profile.posts = Posts(Profile,content=post,image=None,like_conunt=0,comments = None)
    return Profile.posts

def view_post(Profile):
    if Profile.posts.index() == 0:
        print("Você não tem nenhum post")
    else:
        for posts in Profile.posts:
            print(f"{posts}")
    return

def see_folows(Profile):
    if Profile.follows.index() == 0:
        print("Você não segue ninguém")
    else:
        print('Lista de pessoas que você segue ')
        for follows in Profile.follows:
            print(f"- {follows}")

def add_follow(Profile):
    list_users()
    print("\n")
    select = input("Que usuário deseja seguir ?")
    try:
        Profile.follows = select
    except:
        print('Usuário não encontrado')
    
    


def list_users():
    options = []
    for userlist in user_list['users']:
        options.append(user_list)
        print(userlist)
    return

def menu():
    menu_options = ['Criar post','Ver posts','Listar Seguindo','Seguir usuários','Sair']
    for n in range(1,menu_options):
        print(f"{n} - {menu_options[n]}")
    choice = input("O que deseja fazer? ")