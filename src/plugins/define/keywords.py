import pymysql#初始化连接配置
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText

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



define = on_command("define", priority=50)


@define.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  
    if plain_text:
        matcher.set_arg("city", args)  


@define.got("str1", prompt="你想要定义什么关键词喵~")
async def handle_city(str1: Message = Arg(), city_name: str = ArgPlainText("city")):
    if city_name not in ["北京", "上海"]:  # 如果参数不符合要求，则提示用户重新输入
        # 可以使用平台的 Message 类直接构造模板消息
        await define.reject(str1.template("你想查询的城市 {city} 暂不支持，请重新输入！"))

    city_weather = await get_weather(city_name)
    await define.finish(city_weather)


# 在这里编写获取天气信息的函数
async def get_weather(city: str) -> str:
    return f"{city}的天气是..."
    









cursor.execute('insert into people values(%s,%s,%s);',('Bob','dev',50000))#或者也可以一次性添加多条记录

rows = [('Sue','mus',70000),('Ann','adm',60000)]

cursor.executemany('insert into people values(%s,%s,%s);',rows)

#操作完成后还需要进行事务提交以便数据库保存

db.commit()#此外连接对象还有事务回滚操作：db.rollback()

#最后关闭游标对象和连接对象

cursor.close()

db.close()