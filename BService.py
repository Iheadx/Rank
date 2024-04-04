from rank import GetRank
from user import Player
import json

rank = GetRank('http://192.168.31.63/contestrank-oi.php?cid=1060')
with open('team/华山论剑.json','r',encoding='utf-8') as f:
    team_data_hs = json.load(f)
with open('team\珠峰争鼎.json','r',encoding='utf-8') as f:
    team_data_zf = json.load(f)

user_list = {}
user2team = {}
userhs={}
userzf={}
team_hs={}
for it in team_data_hs:
    team_hs.update({it['team_id']:{"member":it['team_member'],"name":it["team_name"]}})
    for mb in it['team_member']:
        user_list.update({mb['id']:mb['name']})
        user2team.update({mb['id']:it['team_id']})
userhs=user_list

team_zf={}
for it in team_data_zf:
    team_zf.update({it['team_id']:{"member":it['team_member'],"name":it["team_name"]}})
    for mb in it['team_member']:
        user_list.update({mb['id']:mb['name']})
        userzf.update({mb['id']:mb['name']})
        user2team.update({mb['id']:it['team_id']})



def userrank():
    data = rank.userRank()
    tmp_usr = user_list.copy()
    
    table_data = []
    for i in range(len(data)):
    # for it in table_data:
        if data[i]['id'] not in tmp_usr:continue
        tmp_usr.pop(data[i]['id'])
        
        data[i]['name'] = user_list[data[i]['id']]

        if (data[i]['L2'] < 40 or data[i]['L1']< 80) and data[i]['L3']>0:
            data[i]['L3'] = str(data[i]['L3'])+'🤡'
        if data[i]['L1'] < 80 and data[i]['L2'] > 0:
            data[i]['L2'] = str(data[i]['L2'])+'🤡'
        for letter in range(ord('A'),ord('O')+1):
            j = chr(letter)
            if data[i][j] == -1:
                data[i][j] = '-'
        table_data.append(data[i])

    for id,name in tmp_usr.items():
        table_data.append({'id':id,'name':name,'L1':0,'L2':0,'L3':0,'A':'-','B':'-','C':'-','D':'-','E':'-','F':'-','G':'-','H':'-','I':'-','J':'-','K':'-','L':'-','M':'-','N':'-','O':'-','score':0,'tot':0})
    
    # 将ans按score降序排列
    table_data.sort(key=lambda x: x['score'],reverse=True)
    # 为ans添加排名
    for i in range(len(table_data)):
        table_data[i]['rank'] = i+1
    
    # print(user_list)
    return table_data

def teamrank(catalog):
    '''
    catalog: 'hs' or 'zf'
    return:{"name","L123","score","Rank"}
    '''
    table_data = rank.userRank()

    ans={}
    if catalog == 'hs':
        for key,value in team_hs.items():
            ans.update({key:{"team_id":key,"name":value['name'],"L123":[0,0,0]}})

    if catalog == 'zf':
        for key,value in team_zf.items():
            ans.update({key:{"team_id":key,"name":value['name'],"L123":[0,0,0]}})

    for it in table_data:
        if catalog=='hs' and (it['id'] not in userhs): continue
        if catalog=='zf' and (it['id'] not in userzf): continue

        if catalog == 'hs' and (user2team[it['id']] in team_hs):
            ans[user2team[it['id']]]['L123'][0]+=it['L1']
            ans[user2team[it['id']]]['L123'][1]+=it['L2'] 
            ans[user2team[it['id']]]['L123'][2]+=it['L3']
        
        if catalog == 'zf' and (user2team[it['id']] in team_zf):
            ans[user2team[it['id']]]['L123'][0]+=it['L1']
            ans[user2team[it['id']]]['L123'][1]+=it['L2'] 
            ans[user2team[it['id']]]['L123'][2]+=it['L3']

    for key,value in ans.items():
        value.update({'score':sum(value['L123'])})
    
    ans_list = [value for key,value in ans.items()]

    for i in range(len(ans_list)):
        if ans_list[i]['L123'][2]>0 and (ans_list[i]['L123'][1]<40*8 or ans_list[i]['L123'][0]<80*8):
            ans_list[i]['L123'][2] = str(ans_list[i]['L123'][2])+'🤡'
        if ans_list[i]['L123'][1]>0 and ans_list[i]['L123'][0]<80*8:
            ans_list[i]['L123'][1] = str(ans_list[i]['L123'][1])+'🤡'

    # 将ans按score降序排列
    ans_list.sort(key=lambda x: x['score'],reverse=True)
    # 为ans添加排名
    for i in range(len(ans_list)):
        ans_list[i]['rank'] = i+1
    
    return ans_list

def getteamans(teamID):
    member = []
    if teamID in team_hs:
        member = team_hs[teamID]['member']
    elif teamID in team_zf:
        member = team_zf[teamID]['member']
    
    member_id = {}
    for item in member:
        member_id.update({item['id']:item['name']})

    data = rank.userRank()

    teamans = []
    for item in data:
        if item['id'] not in member_id:continue
        member_id.pop(item['id'])

        res = item
        res['name'] = user_list[res['id']]
        if (res['L2'] < 40 or res['L1']< 80) and res['L3']>0:
            res['L3'] = str(res['L3'])+'🤡'
        if res['L1'] < 80 and res['L2'] > 0:
            res['L2'] = str(res['L2'])+'🤡'
        for letter in range(ord('A'),ord('O')+1):
            j = chr(letter)
            if res[j] == -1:
                res[j] = '-'

        teamans.append(res)
    
    for id,name in member_id.items():
        teamans.append({'id':id,'name':name,'L1':0,'L2':0,'L3':0,'A':'-','B':'-','C':'-','D':'-','E':'-','F':'-','G':'-','H':'-','I':'-','J':'-','K':'-','L':'-','M':'-','N':'-','O':'-','score':0,'tot':0})
    
    return teamans

