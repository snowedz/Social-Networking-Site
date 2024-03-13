from classes import *
from db import *
from abc import ABC,abstractmethod

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
            return welcome()

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
    profile_menu = ProfileMenuCreator()
    posts_menu = PostsMenuCreator()
    followers_menu = FollowersMenuCreator()
    events_menu = EventsMenuCreator()
    messages_menu = MessagesMenuCreator()
    groups_menu = GroupsMenuCreator()

    menu_options = ['Ver Perfil','Editar Perfil','Ver Seguidores','Seguir usuários','Ver posts','Criar Posts','Desativar conta','Sair']
    while True:
        for n in range(len(main_menu)):
            print(f"{n+1} - {main_menu[n]}")
        choice = input("-> O que deseja fazer? ")
        print('\n')
        if choice == '1':
            profile_menu = ProfileMenuCreator()
            menu_options = ['Ver Perfil','Editar Perfil','Desativar Conta','Menu Anterior']
            for n in range(0,4):
                print(f"{n+1} - {menu_options[n]}")
            print('\n')
            choice_2 = input("-> Escolha uma opção: ")
            print('\n')
            choice_2 = profile_menu.create_menu(choice_2)          

        elif choice == '2':
            menu_options = ['Ver posts','Criar posts','Editar posts','Menu Anterior']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            post_menu = PostsMenuCreator()
            choice_2 = post_menu.create_menu(choice_2)
            

        elif choice == '3':
            menu_options = ['Ver seguidores','Ver quem você segue', 'Seguir usuários', 'Menu Anterior']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("-> Escolha uma opção: ")
            followers_menu = FollowersMenuCreator()
            choice_2 = followers_menu.create_menu(choice_2)
            print('\n')

        elif choice == '4':
            menu_options = ['Ver eventos','Criar eventos','Gerenciar eventos', 'Sair']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("-> Escolha uma opção: ")
            print('\n')
            events_menu = EventsMenuCreator()
            choice_2 = events_menu.create_menu(choice_2)

            
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
    
class MenuOption(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class ViewProfile(MenuOption, Profile):
    def execute(self):
        return show_profile(Profile.username)

class EditProfile(MenuOption,Profile):
    def execute(self):
        return edit_profile()

class DeactivateUser(MenuOption,Profile):
    def execute(self):
        return deactivate_user() 

class ProfileMenuCreator(Profile):
    def create_menu(self, choice):
        options = {
            '1': ViewProfile(Profile),
            '2': EditProfile(Profile),
            '3': DeactivateUser(Profile)
        }
        return options[choice].execute()

class ViewPosts(MenuOption,Profile):
    def execute(self):
        return view_posts()

class InsertPost(MenuOption,Profile):
        def execute(self):
            return insert_post(Profile)

class EditPost(MenuOption,Profile):
    def execute(self):
        return edit_post(Profile)

class PostsMenuCreator(Profile):
    def create_menu(self, choice):
        options = {
            '1': ViewPosts(Profile),
            '2': InsertPost(Profile),
            '3': EditPost(Profile)
        }
        return options[choice].execute()

class ViewFollowers(MenuOption,Profile):
    def execute(self):
        return get_followers()
    
class ViewFollowing(MenuOption,Profile):
    def execute(self):
        return get_following()

class InsertFollower(MenuOption,Profile):
    def execute(self):
        return insert_follower()

class FollowersMenuCreator(Profile):
    def create_menu(self, choice):
        options = {
            '1': ViewFollowers(Profile),
            '2': ViewFollowing(Profile),
            '3': InsertFollower(Profile)
        }
        return options[choice].execute()

class ViewEvents(MenuOption,Profile):
    def execute(self):
        return view_events()

class InsertEvent(MenuOption,Profile):
    def execute(self):
        return insert_event()

class EditEvent(MenuOption,Profile):
    def execute(self):
        return edit_event()

class EventsMenuCreator(Profile):
    def create_menu(self, choice):
        options = {
            '1': ViewEvents(Profile),
            '2': InsertEvent(Profile),
            '3': EditEvent(Profile)
        }
        return options[choice].execute()

class SeeMessages(MenuOption,Profile):
    def execute(self):
        return see_messages()

class SendMessage(MenuOption,Profile):
    def execute(self):
        return send_message()

class MessagesMenuCreator(Profile):
    def create_menu(self, choice):
        options = {
            '1': SeeMessages(Profile),
            '2': SendMessage(Profile)
        }
        return options[choice].execute()

class ViewGroups(MenuOption,Profile):
    def execute(self):
        return view_groups()

class InsertGroups(MenuOption,Profile):
    def execute(self):
        return insert_groups()

class EditGroup(MenuOption,Profile):
    def execute(self):
        return edit_group()

class DeleteGroup(MenuOption,Profile):
    def execute(self):
        return delete_group()

class GroupsMenuCreator(Profile):
    def create_menu(self, choice):
        options = {
            '1': ViewGroups(Profile),
            '2': InsertGroups(Profile),
            '3': EditGroup(Profile),
            '4': DeleteGroup(Profile)
        }
        return options[choice].execute()
    
