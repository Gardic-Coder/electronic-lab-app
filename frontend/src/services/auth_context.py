class AuthContext:
    def __init__(self):
        self.token = None
        self.user_data = None
        self.on_login = None
        self.on_logout = None
    
    def login(self, token, user_data):
        self.token = token
        self.user_data = user_data
        if self.on_login:
            self.on_login(token, user_data)
    
    def logout(self):
        self.token = None
        self.user_data = None
        if self.on_logout:
            self.on_logout()
    
    def is_authenticated(self):
        return self.token is not None

auth_context = AuthContext()