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
    user = Profile
    print(user)
    main_menu = ['Perfil','Posts','Seguidores','Eventos','Chat','Grupos','Sair']
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
            choice_2 = profile_menu.create_menu(choice_2,user)          

        elif choice == '2':
            menu_options = ['Ver posts','Criar posts','Editar posts','Menu Anterior']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            posts_menu = PostsMenuCreator()
            choice_2 = input("-> Escolha uma opção: ")
            choice_2 = posts_menu.create_menu(choice_2,user)
            

        elif choice == '3':
            menu_options = ['Ver seguidores','Ver quem você segue', 'Seguir usuários', 'Menu Anterior']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("-> Escolha uma opção: ")
            followers_menu = FollowersMenuCreator()
            choice_2 = followers_menu.create_menu(choice_2,user)
            print('\n')

        elif choice == '4':
            menu_options = ['Ver eventos','Criar eventos','Editar Evento','Convidar Pessoas','Excluir Evento' 'Sair']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("-> Escolha uma opção: ")
            print('\n')
            events_menu = EventsMenuCreator()
            choice_2 = events_menu.create_menu(choice_2,user)


        elif choice == '5':
            menu_options = ['Ver conversas','Mandar mensagem','Menu anterior']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input('-> Selecione uma opção: ')
            messages_menu = MessagesMenuCreator()
            choice_2 = messages_menu.create_menu(choice_2,user)

        elif choice == '6':
            menu_options = ['Ver Grupos','Criar Grupos','Editar grupo', 'Convidar Pessoas para o Grupo','Excluir Grupo', 'Sair']
            for n in range(len(menu_options)):
                print(f"{n+1} - {menu_options[n]}")
            choice_2 = input("-> Escolha uma opção: ")
            groups_menu = GroupsMenuCreator()
            choice_2 = groups_menu.create_menu(choice_2,user)

        elif choice == '7':
            print('-> Saindo')
            return False
    
class MenuOption(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class ViewProfile(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return show_profile(self.username)

class EditProfile(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return edit_profile(self.username)

class DeactivateUser(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return deactivate_user(self.username) 

class ProfileMenuCreator():
    def create_menu(self, choice,user):
        options = {
            '1': ViewProfile(user),
            '2': EditProfile(user),
            '3': DeactivateUser(user)
        }
        return options[choice].execute()

class ViewPosts(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return view_posts()

class InsertPost(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return insert_post(self.username)

class EditPost(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return edit_post(self.username)

class PostsMenuCreator():
    def create_menu(self, choice, user):
        options = {
            '1': ViewPosts(user),
            '2': InsertPost(user),
            '3': EditPost(user)
        }
        return options[choice].execute()

class ViewFollowers(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return get_followers(self.username)
    
class ViewFollowing(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return get_following(self.username)

class InsertFollower(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return insert_follower(self.username)

class FollowersMenuCreator():
    def create_menu(self, choice,user):
        options = {
            '1': ViewFollowers(user),
            '2': ViewFollowing(user),
            '3': InsertFollower(user)
        }
        return options[choice].execute()

class ViewEvents(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return view_events()

class InsertEvent(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return insert_event(self.username)

class EditEvent(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return edit_event(self.username)

class InvitePeople(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return invite_user_to_event(self.username)

class EventsMenuCreator():
    def create_menu(self, choice, user):
        options = {
            '1': ViewEvents(user),
            '2': InsertEvent(user),
            '3': EditEvent(user),
            '4': InvitePeople(user)
        }
        return options[choice].execute()

class SeeMessages(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return see_messages(self.username)

class SendMessage(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return send_message(self.username)

class MessagesMenuCreator():
    def __init__(self,Profile):
        self.username = Profile.username

    def create_menu(self, choice, user):
        options = {
            '1': SeeMessages(user),
            '2': SendMessage(user)
        }
        return options[choice].execute()

class ViewGroups(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return view_groups()

class InsertGroups(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return insert_groups(self.username)

class EditGroup(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username

    def execute(self):
        return edit_group(self.username)

class DeleteGroup(MenuOption,Profile):
    def __init__(self,Profile):
        self.username = Profile.username
        
    def execute(self):
        return delete_group(self.username)

class GroupsMenuCreator():
    def create_menu(self, choice, user):
        options = {
            '1': ViewGroups(user),
            '2': InsertGroups(user),
            '3': EditGroup(user),
            '4': DeleteGroup(user)
        }
        return options[choice].execute()
    
