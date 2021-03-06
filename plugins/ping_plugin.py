from datetime import datetime
from telethon import events, sync
from probability_function import probability

# /ping
async def ping_pong(event):
    sender = await event.get_sender()
    if event.is_private:
        a = datetime.timestamp(datetime.now())
        message = await event.reply("**Pong!**")
        b = datetime.timestamp(datetime.now()) - a
        print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string} [{b:.3f}]")
        await message.edit(f"**Pong!**\nTook `{b:.3f}` seconds")

ping_pong.event = events.NewMessage(pattern=r"(/ping)$")
