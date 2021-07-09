from nonebot import require
from nonebot import get_bots
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import time
import os
import qzoneget

async def handle(bot: Bot, qqnum: str, to_num: list, to_group_num: list):
    print(f"正在读取{qqnum}的说说...")
    lst = await qzoneget.get_shuo(qqnum)
    # lst = [('大雨倾盆，浑身浇湿', 1625658084), ('从前几天开始上演的“人人比我放的早系列”', 1625040853), ('', 1624594494), ('与哲学的下午茶', 1624258802), ('', 1623599563), ('尊敬的各位老师，各位同学。大家下午好', 1623408875), ('画人画皮，难以真正画骨\n知人知面，终不完全知心\n三分人样，虽然未曾习得\n七分鬼相，却是熟练至极\n好鸿鹄志，谄媚同行舔之\n妒腾蛇翔，恶语流言伤之\n夏虫语冰，不知睫数几何\n井蛙疑海，难明孔光寸短\n君子喻义，岂效背德之法\n小人逐利，安求高洁之道\n', 1623168774)]
    # print("说说:", lst)
    dic = {}
    sender = ""
    if(not os.path.exists("../" + qqnum)):
        print("此人相关文件不存在,正在创建...")
        with open("../" + qqnum, "w") as f:
            print("创建成功!")
    print(f"正在读取{qqnum}已处理的说说...")
    with open("../" + qqnum, "r") as f:
        t = f.readline().replace('\n', "")
        while(t):
            dic[t] = 1
            t = f.readline().replace('\n', "")
    for i in lst:
        print("当前处理的说说:", i)
        if(i[0] == ""):
            continue
        if(dic.get(str(i[1]), -1) == -1):
            print("正在写出...")
            with open("../" + qqnum, "a") as f:
                f.write(str(i[1]) + "\n")
                dic[i[1]] = 1
                sender = i[0]
            for i in to_num:
                await bot.call_api("send_msg", user_id = i, message = sender)
            time.sleep(2)
            for i in to_group_num:
                print(type(i), ":", i)
                await bot.call_api("send_group_msg", message = sender, group_id = i)

        
