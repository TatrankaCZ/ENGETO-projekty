"""
Projekt_1.py: Můj první projekt do Engeto Python kurzu.

autor: Lukáš Horák
email: tatranka520@gmail.com
discord: Vypyx#2641
"""

import sys
import TEXTS

registered_users = {"bob": "123", 
                    "ann": "pass123",
                    "mike": "password123",
                    "liz": "pass123"
}



user = input("Please enter your username: ")
password = input("Please enter your password: ")

# Kód zjístí, jestli uživ.jméno a heslo sedí pro všechny registrované uživatele.
try:
  if password == registered_users[user]:
    print("-" * 40)
    print("Welcome to the app, " + user)
    print("We have " + str(len(TEXTS.TEXTS)) + " texts to be analyzed.")
    print("-" * 40)
  else:
    print("Incorrect credentials, terminating the program...")
except:
  print("Incorrect credentials, terminating the program...")
 

# Zde si uživatel vybere text, který chce analyzovat. Následně dojde k analýze.
try:
  selected_text = int(input("Enter a number btw. 1 and " + str(len(TEXTS.TEXTS)) + " to select: "))
  print("-" * 40)
except:
  print("Unsupported characters, terminating the program...")
  sys.exit()

if selected_text > len(TEXTS.TEXTS):
  print("Selected text does not exist, terminating the program...")
  sys.exit()

selected_text = selected_text - 1
words_1 = TEXTS.TEXTS[selected_text].split()
titlecase_1 = 0
upper = False
lower = False
uppercase_1 = 0
lowercase_1 = 0
numeric_1 = []
for x in range(len(words_1)):
  if words_1[x].istitle():
   titlecase_1 += words_1[x].istitle()
  for e in range(9):
    if words_1[x].isupper():
      if words_1[x].find(str(e)) != -1:
        break
      else:
        upper = True
    if words_1[x].islower():
      if words_1[x].find(str(e)) != -1:
        break
      else:
        lower = True
  if upper:
    uppercase_1 = uppercase_1 + 1
  if lower:
    lowercase_1 = lowercase_1 + 1
  upper = False
  lower = False
  if words_1[x].isnumeric():
   numeric_1.append(int(words_1[x]))
# Dále zobrazí informace o daném textu
print("There are " + str(len(words_1)) + " words in the selected text.")
print("There are " + str(titlecase_1) + " titlecase words.")
print("There are " + str(uppercase_1) + " uppercase words.")
print("There are " + str(lowercase_1) + " lowercase words.")
print("There are " + str(len(numeric_1)) + " numeric strings.")
print("The sum of all the numbers is " + str(sum(numeric_1)))

print("-" * 40)
print("LEN|     OCCURENCES     |NR.")
print("-" * 40)
WordLength = 1
while WordLength <= 11:
  WordsFound = []
  x = 0
  while x < len(words_1):
    if words_1[x].find(",") == -1 and words_1[x].find(".") == -1:
      if len(words_1[x]) == WordLength:
        WordsFound.append(words_1[x])
    else:
      if len(words_1[x]) == WordLength + 1:
        WordsFound.append(words_1[x])
    x = x + 1
  E = 20 - len(WordsFound)
  F = 3 - len(str(WordLength))
  print(" " * F + str(WordLength) + "|" + "*" * len(WordsFound) + " " * E + "|" + str(len(WordsFound)))
  WordLength = WordLength + 1
