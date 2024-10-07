import re

while True:
  true_or_false = input('Would you like to find another word? (y or n): ')
  if true_or_false == 'y':
    string = str(input('What word to you want to make into pig latin?: '))
    position_a = int((string.find('a')) + 1)
    position_e = int((string.find('e')) + 1)
    position_i = int((string.find('i')) + 1)
    position_o = int((string.find('o')) + 1)
    position_u = int((string.find('u')) + 1)

    if position_a == 0:
      position_a = 100000000
    if position_e == 0:
      position_e = 100000000
    if position_i == 0:
      position_i = 100000000
    if position_o == 0:
      position_o = 100000000
    if position_u == 0:
      position_u = 100000000

    if position_a < position_e and position_i and position_o and position_u:
      firstvowel = 'a'
    if position_e < position_a and position_i and position_o and position_u:
      firstvowel = 'e'
    if position_i < position_e and position_a and position_o and position_u:
      firstvowel = 'i'
    if position_o < position_e and position_i and position_a and position_u:
      firstvowel = 'o'
    if position_u < position_e and position_i and position_o and position_a:
      firstvowel = 'u'

    prt_one, prt_two = string.split(firstvowel, 1)
    prt_one = prt_one
    piged = firstvowel + prt_two + prt_one + "ay"
    print("yor word is:", piged)
  if true_or_false == 'n':
    print("Have a good day!")
    break
