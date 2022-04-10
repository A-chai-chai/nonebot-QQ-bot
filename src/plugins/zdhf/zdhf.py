from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.plugin import on_message


#自定义回复词典
reply_dic = {
    'win指导': '是我跌' ,
    '一眼丁真'  : '鉴定为寄' ,
    '打个胶先'    : '打我嘴里',
    '爱你喵'    :'我也爱你喵'
}
#回复部分
reply = on_message(priority=100)
@reply.handle()
async def reply_handle(bot: Bot, event: Event):
    user_msg = str(event.get_message()).strip()
    #对输入进行判断并处理
    try:
        reply_msg = reply_dic[user_msg]
        await reply.finish(reply_msg)
    except KeyError:
        await reply.finish()
