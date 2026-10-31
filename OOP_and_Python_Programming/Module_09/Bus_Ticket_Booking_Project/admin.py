class Admin:
    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

    def login(self, input_username, input_password):
        return self.username == input_username and self.password == input_password