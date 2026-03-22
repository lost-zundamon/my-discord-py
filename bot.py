import discord
from discord import app_commands # スラッシュコマンド用の道具
from discord.ext import commands
import random
import os

# Botの基本設定
intents = discord.Intents.default()
# スラッシュコマンドだけなら message_content は不要な場合もありますが、
# 念のため ON のままにしておきます。
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    # Botが起動した時に実行される特別な処理
    async def setup_hook(self):
        # これを書くことで、Discord側に「新しいコマンドができたよ！」と同期します
        await self.tree.sync()
        print("スラッシュコマンドを同期しました！")

bot = MyBot()

# 占い結果
FORTUNES = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user.name}')

# --- ここからがスラッシュコマンドの設定 ---
@bot.tree.command(name="uranai", description="今日の運勢を占います")
async def uranai(interaction: discord.Interaction):
    """/uranai と打つと実行される"""
    result = random.choice(FORTUNES)
    # スラッシュコマンドでは ctx ではなく interaction を使い、
    # send ではなく response.send_message を使います
    await interaction.response.send_message(f"{interaction.user.mention} さんの運勢は... **【{result}】** です！")

# トークンを貼り付け
token = os.getenv("DISCORD_TOKEN")  # 環境変数からトークンを取得
bot.run(token)