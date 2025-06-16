# ==================================
# Part 1: Imports, Consts, Inits
# ==================================

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
import asyncio
from random import randint

ai = __import__('saves').api_id
ah = __import__('saves').api_hash
fb_list = ['СЛАВА БОЙКИССЕРАМ🙏🏻🩷🤍', 'АНГЕЛА ХРАНИТЕЛЯ КАЖДОМУ ИЗ ВАС 🙏🏻🩷🤍', ' БОЖЕ ХРАНИ БОЙКИССЕРОВ 🙏🏻🩷🤍', ' СПАСИБО ВАМ НАШИ ФЕМБОЙЧИКИ 🙏🏻🩷🤍', ' СПАСИБО 🏳️‍⚧️']
bw = {
    "а": "4", "б": "6", "в": "8", "г": "7", "д": "D", "е": "3", "ё": "3", "ж": "}{",
    "з": "3", "и": "i", "й": "j", "к": "K", "л": "JI", "м": "\/\/", "н": "H", "о": "0",
    "п": "ГI", "р": "P", "с": "C", "т": "7", "у": "Y", "ф": "qp", "х": "X", "ц": "LL",
    "ч": "4", "ш": "III", "щ": "III", "ъ": "b", "ы": "ЬI", "ь": "6", "э": "€", "ю": "I0", "я": "R",
    "a": "4", "b": "8", "c": "<", "d": "|)", "e": "3", "f": "ƒ", "g": "9", "h": "#",
    "i": "!", "j": "_|", "k": "|<", "l": "1", "m": "/\\/\\", "n": "|\\|", "o": "0",
    "p": "|°", "q": "(_,)", "r": "2", "s": "5", "t": "7", "u": "(_)", "v": "\\/", 
    "w": "\\^/", "x": "><", "y": "`/", "z": "2"
}
z_list = ['Слава Богу Z🙏❤️СЛАВА', ' Z🙏❤️АНГЕЛА ХРАНИТЕЛЯ Z КАЖДОМУ ИЗ ВАС🙏❤️', 'БОЖЕ ХРАНИ Z🙏❤️', 'СПАСИБО ВАМ НАШИ СВО🙏🏼❤️', 'СПАСИБО НАШИМ БОЙЦАМ']
prefix = '!'
pmod = 'n'
mods = ["fb", "z", "bw", "n"]
app = Client('NyanBot', 
            api_id=ai, api_hash=ah, 
            device_model='NyanPhone', 
            system_version='wlfrm', 
            system_lang_code='ru-RU', 
            app_version='1.0.0')

# ==================================
# Part 2: Functions
# ==================================

def bwtext(text):
    return ''.join(bw.get(c.lower(), c) for c in text)

@app.on_message(filters.outgoing & filters.text)
async def cmd_handler(client: Client, message: Message):
    global pmod, prefix
    if message.text[0] == prefix:
        cmd = message.text.split()[0]
        if cmd == f'{prefix}мод':
            mod = message.text.split()[1]
            if mod in mods: 
                pmod = mod
                await message.edit_text('Успешно!')
            else: await message.edit_text('режим не найден!')
        elif cmd == f'{prefix}преф':
            prefix = message.text.split()[1]
            await message.edit_text('Успешно!')
    elif pmod != 'n': 
        if pmod == 'z':
            try:
                a = f"{message.text.replace('з', 'Z').replace('в', 'V').replace('З', 'Z').replace('В', 'V').replace('❤', '🇷🇺')}".split()
                if randint(0, 4) == 2:
                    a.insert(randint(0, len(a)-1), z_list[randint(0,4)])
                elif randint(0, 4) == 2:
                    a.insert(randint(0, len(a)-1), z_list[randint(0,4)])
                    a.insert(randint(0, len(a)-1), z_list[randint(0,4)])
                await message.edit_text(" ".join(a))
            except MessageNotModified: pass
        elif pmod == 'fb':
            try:
                a = f"{message.text.replace('❤', '🏳️‍⚧️')}".split()
                if randint(0, 4) == 2:
                    a.insert(randint(0, len(a)-1), fb_list[randint(0,4)])
                elif randint(0, 4) == 2:
                    a.insert(randint(0, len(a)-1), fb_list[randint(0,4)])
                    a.insert(randint(0, len(a)-1), fb_list[randint(0,4)])
                await message.edit_text(" ".join(a))
            except MessageNotModified: pass
        elif pmod == 'bw':
            try:
                await message.edit_text(bwtext(str(message.text)))
            except MessageNotModified: pass

# ==================================
# Part 3: Run
# ==================================
if __name__ == "__main__":
    print(f"running {__name__}")
    app.run()
