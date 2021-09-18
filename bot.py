from typing import Literal
import discord, json, datetime
from discord.ext import commands
from module import useful

intents = discord.Intents.default()
intents.members = True
token = json.load(open("token.json"))[0] + json.load(open("token.json"))[1]
now = datetime.datetime.now()
bot = commands.Bot('/',None,intents=intents)
self_ = object()
passive:list[str] = json.load(open("passiveregister.json"))
registrator:list[int] = json.load(open("registrator.json"))

@bot.event
async def on_ready():
    print(f"{bot.user.name} logged in as {bot.user.id}")
    print("\n--------------------------------\n")

@bot.event
async def on_member_remove(member:discord.Member):
    if member.id in registrator:
        registrator.remove(member.id)
        save.registrator()

@bot.event
async def on_message(message:discord.Message):
    await bot.process_commands(message)
    if message.channel.id == 888308882852692008:
        await message.delete()


async def callfunc(cls:object,funcname,*args):
    for f in cls.__dict__:
        if f.startswith("_"): continue
        if f == funcname:
            await cls.__dict__[f](self_,*useful.args_to_hints(cls.__dict__[f],*args))
            return
    print(f"명령어 {funcname}는 존재하지 않습니다.")

async def isadminp(ctx:commands.Context):
    if not ctx.author.permissions_in(ctx.channel).administrator:
        await ctx.reply("관리자 권한이 없습니다.")
        return False
    return True


class save:
    def passive(): json.dump(passive,open("passiveregister.json",'w'))
    def registrator(): json.dump(registrator,open("registrator.json",'w'))

class Commands:
    class register:
        def init(self):
            @commands.command("register")
            async def register(ctx:commands.Context,nickname:str = None,skil_level:str = None):
                if ctx.author.id in registrator: return
                if not nickname in passive:
                    if int(ctx.guild.id) != 888308649628418069 or int(ctx.channel.id) != 888308882852692008: return
                    if not skil_level in ('강주력','주력','1군','2군','3군','4군','일반유저'): return
                    if len(nickname) > 12: return
                await ctx.author.send(f"{nickname}({skil_level})으로 등록되었습니다.")
                for role in ctx.guild.roles:
                    if role.id == 888309537071824897:
                        a:discord.Member = ctx.author
                        await a.add_roles(role)
                        break
                await ctx.author.edit(nick=f"{nickname}({skil_level})")
                registrator.append(ctx.author.id)
                save.registrator()
                await ctx.message.delete()
                if nickname in passive:
                    passive.remove(nickname)
                    save.passive()
                # await callfunc(Commands.register,command,ctx,*args)
            return register

    class msg:
        def init(self):
            @commands.command("msg")
            async def msg(ctx:commands.Context,command,*args):
                await callfunc(Commands.msg,command,ctx,*args)
            return msg

        async def delete(self,ctx:commands.Context,limit=999):
            if not await isadminp(ctx): return
            c:discord.TextChannel = ctx.channel
            await c.purge(limit=limit)
    
    class member:
        def init(self):
            @commands.command('member')
            async def member(ctx:commands.Context,command,*args):
                await callfunc(Commands.member,command,ctx,*args)
            return member

        async def kick(self,ctx:commands.Context,*mentions):
            if not await isadminp(ctx): return
            success = []
            fail = []
            for m in ctx.message.mentions:
                m:discord.Member
                try:
                    await m.kick()
                    success.append(m)
                except: fail.append(m)
            embed = discord.Embed(title = "Kick",colour=discord.Colour.red())
            embed.add_field(name='Success',value=[s.mention for s in success])
            embed.add_field(name='Fail',value=[f.mention for f in fail])
            await ctx.send(embed=embed)

        async def ban(self,ctx:commands.Context,*mentions):
            if not await isadminp(ctx): return
            success = []
            fail = []
            for m in ctx.message.mentions:
                m:discord.Member
                try:
                    await m.ban()
                    success.append(m)
                except: fail.append(m)
            embed = discord.Embed(title = 'Ban',colour=discord.Colour.red())
            embed.add_field(name='Success',value=[s.mention for s in success])
            embed.add_field(name='Fail',value=[f.mention for f in fail])
            await ctx.send(embed=embed)

    class channel:
        def init(self):
            @commands.command('channel')
            async def channel(ctx,command,*args):
                await callfunc(Commands.channel,command,ctx,*args)
            return channel
        
        async def clear(self,ctx:commands.Context,category:str,channeltype:Literal['all','text','voice']='all'):
            if not await isadminp(ctx): return
            g:discord.Guild = ctx.guild
            ctg:discord.CategoryChannel = discord.utils.get(g.categories,name=category)
            if not ctg:
                await ctx.reply("해당 카테고리가 없습니다.")
                return
            count = 0
            if channeltype == 'all':
                for channel in ctg.channels:
                    await channel.delete()
                    count += 1
            elif channeltype == 'text':
                for channel in ctg.text_channels:
                    await channel.delete()
                    count += 1
            elif channeltype == 'voice':
                for channel in ctg.voice_channels:
                    await channel.delete()
                    count += 1
            else:
                await ctx.reply('channeltype 유형이 잘못되었습니다.')
            await ctx.send(f"{category}의 채널 {count}개가 삭제되었습니다.")

        async def summon(self,ctx:commands.Context,category:str,channeltype:Literal['text','voice'],from_:int,to:int,*name):
            if not await isadminp(ctx): return
            ctg:discord.CategoryChannel = discord.utils.get(ctx.guild.categories,name=category)
            if not ctg:
                await ctx.reply("해당 카테고리가 없습니다.")
                return
            if not channeltype in ('text','voice'):
                await ctx.reply('channeltype 유형이 잘못되었습니다.')
            n = useful.list_to_original(name).split('{')[0]
            m = useful.list_to_original(name).split('}')[1]
            count = 0
            for i in range(from_,to+1):
                if channeltype == 'text':
                    await ctg.create_text_channel(f"{n}{i}{m}")
                elif channeltype == 'voice':
                    await ctg.create_voice_channel(f"{n}{i}{m}")
                count += 1
            await ctx.send(f"채널 {count}개를 생성하였습니다.")

    class test:
        def init(self):
            @commands.command("test")
            async def test(ctx,command,*args):
                await callfunc(Commands.test,command,ctx,*args)
            return test
        async def say(self,ctx:commands.Context,*args):
            await ctx.send(useful.list_to_original(args))
        async def dm(self,ctx:commands.Context,*args):
                await ctx.author.send("a")
        async def role(self,ctx:commands.Context,*args):
            for role in ctx.guild.roles:
                    if role.id == 888309537071824897:
                        a:discord.Member = ctx.author
                        await a.add_roles(role)
                        break

    


for c in Commands.__dict__:
    if c.startswith("_"): continue
    c_ = Commands.__dict__[c]()
    bot.add_command(c_.init())

bot.run(token)