import pyshorteners as pys
import tkinter as tk

s = pys.Shortener()

# Printing available shorteners
for shortener in s.available_shorteners:
    print(shortener)

shortener = s.tinyurl

print(shortener.short('https://www.google.com'))
print(shortener.expand('https://tinyurl.com/8wa5w2o'))