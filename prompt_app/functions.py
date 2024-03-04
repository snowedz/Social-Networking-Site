from classes import *
from db import *

######### Display welcome menu and menu options #########

def welcome():
    print('1 -> Logar\n2 -> Criar uma conta\n3 -> Reativar Usuário \n4 -> Sair\n')
    welcome_answer = input('-> Escolha sua opção: ')
    print('\n')
    if welcome_answer == '1': 
        user = login_user()
        return user

    if welcome_answer == '2':
            insert_user()
            menu()

    if welcome_answer == '3':
        user = input('-> Digite o username: ')
        activate_user(user)
        print('-> faça o login')
        return login_user()
        
    if welcome_answer == '4':
        print('-> Saindo')
        print('\n')
        return False
    else:
        print('-> Opção errada, tente novamente')
        print('\n')
        return welcome()

######### Menu Options #########

def menu(Profile):
    main_menu = ['Perfil','Posts','Seguidores','Eventos','Chat','Grupos','Sair']
    menu_options = ['Ver Perfil','Editar Perfil','Ver Seguidores','Seguir usuários','Ver posts','Criar Posts','Desativar conta','Sair']
    while True:
        for n in range(len(main_menu)):
            print(f"{n+1} - {main_menu[n]}")
        choice = input("-> O que deseja fazer? ")
        print('\n')
        if choice == '1':
            menu_options = ['Ver Perfil','Editar Perfil','Desativar Conta','Menu Anterior']
            for n in range(0,4):
                print(f"{n+1} - {menu_options[n]}")
            print('\n')
            choice_2 = input("-> Escolha uma opção: ")
            print('\n')
            if choice_2 == '1':
                show_profile(Profile.username)
                return menu(Profile)
            
            elif choice_2 == '2':
                choice_3 = input('1 - Primeiro Nome\n2 - Segundo Nome\n3 - Data de Nascimento\n4 - Gênero\n5 - Endereço de Email\n\nO que deseja mudar?')
                if choice_3 == '1':
                    choice_4 = input('-> Novo Primeiro Nome : ')
                    edit_profile(Profile.username,'fname',choice_4)
                    return menu(Profile)
                
                elif choice_3 == '2':
                    choice_4 = input('-> Novo Segundo Nome : ')
                    edit_profile(Profile.username,'lname',choice_4)
                    return menu(Profile)
                
                elif choice_3 == '3':
                    choice_4 = input('-> Nova Data de nascimento : ')
                    edit_profile(Profile.username,'bday',choice_4)
                    return menu(Profile)
                
                elif choice_3 == '4':
                    choice_4 = input('-> Nova Gênero : ')
                    edit_profile(Profile.username,'bday',choice_4)
                    return menu(Profile)
                
                elif choice_3 == '5':
                    choice_4 = input('-> Novo Endereço de Email : ')
                    edit_profile(Profile.username,'email',choice_4)

                    return menu(Profile)
            
            elif choice_2 == '3':
                return deactivate_user(Profile.username)
            return menu(Profile)

        elif choice == '2':
            menu_options = ['Ver posts','Criar posts','Editar posts','Menu Anterior']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("-> Escolha uma opção: ")
            if choice_2 == '1':
                view_posts()
                return menu(Profile)
            elif choice_2 == '2':
                content = input('-> O que deseja Postar:')
                image = input('-> Link de midia (se tiver, caso não, apenas ignore):')
                post = Posts(Profile,content,image,0,None)
                insert_post(post,Profile)
                return menu(Profile)
            
            elif choice_2 == '3':

                userid = general_search('userid','username',Profile.username)
                if my_posts(userid) == 1:
                    choice_3 = input('-> Qual post você quer editar? ')

                    choice_4 = input('1 - Editar Texto\n2 - Editar Midia')

                    if choice_4 == '1':
                        choice_4 = 'content'
                        choice_5 = input('Escreva -> ')
                        edit_post(choice_3,userid,choice_4,choice_5)
                    elif choice_4 == '2':
                        choice_4 = 'image'
                        choice_5 = input('Link da midia -> ')
                        edit_post(choice_3,userid,choice_4,choice_5)
                    return menu(Profile)
            elif choice_2 == '4':
                return menu(Profile) 

        elif choice == '3':
            menu_options = ['Ver seguidores','Ver quem você segue', 'Seguir usuários', 'Menu Anterior']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("-> Escolha uma opção: ")
            print('\n')

            
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
            menu_options = ['Ver eventos','Criar eventos','Gerenciar eventos', 'Sair']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("-> Escolha uma opção: ")
            print('\n')


            if choice_2 == '1':
                view_events()
                return menu(Profile)
            
            elif choice_2 == '2':
                event_name = input('Nome do evento: ')
                event_description = input('Descrição do evento: ')
                event_location = input('Local do evento: ')
                event_date = input('Data do evento: ')
                event_time = input('Hora que vai acontecer(Formato: HH:MM): ')
                Event = Events(Profile, event_name, event_description, event_location, event_date, event_time)
                insert_event(Event)
                return menu(Profile)
            
            elif choice_2 == '3':
                menu_options = ['Ver meus eventos','Editar Evento','Convidar pessoas', 'Excluir evento','Menu']
                for n in range(len(menu_options)):
                    print(f"{n+1} - {menu_options[n]}")
                choice_3 = input("-> Escolha uma opção: ")
                print('\n')
                    
                if choice_3 == '1':
                    my_events(Profile.username)
                    
                elif choice_3 == '2':
                    my_events(Profile.username)
                    eventid = input('-> ID do evento que deseja mudar: ')
                    menu_options = ['Nome do evento','Descrição','Local','Data','Hora','sair']
                    for n in range(len(menu_options)):
                        print(f"{n+1} - {menu_options[n]}")
                    print('\n')
                    choice_4 = input('-> O que deseja mudar? ')
                    print('\n')
                    if choice_4 == '1':
                        new_name = input('-> Novo nome do evento: ')
                        edit_event(eventid,Profile.username,'event_name',new_name)
                    elif choice_4 == '2':
                        new_desc = input('-> Nova descrição: ')
                        edit_event(eventid,Profile.username,'event_description',new_desc)
                    elif choice_4 == '3':
                        new_local = input('-> Nova localização: ')
                        edit_event(eventid,Profile.username,'event_location',new_local)
                    elif choice_4 == '4':
                        new_date = input('-> Nova data: ')
                        edit_event(eventid,Profile.username,'event_date',new_date)
                    elif choice_4 == '4':
                        new_time = input('Novo horário: ')
                        edit_event(eventid,Profile.username,'event_time',new_time)
                    elif choice_4 == '5':
                        menu(Profile)

                elif choice_3 == '3':
                    list_users()
                    choice_4 = input('-> Qual usuário você quer convidar? ')
                    print('\n')
                    # invite_users() ### need to implement notifications and accepting or decline instances
                
                elif choice_3 == '4':
                    my_events()
                    eventid = input('-> Qual ID do evento que você quer deletar? ')
                    print('\n')
                    delete_event(eventid,Profile.username)
                
                elif choice_3 == '5':
                    return menu(Profile)
            
            elif choice_2 == '4':
                return menu(Profile)
            



        elif choice == '5':
            menu_options = ['Ver conversas','Mandar mensagem','Menu anterior']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input('-> Selecione uma opção: ')
            if choice_2 == '1':
                see_messages(Profile.username)
                return menu(Profile)
            elif choice_2 == '2':
                list_users()
                target = input('-> Para quem? ')
                message = input('-> ')
                send_message(Profile.username,target,message)
                return menu(Profile)
        
        elif choice == '6':
            menu_options = ['Ver Grupos','Criar Grupos','Gerenciar grupos', 'Sair']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("-> Escolha uma opção: ")

            if choice_2 == '1':
                view_groups()
                return menu(Profile)
            
            elif choice_2 == '2':
                group_name = input('-> Nome do grupo: ')
                group_description = input('-> Descrição do grupo: ')
                group_date = input('-> Data de criação do grupo: ')
                Group = Groups(Profile, group_name, group_description, group_date)
                insert_groups(Group)
                return menu(Profile)
            
            elif choice_2 == '3':
                menu_options = ['Ver meus grupos','Editar grupo', 'Convidar pessoas para o grupo' 'Excluir grupo','Menu']
                for n in range(len(menu_options)):
                    print(f"{n+1} - {menu_options[n]}")
                choice_3 = input("-> Escolha uma opção: ")
                    
                if choice_3 == '1':
                    my_groups(Profile.username)
                    
                elif choice_3 == '2':
                    my_groups(Profile.username)
                    groupid = input('-> ID do grupo que deseja mudar: ')
                    menu_options = ['Nome do grupo','Descrição','sair']
                    for n in range(len(menu_options)):
                        print(f"{n+1} - {menu_options[n]}")
                    choice_4 = input('-> O que deseja mudar? ')
                    if choice_4 == '1':
                        new_name = input('-> Novo nome do grupo: ')
                        edit_group(groupid,Profile.username,'group_name',new_name)
                    elif choice_4 == '2':
                        new_desc = input('-> Nova descrição: ')
                        edit_group(groupid,Profile.username,'group_desc',new_desc)
                    elif choice_4 == '3':
                        menu(Profile)
                
                elif choice_3 == '4':
                    my_groups(Profile.username)
                    groupid = input('-> Qual ID do grupo que você quer deletar? ')
                    delete_group(groupid,Profile.username)
                    print("Grupo deletado com sucesso")
                    return menu(Profile)
        
        elif choice == '7':
            print('-> Saindo')
            return False
    
