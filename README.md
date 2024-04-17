# 基于HUSTOJ的bs3主题的榜单爬取及天梯赛榜单生成工具
## Quick Start
仅需在BService中的填入链接即可(注意是该比赛oi榜单的url)
```
rank = GetRank('the url of the rank')
```
执行下面的命令
```
python app.py
```
然后访问该主机的80端口即可，如80端口被占用，可使用在app.py中最后修改
```
app.run(port=80)
```

### 数据爬取：
使用的是chrome driver + bs3
目前设置的是按照天梯赛的要求**必须为15个题目**，且每个题的分数分别为[5,5,10,10,15,15,20,20,25,25,25,25,30,30,30]，分数保留至小数点后2位。
