import random
from datetime import date
from nonebot.plugin import on_command
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.adapters.cqhttp import Message

owner = on_command('owner', priority=50)  # 接收关键字

@owner.handle()
async def handle(bot: Bot, event: Event):
    await owner.finish(message=Message(f'主人是最最最最最可爱的小姐姐~可以通过QQ号2659881587联系主人喵~'))