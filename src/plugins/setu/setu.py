from nonebot.adapters.cqhttp import Message
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.adapters.cqhttp import MessageSegment
import requests


pic=on_command('setu', priority=50)
@pic.handle()
async def _(bot:Bot,event:Event,state:T_State):
    msg = await suijitu()
    try:
        await pic.send(Message(msg))
    except CQHttpError:
        await pic.send(Message("error"))
async def suijitu():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
                }
    url = "https://api.lolicon.app/setu/v2"
    params = {"r18": 1,
        "num":1,
    }

    pic = requests.get(url=url, params=params, headers=headers).json()

    data=pic["data"]
    data2=list(data)
    data3=data2[0]
    data4=dict(data3)
    data5=data4['urls']
    url2=data5['original']
    url2=url2.replace("cat","re")
    pic_ti = f"[CQ:image,file={url2}]"
    return pic_ti
