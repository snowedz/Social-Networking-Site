class Profile():
    def __init__(self, username, first_name, second_name, password, age, posts,follows):
        self.username = username
        self.first_name = first_name
        self.second_name = second_name
        self.password = password
        self.age = int(age)
        self.posts = posts
        self.follows = follows



class Posts():
    def __init__(self, Profile, content, image, like_count, comments):
        self.Profile = f"{Profile.first_name} + ' ' +{Profile.second_name}"
        self.content = content
        self.image = image
        self.like_count = int(like_count)
        self.comments = comments

