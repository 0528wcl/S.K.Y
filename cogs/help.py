import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

class Help(commands.Cog):
    def __init__(self, client, RED, BLUE, GREEN):
        self.client = client
        self.RED = RED
        self.GREEN = GREEN
        self.BLUE = BLUE
    
    @app_commands.command(name = "help", description = "View the list of commands you can use")
    async def ping(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Bot Commands",
            description = "Here are the available commands",
            color = self.BLUE,
            timestamp = datetime.now()
        )
        embed.add_field(name = "!help", value = "Displays this message.", inline = False)
        embed.add_field(name = "!ping", value = "Check the bot's latency.", inline = False)
        embed.add_field(name = "!set_channel", value = "Set the current channel as the logging channel.", inline = False)
        embed.add_field(name = "!remove_channel", value = "Remove the current channel from the logging channels.", inline = False)
        embed.set_author(name = interaction.user.name, icon_url = interaction.user.display_avatar.url)
        embed.set_footer(text = self.client.user, icon_url = self.client.user.display_avatar.url)

        await interaction.response.send_message(embed = embed)

async def setup(client):
    from main import RED, BLUE, GREEN
    await client.add_cog(Help(client, RED, BLUE, GREEN))