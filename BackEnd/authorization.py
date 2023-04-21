class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

class Authentication:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                return True
        return False
