#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" twitch_emotes_to_guilded.py: A script to get all Twitch Global Emotes and generate emote packs for use on Guilded.gg."""

# Ownership, licensing and usage documentation
# can be found at the bottom of this script.

import urllib.request
import os
import sys
import json
import time

banner = """
                                                                       
                       ,,                                              
      db             `7MM         .g8\"""bgd                            
     ;MM:              MM       .dP'     `M                            
    ,V^MM.    ,pP"Ybd  MMpMMMb. dM'       ` ,pW"Wq.`7Mb,od8 `7MMpdMAo. 
   ,M  `MM    8I   `"  MM    MM MM         6W'   `Wb MM' "'   MM   `Wb 
   AbmmmqMA   `YMMMa.  MM    MM MM.        8M     M8 MM       MM    M8 
  A'     VML  L.   I8  MM    MM `Mb.     ,'YA.   ,A9 MM       MM   ,AP 
.AMA.   .AMMA.M9mmmP'.JMML  JMML. `"bmmmd'  `Ybmd9'.JMML.     MMbmmd'  
                                                              MM       
                                                            .JMML.     
"""

print(banner)
print("Guilded Emote Pack Generator for Twitch Global Emotes v1.0.0")
print("----")

if not os.path.exists('./emotes'):
    os.makedirs('./emotes')
print('\nFetching global emote list...\n')
emotes = json.load(urllib.request.urlopen(
    'https://api.twitchdatabase.com/global-emotes'))
emotesList = []

# Emote packs can only contain up to 30 emotes.
packNo = 0
emoteCount = 0
totalCounted = 0
emotesToProcess = len(emotes['globalEmotes'])

print("Emotes to process: " + str(emotesToProcess) + "\n")

for emote in emotes['globalEmotes']:
    if ":" not in emote['name']:
        emote = {
            "name": emote['name'],
            "url": emote['images'][2]
        }

        newEmote = json.dumps(emote)
        emotesList.append(emote)
    if emoteCount == 30:
        # Reset the emote count.
        emoteCount = 0

        packFormat = {
            "name": f"Twitch Emotes {packNo}",
            "author": "AshCorpDev",
            "emotes": emotesList
        }
        outputJSON = json.dumps(packFormat)
        with open(f'./emotes/emotes{packNo}.json', 'w') as out_file:
            # Clean up the links for formatting.
            newOutput = outputJSON.replace("/", "\\/")
            out_file.write(newOutput)

        # Start a new pack.
        packNo += 1
        # Reset the emotes list for the next batch.
        emotesList = []
    
    # Increment the count for emotes processed.
    emoteCount += 1
    totalCounted += 1
    percent = 100.0*totalCounted/emotesToProcess
    sys.stdout.write('\r')
    sys.stdout.write("Progress: [{:{}}] {:>3}%"
                     .format('='*int(percent/(100.0/30)),
                             30, int(percent)))
    sys.stdout.flush()
    time.sleep(0.002)

print('\n\nFinished generating JSON files. You can find them in the emotes/ folder.\n')
print('Visit https://github.com/ashcorpdev/twitch-emotes-to-guilded for more information on how to host these files.\n')
"""
@Author = "Ashen"
@Licence = "MIT"
@Version = "1.0.0"
@Email = "ashen@ashcorp.dev"
@Status = "Complete"
"""

"""
Credit to:
- /u/rtainc on Reddit (Initial boilerplate of the script)
- ravenbtw at raven.fo (Created twitch-database, which is used for grabbing the global emotes list)

All emotes are the property of Twitch Interactive.
"""
