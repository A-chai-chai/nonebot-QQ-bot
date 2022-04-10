import random
from datetime import date
from nonebot.plugin import on_command
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.adapters.cqhttp import Message



def luck_simple(num):
    if num < 18:
        return '大吉'
    elif num < 53:
        return '吉'
    elif num < 58:
        return '半吉'
    elif num < 62:
        return '小吉'
    elif num < 65:
        return '末小吉'
    elif num < 71:
        return '末吉'
    else:
        return '凶'
jrrp = on_command('jrrp', priority=50)  # 接收关键字

@jrrp.handle()  # 监听 jrrp
async def jrrp_handle(bot: Bot, event: Event):
    rnd = random.Random()
    rnd.seed((int(date.today().strftime("%y%m%d")) * 45) * (int(event.get_user_id()) * 55))
    lucknum = rnd.randint(1, 100)  

    # 返回QQ号， 发送消息
    await jrrp.finish(message=Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{100-lucknum}/100 为"{luck_simple(lucknum)}"'))
