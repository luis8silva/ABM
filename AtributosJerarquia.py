#!/usr/bin/python
# -*- coding: utf-8 -*-

# Clase para visualizar los atributos de una jerarquia de clases
# Autores: J. Luis Silva, Diego Color, Pedro Zermeño
# Version 1.0

from __future__ import print_function

class AtributosJerarquia():
	#Definicion de la clase para visualizar los atributos de una jerarquia de clases
	def atributosJerarquia(self):
	    #Retorna los atributos de una jerarquia de clases"
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append('%s=%s' % (key, getattr(self, key)))
		return ', '.join(attrs)
        
	def __repr__(self):
		#Visualiza los atributos de una jerarquia de clases 
		return '[%s: %s]' % (self.__class__.__name__, self.atributosJerarquia())

	def visualizaAtributosJeraquia(self):
		#Visualiza los atributos de una jerarquia de clases
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append('%s=%s' % (key, getattr(self, key)))
		print( '[%s: %s]' % (self.__class__.__name__,  ', '.join(attrs)))