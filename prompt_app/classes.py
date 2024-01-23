class Profile():
    def __init__(self, username, first_name, second_name, password, bday, email, gender):
        self.username = username
        self.first_name = first_name
        self.second_name = second_name
        self.password = password
        self.email = email
        self.bday = bday
        self.gender = gender



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
