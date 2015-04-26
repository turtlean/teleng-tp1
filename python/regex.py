# -*- coding: utf-8 -*-
#!/usr/bin/python

def parse_regex(filename):
  f = open(filename, 'r')
  x = parse_regex_aux(f)
  f.close()
  return x

def parse_regex_aux(f):
  l = f.readline()
  if '{' in l:
    operacion = l[l.find("{")+1:l.find("}")]
    argumentos = []
    if (operacion == 'CONCAT') or (operacion == 'OR'):
      cant_argumentos = l[l.find("}")+1]
      cant_argumentos = int(cant_argumentos)
      for i in range(0, cant_argumentos):
        argumentos.append(parse_regex_aux(f))
    else:
      argumentos.append(parse_regex_aux(f))
    return Regex(operacion, '', argumentos)
  else:
    simbolo = l.replace(" ", "")[0]
    return Regex('simbolo', simbolo, [])

class Regex:
  def __init__(self, nombre, valor, argumentos ):
    self.nombre = nombre
    self.valor = valor
    self.argumentos = argumentos