import time
from nonebot import get_driver
from .config import Config
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.rule import Rule
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.params import CommandArg, ArgPlainText, Arg
from nonebot.adapters.onebot.v11 import MessageEvent, Event, Bot, GroupMessageEvent
from nonebot.params import State

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



matcher = on_command("戳我", priority=5, block=False)


@matcher.handle()
async def poke(event: Event, matcher: Matcher):
    user_id = event.get_user_id()

    at = MessageSegment.at(user_id=user_id)
    # poke = MessageSegment.poke(type_="poke", id_=str(user_id))
    poke = f'[CQ:poke,qq={user_id}]'
    await atname.send(at + MessageSegment.face(28) + MessageSegment.face(109) +
                       MessageSegment.face(183) + "rua死你！！！")
    count = 0
    while count <= 8:
        await matcher.send(poke)
        count = count + 2
        time.sleep(1)

    await matcher.finish(poke)


################


async def _checker_(bot: Bot, event: Event, state: T_State) -> bool:
    msg = str(event.get_message())
    return True if 'CQ:at' in msg else False

# rule=Rule(_checker_)


atname = on_command("戳", priority=5, rule=Rule(_checker_), block=False)


@atname.handle()
async def user_id_from_at(event: MessageEvent or Event, matcher: Matcher, state: T_State = State()):  # , args: Message = CommandArg()):
    msg = str(event.get_message())
    # msg = msg.lstrip(str({"".join(list(get_driver().config.command_start))}))
    # msg = msg.replace("/", "")
    # print(type({"".join(list(get_driver().config.command_start))}))
    # msg = msg.lstrip("戳")
    msg = msg.replace("[CQ:at,qq=", "").replace("]", "")
    msg = msg[2:]
    """plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("msg", args)

    if plain_text not in [""]:

        Cache = plain_text
        user_id = Cache"""
    user_id = int(msg)


    # raw_msg = _event_.original_message
    # print(raw_msg)

    # qq=str(raw_msg.data.get("qq", ""))


    count = 0
    at = MessageSegment.at(user_id=user_id)
    # poke = MessageSegment.poke(type_="poke", id_=str(user_id))
    poke = f'[CQ:poke,qq={user_id}]'

    
    await atname.send(at + MessageSegment.face(28) + MessageSegment.face(109) +
                       MessageSegment.face(183) + "rua死你！！！")
    _list_ = ["2821323220"]

    if user_id in _list_:
        while count <= 12:
            await atname.send(poke)
            count = count + 2
        await atname.finish(poke)
    if user_id not in _list_:
        count = 0
        while count <= 8:
            await atname.send(poke)
            count = count + 2
            time.sleep(1)
        await atname.finish(poke)
