Telegram bot for Evernote
=========================
[![Build status](https://travis-ci.org/djudman/evernote-telegram-bot.svg?branch=master)](https://travis-ci.org/djudman/evernote-telegram-bot?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/djudman/evernote-telegram-bot/badge.svg?branch=master)](https://coveralls.io/github/djudman/evernote-telegram-bot?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/1d23d48c1a7370b7b12f/maintainability)](https://codeclimate.com/github/djudman/evernote-telegram-bot/maintainability)


This bot can save everything that you send to Evernote account.


You can use this bot in Telegram: https://t.me/evernoterobot

Environment variables
=====================
| Variable name                | Default value | Description |
|------------------------------|---------------|-------------|
| MONGO_HOST                   | 127.0.0.1     | Hostname for mongodb host|
| TELEGRAM_API_TOKEN           | -             | Access token for telegram API. You can obtain this by BotFather |
| EVERNOTE_BASIC_ACCESS_KEY    | -             | appKey for your Evernote app (with readonly permissions) |
| EVERNOTE_BASIC_ACCESS_SECRET | -             | secret for your Evernote app (with readonly permissions) |
| EVERNOTE_FULL_ACCESS_KEY     | -             | appKey for your Evernote app (with read/write permissions) |
| EVERNOTE_FULL_ACCESS_SECRET  | -             | secret for your Evernote app (with read/write permissions) |
