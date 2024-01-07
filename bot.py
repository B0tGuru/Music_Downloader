#!./my_env/bin python3
from telegram.ext import ApplicationBuilder,filters,MessageHandler, CommandHandler
import autodl,usearch,asyncio,sys
#from telegram import MessageHandler, CommandHandler

token_str = ""

#async def update_msg(dlin,dltotal):

app = None
py_args = sys.argv
async def chatMan(update,context):
    url = 'https://www.youtube.com/watch?v=B6H_x6pj7Ow'
    dl_text = update.message.text
    print(f"\n\ndownloading: {dl_text}")
   # c_id = update.message.chat.id
    dl_inst = usearch.search_youtube(dl_text)
    xdl_title = dl_inst["title"]
    dl_link = dl_inst["link"]
    dl_title = f"{xdl_title}.m4a"
    chatid = update.message.chat_id
    print(f"\n\nchat id is: {chatid}")
    up_msg  = await update.message.reply_text(f"downloading {dl_title} please wait .....")
    #context.bot.send_message(chat_id=chat_id, text=f"downloading {dl_title} please wait")
    
    #update.message.reply_text()
    print(f"\n\ndownloading: {up_msg}")
   # input()
    print(f"started download of {dl_title} from {dl_link}")
    
    dl_bytes = autodl.instantMp3(dl_inst)
    #download_mp3(dl_link)
    #Tele(context,dl_link,up_msg)
    await context.bot.edit_message_text(chat_id=chatid,message_id = up_msg.message_id,text="download completed")
    print("downloaded finished")
    await update.message.reply_audio(filename = dl_title,audio=dl_bytes)
    print("message in")

async def startMan(update,context):
    await update.message.reply_text("hello world, what would you like to download")
    print("got start")

async def chatCmd(update,context):
    asyncio.create_task(chatMan(update,context))
    print("created new tak")

async def init_bot():
    print("loop")
    #loop = asyncio.new_event_loop()
    #asyncio.set_event_loop(loop)
    print("loop and started")
    global app
    app = ApplicationBuilder().token(token = token_str).build()
    msgctrl = MessageHandler(filters.TEXT,chatCmd)
    cmdctrl = CommandHandler("start",startMan)

    app.add_handler(cmdctrl)
    app.add_handler(msgctrl)
    #app.run_webhook(listen="127.0.0.1",port=8000,cert="server.csr",key="server.key")
    app.run_polling(timeout = 0.0)

def start_bot():
    print("loop started")
    #loop = asyncio.get_event_loop()
    #asyncio.set_event_loop(loop)
    #loop.run_forever()
    print("loop and started")
    ##await init_bot()
    #await init_bot()
    #asyncio.create_task(init_bot())
#
#init_bot()
#start_bot()
if (len(py_args)>1):
    token_str = py_args[1]
    print(f"using token: {token_str}")
    app = ApplicationBuilder().token(token = token_str).build()
    msgctrl = MessageHandler(filters.TEXT,chatCmd)
    cmdctrl = CommandHandler("start",startMan)

    app.add_handler(cmdctrl)
    app.add_handler(msgctrl)

    app.run_polling(timeout = 0.0)
else:
    print("hello, please write your bot token in the command line using this format python bot.py [your_bot_token]")