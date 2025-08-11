class User:
    def __init__(self, email, name, password, current_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_j_title = current_title

    def change_password(self, new_password):
        print('changing password')
        self.password = new_password

    def change_current_title(self) -> None:
        print('changing current title')

    def get_user_info(self):
        print(f'"hey!" User name: {self.name} works as {self.current_j_title}.'
              f' you can contact at {self.email}.')

sh_user = User(email='sh@g.com', name='sh patil', password='pwd', current_title='SSE Python')
sh_user.get_user_info()
