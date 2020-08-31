import BDD


class User:
    def __init__(self, user_id: int, user_name: str, user_lastname: str, user_email: str, user_password: str):
        self.user_id = user_id
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_email = user_email
        self.user_password = user_password

    def __str__(self):
        return f"USER -> ID: {self.user_id}, Name: {self.user_name}, LN: {self.user_lastname}, Email: {self.user_email}, Pw: {self.user_password} "

    def insert_user(self):

        create_user = """
        INSERT INTO
            users(user_name, user_lastname, user_email, user_password)
        VALUES
          ("{}", "{}", "{}", "{}")
        """.format(self.user_name, self.user_lastname, self.user_email, self.user_password)
        print("Logical_Data -> Class Insert_user", create_user)

        #Insert user to DBB
        BDD.execute_query(create_user)
