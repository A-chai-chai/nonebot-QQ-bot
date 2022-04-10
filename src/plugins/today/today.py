from nonebot import on_command, on_keyword
from nonebot.adapters import Event
from nonebot.adapters.cqhttp import Bot, Message
from nonebot.typing import T_State
import httpx,requests

zhihu=on_command("daily",priority=50)

@zhihu.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    STORY_URL_FORMAT = 'https://daily.zhihu.com/story/{}'
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://news-at.zhihu.com/api/4/news/latest')
        data = resp.json()
        stories = data.get('stories')
        if not stories:
            await zhihu.send(Message('暂时没有数据，或者服务无法访问'))
            return
        reply = ''
        for story in stories:
            url = STORY_URL_FORMAT.format(story['id'])
            title = story.get('title', '未知内容')
            reply += f'\n{title}\n{url}\n'
        data=reply.strip()
        await zhihu.send(Message(data))
