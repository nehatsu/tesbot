import discord
from discord.ext import commands,tasks
import pickle
import dotenv
import random
from datetime import date
from dotenv import load_dotenv
import requests
import urllib.parse
import os
from discord import Intents, Client, Interaction
from discord import app_commands 
import json
from pytube import YouTube

load_dotenv()

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
intents = discord.Intents.default()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents,heartbeat_timeout=60,case_insensitive=True)
class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Game(name="/help"))
    print(f"{bot.user.name} がログインしました！")
    send_message.start()
    invite_link = discord.utils.oauth_url(
        bot.user.id,
        permissions=discord.Permissions(administrator=True),
        scopes=("bot", "applications.commands")
    )
    print(f"Invite link: {invite_link}")


CHANNEL_ID1 = #お好みのチャンネルid
CHANNEL_ID2 = #お好みのチャンネルid
VIDEO_URL = 'お好みの動画url'

@bot.event
async def on_member_join(member):
    channel1 = bot.get_channel(CHANNEL_ID1)
    channel2 = bot.get_channel(CHANNEL_ID2)
    guild_id =   # サーバーid
    guild = bot.get_guild(guild_id)
    member_count = sum(1 for member in guild.members if not member.bot)
    channel3 = bot.get_channel("お好みのチャンネルid")

    embed1 = discord.Embed(
        title="新しいメンバーが参加しました",
        description=f"{member.mention}さん、{channel3.mention}でサーバールールを確認して、楽しんでくださいね。",
        color=discord.Color.blue()
    )

    embed2 = discord.Embed(
        title="新しいメンバーが参加しました",
        description=f"{member.mention}さん、ようこそ！現在のサーバー人数は{member_count}人です！",
        color=discord.Color.blue()
    )

    await channel1.send(embed=embed1)
    await channel1.send(VIDEO_URL)
    await channel2.send(embed=embed2)
    
@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == 'こんにちは':
        responses = ['こんにちは', 'おはよう', 'こんばんは', 'お疲れ様です', '元気ですか？']  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)   

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == 'こんにちは':
        responses = ['こんにちは', 'おはよう', 'こんばんは', 'お疲れ様です', '元気ですか？']  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)


@bot.hybrid_command(name="youtube", description="youtubeの動画をダウンロードします")
async def youtube1(ctx: commands.Context, url: str):
    await ctx.interaction.response.defer()
    youtube = YouTube(url)

    video = youtube.streams.get_highest_resolution()
    filename = video.default_filename
    new_filename = filename.replace('.mp4', '') + '_new.mp4'
    video.download(filename=new_filename)

    await ctx.interaction.followup.send(file=discord.File(new_filename))
    os.remove(new_filename)

@bot.hybrid_command(name="server", description="現在いるサーバー人数を表示します。")
async def playercount(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return

    guild_id =  # サーバーid
    guild = bot.get_guild(guild_id)
    if guild is None:
        await ctx.send("指定されたサーバーが見つかりません。")
        return

    member_count = sum(1 for member in guild.members if not member.bot)

    embed = discord.Embed(title="プレイヤー数", description=f"サーバー {guild.name} の現在のプレイヤー数は {member_count} 人です。", color=0xffffff)
    await ctx.send(embed=embed)


last_draw = {}

@bot.command()
async def omikuji(ctx):
    user_id = ctx.author.id
    today = date.today()

    if user_id in last_draw and last_draw[user_id] == today:
        await ctx.send(f'{ctx.author.mention} すでに今日のおみくじを引いています。明日また来てください！')
    else:
        last_draw[user_id] = today
        fortune = ['大吉', '中吉', '吉', '小吉', '末吉', '凶', '大凶']
        result = random.choice(fortune)
        await ctx.send(f'{ctx.author.mention} おみくじの結果は... {result} です！')

@bot.hybrid_command(name="keisan",description="四則演算できます")
async def keisan(ctx, operation: str, a: int, b: int):
    if operation == '+':
        await ctx.send(a + b)
    elif operation == '-':
        await ctx.send(a - b)
    elif operation == '*':
        await ctx.send(a * b)
    elif operation == '/':
        if b != 0:
            await ctx.send(a / b)
        else:
            await ctx.send("エラー： ゼロによる除算は許可されていません。")
    else:
        await ctx.send("エラー： 無効な操作です。「+(加算)」、「-(減算)」、「*(乗算)」、「/(除算)」から選択してください。")

@bot.hybrid_command(name="gazou",description="任意の画像を埋め込みます")
@app_commands.describe(picture="ここに画像をアップロード")#使われている引数の名前="詳細"
async def test_command(ctx: discord.Interaction,picture:discord.Attachment):
    embed=discord.Embed(title="画像",color=0xffffff)
    embed.set_image(url=picture.url)
    await ctx.send(embed=embed)

@bot.listen('on_message')
async def on_message(message):
    if message.channel.id != :  # チャンネルIDを指定
        return
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == '好きな食べ物':
        responses = ['は、春です', 'なんだと思いますか？', '桜の花が咲く時期が好きですよ',]  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)

@bot.listen('on_message')
async def on_message(message):
    if message.channel.id != :  # チャンネルIDを指定
        return
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == '好きな季節':
        responses = ['は、春です', 'なんだと思いますか？', '桜の花が咲く時期が好きですよ',]  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel()#チャンネルidを指定
    await channel.send(f"{member.mention}がサーバーから脱退しました。\n[withdrawal_image](お好みの画像url)", )

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if bot.user in message.mentions:  # The bot was mentioned
        await message.channel.send('どうしましたか？')        

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  
        return

    if message.content == 'test':
        await message.channel.send('てすと')

@bot.hybrid_command(name="test", description="test")
async def testcommand(ctx):
    await ctx.send("test is done")


@bot.hybrid_command(name="nisnnsuu",description="2進数を10進数に変換します")
async def convert(ctx, binary: str):
    try:
        decimal = int(binary, 2)
        await ctx.send(f'二進数 `{binary}` の10進数表現は `{decimal}` です。')
    except ValueError:
        await ctx.send('無効な二進数が入力されました。2進数を確認して再度試してください。')

@bot.hybrid_command(name="10sinnsuu",description="10進数を2進数に変換します")
async def convert(ctx, number: int):
    await ctx.send(bin(number)[2:])


@bot.hybrid_command(name="8sinnsuu",description="10進数を8進数に変換します")
async def convert_to_oct(ctx, number: int):
    try:
        result = oct(number)
        await ctx.send(f"10進数の {number} は8進数で {result} です。")
    except ValueError:
        await ctx.send("無効な数値が入力されました。")


@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == 'ぼっち':
        responses = ['https://tenor.com/view/bocchi-bocchi-the-rock-anime-cringe-freak-out-gif-27026752', 'https://tenor.com/view/bocchitherock-bocchi-hitori-gotou-%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%96%E3%82%8D%E3%81%A3%E3%81%8F-anime-gif-26998598', 'https://tenor.com/view/bocchi-the-rock-ikuyo-kita-bocchi-hitori-gotou-%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%96%E3%82%8D%E3%81%A3%E3%81%8F-gif-26974910', 'https://tenor.com/view/bocchi-the-rock-oomfie-bocchi-the-rock-bocchi-shake-head-hitoribocchi-gif-27010676', 'https://tenor.com/view/bocchi-bocchi-the-rock-anime-hitori-gotou-you-wot-gif-27026760']  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:  
        return

    if message.content == 'きたーん':
        await message.channel.send('https://tenor.com/view/%E3%81%BC%E3%81%A3%E3%81%A1%E3%81%96%E3%82%8D%E3%81%A3%E3%81%8F-%E5%96%9C%E5%A4%9A%E9%83%81%E4%BB%A3-bocchi-the-rock-bothero-bozaro-gif-27262605')



@tasks.loop(hours=1)  # この関数を1時間ごとに実行する
async def send_message():
    channel = bot.get_channel()  # チャンネルID
    with open('daihon.txt', 'r', encoding='utf-8') as f:  # UTF-8でエンコードされたテキストファイルを開く
        lines = f.readlines()  # ファイルのすべての行を読み込む
    message = random.choice(lines)  # ランダムな行を選択する
    await channel.send(message)  # メッセージを送信する

async def on_button_click(ctx:discord.Interaction):
    custom_id = ctx.data["custom_id"]#inter.dataからcustom_idを取り出す
    if custom_id == "check":
        embed = discord.Embed(
            title = "あなたのユーザー名",
            description = ctx.user.name + "#" + ctx.user.discriminator,
            color = 0x0000ff
        )
        await ctx.send(embed=embed,ephemeral=True)#Embedを「これらはあなただけに表示されています」の状態で送信。

siritori_words = []
channel_id = 
turn = 0

@bot.hybrid_command(name="しりとり",description="名前の通りしりとりを開始します")
async def siritori(ctx):
    global siritori_words
    global turn
    if ctx.channel.id != channel_id:
        return
    siritori_words = ['しりとり']
    turn = 0
    await ctx.send('ゲームスタート！ 最初の単語は "しりとり" です。')

@bot.event
async def on_message(message):
    global siritori_words
    global turn
    if message.author == bot.user or message.channel.id != channel_id:
        return

    await bot.process_commands(message)

    if len(siritori_words) == 0:
        return

    word = message.content

    if word in siritori_words:
        embed = discord.Embed(title="すでに使われた単語です！", description=f"{message.author.mention}さん、'{word}'はすでに使われました。5秒後にメッセージが削除されます。", color=0xff0000)
        await message.channel.send(embed=embed)
        await message.delete(delay=5)
    elif word[-1] == 'ん':
        embed = discord.Embed(title="ゲームオーバー！", description=f"{message.author.mention}さん、'{word}'は 'ん'で終わっています。あなたの負けです。", color=0xff0000)
        await message.channel.send(embed=embed)
        siritori_words = []
    else:
        siritori_words.append(word)
        turn += 1
        if turn % 10 == 0:
            bot_word = 'りんご'  # Botの単語を適切に選択または生成します。
            siritori_words.append(bot_word)
            await message.channel.send(f'Botのターン：{bot_word}')

    
@bot.listen('on_message')
async def on_message(message):
    if message.channel.id != :  # チャンネルIDを指定
        return
    if message.author == bot.user:  # Ignore bot's own messages
        return

    if message.content == 'www':
        responses = ['おもしろいですね！', '笑', 'www',]  # Replace with your responses
        response = random.choice(responses)
        await message.channel.send(response)

@bot.hybrid_command(name="sakujyo", description="特定のユーザーのメッセージを削除する")
@commands.has_permissions(administrator=True)
async def delete(ctx, member: discord.Member, num_messages: int):
    if num_messages < 1:
        await ctx.send("削除するメッセージ数は1以上でなければなりません。")
        return

    def check(message):
        return message.author == member

    deleted = await ctx.channel.purge(limit=num_messages, check=check)
    await ctx.send(f'大体{len(deleted)}くらいのメッセージを削除しました')

token = os.getenv('DISCORD_TOKEN')

bot.run(token)
