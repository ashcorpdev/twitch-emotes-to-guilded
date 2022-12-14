# Guilded Emotes Pack Generator for Twitch Global Emotes

This script lets you create [Guilded.gg](https://guilded.gg)-compatible emote packs for the current Twitch Global Emotes, so you can add them to your Guilded server.

This script will generate a number of `.json` files which contain the necessary information to import them into Guilded.

_**Note**: This tool will not allow you to download any streamers' emotes. It is only used to download the Twitch Global emotes. **Do not download any streamers' emotes without express permission from them**._

# Usage

Download the script (or clone this repository) and run it with the following command.

`python3 twitch_emotes_to_guilded.py`

The script will then run and generate a number of `.json` files in the `emotes/` directory.

# Adding them to Guilded

You'll need to host these `.json` files somewhere accessible on the internet.

One way to do this is to upload them to your Guilded server, and then click the 'Download' option, which will give you the link to the JSON file. 

![](https://img.guildedcdn.com/ContentMediaGenericFiles/7a07d80e79a36a5f879be3b7723342c2-Full.webp?w=608&h=96)

Alternatively, you could host them on a file-sharing site such as Dropbox, Google Drive etc. As long as you can access the file directly, it should work.

Once you've got access to your files somehow, simply do the following:

1. Go to your Guilded server settings.
2. Click on 'Emotes' on the left-hand sidebar
3. Click on the 'import an external emote pack' option at the top of the Emotes section.

![](https://img.guildedcdn.com/ContentMediaGenericFiles/7ce556cf6ccb68e800c93fd61285eddf-Full.webp?w=802&h=235)

4. Paste the link for the pack and click 'Import'.

![](https://img.guildedcdn.com/ContentMediaGenericFiles/8b3d58867de5764ae9e3879e5c071388-Full.webp?w=519&h=221)

5. You will be prompted as to whether or not you want to add the emotes. 
6. Click 'Import' again and your emotes should appear in a few moments.

# Limitations

This script only grabs the Twitch Global Emotes at the time you run it and won't be able to update them. 

Additionally, if you try to add the same emote pack to Guilded multiple times, you'll end up with duplicated emotes in your Emotes section. 

This isn't something I can do something about, so you'll either have to stick to the ones you get at the time, or maybe host them on a server where you don't have any other emotes.

# How it works

1. The script will reach out to the https://twitchdatabase.com API to get a list of global emotes.
2. It loops through each of the emotes listed and re-formats them in a way that Guilded can understand.
3. Every 30 emotes, it will create a new `.json` file which contains all of the processed emotes so far. This is because Guilded only supports up to 30 emotes at a time using the [emote pack format](https://support.guilded.gg/hc/en-us/articles/360058870494-Emote-pack-import-support-with-Guilded-Developers-).

_**This script does not download any files to your machine, nor does it reach out to the Twitch servers.**_

# Disclaimer

### All Twitch Emotes are the property/copyright of Twitch Interactive, Inc. and are in no-way owned by or affiliated with me.