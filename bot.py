import os
import discord
from discord.ext import commands

# Get the bot token from environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Create a new bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Dictionary to store FAQ entries
faq = {
    'help': 'Use !faq <topic> to get information about a topic.',
    'github': 'Our GitHub repository can be found at: https://github.com/yourusername/discord_faq_bot',
    'deploy': 'We use GitHub Actions to automatically deploy our bot to a DigitalOcean Droplet.',
}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='faq')
async def get_faq(ctx, topic: str):
    """Retrieve FAQ information for a given topic."""
    if topic.lower() in faq:
        await ctx.send(faq[topic.lower()])
    else:
        await ctx.send(f"Sorry, I don't have information about '{topic}'. Try !faq help for available topics.")

# Run the bot
bot.run(TOKEN)
