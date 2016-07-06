#! /usr/bin/env python3
#coding=utf-8
import urllib.parse
import urllib.request
import json
import time
import socket
import os


member_url="http://qun.qzone.qq.com/cgi-bin/get_group_member";
group_url="http://qun.qzone.qq.com/cgi-bin/get_group_list";
friend_url="http://r.qzone.qq.com/cgi-bin/tfriend/friend_show_qqfriends.cgi";

socket.setdefaulttimeout(9.0)

tNum=50003251804803;
qqid="484641127"


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#district=0&hcountry=0&hprovince=0&hcity=0&hdistrict=0&online=1&ldw=360759066
values = {
          'uin' : qqid,
          'g_tk' : '98774747'
          #'g_tk' : '127746213'
         }
values["groupid"]=104144216;
values["callbackFun"]="_GroupMember";

headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Host': 'qun.qzone.qq.com',
    #'Host': 'r.qzone.qq.com',
    #'Origin': 'http://find.qq.com',
    #'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection' : 'keep-alive',
    'Cookie' : 'uin=o0'+qqid+'; skey=@HgN7i4hzc;',
    #'Cookie' : '',
    #'Referer' : 'http://qun.qzone.qq.com/group',
   # 'Referer' : 'http://ctc.qzs.qq.com/qzone/v8/pages/friends/newfriends_chain_req.html',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
            }

displayed={};
ISOTIMEFORMAT='%Y-%m-%d %X'

baseForder="qqGroups"

splitSign="|@|"

def saveFile(file,msg):
    if os.path.exists(baseForder):
        pass;
    else:
        os.makedirs(baseForder)
    f=open(baseForder+"/"+file,"w",encoding="utf-8");
    f.write(msg)
    f.close()

def getGroupMember(groupid,groupName):
    print("getGroupMember:",groupid)
    values["groupid"]=groupid;
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') 
    turl=member_url;
    req = urllib.request.Request(turl, data, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    #print(the_page)
    #the_page=the_page[2:-1]
    tStr=the_page.decode("utf8")
    tStr=tStr.replace("_GroupMember_Callback(","")
    tStr=tStr[0:-2];
    #print(tStr[-3:])

   
    jsonData=json.loads(tStr);

    mList=jsonData["data"]["item"]
    #{"iscreator":0,"ismanager":0,"nick":"咖啡","uin":176206}
    members=[groupName+splitSign+str(groupid)]
    for kk in mList:
        #print(kk)
        #print(kk["uin"])
        members.append(kk["nick"]+splitSign+str(kk["uin"])+splitSign+str(kk["iscreator"])+splitSign+str(kk["ismanager"]));

    groupName=groupName.replace("/","@")
    groupName=groupName.replace("|","@")
    groupName=groupName.replace("*","@")

    saveFile(str(groupid)+".txt","\n".join(members))
        
def getGroupList(words):

    print("getQQGroupList")
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') 
    turl=group_url;
    req = urllib.request.Request(turl, data, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    #print(the_page)
    #the_page=the_page[2:-1]
    tStr=the_page.decode("utf8")
    tStr=tStr.replace("_GroupMember_Callback(","")
    tStr=tStr[0:-2];
    #print(tStr)

   
    jsonData=json.loads(tStr);

    mList=jsonData["data"]["group"]
    #{"auth":0,"flag":0,"groupid":258609451,"groupname":"产品运营经理-产品邦"}
    for kk in mList:
        #print(kk)
        print(kk["groupid"])
        getGroupMember(kk["groupid"],kk["groupname"]);

    return

def getFriendList():

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') 
    turl=friend_url;
    req = urllib.request.Request(turl, data, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    #print(the_page)
    #the_page=the_page[2:-1]
    tStr=the_page.decode("utf8")
    tStr=tStr.replace("_GroupMember_Callback(","")
    tStr=tStr[0:-2];
    print(tStr)

   
    jsonData=json.loads(tStr);
    for kk in jsonData:
        print(kk)
    mList=jsonData["items"]
    #{"uin":50126243, "groupid":5, "name":"yung", "remark":"朱春阳", "img":"http://qlogo4.store.qq.com/qzone/50126243/50126243/30", "yellow":-1, "online":0, "v6":1}
    for kk in mList:
        #print(kk)
        print(kk["uin"])

    return 

#getFriendList()
getGroupList('')
print("work done")
#getGroupMember("7044280")
##while(1):
##    try:
##        getInfo('484641127');
##        break
##    except:
##        print('error')
##    time.sleep(10)





