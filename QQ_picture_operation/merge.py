import datetime
import json
import os
import re
import sys
import shutil
def app_path():
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        return os.path.dirname(sys.executable)  #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)                 #没打包前的py目录

def readFile(path,content={}):
    if '.json' in path:
        if not os.path.exists(path):
            with open(path,'w',encoding='utf-8') as fp:
                json.dump(content,fp,ensure_ascii=False)
        with open(path,'r',encoding='utf-8') as fp:
            content = json.loads(fp.read())
    else:
        if not os.path.exists(path):
            with open(path,'w',encoding='utf-8') as fp:
                fp.write('{}'.format(content))
        with open(path,'r',encoding='utf-8') as fp:
            content = fp.read()
    return content

def getCreateTime(path)->str:
    return str(datetime.datetime.fromtimestamp(os.path.getctime(path))).replace(':',"-").replace(' ','-')
def renameTime(basedir,filename):
    if '.' in filename:
        exp=filename[filename.rfind('.'):]
    else:
        exp=''
    resource=os.path.join(basedir,filename)
    target=os.path.join(basedir,getCreateTime(resource)+exp)
    os.rename(resource,target)
def merge(resource='',target='',count=0,maxCount=999,op='move',timename=0):
    count+=1
    print(resource,count)
    basedir=resource
    for dirs in os.listdir(resource):
        resource=os.path.join(basedir,dirs)
        if os.path.isdir(resource) and count<maxCount:
            merge(resource,target,count,maxCount,op,timename)
        else:
            print(resource)
            if op=='move':
                shutil.move(resource,target)
            else:
                shutil.copy2(resource,target)
            if timename==1:
                renameTime(target,dirs)
            
def isExist(path:str,op=1):
    if '.' in path:
        path=path[:path.rfind('.')]
    print(path)
    if not os.path.exists(path):
        if op==1:
            
            os.makedirs(path)
        return False
    else:
        return True
def inputText(resource,target,op=0):
    if op==0 or op==1:
        resource=input('请输入源路径:')
    elif op==0 or op==2:
        target=input('请输入目的路径:')
    else:
        if op!=4:
            return
    if not isExist(resource,0):
        inputText(resource,target,1)
    if not isExist(target):
        inputText(resource,target,2)
    return resource,target
if __name__=='__main__':
    resource=r'F:\Group2'
    target=r'F:\Group'
    inputText(resource,target,4)
    merge(resource,target,op='c',timename=1)
    