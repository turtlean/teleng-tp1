# -*- coding: utf-8 -*-
#!/usr/bin/python

import automata
from automata import *

transiciones1 = [[0,'lambda',1],[0,'a',2],[0,'lambda',3], [1,'lambda',4], [3,'lambda',4]]
estados = [0,1,2,3,4]
finales = []
alfabeto = ['lambda','a']
inicial = 0

transiciones2 = [[0,'lambda',1], [1,'lambda',2],[2,'lambda',0]]
transiciones3 = []
finales4 = [2]
transiciones4 = [[0,'lambda',1],[1,'lambda',2],[2,'lambda',0]]

alfabeto5 = ['a','lambda']
finales5 = [2,3,4]
transiciones5 = [[0,'lambda',1],[1,'a',2],[1,'a',3],[1,'a',4], [2,'lambda',3], [2,'lambda',4], [3,'lambda',2], [3, 'lambda', 4], [4, 'lambda',2], [4,'lambda',3]]

automata1 = Automata(estados,alfabeto5,inicial,finales,transiciones1)
automata2 = Automata(estados,alfabeto,inicial,finales,transiciones2)
automata3 = Automata(estados,alfabeto,inicial,finales,transiciones3)
automata4 = Automata(estados,alfabeto,inicial,finales4,transiciones4)
automata5 = Automata(estados,alfabeto,inicial,finales5,transiciones5)
automata6 = automata5.remover_transiciones_lambda()
automata7 = automata6.determinizar_automata()

estados29 = [0,1,2]
alfabeto29 = ['a','b']
finales29 = [2]
inicial29 = 0
transiciones29 = [[0,'a',0],[0,'b',0],[0,'a',1],[1,'b',2]]
automata29 = Automata(estados29, alfabeto29, inicial29, finales29, transiciones29)

estados8 = [0,1]
alfabeto8 = ['a','b']
finales8 = [1]
inicial8 = 0
transiciones8 = [ [0,'a',1] ]
automata8 = Automata(estados8, alfabeto8, inicial8, finales8, transiciones8)


estados10 = ['A','B']
alfabeto10 = [0,1]
finales10 = ['B']
inicial10 = 'A'
transiciones10 = [ ['A',0,'B'],['A',1,'A'],['B',0,'B'],['B',1,'B'] ]
automata10 = Automata(estados10, alfabeto10, inicial10, finales10, transiciones10)

estados11 = ['C','D']
alfabeto11 = [0,1]
finales11 = ['D']
inicial11 = 'C'
transiciones11 = [ ['C',1,'D'],['C',0,'C'],['D',0,'D'],['D',1,'D'] ]
automata11 = Automata(estados11, alfabeto11, inicial11, finales11, transiciones11)



estados12 = [0,1]
alfabeto12 = ['a','b']
finales12 = [1]
inicial12 = 0
transiciones12 = [ [1,'b',1], [1,'a',0], [0,'b',1] ]
automata12 = Automata(estados12, alfabeto12, inicial12, finales12, transiciones12)

estados13 = [0,1]
alfabeto13 = ['b','c']
finales13 = [1]
inicial13 = 0
transiciones13 = [ [0,'c',0], [0,'b',1], [1,'b',0] ]
automata13 = Automata(estados13, alfabeto13, inicial13, finales13, transiciones13)

