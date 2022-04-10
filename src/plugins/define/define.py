import pymysql#初始化连接配置
from nonebot.adapters.cqhttp import Message
from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.adapters.cqhttp import MessageSegment

ConnectConfig ={'host': 'localhost',
                'port': 3306,
                'user': 'root',
                'passwd': 'Ykq159357#',
                'charset': 'utf8',
                'db': 'bot_data'}#创建连接对象

db =pymysql.connect(

host=ConnectConfig['host'],

port=ConnectConfig['port'],

user=ConnectConfig['user'],

passwd=ConnectConfig['passwd'],

charset=ConnectConfig['charset'],

db=ConnectConfig['db']


)#创建游标对象

cursor = db.cursor()


define=on_command({'define'})
@define.handle()
async def _(bot:Bot,event:Event):
    id=event.get_user_id()
    sql="use keywords(input char(30),output char(10),id var(10));"
    try:    
        await define.finish(message=Message(f'[CQ:at,qq={id}]请问你想要定义什么关键词喵~'))
    except CQHttpError:
        await input.send(Message("出错了喵~"))


matcher = on_message()
@matcher.receive()
async def handle_func(bot:Bot,e: Event):
    try:
        str1=e.get_message()
        await input.send(Message(""))
    except CQHttpError:
        await input.send(Message("出错了喵~"))
    

    async def selfdefine():
        print("请问你想要定义什么关键词喵~")
    sql="use keywords(input char(30),output char(10));"
    cursor.execute(sql)
    









cursor.execute('insert into people values(%s,%s,%s);',('Bob','dev',50000))#或者也可以一次性添加多条记录

rows = [('Sue','mus',70000),('Ann','adm',60000)]

cursor.executemany('insert into people values(%s,%s,%s);',rows)

#操作完成后还需要进行事务提交以便数据库保存

db.commit()#此外连接对象还有事务回滚操作：db.rollback()

#最后关闭游标对象和连接对象

cursor.close()

db.close()