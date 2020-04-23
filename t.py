#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ejemplo de Clase de Altas, Bajas y Cambios y mas
# Autores: J. Luis Silva, Diego Color, Pedro Zermeño
# Version 1.0

from __future__ import print_function


class Producto():
	#Definicion de la clase producto
	def __init__(self):
		#Constructor de la clase producto
		self.id = None
		self.nomb = None
		self.precio = None
		self.cant = None
		
	def inicializa(self,id,nomb,precio,cant):
		#Inicializa la clase producto
		self.id = id
		self.nomb = nomb
		self.precio = precio
		self.cant = cant
		
	def captura(self):
		#Captura la clase producto
		self.id = input('ID: ')
		self.nomb = input('Nombre del producto: ')
		self.precio = float(input('Precio: '))
		self.cant = int(input('Cantidad: '))
		
	def visualizar(self):
		#Visualiza la clase producto
		print(self)
		
	def __repr__(self):
		#Visualiza la clase producto
		a = 'ID: {0}\n'.format(self.id)
		a += 'Nombre del producto: {0}\n'.format(self.nomb)
		a += 'Precio: {:,.2f}\n'.format(self.precio)
		a += 'Cantidad: {0}\n'.format(self.cant)
		return a


class BodegaDonJulio(Producto):
	#Definicion de la clase BodegaDonJulio
	def __init__(self):
		#Constructor de la clase BodegaDonJulio
		Producto.__init__(self)
		self.caja = None
		self.camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camiones):
		#Inicializa la clase BodegaDonJulio
		Producto.inicializa(self, id, nomb, precio, cant)
		self.caja = caja
		self.camion = camion
		
	def captura(self):
		#Captura la clase BodegaDonJulio
		Producto.captura(self)
		self.caja = int(input('Cajas: '))
		self.camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase BodegaDonJulio
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.caja)
		a += 'Camiones: {0}\n'.format(self.camion)
		return a


class AlmacenLaEsperanza(Producto):
	#Definicion de la clase AlmacenLaEsperanza
	def __init__(self):
		#Constructor de la clase Televisor
		Producto.__init__(self)
		self.caja = None
		self.camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase AlmacenLaEsperanza
		Producto.inicializa(self, id, nomb, precio, cant)
		self.caja = caja
		self.camion = camion
		
	def captura(self):
		#Captura la clase AlmacenLaEsperanza
		Producto.captura(self)
		self.caja = int(input('Cajas: '))
		self.camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase AlmacenLaEsperanza
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.caja)
		a += 'Camiones: {0}\n'.format(self.camion)
		return a


class AbastecedoraLaUnion(Producto):
	#Definicion de la clase AbastecedoraLaUnion
	def __init__(self):
		#Constructor de la clase AbastecedoraLaUnion
		Producto.__init__(self)
		self.caja = None
		self.camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase AbastecedoraLaUnion
		Producto.inicializa(self, id, nomb, precio, cant)
		self.caja = caja
		self.camion = camion
		
	def captura(self):
		#Captura la clase AbastecedoraLaUnion
		Producto.captura(self)
		self.caja = int(input('Cajas: '))
		self.camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase AbastecedoraLaUnion
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.caja)
		a += 'Camiones: {0}\n'.format(self.camion)
		return a


class SalsasDoniaMary(Producto):
	#Definicion de la clase SalsasDoniaMary
	def __init__(self):
		#Constructor de la clase SalsasDoniaMary
		Producto.__init__(self)
		self.caja = None
		self.camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase SalsasDoniaMary
		Producto.inicializa(self, id, nomb, precio, cant)
		self.caja = caja
		self.camion = camion
		
	def captura(self):
		#Captura la clase SalsasDoniaMary
		Producto.captura(self)
		self.caja = int(input('Cajas: '))
		self.camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase SalsasDoniaMary
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.caja)
		a += 'Camiones: {0}\n'.format(self.camion)
		return a


class VerdurasMax(Producto):
	#Definicion de la clase VerdurasMax
	def __init__(self):
		#Constructor de la clase VerdurasMax
		Producto.__init__(self)
		self.caja = None
		self.camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase VerdurasMax
		Producto.inicializa(self, id, nomb, precio, cant)
		self.caja = caja
		self.camion = camion
		
	def captura(self):
		#Captura la clase VerdurasMax
		Producto.captura(self)
		self.caja = int(input('Cajas: '))
		self.camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase VerdurasMax
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.caja)
		a += 'Camiones: {0}\n'.format(self.camion)
		return a


class AbastecedoraDonLupe(Producto):
	#Definicion de la clase AbastecedoraDonLupe
	def __init__(self):
		#Constructor de la clase AbastecedoraDonLupe
		Producto.__init__(self)
		self.caja = None
		self.camion = None
		
	def inicializa(self, id, nomb, precio, cant, caja, camion):
		#Inicializa la clase AbastecedoraDonLupe
		Producto.inicializa(self, id, nomb, precio, cant)
		self.caja = caja
		self.camion = camion
		
	def captura(self):
		#Captura la clase AbastecedoraDonLupe
		Producto.captura(self)
		self.caja = int(input('Cajas: '))
		self.camion = input('Camiones: ')
		
	def __repr__(self):
		#Visualiza la clase AbastecedoraDonLupe
		a = Producto.__repr__(self)
		a += 'Cajas: {0}\n'.format(self.caja)
		a += 'Camiones: {0}\n'.format(self.camion)
		return a



#Prueba de las clases
if __name__ == '__main__':
	a = BodegaDonJulio()
	a .captura()
	print(a)
	
	b = AlmacenLaEsperanza()
	b.captura()
	print(b)

    c = AbastecedoraLaUnion()
	c.captura()
	print(c)

    d = SalsasDoniaMary()
	d.captura()
	print(d)

    e = VerdurasMax()
	e.captura()
	print(e)

    f = AbastecedoraDonLupe()
	f.captura()
	print(f)


