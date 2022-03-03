import os
import pymysql
import xlsxwriter





from datetime import datetime
thetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class SQLLink:
    def __init__(self):
        # self.conn = pymysql.connect(host='127.0.0.1', port=3306, database='guo',
        #                     user='root', password='204800',
        #                     charset="utf8")

        self.conn = pymysql.connect(host='127.0.0.1', port=3306, database='xinpin',
                            user='root', password='204800',
                            charset="utf8")

        # self.conn = pymysql.connect(host='127.0.0.1', port=3306, database='weibo',
        #                     user='root', password='204800',
        #                     charset="utf8")

        self.cursor =  self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def insert_tb_index_data(self,title,price,shop_name,fake_link,thumb_pic_url):
        sql = "INSERT INTO tb(title,price,shop_name,fake_link,thumb_pic_url) VALUES(%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,(title,price,shop_name,fake_link,thumb_pic_url))
        self.conn.commit()
        print(title)


    def insert_zxcc_table(self,d_link,title,price,online_time):
        sql = "INSERT INTO zx_cc(d_link,title,price,online_time) VALUES(%s,%s,%s,%s)"
        self.cursor.execute(sql,(d_link,title,price,online_time))
        self.conn.commit()
        print(title)

    def get_wechat_data(self):
        sql = "SELECT * FROM tmp_search_url WHERE id BETWEEN 90600 AND 200000;"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def write_ph_db(self,ph_code):
        sql = "INSERT into ph_xinpin(ph_code) VALUES(%s)"
        self.cursor.execute(sql,(ph_code))
        self.conn.commit()
        print(ph_code)

    def get_ph_data(self):
        sql = "SELECT * FROM ph_xinpin"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res




    def close_db(self):
        self.conn.close()