from sre_parse import State
from nonebot.adapters.cqhttp import Message
from nonebot import on_command, on_keyword, on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.adapters.cqhttp import MessageSegment

pic=on_command('pic', priority=50)
@pic.handle()
async def _(bot:Bot,event:Event,state=T_State):
    msg = await suijitu()
    try:
        await pic.send(Message(msg))
    except CQHttpError:
        await pic.send(Message("error"))
async def suijitu():
    #url='https://api.ghser.com/random/api.php'
    #url='https://api.lolicon.app/setu/v2'
    #url='https://api.yimian.xyz/img'
    #url='https://www.dmoe.cc/random.php'
    #url='https://lapsepi/org/pic.php'
    #url='https://api.ixiaowai.cn/api/api.php'
    #url='https://imgapi.cn/cos.php?return=img'
    #url='http://www.dmoe.cc/random.php'
    url='https://acg.toubiec.cn/random.php'
    pic = requests.get(url)
    pic_ti = f"[CQ:image,file={pic.url}]"
    return pic_ti
