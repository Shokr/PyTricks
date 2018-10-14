
"""
<Python 2.7>
"""

"""
sh < sudo pip install --user sh >

Python makes a great scripting language.
Sometimes using the standard os and subprocess libraries
can be a bit of a headache.
"""

import sh

print(sh.pwd())
print(sh.whoami())

#sh.mkdir('new_folder')
#sh.touch('new_file.txt')

print('-------------------------------------------------------------------')

"""
emoji  :: https://pypi.org/project/emoji/

pip install emoji
"""

import emoji

print(emoji.emojize('Python is :thumbs_up:'))

