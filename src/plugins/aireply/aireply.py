from nonebot.adapters.cqhttp import Bot, Event
from nonebot.plugin import on_command
from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword, on_metaevent, on_notice
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.adapters.cqhttp import MessageSegment
import requests

#自定义回复词典

#回复部分
reply=on_command("chat",priority=50) 
@reply.handle()
async def reply_handle(bot: Bot, event: Event):
    user_msg = str(event.get_message())
    #对输入进行判断并处理
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        }
        url = "http://api.qingyunke.com/api.php?key=free&&appid=0"
        params = {"msg": user_msg}
        response = requests.get(url=url, params=params, headers=headers).json()
        response2=response["content"]
        reply_msg = response2
        await reply.finish(reply_msg)
    except KeyError:
        await reply.finish()
