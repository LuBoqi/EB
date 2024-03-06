import pandas as pd


class ChatLogs:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        print(self.df)

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
        self.df = pd.read_csv(file_path)
        print(self.df)

    def insert_user(self, user_id, user_name, password):
        new_row = {'User_ID': user_id, 'User_Name': user_name, 'Password': password}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True, sort=False)
        self.df.to_csv(self.file_path, index=False)

    def get_user(self, user_id, user_password):
        user = self.df[self.df['User_ID'] == user_id]
        if user.empty or user['Password'].iloc[0] != user_password:
            print("User not found or incorrect password")
            return None
        return user

    def close_connection(self):
        self.df.to_csv(self.file_path, index=False)


if __name__ == '__main__':
    chat_logs = ChatLogs('chat_logs.csv')
    chat_logs.insert_message(2, 1, 'Hi')
    chat_logs.insert_message(1, 2, 'How are you?')
    chat_logs.insert_message(2, 1, 'I am good, thank you!')

    messages = chat_logs.get_messages(6, 2)
    print(messages)

    chat_logs.close_connection()

    log_in = User_info('user_info.csv')
    # log_in.insert_user(1, 'user1', 'password1')
    # log_in.insert_user(2, 'user2', 'password2')
    # log_in.insert_user(3, 'user3', 'password3')

    user = log_in.get_user(1, 'password1')
    print(user)
    log_in.close_connection()
