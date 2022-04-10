from unicodedata import name
from matplotlib.pyplot import title
from nonebot import on_command, on_keyword
from nonebot.adapters import Event
from nonebot.adapters.cqhttp import Bot, Message
from nonebot.typing import T_State
import httpx,requests
from nonebot.adapters import MessageSegment
from nonebot.adapters.cqhttp import MessageSegment

news=on_command("news weibo",priority=50)

@news.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    async with httpx.AsyncClient() as client:
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        url = "https://v2.alapi.cn/api/tophub/get"
        payload = "token=WMd0c9eBJUlMy4iE&type=weibo"
        response = requests.request("POST", url, data=payload, headers=headers).json()
        data=response["data"]
        name=data.get('name')
        list=data.get('list')
        reply=''
        reply2=''
        flag=0
        for story in list:
            title=story.get('title')
            url=story.get('link')
            if flag<=24:
                reply += f'\n{title}\n{url}\n'
            else:
                reply2 += f'\n{title}\n{url}\n'
            flag=flag+1
        data=reply.strip()
        data2=reply2.strip()
        await news.send(Message(name))
        await news.send(Message(data))
        #await news.send(Message(data2))
        