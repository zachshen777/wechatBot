# -*- coding:UTF-8 -*-
# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
# 如果二维码变形，传入console_qr=1（或其他倍数）来进行调整字幅宽度
# 如果需要反色显示，可以使用负数来进行反色操作
# 启用缓存，来保存自己的登录状态
bot = Bot(console_qr=True, cache_path=True)
# 启用puid属性
bot.enable_puid()
# 接入图灵机器人
tuling = Tuling("508ea322942e446f81b49fb8552fdb74")
# 使用图灵回复消息
# 自动回复所有文字消息
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)
    print(msg)
# 进入 Python 命令行、让程序保持运行
# 推荐使用
embed()
