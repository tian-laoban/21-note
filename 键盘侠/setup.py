import pexpect
import time

ch = pexpect.spawn('sudo su', encoding='utf-8')
ch.expect('密码')
ch.sendline('tkx102')
ch.expect('验证成功')
print('success')
ch.sendline('python3 键盘侠.py')
