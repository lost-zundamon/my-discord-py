import discord
from discord import app_commands
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print("スラッシュコマンドを同期しました！")

bot = MyBot()

# --- 占いのデータ設定 ---
FORTUNES = ["超大吉", "大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]
COLORS = ["赤", "青", "黄色", "緑", "ピンク", "紫", "オレンジ", "白", "黒", "水色", "金色", "銀色"]
# ひらがな50音（濁音などは好みで追加してください）
HIRAGANA = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user.name}')

@bot.tree.command(name="uranai", description="運勢、ラッキーカラー、ラッキー文字を占います")
async def uranai(interaction: discord.Interaction):
    # ランダムに要素を抽出
    fortune = random.choice(FORTUNES)
    color = random.choice(COLORS)
    char = random.choice(HIRAGANA)
    
    # メッセージの組み立て
    response = (
        f"{interaction.user.mention} さんの今日の運勢はこちら！\n"
        f"------------------------------\n"
        f"🌟 **運勢**：【{fortune}】\n"
        f"🎨 **ラッキーカラー**：【{color}】\n"
        f"🔤 **今日のー文字**：【{char}】\n"
        f"------------------------------"
    )
    
    await interaction.response.send_message(response)

# Renderの環境変数からトークンを読み込む
token = os.getenv('DISCORD_TOKEN')
bot.run(token)