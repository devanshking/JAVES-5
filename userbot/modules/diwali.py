#made by shivam patel
from telethon import events

import asyncio

from userbot.utils import admin_cmd
from userbot import bot as javes
@javes.on(admin_cmd("hdd"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,20)
    await event.edit("Happy Diwali Dosto🤗")
    animation_chars = [
            """-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙""",
            """💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜""",
            """"💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖""",
            """❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖 
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙""",
            """💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖 
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️""",
 """💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖 
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚"""           ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])
@javes.on(admin_cmd("diwali"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(80)
    await event.edit("❤Happy Diwali Dosto❤")
    animation_chars = ["💖happy💖diwali💖","💙happy💙diwali💙","❤️happy♥️diwali❤️","💚happy💚diwali💚","💜happy💜diwali💜",]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])
@javes.on(admin_cmd("dosto"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(22)
    await event.edit("❤Dosto❤")
    animation_chars = ["""💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜""","""ㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
                    💙💙
                 💙💙💙
             💙💙💙💙
            💙💙 💙💙
          💙💙    💙💙
        💙💙       💙💙
     💙💙💙💙💙💙
      💙💙💙💙💙💙
   💙💙                 💙💙
  💙💙                    💙💙
💙💙                       💙💙""","""💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚                     💚💚
💚💚                     💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚
💚💚
💚💚
💚💚
💚💚""","""💛💛💛💛💛💛
💛💛💛💛💛💛💛
💛💛                💛💛
💛💛                💛💛
💛💛💛💛💛💛💛
💛💛💛💛💛💛
💛💛
💛💛
💛💛
💛💛""","""💜💜                    💜💜
   💜💜              💜💜
      💜💜        💜💜
         💜💜  💜💜
            💜💜💜
              💜💜
              💜💜
              💜💜
              💜💜
              💜💜""","""💖💖💖💖💖💖💖
💖💖💖💖💖💖💖💖
💖💖                      💖💖
💖💖                         💖💖
💖💖                         💖💖
💖💖                         💖💖
💖💖                         💖💖
💖💖                      💖💖
💖💖💖💖💖💖💖💖
💖💖💖💖💖💖💖""","""💝💝💝💝💝💝
💝💝💝💝💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
💝💝💝💝💝💝
💝💝💝💝💝💝""","""💖💖                               💖💖
💖💖                               💖💖
💖💖                               💖💖
💖💖                               💖💖
💖💖              💖            💖💖
 💖💖           💖💖          💖💖
 💖💖        💖💖💖       💖💖
  💖💖   💖💖  💖💖   💖💖
   💖💖💖💖      💖💖💖💖
    💖💖💖             💖💖💖""","""ㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
                    💙💙
                 💙💙💙
             💙💙💙💙
            💙💙 💙💙
          💙💙    💙💙
        💙💙       💙💙
     💙💙💙💙💙💙
      💙💙💙💙💙💙
   💙💙                 💙💙
  💙💙                    💙💙
💙💙                       💙💙""","""💘💘
💘💘
💘💘
💘💘
💘💘
💘💘
💘💘
💘💘
💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘""","""💝💝💝💝💝💝
💝💝💝💝💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
💝💝💝💝💝💝
💝💝💝💝💝💝""",]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])
