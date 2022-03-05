from playwright.sync_api import Playwright, sync_playwright
from time import sleep

def login(phone):
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.taobao.com/")
        flag = 0
        flag =input('是否登录完毕？(填写数字1)'+'\n：')
        while True:
            sleep(1)
            if flag:
                break

        context.storage_state(path=phone +'.json')
        browser.close()

# login('haha')

def run(phone) -> None:
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless =False)
        context = browser.new_context(storage_state = phone +'.json')
        page = context.new_page()
        page.goto("https://cart.taobao.com/cart.htm")  #购物车链接
        # sleep(10)
        order_lis = page.query_selector_all('.J_Order') #店铺列表
        for _,order in enumerate(order_lis):
            order_name = order.query_selector('.J_MakePoint').inner_text()
            #店铺名字
            print(_+1,'\n','店铺名称：', order_name)
            item_lis = order.query_selector_all('.item-holder') #商品列表
            for i,item in enumerate(item_lis):
                item_name = item.query_selector('.item-title').inner_text()
                item_prop = item.query_selector('.item-props').inner_text()
                item_price = item.query_selector('.price-now').inner_text() #单价
                try:
                    item_amount = item.query_selector('.J_ItemAmount').get_attribute('value')
                except:
                    item_amount ='1'
                item_price_sum = item.query_selector('.J_ItemSum').inner_text()

                print('商品编号：',i+1)
                print('商品名称',item_name)
                print(item_prop)
                print('单价：',item_price)
                print('购买数量：',item_amount)
                print('总价：',item_price_sum)
                print('-'*32)
            buy_password = input('请输入支付密码：')
            while True:
                order_id = input('请输入店铺编号：')
                buy_time = input('请选择购买时间')
                page.click('.shop-info .cart-checkbox')
                page.click('#J_Go')
                page.click('.go-btn')
                page.fill("input[name=\"payPassword_rsainput\"]", buy_password)
                # break

def init():
    pass

  







        # 展示购物车商品
        # # for 
        #     选择购物车商品
        #     选择数量
        #     选择时间




        # # Click i:nth-child(5)
        # page.click("i:nth-child(5)")

        # Click text=确认付款
        # page.click("text=确认付款")
        # 保存登录信息
        context.storage_state(path= phone +'.json')

        # Close page
        # page.close()


        # # ---------------------
        # context.close()
        browser.close()



def main():
    phone = input('输入手机号：')
    # login(phone)
    run(phone)

if __name__ == '__main__':
    main()

