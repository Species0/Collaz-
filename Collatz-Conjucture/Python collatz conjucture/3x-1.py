

from time import sleep
import sys

string = "𝖒𝖆𝖉𝖊 𝖇𝖞 𝕬𝖆𝖉𝖎 𝕬𝖕𝖔𝖔𝖗𝖛𝖆"

for letter in string:
  sleep(0.1) # In seconds
  sys.stdout.write(letter)
  sys.stdout.flush()


print("""

████████╗██╗░░██╗░█████╗░████████╗██╗░░██╗
╚══██╔══╝██║░░██║██╔══██╗╚══██╔══╝██║░░██║
░░░██║░░░███████║██║░░██║░░░██║░░░███████║
░░░██║░░░██╔══██║██║░░██║░░░██║░░░██╔══██║
░░░██║░░░██║░░██║╚█████╔╝░░░██║░░░██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝

""")

number =  int(input('enter a number: '))


while number != 1:
    print(number)
    if number % 2 == 0:
        number = number // 2
    else:
        number = (number * 3) + 1

print(number)
         




    

