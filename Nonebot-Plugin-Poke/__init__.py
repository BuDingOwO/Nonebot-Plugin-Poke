import time
from nonebot import get_driver
from .config import Config
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.rule import Rule
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.params import CommandArg, ArgPlainText, Arg
from nonebot.adapters.onebot.v11 import MessageEvent, Event, Bot
from nonebot.params import State
from typing import Union
import json
import random

global_config = get_driver().config
config = Config.parse_obj(global_config)

__help_plugin_name__ = '戳一戳,rua一rua'
__help_version__ = '1.0'

__des__ = "戳一戳"
__cmd__ = f"""
指令前缀 + 指令
当前配置的指令前缀为: {" ".join(list(get_driver().config.command_start))}
""".strip()
__list__ = """

戳我 | 连续戳你自己 5 次，每次间隔 1s
戳@qq | 连续戳 被艾特到的兽兽 5次，每次间隔1s

""".strip()
__usage__ = f"{__des__}\n\nUsage:\n{__cmd__}\n\nCommandList:[指令名 | 指令介绍]\n{__list__}"


def get_at_user_id(data: str) -> Union[list[str], list[int], list]:
    """
    获取at里的qq，返回[qq, qq, qq,...]
    全体成员直接返回['all']
    如果没有at任何人，返回[]
    :param data: event.json
    :return: list
    """
    try:
        qq_list = []
        data = json.loads(data)
        for msg in data["message"]:
            if msg["type"] == "at":
                if 'all' not in str(msg):
                    qq_list.append(int(msg["data"]["qq"]))
                else:
                    return ['all']
        return qq_list
    except KeyError:
        return []


matcher = on_command("戳我", priority=5, block=False)


@matcher.handle()
async def poke(event: Event, matcher: Matcher, arg: Message = CommandArg()):
    user_id = event.get_user_id()
    IntArg = 0
    at = MessageSegment.at(user_id=user_id)

    await matcher.send(at + MessageSegment.face(28) + MessageSegment.face(109) +
                       MessageSegment.face(183) + "rua死你！！！")
    arg = arg.extract_plain_text()
    if not arg == "":
        try:
            IntArg = int(str(arg))
        except ValueError:
            await matcher.finish(";w; 只能是数字哦~")

        if IntArg == 0:
            await matcher.finish("让我戳0下是罢！！")

        elif IntArg > 20:
            Random_key = random.randint(1, 10)
            await matcher.send(f"戳这么多下爪爪会断掉的叭，那还是戳{Random_key}下叭~ UwU")
            count = Random_key
        else:
            count = IntArg
    else:
        count = 5
    # poke = MessageSegment.poke(type_="poke", id_=str(user_id))
    poke = f'[CQ:poke,qq={user_id}]'
    temp_count = 0
    while not temp_count == count:
        await matcher.send(poke)
        temp_count = temp_count + 1
        time.sleep(1)


################


async def _checker_(bot: Bot, event: Event, state: T_State) -> bool:
    msg = str(event.get_message())
    return True if 'CQ:at' in msg else False


atname = on_command("戳", priority=5, block=False)


@atname.handle()
async def user_id_from_at(event: MessageEvent or Event, matcher: Matcher, arg: Message = CommandArg()):
    msg = str(event.get_message())
    IntArg = 0
    user_id = 0
    if 'CQ:at' in msg:
        user_id = get_at_user_id(event.json())[0]
        at = MessageSegment.at(user_id=user_id)
        # poke = f'[CQ:poke,qq={user_id}]'

        await matcher.send(at + MessageSegment.face(28) + MessageSegment.face(109) +
                           MessageSegment.face(183) + "rua死你！！！")
        arg = arg.extract_plain_text()
    if not arg == "":
        try:
            IntArg = int(str(arg))
        except ValueError:
            await matcher.finish(";w; 只能是数字哦~")

        if IntArg == 0:
            await matcher.finish("让我戳0下是罢！！")
        elif IntArg > 20:
            Random_key = random.randint(1, 10)
            await matcher.send(f"戳这么多下爪爪会断掉的叭，那还是戳{Random_key}下叭~ UwU")
            count = Random_key
        else:
            count = IntArg
    else:
        count = 5
    # poke = MessageSegment.poke(type_="poke", id_=str(user_id))
    poke = f'[CQ:poke,qq={user_id}]'
    temp_count = 0
    while not temp_count == count:
        await matcher.send(poke)
        temp_count = temp_count + 1
        time.sleep(1)
