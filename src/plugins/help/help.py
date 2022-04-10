import random
from datetime import date
from nonebot.plugin import on_command
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.adapters.cqhttp import Message

help = on_command('help', priority=50)  # 接收关键字

@help.handle()
async def handle(bot: Bot, event: Event):
    await help.finish(message=Message(f'目前功能还不是很完善，有待主人进一步更新捏~目前有的功能有：/chat 和人工智障聊天 指令格式形如（/chat 你好） /jrrp 测一下今天的人品怎么样 /塔罗牌 抽卡喵 /占卜 抽四张卡喵 /owner 查看主人信息 /pic 获取随机二次元图片 /news  查看热榜（包括知乎 微博 头条 csdn）指令格式为:/news zhihu（weibo/toutiao/csdn） /setu 不可以涩涩喵(如果实在忍不住要涩涩请联系管理员喵)'))
    