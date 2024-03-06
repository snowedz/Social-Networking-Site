import sqlite3

class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, post):
        for observer in self._observers:
            observer.update(post)


class Profile(Observable):
    def __init__(self, username, first_name, second_name, password, bday, email, gender):
        super().__init__()
        self.username = username
        self.first_name = first_name
        self.second_name = second_name
        self.password = password
        self.email = email
        self.bday = bday
        self.gender = gender

    def follow_user(self, user_to_follow):
        user_to_follow.add_observer(self)

    def create_post(self, content, image):
        post = Posts(self, content, image, 0, None)
        self.notify_observers(post)

class Posts():
    def __init__(self, Profile, content, image, like_count, comments):
        self.Profile = f"{Profile.first_name} + ' ' +{Profile.second_name}"
        self.content = content
        self.image = image
        self.like_count = int(like_count)
        self.comments = comments

class Events():
    def __init__(self, Profile,name,description,location,date,time):
        self.owner = Profile.username
        self.name = name
        self.description = description
        self.location = location
        self.date = date
        self.time = time

class Groups():
    def __init__(self, Profile,name,description,date):
        self.owner = Profile.username
        self.name = name
        self.description = description
        self.date = date

