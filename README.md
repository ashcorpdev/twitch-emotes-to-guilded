# Guilded Emotes Pack Generator for Twitch Global Emotes

This script lets you create [Guilded.gg](https://guilded.gg)-compatible emote packs for the current Twitch Global Emotes, so you can add them to your Guilded server.

This script will generate a number of `.json` files which contain the necessary information to import them into Guilded.

# Usage

Download the script (or clone this repository) and run it with the following command.

`python3 twitch_emotes_to_guilded.py`

The script will then run and generate a number of `.json` files in the `emotes/` directory.

# Adding them to Guilded

You'll need to host these `.json` files somewhere accessible on the internet.

One way to do this is to upload them to your Guilded server, and then click the 'Download' option, which will give you the link to the JSON file. Alternatively, you could host them on a file-sharing site such as Dropbox, Google Drive etc. As long as you can access the file directly, it should work.

Once you've got access to your files somehow, simply go to your Guilded server, click on 'Emotes', and then click on the 'import an external emote pack' option.

Paste the link for the pack, click 'Import' and you will be prompted as to whether or not you want to add the emotes.

Simply click 'Import' again and your emotes should appear in a few moments.

# How it works

1. The script will reach out to the https://twitchdatabase.com API to get a list of global emotes.
2. It loops through each of the emotes listed and re-formats them in a way that Guilded can understand.
3. Every 30 emotes, it will create a new `.json` file which contains all of the processed emotes so far. This is because Guilded only supports up to 30 emotes at a time using the [emote pack format](https://support.guilded.gg/hc/en-us/articles/360058870494-Emote-pack-import-support-with-Guilded-Developers-).

_**This script does not download any files to your machine, nor does it reach out to the Twitch servers.**_


### All Twitch Emotes are the property of Twitch Interactive and are in no-way owned by me.