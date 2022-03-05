import asyncio  
from telethon import TelegramClient
from settings import api_id,api_hash
from mylog import LOG
logger = LOG('LOG/upload.log',text='日志开始记录')
log = logger.log


async def main():
    client = TelegramClient('upload', api_id, api_hash,proxy=('socks5', '127.0.0.1',8888))
    await client.start()
    me = await client.get_me()
    print('你好啊，',me.username,'!')


    while True:
        mode = input('切换模式：')
        if mode in ('@f',''):
            while True:
                file_path = input('请输入文件路径：')
                if file_path == 'end':
                    break
                if file_path == 'dir':
                    import os
                    dir_path = input('请输入目录路径：')
                    for _ in os.listdir(dir_path):
                        file_path = os.path.join(dir_path,_)
                        if not os.path.isdir(file_path):
                            log('正在上传：',file_path)
                            await client.send_file('me',file_path)
                else:
                    log('正在上传：',file_path)
                    await client.send_file('me',file_path)
        if mode in ('@t','@message','@text'):
            while True:
                text = input('输入文本：')
                if text == 'end':
                    break
                else:
                    await client.send_message('me',text) # 发到“收藏夹”
        if mode in ('exit','end'):
            return
         

asyncio.run(main())


