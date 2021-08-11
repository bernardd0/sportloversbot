import logging
import ssl
import olympic

ssl._create_default_https_context = ssl._create_unverified_context

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Olá {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Comando:\n/esportes\n/modalidades\n/horariosesportes')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def reverse_echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text[::-1])

def esporte(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(listar_esportes())

def agenda_esporte(update: Update, context: CallbackContext) -> None:
    esportes_idx = int(context.args[0])
    horarios_por_esportes(esportes_idx)
    update.message.reply_photo(photo=open(temp_path, "rb"))

def modalidade(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(listar_modalidades())

def agenda_modalidade(update: Update, context: CallbackContext) -> None:
    mods_idx = int(context.args[0])
    horarios_por_modalidade(mods_idx)
    update.message.reply_photo(photo=open(temp_path, "rb"))

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    # 
    # arquivo = open("token.txt")
    # token = arquivo.read()
    # arquivo.close()
    # updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("horariosesporte", agenda_esporte))
    dispatcher.add_handler(CommandHandler("horariosmodalidade", agenda_modalidade))
    dispatcher.add_handler(CommandHandler("esportes", esportes))
    dispatcher.add_handler(CommandHandler("modalidade", modalidades))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reverse_echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
