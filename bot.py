import os
import telebot
import subprocess

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


def return_active_users_string() -> str:
    # output = subprocess.check_output("w").decode("utf-8")
    # lines_list = subprocess.check_output("w").decode("utf-8").splitlines()[2:]
    active_users = []
    for line in subprocess.check_output("w").decode("utf-8").splitlines()[2:]:
        active_users.append(line.split()[0])
    active_users_fmt = "\n".join(active_users)
    return active_users_fmt


@bot.message_handler(commands=["users"])
def give_users(message):
    users = return_active_users_string()
    bot.send_message(message.chat.id, users)


bot.infinity_polling()
