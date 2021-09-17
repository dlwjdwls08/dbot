import discord, json
from discord.ext import commands
from module import useful


token = json.load(open("token.json"))[0] + json.load(open("token.json"))[1]
bot = commands.Bot('/',None,)
self_ = object()

@bot.event
async def on_ready():
    print(f"{bot.user.name} logged in as {bot.user.id}")
    print("\n--------------------------------\n")



async def callfunc(cls:object,funcname,*args):
    for f in cls.__dict__:
        if f.startswith("_"): continue
        if f == funcname:
            await cls.__dict__[f](self_,*useful.args_to_hints(cls.__dict__[f],*args))
            return
    print(f"command {funcname} is not defind")

class Commands:
    class setting:
        def init(self):
            @commands.command("setting")
            async def setting(ctx,command,*args):
                await callfunc(Commands.setting,command,ctx,*args)
            return setting

    class test:
        async def say(self,ctx:commands.Context,*args):
            await ctx.send(useful.list_to_original(args))
        def init(self):
            @commands.command("test")
            async def test(ctx,command,*args):
                await callfunc(Commands.test,command,ctx,*args)
            return test




for c in Commands.__dict__:
    if c.startswith("_"): continue
    c_ = Commands.__dict__[c]()
    bot.add_command(c_.init())

bot.run(token)