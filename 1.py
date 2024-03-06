import pandas as pd

# 创建聊天记录DataFrame
chat_data = {
    'Sender_ID': [1, 2, 1, 3],
    'Receiver_ID': [2, 1, 3, 1],
    'Message': ['Hello, how are you?', 'I am fine, thank you!', 'Hi there!', 'Hello!']
}
chat_df = pd.DataFrame(chat_data)

# 将DataFrame写入CSV文件
chat_df.to_csv('chat_logs.csv', index=False)

# 从CSV文件读取数据到DataFrame
read_df = pd.read_csv('chat_logs.csv')

# 打印读取的数据
print(read_df)
