from selenium import webdriver
from bs4 import BeautifulSoup
from user import Player
import re
import time

class GetRank:
    def __init__(self,url) -> None:
        # 设置Chrome Driver的选项
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # 可选，无头模式运行Chrome，即不会打开浏览器窗口
        # 创建一个WebDriver实例，例如ChromeDriver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = url
        # 获取原始数据
        self.table = None
        # 处理后的数据
        self.table_data = None
        self.lasttime = None
    def get_url(self):
        # 打开网页
        self.driver.get(self.url)
        # 获取页面源代码
        html_source = self.driver.page_source
        # 使用BeautifulSoup解析页面源代码
        self.soup = BeautifulSoup(html_source, 'html.parser')
        # 定位目标表格
        self.table = self.soup.find('table', {'id': 'rank'}) 
    def get_user_data(self,row_data):
        # 每题最高分
        tot_list = [5,5,10,10,15,15,20,20,25,25,25,25,30,30,30]
        get_score = []
        # 总共15题 下标6-21 可根据不同题目数量调整
        for i in range(6,21):
            score = row_data[i]
            if len(score) >= 8:
                get_score.append(tot_list[i-6])
            elif len(score) == 0:
                get_score.append(-1)
            else:
                # 新oj 从(+n)中提取数字
                num = int(re.search(r'\d+', score).group())
                get_score.append(num*tot_list[i-6]/100)

                # # 老OJ 直接提取数字
                # get_score.append(score*tot_list[i-6]/100)
        return Player(row_data[1],row_data[2],get_score)
 
    def list2json(self,table_date):
        ans = []
        for item in table_date:
            L1,L2,L3,L2_istrue,L3_istrue,score = item.get_score()
            ans.append({
                'id':item.id,
                'name':item.name,
                'L1':L1,
                'L2':L2,# if L2_istrue or L2==0 else str(L2)+'🤡',
                'L3':L3,# if L3_istrue or L3==0 else str(L3)+'🤡',
                'A':item.score_list[0],# if item.score_list[0] != -1 else '-',
                'B':item.score_list[1],# if item.score_list[1] != -1 else '-',
                'C':item.score_list[2],# if item.score_list[2] != -1 else '-',
                'D':item.score_list[3],# if item.score_list[3] != -1 else '-',
                'E':item.score_list[4],# if item.score_list[4] != -1 else '-',
                'F':item.score_list[5],# if item.score_list[5] != -1 else '-',
                'G':item.score_list[6],# if item.score_list[6] != -1 else '-',
                'H':item.score_list[7],# if item.score_list[7] != -1 else '-',
                'I':item.score_list[8],# if item.score_list[8] != -1 else '-',
                'J':item.score_list[9],# if item.score_list[9] != -1 else '-',
                'K':item.score_list[10],# if item.score_list[10] != -1 else '-',
                'L':item.score_list[11],# if item.score_list[11] != -1 else '-',
                'M':item.score_list[12],# if item.score_list[12] != -1 else '-',
                'N':item.score_list[13],# if item.score_list[13] != -1 else '-',
                'O':item.score_list[14],# if item.score_list[14] != -1 else '-',
                'score':score,
                'tot':item.tot
            })
        # 将ans按score降序排列
        ans.sort(key=lambda x: x['score'],reverse=True)
        # 为ans添加排名
        for i in range(len(ans)):
            ans[i]['rank'] = i+1
        return ans

    def getRank(self):
        self.lasttime = time.time()
        self.get_url()
        # 初始化二维列表
        table_data = []
        # 去除表头
        tmp = self.table.find('tbody')
        # 遍历每个<tr>元素
        for row in tmp.find_all('tr'):
            row_data = [cell.text for cell in row.find_all('td')]
            res = self.get_user_data(row_data)
            table_data.append(res)
        self.table_data = table_data
        return table_data
    
    def userRank(self):
        if self.table_data == None or time.time()-self.lasttime > 5:
            self.getRank()
        return self.list2json(self.table_data)

    def close_driver(self):
        self.driver.close()