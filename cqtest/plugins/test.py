from nonebot import require
from nonebot import get_bots
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import handler
import qzoneget

# bot = get_bots()

# scheduler = require('nonebot_plugin_apscheduler').scheduler
# @scheduler.scheduled_job("cron", second="*/5", id="xxx")
# async def run():
    # await bot['2080306772'].call_api("send_group_msg", message = "f", group_id = 1007891065)