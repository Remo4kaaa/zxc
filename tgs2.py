from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id='27231578', api_hash='b7559f04b70afd4ee92d31538a56cb08')

chat_id = "@anonkarubot"

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "/stop - завершить диалог" in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(1.8)
        await app.send_message(chat_id, "Приветик, Д")
        sleep(2.2)
        await app.send_message(chat_id, "Если хочешь посмотреть как я вставляю в себя 25см, то.. смотри тут ")
        sleep(2)
        if '/stop - завершить диалог' in message.text:
             sleep(1.7)
             await app.send_sticker(chat_id, "CAACAgIAAxkBAAEHimRj2kEWCMHcI883ffJ3kFbpijS7NgAC5yQAAgTbuErwHbfUyBhwFi4E")
             sleep(2)

             if "/stop - завершить диалог"  in message.text:  # Меняем это значение если хотим спамить в другом чате
                 await app.send_message(chat_id, "/stop")
                 sleep(1.3)
                 await app.send_message(chat_id, "/search")





app.run()