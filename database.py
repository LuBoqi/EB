import pymysql


class user_data:
    def __init__(self, username, password, ip='0.0.0.0'):
        self.username = username
        self.password = password
        self.ip = ip
        self.cnnect_to_database()

        self.connection = pymysql.connect(host=self.ip,
                                          user=self.username,  # 替换为您的MySQL用户名
                                          password=self.password,  # 替换为您的MySQL密码
                                          database='chat_database',  # 替换为您的数据库名称
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.create_table()

    def create_table(self):
        with self.connection.cursor() as cursor:
            # 创建用户表
            create_table_query = """
                            CREATE TABLE IF NOT EXISTS chat_logs (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                sender_id INT NOT NULL,
                                receiver_id INT NOT NULL,
                                message TEXT NOT NULL,
                                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            )
                            """
            cursor.execute(create_table_query)
            self.connection.commit()

    def insert_message(self, sender_id, receiver_id, message):
        with self.connection.cursor() as cursor:
            insert_query = """
                            INSERT INTO chat_logs (sender_id, receiver_id, message)
                            VALUES (%s, %s, %s)
                            """
            cursor.execute(insert_query, (sender_id, receiver_id, message))
            self.connection.commit()

    def get_messages(self, sender_id, receiver_id):
        with self.connection.cursor() as cursor:
            select_query = """
                            SELECT * FROM chat_logs
                            WHERE (sender_id = %s AND receiver_id = %s)
                                OR (sender_id = %s AND receiver_id = %s)
                            """
            cursor.execute(select_query, (sender_id, receiver_id, receiver_id, sender_id))
            messages = cursor.fetchall()
            return messages

    def close_connection(self):
        self.connection.close()
