from .. import loader

@loader.tds
class foxMod(loader.Module):
    strings = {"name": "fox"}

    async def watcher(message):
        if "Продолжить 🛠 Работать" in message.raw_text:
            await message.client.send_message("/work")
