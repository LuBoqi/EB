import pandas as pd


class ChatLogs:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.df = pd.read_csv(file_path)
        except pd.errors.EmptyDataError or FileNotFoundError:
            self.df = pd.DataFrame(columns=['Sender_ID', 'Receiver_ID', 'Message', 'Time'])
            self.df.to_csv(file_path, index=False)

    def insert_message(self, sender_id, receiver_id, message, time):
        new_row = {'Sender_ID': sender_id, 'Receiver_ID': receiver_id, 'Message': message, 'Time': time}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True, sort=False)
        self.df.to_csv(self.file_path, index=False)

    def get_messages(self, sender_id=None, receiver_id=None):
        if sender_id!= None:
            sender_id = eval(sender_id)
        if receiver_id != None:
            receiver_id =eval(receiver_id)
        messages = self.df[(self.df['Sender_ID'] == sender_id) | (self.df['Receiver_ID']==sender_id) | (self.df['Receiver_ID']==0) | (self.df['Sender_ID']==receiver_id) | (self.df['Receiver_ID']==receiver_id)]
        messages = messages.values
        return messages


    def close_connection(self):
        self.df.to_csv(self.file_path, index=False)


class User_info:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.df = pd.read_csv(file_path)
        except pd.errors.EmptyDataError or FileNotFoundError:
            self.df = pd.DataFrame(columns=['User_ID', 'User_Name', 'Password'])
            self.df.to_csv(file_path, index=False)

    def insert_user(self, user_id, user_name, password):
        new_row = {'User_ID': user_id, 'User_Name': user_name, 'Password': password}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True, sort=False)
        self.df.to_csv(self.file_path, index=False)

    def get_user(self, user_id, user_password):
        user_id = eval(user_id)
        user = self.df[self.df['User_ID'] == user_id]
        a = user['Password'].iloc[0]
        if user.empty:
            print("User not found or incorrect password")
            return None
        else:
            if user['Password'].iloc[0]==user_password:
                return True
            else:
                return False


    def ID_check(self,user_id):
        user_id = eval(user_id)
        user = self.df[self.df['User_ID'] == user_id]
        if user.empty:
            print("注册成功")
            return True
        else:
            print("注册失败")
            return False

    def close_connection(self):
        self.df.to_csv(self.file_path, index=False)


class Friend_list:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.df = pd.read_csv(file_path)
        except pd.errors.EmptyDataError or FileNotFoundError:
            self.df = pd.DataFrame(columns=['User_ID', 'Friend_ID'])
            self.df.to_csv(file_path, index=False)

    def insert_friend(self, user_id, friend_id):
        user_id = eval(user_id)
        new_row = {'User_ID': user_id, 'Friend_ID': friend_id}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True, sort=False)
        self.df.to_csv(self.file_path, index=False)

    def get_friends(self, user_id):
        user_id = eval(user_id)
        friends = self.df[self.df['User_ID'] == user_id]
        return friends["Friend_ID"].tolist()

    def delete_friend(self, user_id, friend_id):
        user_id = eval(user_id)
        self.df = self.df[(self.df['User_ID'] != user_id) | (self.df['Friend_ID'] != friend_id)]
        self.df.to_csv(self.file_path, index=False)

    def close_connection(self):
        self.df.to_csv(self.file_path, index=False)


if __name__ == '__main__':
    chat_logs = ChatLogs('chat_logs.csv')
    user_info = User_info('user_info.csv')
    friend_list = Friend_list("friend_list.csv")
    chat_logs.insert_message('1','1','213','4')
    chat_logs.insert_message('1','1','213','4')
    chat_logs.insert_message('1','1','213','4')
    chat_logs.insert_message('123','234','213','4')
    chat_logs.get_messages('123','234')


