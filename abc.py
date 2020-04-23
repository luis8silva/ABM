#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ejemplo de Clase de Altas, Bajas y Cambios y mas
# Autores: J. Luis Silva, Diego Color, Pedro Zermeño
# Version 1.0

from __future__ import print_function
import sys
if sys.version[0] == '2': input = raw_input 

import shelve 
import os
from AtributosJerarquia import AtributosJerarquia


class Producto(AtributosJerarquia):
	#Definicion de la clase producto
	def __init__(self):
		#Constructor de la clase producto
		self.__id = None
		self.__nomb = None
		self.__precio = None
		self.__cant = None
		
	def inicializa(self, id, nomb, precio, cant):
	    #Inicializa la clase producto
		self.__id = id
		self.__nomb = nomb
		self.__precio = precio
		self.__cant = cant
		
	def captura(self):
		#Captura la clase producto
		self.__id = input('ID: ')
		self.__nomb = input('Nombre del producto: ')
		self.__precio = float(input('Precio: '))
		self.__cant = int(input('Cantidad: '))

	def identificador(self):
		#Retorna el identificador producto#
		return self.__id
		
	# Acceso al valor self.__id mediante la variable id
	id = property(identificador)
		
	def visualizar(self):
		#Visualiza la clase producto
		print(self)

	def __repr__(self):
		#Visualiza la clase producto
		a = '\nID: {0}\n'.format(self.__id)
		a += 'Nombre del producto: {0}\n'.format(self.__nomb)
		a += 'Precio: {:,.2f}\n'.format(self.__precio)
		a += 'Cantidad: {0}\n'.format(self.__cant)
		return a


class BodegaDonJulio(Producto):
	#Definicion de la clase BodegaDonJulio
	def __init__(self):
		#Constructor de la clase BodegaDonJulio
		Producto.__init__(self)
		self.__caja = None
		self.__camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase BodegaDonJulio
		Producto.inicializa(self, id, nomb, precio, cant)
		self.__caja = caja
		self.__camion = camion
		
	def captura(self):
		#Captura la clase BodegaDonJulio
		Producto.captura(self)
		self.__caja = int(input('Cajas: '))
		self.__camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase BodegaDonJulio
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.__caja)
		a += 'Camiones: {0}\n'.format(self.__camion)
		return a


class AlmacenLaEsperanza(Producto):
	#Definicion de la clase AlmacenLaEsperanza
	def __init__(self):
		#Constructor de la clase Televisor
		Producto.__init__(self)
		self.__caja = None
		self.__camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase AlmacenLaEsperanza
		Producto.inicializa(self, id, nomb, precio, cant)
		self.__caja = caja
		self.__camion = camion
		
	def captura(self):
		#Captura la clase AlmacenLaEsperanza
		Producto.captura(self)
		self.__caja = int(input('Cajas: '))
		self.__camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase AlmacenLaEsperanza
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.__caja)
		a += 'Camiones: {0}\n'.format(self.__camion)
		return a


class AbastecedoraLaUnion(Producto):
	#Definicion de la clase AbastecedoraLaUnion
	def __init__(self):
		#Constructor de la clase AbastecedoraLaUnion
		Producto.__init__(self)
		self.__caja = None
		self.__camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase AbastecedoraLaUnion
		Producto.inicializa(self, id, nomb, precio, cant)
		self.__caja = caja
		self.__camion = camion
		
	def captura(self):
		#Captura la clase AbastecedoraLaUnion
		Producto.captura(self)
		self.__caja = int(input('Cajas: '))
		self.__camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase AbastecedoraLaUnion
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.__caja)
		a += 'Camiones: {0}\n'.format(self.__camion)
		return a


class SalsasDoniaMary(Producto):
	#Definicion de la clase SalsasDoniaMary
	def __init__(self):
		#Constructor de la clase Salsas Doña Mary
		Producto.__init__(self)
		self.__caja = None
		self.__camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase SalsasDoniaMary
		Producto.inicializa(self, id, nomb, precio, cant)
		self.__caja = caja
		self.__camion = camion
		
	def captura(self):
		#Captura la clase SalsasDoniaMary
		Producto.captura(self)
		self.__caja = int(input('Cajas: '))
		self.__camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase SalsasDoniaMary
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.__caja)
		a += 'Camiones: {0}\n'.format(self.__camion)
		return a


class VerdurasMax(Producto):
	#Definicion de la clase VerdurasMax
	def __init__(self):
		#Constructor de la clase VerdurasMax
		Producto.__init__(self)
		self.__caja = None
		self.__camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase VerdurasMax
		Producto.inicializa(self, id, nomb, precio, cant)
		self.__caja = caja
		self.__camion = camion
		
	def captura(self):
		#Captura la clase VerdurasMax
		Producto.captura(self)
		self.__caja = int(input('Cajas: '))
		self.__camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase VerdurasMax
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.__caja)
		a += 'Camiones: {0}\n'.format(self.__camion)
		return a


class AbastecedoraDonLupe(Producto):
	#Definicion de la clase AbastecedoraDonLupe
	def __init__(self):
		#Constructor de la clase AbastecedoraDonLupe
		Producto.__init__(self)
		self.__caja = None
		self.__camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase AbastecedoraDonLupe
		Producto.inicializa(self, id, nomb, precio, cant)
		self.__caja = caja
		self.__camion = camion
		
	def captura(self):
		#Captura la clase AbastecedoraDonLupe
		Producto.captura(self)
		self.__caja = int(input('Cajas: '))
		self.__camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase AbastecedoraDonLupe
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.__caja)
		a += 'Camiones: {0}\n'.format(self.__camion)
		return a



class Prueba():
	#Clase de prueba
	def __init__(self):
		#Constructor de la clase
		self.__lista = []	# Lista para los objetos creados
		self.__archivo = 'ArchivoBD'
		self.__msw = 1
		self.__db = shelve.open(self.__archivo)
		for k in self.__db:
			self.__lista.append(self.__db[k])
		print("\nConstructor")
		
	def __del__(self):
		#Destructor
		print("\nDestructor")
		
	def menu(self):
		#Menu
		sw = {'1':self.f1, '2':self.f2, '3':self.f3, '4':self.f4, '0':self.f9}
		while self.__msw:		
			#os.system('clear') # NOTA para windows tienes que cambiar clear por cls
			print("\nSelecciona una opcion")
			print("\t1 - Altas")
			print("\t2 - Bajas")
			print("\t3 - Cambios")
			print("\t4 - Visualizar")
			print("\t0 - salir")
			# solicitamos una opcion al usuario 
			opcionMenu = input("\nInserta un numero >> ")
			sw.get(opcionMenu,self.otro)()

	def f1(self):
		#Altas de los productos
		print("")
		opcion = input("\nDeseas dar de alta productos de:\n\t1 - Bodega Don Julio (Fruta (piña, melon, sandia)) \n\t2 - Almacen La Esperanza (Fruta (manzana, pera, durazno)) \n\t3 - Abastecedora La Union (Sal, clavo, tomillo, mejorana) \n\t4 - Salsas Donia Mary (Salsa verde, roja, mole rojo) \n\t5 - Verduras Max (Verduras (tomate, cebolla, chile)) \n\t6 - Abastecedora Don Lupe (Verduras (lechuga, apio, pimiento)) \n")
		if opcion == "1":
			a = BodegaDonJulio()
			a .captura()
			for i in self.__lista:
				if a.id == i.id:
					print("\nError identificador existe")
					break
			else:
				self.__lista.append(a)
		elif opcion == "2":
			b = AlmacenLaEsperanza()
			b.captura()
			for i in self.__lista:
				if b.id == i.id:
					print("\nError identificador existe")
					break
			else:
				self.__lista.append(b)
        elif opcion == "3":
			c = AbastecedoraLaUnion()
			c.captura()
			for i in self.__lista:
				if c.id == i.id:
					print("\nError identificador existe")
					break
			else:
				self.__lista.append(c)
        elif opcion == "4":
			d = SalsasDoniaMary()
			d.captura()
			for i in self.__lista:
				if d.id == i.id:
					print("\nError identificador existe")
					break
			else:
				self.__lista.append(d)               
        elif opcion == "5":
			e = VerdurasMax()
			e.captura()
			for i in self.__lista:
				if e.id == i.id:
					print("\nError identificador existe")
					break
			else:
				self.__lista.append(e)
        elif opcion == "6":
			f = AbastecedoraDonLupe()
			f.captura()
			for i in self.__lista:
				if f.id == i.id:
					print("\nError identificador existe")
					break
			else:
				self.__lista.append(f)



	def f2(self):
		#Bajas de productos
		print("")
		id = input("\nIdentificador a borrar?: ")
		for i in self.__lista:
			if id == i.id:
				print("\nIdentificador borrado")
				print(i.identificador())
				self.__lista.remove(i)
		
	def f3(self):
		#Cambios 
		print("")
		id = input("\nIdentificador a cambiar?: ")
		for i in self.__lista:
			if id == i.id:
				i.captura()
		else:
			print("\nIdentificador no encontrado")
		
	def f4(self):
		#Visualizar
		#print("Visualiza la lista de articulos desde la lista")
		#print(self.__lista) # Visualiza el objeto lista
		print("\nVisualiza la lista de articulos")
		for i in self.__lista:
			#i.visualizar()
			#i.visualizaAtributosJeraquia()
			print(i)

	def f9(self):
		#Salir
		self.__msw = 0
		for reg in self.__lista:
			self.__db[reg.id] = reg
		self.__db.close()
		
	def otro(self):
		#En caso de no ser alguna de las opciones definidas 
		print ("")
		input("\nNo has pulsado ninguna opcion correcta...\npulsa una tecla para continuar ")



#Prueba de las clases
if __name__ == '__main__':
	a = Prueba()
	a.menu()
