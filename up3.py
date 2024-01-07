import autodl,usearch,asyncio,sys
import requests
import yt_dlp

#https://gist.github.com/MartinEesmaa/2f4b261cb90a47e9c41ba115a011a4aa

url = 'https://www.youtube.com/watch?v=B6H_x6pj7Ow'
dl_text = "i need you by marc anthony"
print(f"\n\ndownloading: {dl_text}")
   # c_id = update.message.chat.id
dl_inst = usearch.search_youtube(dl_text)
dl_title = dl_inst["title"]
dl_link = dl_inst["link"]
dl_id = dl_inst['id']

print(f"downloading {dl_title} please wait .....")
    #context.bot.send_message(chat_id=chat_id, text=f"downloading {dl_title} please wait")
    
    #update.message.reply_text()
#print(f"\n\ndownloading: {up_msg}")
   # input()
print(f"started download of {dl_title} from {dl_link}")
yt_opts = {'format':'140'}
#{'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4+best[height<=480]'}
utube = yt_dlp.YoutubeDL(yt_opts)

info_dict = utube.extract_info(dl_link, download=True)

title_song = f"{dl_title} [{dl_id}].m4a"
print("downling ",title_song)
print("\n\n\n")

return title_song
#print(info_dict)
#for info in info_dict['formats']:
#    if (info['ext'] == 'm4a') and (info['format_id']=='140'):
#        print("downloading: ",info["url"])
#        print('\n\n')
        #py_bytes = requests.get(info['url'])
        #print("\ndownloaded bytes of: ",len(py_bytes))