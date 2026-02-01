class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def update(self, name=None, email=None, role=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if role:
            self.role = role
