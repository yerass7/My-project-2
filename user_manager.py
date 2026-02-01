from user import User

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email, role):
        self.users.append(User(name, email, role))

    def remove_user(self, email):
        self.users = [u for u in self.users if u.email != email]

    def update_user(self, email, name=None, new_email=None, role=None):
        for user in self.users:
            if user.email == email:
                user.update(name, new_email, role)
                return
