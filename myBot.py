# -*- coding: UTF-8 -*-
from wxpy import *
# 扫码登录
bot = Bot(console_qr=True, cache_path=True)
# 启用puid属性(可作为用户唯一标识)
bot.enable_puid()
# 接入图灵机器人
tuling = Tuling("key")
# 自定义多群组
groups = []
def my_groups()
    groups.append(ensure_one(bot.groups().search('test'.decode("utf-8"))))
print(groups)
# 自定义多好友
friends = []
def my_friends()
    friends.append(ensure_one(bot.friends().search('小马'.decode("utf-8"))))
print(friends)

# 自定义群组内自动回复
@bot.register(groups, TEXT)
def tuling_auto_reply(msg):
        #log.info(msg)
        # 如果是群聊但未被@则不做回复
        print(msg)
        if isinstance(msg.chat, Group) and not msg.is_at :
                #log.info ("<TL> group no at")
                return
        else:
                #log.info ("<TL> tuling auto reply")
                tuling.do_reply(msg)
# 自定义好友自动回复
@bot.register(friends, TEXT)
def tuling_auto_reply1(msg):
        tuling.do_reply(msg)
# 堵塞
embed()
