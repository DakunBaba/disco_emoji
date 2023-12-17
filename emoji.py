# disco_emoji

# CLDR is Common Locale Data Repository, providing data on languages, cultures, regions, and more.
# It includes locale-specific details, language info, country data, currency symbols, and emoji names.
# The heart emoji "❤️" is known as "heavy black heart" with the CLDR code ":heavy_black_heart."
# These standardized names and codes ensure consistency and compatibility in applications using emojis.
# Python's `emoji` library facilitates working with emojis using CLDR names and codes in projects.

# https://pypi.org/project/emoji/

!pip install emoji

# Install & upgrade using: python -m pip install emoji --upgrade

import emoji

print(emoji.emojize('Hello, Python I :heart: U!')) # if the code is incorrect, you'll know

# for all emojis shortcode visit
# https://www.webfx.com/tools/emoji-cheat-sheet/

print(emoji.emojize("Python is fun :red_heart:")) # when the CLDR code is correct

print(emoji.emojize("Python is fun :thumbsup:", language='alias'))

#:skull_and_crossbones:
print(emoji.emojize("Python is :skull_and_crossbones:"))

print(emoji.emojize("Python is lightning fast! :high_voltage: "))

print(emoji.emojize("Python is lightning fast! :zap:")) # when the code is incorrect, you'll know

# Tried something new
emojified_text = emoji.emojize("Python is awesome :thumbs_up:", language='en')
print(emojified_text)

print(emoji.demojize('Python is 👍')) # how does that work ?

# Add "d" before "emojize" to find the CLDR code
print(emoji.demojize('Python is 🚀'))
# Remove "d" before "emojize" and type the CLDR code
print(emoji.emojize('Python is :rocket:'))

print(emoji.demojize("Python is 😱 "))
print(emoji.emojize("Python is :face_screaming_in_fear: "))

# this is a test for git cmd




