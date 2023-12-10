# -*- coding: utf-8 -*-
# @Time    : 2023/11/18 上午12:18
# @File    : controller.py
# @Software: PyCharm

from asgiref.sync import sync_to_async
from loguru import logger
from telebot import types
from telebot import util, formatting
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_helper import ApiTelegramException
from telebot.asyncio_storage import StateMemoryStorage

from setting.telegrambot import BotSetting

StepCache = StateMemoryStorage()


@sync_to_async
def sync_to_async_func():
    pass


class BotRunner(object):
    def __init__(self):
        self.bot = AsyncTeleBot(BotSetting.token, state_storage=StepCache)

    async def run(self):
        logger.info("Bot Start")
        bot = self.bot
        if BotSetting.proxy_address:
            from telebot import asyncio_helper

            asyncio_helper.proxy = BotSetting.proxy_address
            logger.info("Proxy tunnels are being used!")

        @bot.message_handler(
            commands="help", chat_types=["private", "supergroup", "group"]
        )
        async def listen_help_command(message: types.Message):
            _message = await bot.reply_to(
                message=message,
                text=formatting.format_text(
                    formatting.mbold("🥕 Help"),
                    formatting.mlink(
                        "🍀 Github", "https://github.com/sudoskys/TelegramBotTemplate"
                    ),
                ),
                parse_mode="MarkdownV2",
            )

        try:
            await bot.polling(
                non_stop=True, allowed_updates=util.update_types, skip_pending=True
            )
        except ApiTelegramException as e:
            logger.opt(exception=e).exception("ApiTelegramException")
        except Exception as e:
            logger.exception(e)
