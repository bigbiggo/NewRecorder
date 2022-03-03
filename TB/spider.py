import requests
from scrapy import Selector
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from w3lib.html import remove_tags
from urllib.parse import urljoin
from TB.db import SQLLink


sql_link = SQLLink()


time_list = [1.7,1.5,1.8,1.6,1.4,1.5]


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9888")
chrome_driver = "D:\Temp\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.set_page_load_timeout(320)




head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

url_queue = []

def page_down():
    try:
        crawl_status = 1
        if crawl_status:
            js_height = 'return document.body.parentNode.scrollHeight'
            height = driver.execute_script(js_height)
            k = 1
            while True:
                if k > 16:
                    break
                if k * 500 < height:
                    nex_vi = str(k * 500)
                    js_move = "window.scrollTo(0,{})".format(nex_vi)
                    driver.execute_script(js_move)
                    height = driver.execute_script(js_height)
                    k += 1
                    sleep_pop = [0.55,0.45,0.65,0.57,0.54]
                    time.sleep(random.choice(sleep_pop))
                else:
                    break
    except Exception as e:
        print("page_down-----", e.args)


def append_task_url(url):
    url_queue.append(url)


def send_requests_by_bro():
    while True:
        try:
            url = url_queue.pop()
            driver.get(url)
            time.sleep(random.choice(time_list))
            page_down()
            source = driver.page_source
            parse_source(source)

            if "下一页" in source:
                driver.find_element_by_class_name("pc-search-page-item-after").click()
                sleep_pop = [0.23, 0.31, 0.35, 0.37, 0.44]
                time.sleep(random.choice(sleep_pop))
                next_url = driver.current_url
                print("next_url：",next_url)
                url_queue.append(next_url)
                driver.maximize_window()
            else:
                break
        except Exception as e:
            print(e.args)

            time.sleep(random.choice(time_list))


def parse_source(html):
    response = Selector(text=html)
    nodes = response.xpath("//ul[@class='pc-search-items-list']/li")
    for node in nodes:
        title = node.xpath(".//span[@class='title-text']/text()").extract_first("")
        price = node.xpath(".//span[@class='coupon-price-afterCoupon']/text()").extract_first("")
        shop_name = node.xpath(".//div[@class='seller-name']/text()").extract_first("")
        fake_link = node.xpath("./a[@class='pc-items-item-a']/@href").extract_first("")
        thumb_pic_url = node.xpath(".//img/@src").extract_first("")
        sql_link.insert_tb_index_data(title,price,shop_name,fake_link,thumb_pic_url)




if __name__ == "__main__":
    f = open("init_url.txt","r",encoding="utf8")
    data = f.read()
    inti_url = data.strip()
    append_task_url(inti_url)
    send_requests_by_bro()


