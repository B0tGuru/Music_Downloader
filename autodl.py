import requests,os
import yt_dlp

def write_bytes_to_file(bytes_data):
    with open("hi.mp3", "ab") as file:
        file.write(bytes_data)

def instantMp3(dl_inst):
    dl_title = dl_inst["title"]
    dl_link = dl_inst["link"]
    dl_id = dl_inst['id']
    print(f"downloading {dl_title} please wait .....")
    print(f"started download of {dl_title} from {dl_link}")
    yt_opts = {'format':'140'}
    utube = yt_dlp.YoutubeDL(yt_opts)
    info_dict = utube.extract_info(dl_link, download=True)
    title_song = f"{dl_title} [{dl_id}].m4a"
    print("downling ",title_song)
    afile = open(title_song,'rb')
    afile_bytes = afile.read()
    os.remove(title_song)
    return afile_bytes
    #for info in info_dict['formats']:
    #    if (info['ext'] == 'm4a') and (info['format_id']=='140'):
    #        print("downloading: ",info["url"])
    #        print('\n\n')
    #        return info["url"]


async def download_mp3Tele(context,url,msg_ctx):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        #print(info_dict['formats'])
        #input()
        audio_infos = info_dict['formats']
        audio_info = None
        for audio_infox in audio_infos:
            #print(f"\n\n\naudio info: {audio_infox}")
            if audio_infox['format'] ==  '140 - audio only (medium)':
                audio_info = audio_infox
                
                break
            #input()
        #audio_info = audio_infos[0]
        print(audio_info)
        #input()
        chunk_size = 5024
        dl_chunks = 0
        ind = 0
        bytes_read = bytearray()
        total_bytes =  audio_info['filesize']
        with requests.get(audio_info['url'], stream=True) as response:
           # print(f"\n\ndata packet: {audio_info}")
           # input()
            for chunk in response.iter_content(chunk_size=chunk_size):
                # Process the bytes in the chunk here.
                #print(f"video {ind}")
                bytes_read.extend(chunk)
                dl_chunks = dl_chunks+chunk_size
                chatid = msg_ctx.chat.id
                #up_msg  = await update.message.reply_text(f"downloading {dl_title} please wait")
                dl_100 = round(((dl_chunks*100)/total_bytes),2)
                dl_total_mb = round(total_bytes/1000000)

                dl_str = (f"downloaded {dl_100} % of {dl_total_mb} MB")
                await context.bot.edit_message_text(chat_id=chatid,message_id = msg_ctx.message_id,text=dl_str)
                #cb_fx(dl_chunks,total_bytes)
                #write_bytes_to_file(bytes(bytes_read)
                ind = ind +1
                pass
        
        #write_bytes_to_file(bytes(bytes_read))
        return bytes(bytes_read)

def download_mp3(url):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        #print(info_dict['formats'])
        #input()
        audio_infos = info_dict['formats']
        audio_info = None
        for audio_infox in audio_infos:
            #print(f"\n\n\naudio info: {audio_infox}")
            if audio_infox['format'] ==  '140 - audio only (medium)':
                audio_info = audio_infox
                
                break
            #input()
        #audio_info = audio_infos[0]
        print(audio_info)
        #input()
        chunk_size = 1024
        ind = 0
        bytes_read = bytearray()
        total_bytes =  audio_info['filesize']
        with requests.get(audio_info['url'], stream=True) as response:
           # print(f"\n\ndata packet: {audio_info}")
           # input()
            for chunk in response.iter_content(chunk_size=chunk_size):
                # Process the bytes in the chunk here.
                #print(f"video {ind}")
                bytes_read.extend(chunk)
                #write_bytes_to_file(bytes(bytes_read)
                ind = ind +1
                pass
        
        #write_bytes_to_file(bytes(bytes_read))
        return bytes(bytes_read)
        #ind

    
def download_mp3CB(url,cb_fx):
      with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        #print(info_dict['formats'])
        #input()
        audio_infos = info_dict['formats']
        audio_info = None
        for audio_infox in audio_infos:
            #print(f"\n\n\naudio info: {audio_infox}")
            if audio_infox['format'] ==  '140 - audio only (medium)':
                audio_info = audio_infox
                
                break
            #input()
        #audio_info = audio_infos[0]
        print(audio_info)
        #input()
        chunk_size = 1024
        dl_chunks = 0
        ind = 0
        bytes_read = bytearray()
        total_bytes =  audio_info['filesize']
        with requests.get(audio_info['url'], stream=True) as response:
           # print(f"\n\ndata packet: {audio_info}")
           # input()
            for chunk in response.iter_content(chunk_size=chunk_size):
                # Process the bytes in the chunk here.
                #print(f"video {ind}")
                bytes_read.extend(chunk)
                dl_chunks = dl_chunks+chunk_size
                cb_fx(dl_chunks,total_bytes)
                #write_bytes_to_file(bytes(bytes_read)
                ind = ind +1
                pass
        
        #write_bytes_to_file(bytes(bytes_read))
        return bytes(bytes_read)

def callb(a,b):
    dl_100 = round(((a*100)/b),2)
    print(f"downloaded {dl_100} % of {b}")
#if __name__ == '__main__':
#    url = 'https://www.youtube.com/watch?v=B6H_x6pj7Ow'
#    download_mp3CB(url,callb)