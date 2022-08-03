from .. import loader

@loader.tds
class foxMod(loader.Module):
    strings = {"name": "fox"}

    async def watcher(message):
        if message.raw_text == "Продолжить 🛠 Работать - ":
            await message.client.send_message("/work")
