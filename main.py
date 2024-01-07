from fastapi import FastAPI
from fastapi.responses import FileResponse
#from telegram.utils.asyncio import run_coroutine_threadsafe
#import asyncio,threading
import subprocess
import asyncio,bot
from concurrent.futures import ThreadPoolExecutor


app = FastAPI()
athd = None
#3991
#loop = asyncio.get_event_loop()
print("event loop ok")
#asyncio.set_event_loop(loop)
#loop.run_forever()
@app.get("/")
async def root():
    #loop = asyncio.get_running_loop()
    await bot.app.run_polling()
    # Create a ThreadPoolExecutor with a specific number of threads
    #executor = ThreadPoolExecutor(max_workers=5)
    
    # Submit tasks to the executor
    #tasks = [loop.run_in_executor(executor, bot.init_bot)]
    #results = await asyncio.gather(*tasks)
    #video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    #chunks.download_video_in_chunks(video_url)
    #video_url = "https://www.youtube.com/watch?v=B6H_x6pj7Ow"
    #video_dt = sing.download_video(video_url)
    #ind_last = autodl.download_mp3(video_url)
    #print("ok http")
    #bot.start_bot()
    
    #loop.create_task(bot.init_bot())
    
    #asyncio.run_coroutine_threadsafe(bot.init_bot(),asyncio.create_event_loop())
    #bot.init_bot()
    #global athd
    #athd = threading.Thread(target=bot.init_bot)
    #athd.start()
    #process = subprocess.Popen(['python', 'bot.py'], shell=False)
    return f"Hello from Space! 🚀: man"
@app.get("/mefile")#, response_class=HTMLResponse)
async def get_index():
    # Load the index.html file
    with open("hi.mp3") as f:
        index_html = f.read()
    if index_html == None:
        return "file error"
    else:
        return index_html


#asyncio.set_event_loop(loop)

import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8080)