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


def menu(Profile):
    main_menu = ['Perfil','Posts','Seguidores','Sair']
    menu_options = ['Ver Perfil','Editar Perfil','Ver Seguidores','Seguir usuários','Ver posts','Criar Posts','Desativar conta','Sair']
    while True:
        for n in range(0,4):
            print(f"{n+1} - {main_menu[n]}")
        choice = input("O que deseja fazer? ")
        if choice == '1':
            menu_options = ['Ver Perfil','Editar Perfil','Desativar Conta','Menu Anterior']
            for n in range(0,4):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("Escolha uma opção: ")
            if choice_2 == '1':
                show_profile(Profile.username)
                return menu(Profile)
            elif choice_2 == '2':
                choice_3 = input('1 - Primeiro Nome\n2 - Segundo Nome\n3 - Data de Nascimento\n4 - Gênero\n5 - Endereço de Email\n\nO que deseja mudar?')
                if choice_3 == '1':
                    choice_4 = input('novo Primeiro Nome : ')
                    edit_profile(Profile.username,'fname',choice_4)
                    return menu(Profile)
                elif choice_3 == '2':
                    choice_4 = input('Novo Segundo Nome : ')
                    edit_profile(Profile.username,'lname',choice_4)
                    return menu(Profile)
                elif choice_3 == '3':
                    choice_4 = input('Nova Data de nascimento : ')
                    edit_profile(Profile.username,'bday',choice_4)
                    return menu(Profile)
                elif choice_3 == '4':
                    choice_4 = input('Nova Gênero : ')
                    edit_profile(Profile.username,'bday',choice_4)
                    return menu(Profile)
                elif choice_3 == '5':
                    choice_4 = input('Novo Endereço de Email : ')
                    edit_profile(Profile.username,'email',choice_4)
                    return menu(Profile)
            
            elif choice_2 == '3':
                return deactivate_user(Profile.username)
            return menu(Profile)

        elif choice == '2':
            menu_options = ['Ver posts','Criar posts','Editar posts','Menu Anterior']
            for n in range(0,4):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("Escolha uma opção: ")
            if choice_2 == '1':
                view_posts()
                return menu(Profile)
            elif choice_2 == '2':
                content = input('O que deseja Postar:')
                image = input('Link de midia (se tiver, caso não, apenas ignore):')
                post = Posts(Profile,content,image,0,None)
                insert_post(post,Profile)
                return menu(Profile)
            
            elif choice_2 == '3':
                userid = general_search('userid','username',Profile.username)
                my_posts(userid)
                choice_3 = input('Qual post você quer editar? ')
                choice_4 = input('1 - Editar Texto\n2 - Editar Midia')
                if choice_4 == '1':
                    choice_4 = 'content'
                    choice_5 = input('Escreva -> ')
                    edit_post(choice_3,choice_4,choice_5)
                elif choice_4 == '2':
                    choice_4 = 'image'
                    choice_5 = input('Link da midia -> ')
                    edit_post(choice_3,choice_4,choice_5)
                return menu(Profile)
            elif choice_2 == '3':
                return menu(Profile) 

        elif choice == '3':
            menu_options = ['Ver seguidores','Ver quem você segue', 'Seguir usuários', 'Menu Anterior']
            for n in range(0,4):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("Escolha uma opção: ")
            
            if choice_2 == '1':
                get_followers(Profile.username)
                return menu(Profile)
            elif choice_2 == '2':
                get_following(Profile.username)
                return menu(Profile)
            elif choice_2 == '3':
                insert_follower(Profile)
                return menu(Profile)
            elif choice_2 == '4':
                menu(Profile)
                return menu(Profile)

        elif choice == '4':
            print('Saindo')
            return False
    
