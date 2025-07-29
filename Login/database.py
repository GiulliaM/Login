import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.load()
        
    def load(self):
        self.users = {}
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    email, password, name, created = line.strip().split(";")
                    self.users[email] = (password, name, created)
        except FileNotFoundError:
            pass

    def add_user(self, email, password, name):
        email = email.strip()
        if email not in self.users:
            self.users[email] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email já existente")
            return -1
        
    def validate(self, email, password):
        user = self.get_user(email)
        if user != -1:
            return user[0] == password
        else:
            return False

    def get_user(self, email):
        email = email.strip()
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(
                    user + ";" +
                    self.users[user][0] + ";" +
                    self.users[user][1] + ";" +
                    self.users[user][2] + "\n"
                )

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]