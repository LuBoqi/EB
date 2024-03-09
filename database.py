import pandas as pd


class ChatLogs:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.df = pd.read_csv(file_path)
            print(self.df)
        except pd.errors.EmptyDataError or FileNotFoundError:
            self.df = pd.DataFrame(columns=['Sender_ID', 'Receiver_ID', 'Message'])
            self.df.to_csv(file_path, index=False)

    def insert_message(self, sender_id, receiver_id, message):
        new_row = {'Sender_ID': sender_id, 'Receiver_ID': receiver_id, 'Message': message}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True, sort=False)
        self.df.to_csv(self.file_path, index=False)

    def get_messages(self, sender_id, receiver_id):
        messages = self.df[(self.df['Sender_ID'] == sender_id) & (self.df['Receiver_ID'] == receiver_id)]
        return messages['Message'].tolist()

    def close_connection(self):
        self.df.to_csv(self.file_path, index=False)


class User_info:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.df = pd.read_csv(file_path)
            print(self.df)
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
        if user.empty or user['Password'].iloc[0] != user_password:
            print("User not found or incorrect password")
            return None
        return user

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


class Chat_logs:

    def close_connection(self):
        self.df.to_csv(self.file_path, index=False)


if __name__ == '__main__':
    chat_logs = ChatLogs('chat_logs.csv')
    # chat_logs.insert_message(2, 1, 'Hi')
    # chat_logs.insert_message(1, 2, 'How are you?')
    # chat_logs.insert_message(2, 1, 'I am good, thank you!')
    #
    # messages = chat_logs.get_messages(6, 2)
    # print(messages)
    #
    # chat_logs.close_connection()

    # # log_in.insert_user(2, 'user2', 'password2')
    # # log_in.insert_user(3, 'user3', 'password3')
    #
    # user = log_in.get_user(1, 'password1')
    # print(user)
    # log_in.close_connection()
    # friends = Friend_list('friend_list.csv')
    # friends.insert_friend("1", "sam")
    # friends.insert_friend("1", "sam")
    # friends.insert_friend("2", "john")
    # friends.insert_friend("3", "tom")
    # friends.insert_friend("4", "jerry")
    # friends.insert_friend("1", "jim")
    # friends.insert_friend("1", "Daming")
    # friend = friends.get_friends("1")
    # print(friend)
    # friends.delete_friend("1", "sam")
    # friend = friends.get_friends("1")
    # print(friend)
