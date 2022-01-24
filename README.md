# WordCloudGenerator
This script creates WordCloud Art from a facebook message log and an image mask.

# Setup
The First thing you need to do is create a word_collection (a.k.a. lexicon).
The way I've done it is by downloading my conversation logs from the facebook servers.

NOTE: We'll be working with that, HOWEVER, if you have another word bank you wanted to use,
feel free to place it in the temp/word_collection folder (I'll work the same).

To download from the facebook servers, you'll need to log into facebook via a web-browser and follow:
Top-Right Arrow (facing downwards) >
Settings & Privacy >
Settings >
Your Facebook Information (Left-Hand Side) >
Download Your Information >
Format = JSON, Media Quality = Low (For higher download speed), Date Range = Whatever you want (I did 'All Time') >
Only select 'Messages' >
Start your download.

This will send a download request, that facebook will accept and prepare for you.

You'll get a notification once it's been processed and readied.

Then in 'Available Files' you'll be able to download your information.

Once downloaded, bring the .zip file into the root project folder (/WordArtGenerator).

Then extract using the "Extract to facebook-johnsmith\" option

You should now have a folder call "facebook-YOURNAME123", we'll call this folder "/facebook" for short.

The script uses "./facebook/messages/inbox/*" then reads all the "messages_X.json" files within those folders.
As you may have notices, those folders are all your messages. I suggest deleting those that you do not want formatted.

And that's it, you've done all the setup :)


    © 2022 GitHub, Inc.

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

