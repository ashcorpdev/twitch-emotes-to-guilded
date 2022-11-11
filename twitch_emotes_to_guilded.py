#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" twitch_emotes_to_guilded.py: A script to get all Twitch Global Emotes and generate emote packs for use on Guilded.gg."""

# Ownership, licensing and usage documentation
# can be found at the bottom of this script.

import urllib.request
import os
import json

if not os.path.exists('./emotes'):
    os.makedirs('./emotes')
print('Grabbing emote list...')
emotes = json.load(urllib.request.urlopen(
    'https://api.twitchdatabase.com/global-emotes'))
emotesList = []

# Emote packs can only contain up to 30 emotes.
packNo = 0
emoteCount = 0
emotesToProcess = len(emotes['globalEmotes'])

print("Emotes to process: " + str(emotesToProcess))

for emote in emotes['globalEmotes']:
    if ":" not in emote['name']:
        emote = {
            "name": emote['name'],
            "url": emote['images'][2]
        }

        newEmote = json.dumps(emote)
        emotesList.append(emote)
        # Increment the count for emotes processed.
        emoteCount += 1
        print("Processing: " + emote['name'])
    if emoteCount == 30:
        print("Creating pack for batch count: " + str(packNo))
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

print('Finished generating JSON files. You can find them in the emotes/ folder.')

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
