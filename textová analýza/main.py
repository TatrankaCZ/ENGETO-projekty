"""
Projekt_1.py: Můj první projekt do Engeto Python kurzu.

autor: Lukáš Horák
email: tatranka520@gmail.com
discord: Vypyx#2641
"""

import sys
import TEXTS

registered_users = ["bob", "ann", "mike", "liz"]
registered_passwords = ["123", "pass123", "password123", "pass123"]

user = input("Please enter your username: ")
password = input("Please enter your password: ")

# Kód zjístí, jestli uživ.jméno a heslo sedí pro všechny registrované uživatele.
y = 0
while y < len(registered_users):
  if user == registered_users[y] and password == registered_passwords[y]:
    print("-" * 40)
    print("Welcome to the app, " + user)
    print("We have " + str(len(TEXTS)) + " texts to be analyzed.")
    print("-" * 40)
    break
  y = y + 1
else:
  print("Incorrect credentials, terminating the program...")
  sys.exit()


# Zde si uživatel vybere text, který chce analyzovat. Následně dojde k analýze.
try:
  selected_text = int(input("Enter a number btw. 1 and " + str(len(TEXTS)) + " to select: "))
  print("-" * 40)
except:
  print("Unsupported characters, terminating the program...")
  sys.exit()
else:
  if selected_text > len(TEXTS):
    print("Selected text does not exist, terminating the program...")
    sys.exit()
  else:
    selected_text = selected_text - 1
    words_1 = TEXTS[selected_text].split()
    titlecase_1 = 0
    x = 0
    while x < len(words_1):
      if words_1[x].istitle() == True:
       titlecase_1 = titlecase_1 + 1
      x = x + 1
    x = 0
    upper = False
    lower = False
    uppercase_1 = 0
    lowercase_1 = 0
    while x < len(words_1):
      e = 0
      while e <= 9:
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
        e = e + 1
      if upper:
        uppercase_1 = uppercase_1 + 1
      if lower:
        lowercase_1 = lowercase_1 + 1
      upper = False
      lower = False
      x = x + 1
    numeric_1 = []
    x = 0
    while x < len(words_1):
      if words_1[x].isnumeric() == True:
       numeric_1.append(int(words_1[x]))
      x = x + 1
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
    O = 1
    while O <= 11:
      Z = []
      x = 0
      while x < len(words_1):
        if words_1[x].find(",") == -1 and words_1[x].find(".") == -1:
          if len(words_1[x]) == O:
            Z.append(words_1[x])
        else:
          if len(words_1[x]) == O + 1:
            Z.append(words_1[x])
        x = x + 1
      E = 20 - len(Z)
      F = 3 - len(str(O))
      print(" " * F + str(O) + "|" + "*" * len(Z) + " " * E + "|" + str(len(Z)))
      O = O + 1
