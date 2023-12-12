import json
from classes import *
from db import *

def welcome():
    print('1 -> Logar\n2 -> Criar uma conta\n3 -> Sair\n')
    welcome_answer = input('Escolha sua opção: ')
    if welcome_answer == '1': 
        user = login_user()
        return user

    if welcome_answer == '2':
            try:
                insert_user(Profile)
                welcome()
            except NameError:
                print("Você não está logado")
                welcome()

    if welcome_answer == '3':
        print('Saindo')
        return False


def view_post(Profile):
    n_post = (len(Profile.posts))
    if n_post == 0:
        print("Você não tem nenhum post")
    else:
        for posts in Profile.posts:
            print(f"{posts['content']} -> Curtidas: {posts['like_count']} -> Comentários: {posts['comments']}\n")
    return


def menu(Profile):
    menu_options = ['Criar post','Ver posts','Listar Seguindo','Seguir usuários','Sair']
    while True:
        for n in range(0,5):
            print(f"{n+1} - {menu_options[n]}")
        choice = input("O que deseja fazer? ")
        if choice == '1':
            return insert_post(Posts,Profile)
        elif choice == '2':
            return view_post(Profile)
        elif choice == '3':
            return get_followers(Profile.username)
        elif choice == '4':
            return insert_follower(Profile)
        elif choice == '5':
            return following(Profile.username)
        elif choice == '6':
            print('Saindo')
            return False
    
