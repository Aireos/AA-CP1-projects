

vowel = ['a', 'e', 'i', 'o', 'u']

string = str(input('What word to you want to make into pig latin?: '))

position_a = (string.find(a)) + 1
position_e = (string.find(e)) + 1
position_i = (string.find(i)) + 1
position_o = (string.find(o)) + 1
position_u = (string.find(u)) + 1

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

if position_a < position_e, position_i, position_o or position_u:
  firstvowel = position_a
if position_e < position_a, position_i, position_o or position_u:
  firstvowel = position_e
if position_i < position_e, position_a, position_o or position_u:
  firstvowel = position_i
if position_o < position_e, position_i, position_a or position_u:
  firstvowel = position_o
if position_u < position_e, position_i, position_o or position_a:
  firstvowel = position_u

split = string.split(firstvowel)
print(split)

