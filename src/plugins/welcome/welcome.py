from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Message, GroupDecreaseNoticeEvent, GroupIncreaseNoticeEvent
 
welcome = on_notice()
#朋友加群
@welcome.handle()
async def _(bot: Bot, event:GroupIncreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '欢迎新人喵~'
    msg = Message(msg)
    await welcome.finish(message=msg)
 
#群友退群
@welcome.handle()
async def _(bot: Bot, event:GroupDecreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '\n' + '呜呜，别走喵~'
    msg = Message(msg)
    await welcome.finish(message=msg)