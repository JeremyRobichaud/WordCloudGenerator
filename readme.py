# This script creates WordCloud Art from a facebook message log and an image mask.


# The First thing you need to do is create a word_collection (a.k.a. lexicon).
# The way I've done it is by downloading my conversation logs from the facebook servers.

# NOTE: We'll be working with that, HOWEVER, if you have another word bank you wanted to use,
# feel free to place it in the temp/word_collection folder (I'll work the same).

# To download from the facebook servers, you'll need to log into facebook via a web-browser and follow:
# Top-Right Arrow (facing downwards) >
# Settings & Privacy >
# Settings >
# Your Facebook Information (Left-Hand Side) >
# Download Your Information >
# Format = JSON, Media Quality = Low (For higher download speed), Date Range = Whatever you want (I did 'All Time') >
# Only select 'Messages' >
# Start your download.

# This will send a download request, that facebook will accept and prepare for you.

# You'll get a notification once it's been processed and readied.

# Then in 'Available Files' you'll be able to download your information.

# Once downloaded, bring the .zip file into the root project folder (/WordArtGenerator).

# Then extract using the "Extract to facebook-johnsmith\" option

# You should now have a folder call "facebook-YOURNAME123", we'll call this folder "/facebook" for short.

# The script uses "./facebook/messages/inbox/*" then reads all the "messages_X.json" files within those folders.
# As you may have notices, those folders are all your messages. I suggest deleting those that you do not want formatted.

# And that's it, you've done all the set up for this part :)


from helpers.facebook_2_word_collection import facebook_2_word_collection

# This variable will dictate with conversation it'll transform.
# It transforms ALL your conversations by default, so if you don't set it, IT WILL BE SLOW.
# This variable will be used by all 3 stages, even if you skip the facebook part, I would suggest setting it.
# If you are using the facebook method, the filename will be "./facebook/messages/inbox/XXXXXX/" ONLY the XXXXXX part.

file_name = "maddyrideout_02p66t7g2w.txt"

# This function transforms the facebook data to the word_collection format.
# It will create a temp folder to hold the word_collection data, '/temp/word_collection'
# NOTE: If you don't want to run this part, just comment it out.

# facebook_2_word_collection(
#     facebook_filename=file_name
# )


# The second function will transform those .txt word files into frequencies.
# If you have your own .txt file,
# place in the ./WordArtGenerator/temp/word_collection folder (If it doesn't exist, create it).

# Frequencies are a file that shows every word in the word_collection file and the amount of times it showed up.

from helpers.word_collection_2_frequency import word_collection_2_frequency

# word_collection_2_frequency(
#     wc_filename=file_name
# )


# Finally, the third and last function creates the WordArt from the frequency file.
# However, there is some set up for this step.

# First, you'll need a Blank and White photo to mask the print. This photo will set the boundaries of the words.
# Once you have that created, put the file in the masks folder and point the variable below to it.

# Secondly, you need to chose if words will appear in both the White and Black areas or just the White areas
# Set the "outside_words" variable to True/False for Yes/No

# Secondly, you'll need to chose the colors for the following variables:
# inside_color = The color of the words inside the white
# inside_bg_color = The color of the inside background, if you didn't want white (Default: White)
# outside_color = The color of the words inside the black
# outside_bg_color = The color of the outside background, if you didn't want white (Default: White)

# For inside/outside colors, you can chose from Color Maps or RGB values.
# Color Maps will assign random colors within the map to each word,
#   see https://matplotlib.org/stable/tutorials/colors/colormaps.html for all available maps. Use a "string" for this
# RGB colors will be a static color to all words,
#   see https://www.w3schools.com/colors/colors_rgb.asp for a calculator. Use a tuple (X, X, X) for this.

# For background colors, only RGB is available.

from helpers.frequency_2_typography import frequency_2_typography

frequency_2_typography(
    "./masks/Maddy and I.png",
    frequency_filename=file_name,
    inside_color="winter",
    inside_bg_color=(0, 0, 0),
    outside_color="summer",
    outside_bg_color=(255, 255, 255),
    outside_words=True
)
