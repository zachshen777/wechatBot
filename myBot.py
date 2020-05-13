from wxpy import *

bot = Bot(console_qr=True, cache_path=True)

bot.enable_puid()

tuling = Tuling('---key---')

groups = []

friends = []

groups.append(ensure_one(bot.groups().search('szzzk')))
print(groups)

friends.append(ensure_one(bot.friends().search('小马')))
friends.append(ensure_one(bot.friends().search('ddd')))
print(friends)

@bot.register(groups, TEXT)
def tuling_auto_reply(msg):
    print(msg)
    if isinstance(msg.chat, Group) and not msg.is_at :
        #log.info ("<TL> group no at")
        return
    else:
        #log.info ("<TL> tuling auto reply")
        tuling.do_reply(msg)

@bot.register(friends, TEXT)
def tuling_auto_reply1(msg):
        tuling.do_reply(msg)
embed()
