import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログイン完了: {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"スラッシュコマンドを同期: {len(synced)}個")
    except Exception as e:
        print(e)

@bot.tree.command(name="adb", description="あって返すよ")
async def adb_command(interaction: discord.Interaction):
    await interaction.response.send_message("あ")

bot.run(os.getenv("KIDOU_MOJI"))
