from nonebot import get_driver
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_command

from nonebot.adapters import Message
from nonebot.params import CommandArg

import g4f 
__plugin_meta__ = PluginMetadata(
    name="g4f",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)


g4f_rpl = on_command("g4f")

@g4f_rpl.handle()
async def handle_function(args: Message = CommandArg()):
    if prompt := args.extract_plain_text():
        r = g4f.ChatCompletion.create(model=g4f.models.gpt_4,provider=g4f.Provider.OnlineGpt,messages=[{"role": "user", "content": "你是温迪。"+prompt}],)  # Alternative model setting

        #r = g4f.ChatCompletion.create(model=g4f.models.default,provider=g4f.Provider.ChatgptNext,messages=[{"role": "user", "content": "你是温迪。"+prompt}],)
        with open("/home/gtreesserver01/g4f.log","a") as f:
            f.write(str(r)+"\n")
        await g4f_rpl.finish(r)
    else:
        await g4f_rpl.finish("请输入对话内容")

