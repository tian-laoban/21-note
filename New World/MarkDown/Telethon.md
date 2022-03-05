# Telethon

> Telethon 是Telegram官方发布的用于操纵telegram的Python异步库。

## 基操

1. 安装pip库<br>
    必装：telethon<br>
    可选
    - cryptg(提升运行速度)
    - pillow(自动调整大图像大小以保证图片成功发送)
    - aiohttp(下载WebDocument媒体文件)
    - hachoir(显示歌曲的信息)<br>

2. 获取api_id和api_hash
    1. 登录 https://my.telegram.org/
    2. 点击“API Development tools”
    3. 填写“App title” 和 “Short name”
    4. 点击“Create application”

3. 简单代码
```python
import asyncio
from telethon import TelegramClient


api_id:int = 
api_hash:str = 

async def main():
    client = TelegramClient('anon', api_id, api_hash,proxy=('socks5', '127.0.0.1',8888))
    await client.start()
    me = await client.get_me()
    print(me.stringify())
    print(me.username)
    print(me.phone)    
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(dialog.name, '-----------ID：', dialog.id)
    await client.send_message('me','晚来天欲雪') # 发到“收藏夹”
    await client.send_message(-1001249071303,"能饮一杯无") #依据“dialog.id”发送，第一个参数：int
    await client.send_message('+8618734241370',"来来去去") #依据 手机号 发送，第1个参数：str
    await client.send_message('tianlaoban',"走走空空") #依据 username 发送
    message = await client.send_message('me','滴答滴答')
    print(message.raw_text)     #查看消息
    await message.reply('cnm')  #回复该消息
    await client.send_file('me','/home/tianlaoban/Pictures/壁纸.jpg') #发送文件
    # 输出一个  聊天会话的消息
    messages = await client.get_messages('me',min_id=1,max_id=500) #get_messages()有很多参数，参考官方文档
    print(len(messages))
    for message in messages:
        print(message.id,message.text)


asyncio.run(main())


```
