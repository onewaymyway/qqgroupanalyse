#! /usr/bin/env python3
#coding=utf-8
import os

dataFolder="qqGroups"
splitSign="|@|"
groupDic={}
userDic={}
userInfoDic={}
vipDic={}

baseForder="result"
def saveFile(file,msg):
    if os.path.exists(baseForder):
        pass;
    else:
        os.makedirs(baseForder)
    f=open(baseForder+"/"+file,"w",encoding="utf-8");
    f.write(msg)
    f.close()
    
def initGroupData():
    files=os.listdir(dataFolder)
    for f in files:
        tpath=os.path.join(dataFolder,f)
        if os.path.isfile(tpath):
            readGroupData(tpath)

def readGroupData(file):
    print("read",file)
    f=open(file,"r",encoding="utf-8")
    flines=f.readlines()
    f.close()
    group={}
    line=flines[0]
    arr=line.split(splitSign)
    group["id"]=arr[1]
    group["name"]=arr[0]
    members={}
    flines=flines[1:]
    for mem in flines:
        arr=mem.split(splitSign)
        memo={}
        memo["name"]=arr[0];
        memo["qq"]=arr[1];
        memo["iscreator"]=arr[2];
        memo["ismanager"]=arr[3];
        members[memo["qq"]]=memo
        addUserInfo(memo["qq"],group["id"],memo)
    group["mem"]=members
    groupDic[group["id"]]=group

def getGroupName(gid):
    return groupDic[gid]["name"];

def addVip(uid,gid):
    if uid in vipDic:
        pass;
    else:
        vipDic[uid]=[]
    vipDic[uid].append(gid)

    
def addUserInfo(uid,gid,uinfo):
    if uid in userDic:
        pass;
    else:
        userDic[uid]=[]

    #print(int(uinfo["iscreator"])!=0 , int(uinfo["ismanager"])!=0)
    if int(uinfo["iscreator"])!=0 or int(uinfo["ismanager"])!=0:
        addVip(uid,gid)

    userInfoDic[uid]=uinfo
    uglist=userDic[uid]
    uglist.append(gid)

def getGroupNames(gidList):
    nameList=[]
    for gid in gidList:
        nameList.append(getGroupName(gid))
    return ",".join(nameList);

def getMultiGroupUser():
    rstStrs=[]
    for user in userDic:
        uglist=userDic[user]
        if len(uglist)>1:
            usero=userInfoDic[user]
            uStr=usero["name"]+","+usero["qq"]
            isVip=False
            if user in vipDic:
                uStr+="\n*群管*"+getGroupNames(vipDic[user])
                isVip=True
            
            tL=getGroupNames(uglist)
            ifShow=isVip
            if ifShow:
                rstStrs.append(uStr+"\n加入的群-->"+tL)

            

    return "\n\n".join(rstStrs)


    
initGroupData()

saveFile("加入多群的用户.txt",getMultiGroupUser())

print("work done")
        
    
    
