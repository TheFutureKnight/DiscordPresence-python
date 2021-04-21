# RichPresence-python-running-in-background
A .pyw script that runs always in the background and updates from a config.ini file to configure rich presence for discord


this is small project that was improvised by [pypresence](https://github.com/qwertyquerty/pypresence)

# Features
- Error logging in a text file within the directory (can be disabled in the config.ini file by typing no_logging=True)
- Reports the status every minute in a json format (can be disabled in the config.ini file by typing no_status=True)
- Even when you close discord, it will remain running until you open it once more
- You can put it to startup with your PC (has a small bug that will be mentioned later)
- If Discord is closed or the pc doesn't have connection to the internet it will check every minute to see if both conditions are met in order to connect again to Discord, including saving the start time

# Known Issues
- If you make the script startup with your pc and Discord didn't have the time to open yet it will output an error_log and spam the error every 10 seconds (note: you can put a shortcut to the script into your startup folder) Partial Solution: I added 5 minute if the script runs into an issue not finding discord, in case of Discord updates it might surpass 5 minutes, for slow PCs you can edit the 5 minutes to anything that suits you (line 65)

# Requirments
- [psutil](https://pypi.org/project/psutil/)
- [pypresence](https://github.com/qwertyquerty/pypresence) and their requirments of course
- [python](https://www.python.org/)

# Notes
- You need to put your client ID in the script, it's the only thing that doesn't update from the config file (if needed I can change that and add it to the config file)
- To turn the script off once you ran it, open cmd and type `tasklist`, find the one called pythonw and copy the id, then type in `taskkill /pid ID /f`
