
import calendar
import time


def trans_wday(wday):
    trans_dic = {0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期日'}
    return trans_dic[wday]

# 输入
local_time = time.localtime()
year = str(local_time[0])
month = str(local_time[1])
day = str(local_time[2])
wday = trans_wday(local_time[6]) #星期 range  [0,6]
date_view = year + '年'+ month +'月'+day+'日\n                                  ' + wday 
# print(date_view)


# 支出
def out_money():
    thing = input('物品名称：')
    price = input('单价：')
    amount = input('数量：')
    pay_way = input('支付方式：\n1.支付宝  2.微信  3.银行卡  4.现金\n')
    is_submit = input('是否提交？（y/n）')
    if is_submit in ['y','Y','是','1']:
        print(thing,price,amount,pay_way)


# 收入
def in_money():
    # 收入 收入类型 
    income = input('收入金额：')
    income_type = input('收入类型：')
    is_submit = input('是否提交？（y/n）')
    if is_submit in ['y','Y','是','1']:
        print(income,income_type)
  
# 查询


# 借出：
#     犀利 700
#     李靖 200
#     刁梦丽  400
#     李梦前  2000

# 借入：
#     支付宝
#     美团
#     京东金融
#     国家开发银行

def go():
    s = '''田先生♂，欢迎使用money系统，爱你哟♥！
                            ''' + date_view
    print(s)
    while True:
        mode = input('输入指令：')
        if mode in ['']

    


if __name__ == '__main__':
    go()


