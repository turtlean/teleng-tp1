# -*- coding: utf-8 -*-
#!/usr/bin/python

def armar_automata(regpars):

	if regpars.nombre == 'CONCAT':

		cant_arg = len(regpars.argumentos)
		automataM1 = armar_automata(regpars.argumentos[0])

		for i in range(1,cant_arg):

			automataM2 = armar_automata(regpars.argumentos[i])
			automataM1 = armarConcat(automataM1, 'lambda', automataM2) #agregar transición final M1 con iinicial M2

	if regpars.nombre == 'OR':

		cant_arg = len(regpars.argumentos)
		automataM1 = armar_automata(regpars.argumentos[0])

		automata0 = Automata([0],['lambda'], 0, [0], [])
		automataF = Automata([0],['lambda'], 0, [0], [])

		automataM1 = armarConcat(automata0, 'lambda', automataM1)  #agregar transición final 0 con inicial
		automataM1 = armarConcat(automataM1, 'lambda', automataF)

		for i in range(1,cant_arg):

			automataM2 = armar_automata(regpars.argumentos[i])
			automataM1 = armarOr(automataM1, 'lambda', automataM2) #agregar transicion desde estado inicial M1 con inicialM2

	if (regpars.nombre == 'STAR') or (regpars.nombre == 'PLUS'):

		automata0 = Automata([0],['lambda'], 0, [0], [])
		automataF = Automata([0],['lambda'], 0, [0], [])
		automataM1 = armar_automata(regpars.argumentos[0])

		automataM1 = armarPlus(automata0, automataM1, automataF)

		if (regpars.nombre == 'STAR'):

			estado_final_M1 = automataM1.estados_finales[0] #Se que siempre es único por definición de Plus del algoritmo Thompson
			estado_inicial_M1 = automataM1.estado_inicial

			automataM1.transiciones.append([estado_inicial_M1, 'lambda',estado_final_M1])

	if regpars.nombre == 'simbolo':

		automataM1 = Automata([0,1],['lambda',regpars.valor], 0, [1], [[0,regpars.valor,1]])

	return automataM1

def armarConcat(automata1, lamb, automata2):

	automata2 = renombrarAutomata(automata1, automata2)

	estados_finales_A1 = automata1.estados_finales
	estado_inicial_A2 = automata2.estado_inicial

	automata1 = unirAutomatas(automata1,automata2, 'CONCAT')

	for i in range(0,len(estados_finales_A1)):
		automata1.transiciones.append([estados_finales_A1[i], lamb,estado_inicial_A2])

	return automata1

def armarOr(automata1, lamb, automata2):

	automata2 = renombrarAutomata(automata1, automata2)

	estado_inicial_A1 = automata1.estado_inicial
	estado_final_A1 = automata1.estados_finales[0] #Se que siempre es único por definición de Or del algoritmo Thompson
	estado_inicial_A2 = automata2.estado_inicial
	estados_finales_A2 = automata2.estados_finales

	automata1 = unirAutomatas(automata1,automata2, 'OR')

	automata1.transiciones.append([estado_inicial_A1, lamb,estado_inicial_A2])

	for i in range(0,len(estados_finales_A2)):
		automata1.transiciones.append([estados_finales_A2[i], lamb,estado_final_A1])

	return automata1

def armarPlus(automata0, automataM1, automataF):

	estado_inicial_M1 = automataM1.estado_inicial
	estados_finales_M1 = automataM1.estados_finales
	for i in range(0,len(estados_finales_M1)):
		automataM1.transiciones.append([estados_finales_M1[i], 'lambda',estado_inicial_M1])

	automataM1 = armarConcat(automata0, 'lambda', automataM1)
	automataM1 = armarConcat(automataM1, 'lambda', automataF)

	return automataM1

def unirAutomatas(automata1, automata2, forma_de_union):

	automata1.estados = automata1.estados + automata2.estados
	automata1.alfabeto = list(set(automata1.alfabeto + automata2.alfabeto))

	if forma_de_union == 'CONCAT':
		automata1.estados_finales = automata2.estados_finales

	for i in (range(0,len(automata2.transiciones))):
		automata1.transiciones.append(automata2.transiciones[i])

	return automata1

def renombrarAutomata(automata1, automata2):

	for i in (range(0, len(automata2.estados))):

		if (automata2.estados[i] in automata1.estados):

			nuevoEstado = buscarEstadoQueNoExista(automata1.estados, automata2.estados)
			automata2.transiciones = renombrarTransiciones(automata2.transiciones, automata2.estados[i], nuevoEstado)

			if (automata2.estados[i] == automata2.estado_inicial):
				automata2.estado_inicial = nuevoEstado

			for j in (range(0, len(automata2.estados_finales))):

				if (automata2.estados[i] == automata2.estados_finales[j]):
					automata2.estados_finales[j] = nuevoEstado

			automata2.estados[i] = nuevoEstado

	return automata2

def buscarEstadoQueNoExista(estados1, estados2):
	i = 0
	while ((i in estados1) or (i in estados2)):
		i = i + 1

	return i

def renombrarTransiciones(transiciones, estado, nuevoEstado):

	for i in (range(0, len(transiciones))):
		if (transiciones[i][0] == estado):
			transiciones[i][0] = nuevoEstado
		if (transiciones[i][2] == estado):
			transiciones[i][2] = nuevoEstado

	return transiciones

class Automata:
  def __init__(self, estados, alfabeto, estado_inicial, estados_finales, transiciones):
    self.estados = estados
    self.alfabeto = alfabeto
    self.estado_inicial = estado_inicial
    self.estados_finales = estados_finales
    self.transiciones = transiciones

  def clausura(self, estado, simbolo):
  	resto_transiciones = list(self.transiciones)
  	if simbolo == 'lambda':
  		clausura = [estado]
  	else:
  		clausura = []
  	return self.clausura_aux(estado,simbolo,resto_transiciones,clausura)

  def clausura_aux(self, estado, simbolo, resto_transiciones, clausura):
    resto_transiciones_copy = list(resto_transiciones)
    resto_transiciones = [t for t in resto_transiciones if (t[0] == estado) and (t[1] == simbolo)]
    for t in resto_transiciones:
      resto_transiciones_copy.remove(t)
      clausura = self.clausura_aux(t[2], simbolo, resto_transiciones_copy, clausura)
      if not (t[2] in clausura):
        clausura.append(t[2])
      resto_transiciones_copy.append(t)
    return clausura

  def clausura_lambda(self,estado):
    return self.clausura(estado,'lambda')

  #La idea para calcular las nuevas transiciones es la siguiente:
  #Dado un estado q y un símbolo de transición s
  #Primero calculo la clausura lambda de q
  #Para cada uno de los elementos de la clausura obtengo la clausura tomando la transición s
  #Sobre cada uno de estos elementos, obtengo la clausura lambda nuevamente
  #Finalmente, creo una transición del estilo (q,s,e) por cada uno de estos elementos
  def remover_transiciones_lambda(self):
    clausura_lambda_inicial = self.clausura_lambda(self.estado_inicial)
    intersection = [x for x in clausura_lambda_inicial if x in self.estados_finales]
    finales = list(self.estados_finales)
    if len(intersection) > 0 and not(self.estado_inicial in self.estados_finales):
      finales.append(self.estado_inicial)

    nuevas_transiciones = []
    for q in self.estados:
      for s in self.alfabeto:
        if s != 'lambda':
          clausura_lambda_q = self.clausura_lambda(q)
          for e in clausura_lambda_q:
            estados_alcanzables_por_transicion = self.clausura(e,s)
            clausura_lambda_estados_alcanzables = [self.clausura_lambda(x) for x in estados_alcanzables_por_transicion ]
            clausura_lambda_estados_alcanzables = [x for sublist in clausura_lambda_estados_alcanzables for x in sublist]
            clausura_lambda_estados_alcanzables = set(clausura_lambda_estados_alcanzables)
            for estado_clausura in clausura_lambda_estados_alcanzables:
              nueva_t = [q, s, estado_clausura]
              if not(nueva_t in nuevas_transiciones):
                nuevas_transiciones.append(nueva_t)

    return Automata(self.estados, self.alfabeto, self.estado_inicial, finales, nuevas_transiciones)

