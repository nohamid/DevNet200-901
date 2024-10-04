from webex_bot.webex_bot import WebexBot
from webex_bot.models.command import Command

api_token = "N2Q1MDdmYmEtNGI0Yy00YzM0LWFjODgtOTVlNDRmNjgzOTY4NTA1ZjRhNDktYjFm_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
bot = WebexBot(api_token, approved_domains=["cisco.com"])

def handle_hello(bot, message):
    return "Hello! How can I help you today?"

def handle_weather(bot, message):
    # Implement weather checking logic here
    return "The weather is sunny today!"

def handle_help(bot, message):
    return "Available commands: hello, weather, help"

bot.run()