import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Lista di frasi tipiche
frasi_tipiche = [
    "F:Dove vai a pranzo?\nJ: Nel regno quantico!",
    "F: Hai provato la melatonina?\nJ: Il siero della verità………….",
    "J: Ti spremo un limone nell’occhio…………………….",
    "M: Ma son tutti fuori di testa in Polaris...\nJ: Bipolaris!",
    "F: Ma non dormi la notte?\nJ: No vedo cose strane,i multiversi.",
    "F: Ce l’hai piccolo, si sa…\nJ: Di più, sono asessuato, anzi assessore.",
    "L. Ho la batteria al 3%\nJ. Se vuoi c’è il wifi",
    "Marco: Adesso ci sei per un caffè ?\nJ: Datemi due secondi !\nMichael: uno… due…\nJ: VULCANIANI però !!!",
    "Michele: Hai le mutande da capodanno?\nJ: Le mutande da caponata!",
    "F: Se hai bisogno mandami un’email, un piccione viaggiatore…..\nJ: Ti mando un no-vax,",
    "F: Non c’è bisogno che cambi la stampante, hai la share di windows.\nJ: L’ascella di windows?",
    "Marco: carichiamo tutto sul cloud\nJ: Carichiamo la vecchia?",
    "F: io lo dico perché sai..vengo dal mondo…\nJ: dal mondo della moda??",
    "F: Ma si dai, rispondi di pancia.\nJ: Posso mettere la danza del ventre?",
    "Nicolò: il mio condizionatore è molto vecchio quando lo accendo………\nJohanatan: Tossisce?",
    "Nicolò: Massimo Lo Rizzo stava parlando con una concessionaria per il leasing.\nJohnatan: Michael Schumacher?",
    "Marco: L’AI dell’iphone ti permette di cancellare qualcuno dalla foto\nJohanatan: E aggiungere Scalfaro."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Ciao! Scrivi /parla per sentire le battute epiche!")

async def parla(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    frase = random.choice(frasi_tipiche)
    await update.message.reply_text(frase)

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.getenv('TOKEN')).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("parla", parla))

    app.run_polling()
