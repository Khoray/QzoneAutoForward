from nonebot import require
from nonebot import get_bots
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import handler
import qzoneget

bot = get_bots()

scheduler = require('nonebot_plugin_apscheduler').scheduler
@scheduler.scheduled_job("cron", minute="*/5", id="xxx")
async def run_every_day_from_program_start():
    QQnums = ['2213622817', '1903388692']
    # await handler.handle(bot['2080306772'], QQnums[0], [935594374, 1251433731], [])
    await handler.handle(bot['2080306772'], QQnums[1], [1251433731], [1007891065])