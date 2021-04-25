from pypresence import Presence
import time
import configparser
import os
import json
import psutil
import urllib.request

from pypresence.exceptions import InvalidPipe

firstrun = True
startup = True
start_time=time.time()
configpar = configparser.ConfigParser(allow_no_value=True)


while True:
    try:
        configpar.read('config.ini')
        if configpar.has_section("Config") == True:
            config = configpar['Config']
        else:
            with open("config.ini", "w+") as f:
                f.write("[Config]\nclient_id=\nstate=\ndetails=\nlarge_image=\nsmall_image=\nlarge_text=\nsmall_text=\nbutton1=\nbutton1_url=\nbutton2=\nbutton2_url=")
            print("Config file not found!")
            continue

        def check(value):
            try:
                if config[value] in ["", " "]:
                    return None
                return config[value]
            except KeyError:
                return None
        
        if firstrun == True:
            client_id = check("client_id")
            RPC = Presence(client_id) 
            RPC.connect()
            firstrun = False

        button1 = check("button1")
        button2 = check("button2")
        button1_url = check("button1_url")
        button2_url = check("button2_url")

        if (button1 and button1_url) and (button2 and button2_url):
            Status = RPC.update(state=check("state"), details=check("details"), large_image=check("large_image"), small_image=check("small_image"), large_text=check("large_text"),small_text=check("small_text"),buttons=[{"label": check("button1"), "url": check("button1_url")}, {"label": check("button2"), "url": check("button2_url")}], start=start_time)
        elif button1 and button1_url:
            Status = RPC.update(state=check("state"), details=check("details"), large_image=check("large_image"), small_image=check("small_image"), large_text=check("large_text"),small_text=check("small_text"),buttons=[{"label": check("button1"), "url": check("button1_url")}], start=start_time)
        elif button2 and button2_url:
            Status = RPC.update(state=check("state"), details=check("details"), large_image=check("large_image"), small_image=check("small_image"), large_text=check("large_text"),small_text=check("small_text"),buttons=[{"label": check("button2"), "url": check("button2_url")}], start=start_time)
        else:
            Status = RPC.update(state=check("state"), details=check("details"), large_image=check("large_image"), small_image=check("small_image"), large_text=check("large_text"),small_text=check("small_text"), start=start_time)

        if check("no_status") not in ["True", "true"]:
            with open("status.json","w+") as f:
                json.dump(Status, f)
        time.sleep(60)

    except Exception as e:
        
        if startup == True and e.__class__ == InvalidPipe:
            time.sleep(300)
            startup = False
            continue
    

        if check("no_logging") not in ["True", "true"]:
            if os.path.exists("error_log.txt"):
                mode = 'a'
            else:
                mode = 'w'
            
            with open("error_log.txt", mode) as f:
                now = time.localtime()
                if mode == "w":
                    f.write(f"[{now[1]}/{now[2]}/{now[0]} {now[3]}:{now[4]}]: {e.__class__.__name__}: {e}")
                else:
                    f.write(f"\n[{now[1]}/{now[2]}/{now[0]} {now[3]}:{now[4]}]: {e.__class__.__name__}: {e}")

        def connect():
            try:
                urllib.request.urlopen("http://google.com")
                return True
            except:
                return None

        firstrun = True
        while True:
            if any(i.name() in ["DiscordPTB.exe", "Discord.exe", "DiscordCanary.exe"] for i in psutil.process_iter()):
                if connect():
                    time.sleep(10)
                    break
            time.sleep(60)
        continue
