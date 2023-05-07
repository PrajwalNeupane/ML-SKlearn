import os
import openai
import discord
from discord.ext import commands

# Set up Discord bot
TOKEN = 'MTEwMTU1OTg1MDMxMzQ3MDAyMg.GaWrQb.w0KSW45JsIVaap8SFkte1fZB8OIOibGZ6uWnFc'

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Set up OpenAI API
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

async def generate_gpt4_response(prompt):
    response = openai.Completion.create(
        engine="gpt-4-32k-0314",  # Replace with the appropriate GPT-4 engine name
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
    )

    return response.choices[0].text.strip()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='ask', help='Ask a question to GPT-4.')
async def ask(ctx, *, question):
    prompt = f"{question}\nAnswer:"
    gpt4_response = await generate_gpt4_response(prompt)
    await ctx.send(gpt4_response)

bot.run(TOKEN)
