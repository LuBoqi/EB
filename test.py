import re
import time

req="@123:你好"
result = re.findall(r'\W',req)
print(result)
p = re.compile(r'[@](.*?)[:]', re.S)
result =re.findall(p,req)
print(result)
# 字符串前带上r标记，表示字符串中转义字符无效，是普通字符
# result=re.findall(r"\W",s)
# p=re.compile(r'[@](.*?)[:]', re.S)
# p1=re.compile(r'[:](.*?)', re.S)
# sendto=re.findall(p,s)
# massage=s.split(':',1)[1]
# s=re.findall(r"\W",req)
# if s!=[]:
#     sym1 = re.findall(r"\W",req)[0]
#     sym2 = re.findall(r"\W",req)[1]
# else:
#     sym1=0
#     sym2=0
# Time = time.strftime("%H:%M:%S", time.localtime())
# if sym1 == '@' and (sym2==':' or sym2 == '：'):
#             # sendto =
#     if sym2==':':
#         p = re.compile(r'[@](.*?)[:]', re.S)
#         sendto = re.findall(p, req)[0]
#         reqs = '我 ' + '(私聊'+ str(sendto) +')' +'(' + str(Time) + ')' + ':' + req.split(':',1)[1]
#         print(sendto)
#         print(reqs)
#     elif sym2=="：":
#         p = re.compile(r'[@](.*?)[：]', re.S)
#         sendto = re.findall(p, req)[0]
#         reqs = '我 ' + '(私聊'+ str(sendto) +')' +'(' + str(Time) + ')' + ':' + req.split('：',1)[1]
#         print(sendto)
#         print(reqs)
# else:
#     sendto = 0
#     reqs = '我 ' + '(' + str(Time) + ')' + ':' + req
#     print(sendto)
#     print(reqs)

# print(result)
# print(sendto)
# print(massage)
# print(massage[0])