# password = 'a123456'
# 请使用者重复输入密码
# 最多输入3次
# 如果正确就印出"登入成功"
# 如果不正确 就印出"密码错误" 还有_次机会

password = 'a123456'
i = 3 #剩余机会
while i > 0:
	pwd = input('请输入密码：')
	if pwd == password:
		print('登入成功')
		break
	else:
		i = i - 1
		print('密码错误!还有', i, '次机会')
