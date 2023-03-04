#token = '6294908851:AAFtoAqyz34uU5PljtyVcNy47Otk-gLFR2E'

#openai.api_key = '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' 

import logging

from aiogram import Bot, Dispatcher, executor, types
import openai

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6294908851:AAFtoAqyz34uU5PljtyVcNy47Otk-gLFR2E')
dp = Dispatcher(bot)

openai.api_key = "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"

async def generate_response(text):
    prompt = f"User: {text}\nChatGPT: "
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

@dp.message_handler()
async def send_response(message: types.Message):
    response = await generate_response(message.text)
    await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
