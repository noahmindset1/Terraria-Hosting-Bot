import discord
from discord.ext import commands
import subprocess

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def host_terraria_server(ctx, server_name: str, port: int = 7777):
    # Start the Terraria server
    try:
        subprocess.run(['./windows/TerrariaServer.exe', '-world', server_name, '-port', str(port)], check=True)
        embed = discord.Embed(
            title="Terraria Server Information",
            description="The Terraria server has been started.",
            color=discord.Color.green()
        )
        embed.add_field(name="Server Name", value=server_name, inline=False)
        embed.add_field(name="Port", value=port, inline=False)
        embed.set_footer(text="You can join the server using the IP address provided.")
        await ctx.send(embed=embed)
    except FileNotFoundError:
        await ctx.send("Failed to start the Terraria server. Make sure the TerrariaServer.exe file exists and is accessible.")
    except subprocess.CalledProcessError:
        await ctx.send("Failed to start the Terraria server.")

bot.run('')
