# Übungsblatt_4.py
#
# Alexander Blesius & Denise Schmidt
#
#
#
# Aufgabe 3

import nltk,re,pprint

from nltk import word_tokenize

text = word_tokenize("They wind back the clock, while we chase after the wind.")

nltk.pos_tag(text)

# Output: [('They', 'PRP'), ('wind', 'VBP'), ('back', 'RB'), ('the', 'DT'),
# ('clock', 'NN'), (',', ','), ('while', 'IN'), ('we', 'PRP'), ('chase', 'VBP'),
# ('after', 'IN'), ('the', 'DT'), ('wind', 'NN'), ('.', '.')]
# Bei "wind" kommt es zu Unterschieden bei der Wortart und der Aussprache.
# "wind" wird zunächst als Verb benutzt (die Uhr zurückdrehen) und dann als Nomen (der Wind).
# Bei wind/Verb wird das i als ei ausgesprochen.
# Bei wind/Nomen wird das i als i ausgesprochen.

#Aufgabe 34



#Aufgabe 5
# 5.1

grammar1 = nltk.ContextFreeGrammar.fromstring("""
PHRASE -> AdjP | NP CON NP
NP -> Adj N | N 
AdjP -> Adj Obj
Obj -> N CON N
Adj -> 'old'
N -> 'men' | 'women'
CON -> 'and'
""")

sent = [("old"), ("men"), ("and"), ("women")]

rd_parser = nltk.RecursiveDescentParser(grammar1)

for tree in rd_parser.parse(sent):
	print(tree)
        
# Lesart 1: old men and old women (das Adjektiv wird auf beide Nomen bezogen und
# dominiert die Nomen = steht im Baum oben).
# Lesart 2: die Phrase besteht aus zwei "unabhängigen Nomen", nämlich alten Männern
# und Frauen aller Altersstufen.

# 5.2 Satz (S (NP Mary) (VP (V saw) (NP Bob)))

tree1 = nltk.Tree('NP', ['Mary'])

tree2 = nltk.Tree('NP', ['Bob'])

tree3 = nltk.Tree('V', ['saw'])

tree4 = nltk.Tree('VP', [tree3, tree2])

tree5 = nltk.Tree('S', [tree1, tree4])

print(tree5)

tree5.draw()

# 5.3
grammar2 = nltk.ContextFreeGrammar.fromstring("""
S -> NP VP | NP VP Time
NP -> Det N
VP -> V NP VTemp | V NP TemP
TemP -> VTemp Day
Time -> Day
Det -> 'The' | 'a'
N -> 'man' | 'woman'
V -> 'saw'
VTemp -> 'last'
Day -> 'Thursday'
""")

sent = "The woman saw a man last Thursday".split()

rd_parser = nltk.RecursiveDescentParser(grammar2)

for tree in rd_parser.parse(sent):
	print(tree)

# Lesart 1: Sie sah ihn zuletzt Dienstag.
# Lesart 2: Sie sah ihn letzten Dienstag.
# Lesart mit saw = sägen: überprüft, aber da Vergangenheit vorliegt, keine
# Lesart möglich, da saw im Präsens (Vergangenheit sawed) keinen Sinn ergibt

#Aufgabe 25
