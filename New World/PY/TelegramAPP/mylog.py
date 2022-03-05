from time import strftime
'''我真是个天才'''

class LOG():
    def __init__(self,log_path,text =''):
        self.log_path = log_path
        with open(self.log_path,'a',encoding='utf-8') as log_file:
            log_file.write(strftime('%Y-%m-%d %H:%M:%S') + '---'+ text + '\n')

    def log(self,*x):
        s = ''
        for i in x:
            s += str(i)
        with open(self.log_path,'a',encoding='utf-8') as log_file:
            log_file.write(strftime('%Y-%m-%d %H:%M:%S') + '---'+ s +'\n')


if __name__ == '__main__':
    logger = LOG('mylog.log',text='日志开始记录')
    log = logger.log
    log('cnm ',[1,2,3],('a','b',4))
    log('nmb',[1,2,3],('a','b',4))