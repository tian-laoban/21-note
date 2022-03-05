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
    await client.send_message('me','I love you') # 发到“收藏夹”
    await client.send_message(-1001249071303,"but I can't tell you") #依据“dialog.id”发送，第一个参数：int
    await client.send_message('+8618734241370',"Sad.") #依据 手机号 发送，第1个参数：str
    await client.send_message('tianlaoban',"or Good？") #依据 username 发送
    message = await client.send_message('me','I love you,LD')
    print(message.raw_text)     #查看消息
    await message.reply('cnm')  #回复该消息
    await client.send_file('me','/home/tianlaoban/Pictures/壁纸.jpg') #发送文件
    # 输出一个  聊天会话的消息
    messages = await client.get_messages('me',min_id=1,max_id=500) #get_messages()有很多参数，参考官方文档
    print(len(messages))
    for message in messages:
        print(message.id,message.text)





asyncio.run(main())