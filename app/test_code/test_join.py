import string
import secrets


string_test = ['how','are','you']
#print('A'.join(string_test))


alphabet = string.ascii_letters + string.digits
#print(alphabet)

letter = secrets.choice(alphabet)
#print(letter)  # 输出一个字符，随机的

#print(secrets.choice(alphabet) for _ in range(5))  # 这样不行，因为print()里面其实是一个元组，print函数先自己独立执行了

#secrets.choice(alphabet) for _ in range(5) #这样两句代码就割裂了。


# for i in range(5):
#     print(i)

tokens = [secrets.choice(alphabet) for _ in range(5)]  # 生成列表，如 ['A', 'b', '3', 'd', '2']
print(tokens)
print(''.join(tokens))  # 拼接成字符串，如 "Ab3d2"  --直接打印出来了字符串，没有中括号

print(list(secrets.choice(alphabet) for _ in range(5)))