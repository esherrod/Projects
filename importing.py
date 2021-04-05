# Python program to
# demonstrate pyperclip module
# The Pyperclip works like copying and pasting on your computer
#
#
#
  
# This will import pyperclip
import pyperclip

# You can then save a string to the clip like you would with CTRL+C on your Keyboard
pyperclip.copy("Hello world !")
print(pyperclip.paste())
  
pyperclip.copy("Isn't pyperclip interesting?")
pyperclip.paste()

print("Currently, you have:\n" + pyperclip.paste() + "\n on your clipboard")