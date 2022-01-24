from WordArtGenerator.example.helpers.facebook_2_word_collection import facebook_2_word_collection

file_name = "mysteryincorporated_rooohroooh" # or None

facebook_2_word_collection(
    facebook_filename=file_name
)

from WordArtGenerator.example.helpers.word_collection_2_frequency import word_collection_2_frequency

word_collection_2_frequency(
    wc_filename=file_name
)

from WordArtGenerator.example.helpers.frequency_2_typography import frequency_2_typography

frequency_2_typography(
    "./masks/scooby_mask.png",
    frequency_filename=file_name,
    inside_color="brg",
    inside_bg_color=(0, 0, 0),
    outside_color="gist_gray",
    outside_bg_color=(255, 255, 255),
    outside_words=True
)
