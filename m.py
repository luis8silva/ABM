#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ejemplo de Clase de Altas, Bajas y Cambios y mas
# Autores: J. Luis Silva, Diego Color, Pedro Zermeño
# Version 1.0

from __future__ import print_function
import sys
if sys.version[0] == '2': input = raw_input 

import os
import pickle
import t
 
# Lista para almacenar los objetos
lista = []

def menu():
	#Control del menu
	#os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print("\nSelecciona una opcion")
	print("\t1 - Altas")
	print("\t2 - Bajas")
	print("\t3 - Cambios")
	print("\t4 - Visualizar")
	print("\t5 - Grabar")
	print("\t6 - Leer")
	print("\t0 - salir")

while True:
	# Mostramos el menu
	menu()
	# solicituamos una opcion al usuario
	opcionMenu = input("\nInserta un numero >> ")
	if opcionMenu=="1":
		print("")
		opcion = input("\nDeseas dar de alta productos de:\n\t1 - Bodega Don Julio (Fruta (piña, melon, sandia)) \n\t2 - Almacen La Esperanza (Fruta (manzana, pera, durazno)) \n\t3 - Abastecedora La Union (Sal, clavo, tomillo, mejorana) \n\t4 - Salsas Donia Mary (Salsa verde, roja, mole rojo) \n\t5 - Verduras Max (Verduras (tomate, cebolla, chile)) \n\t6 - Abastecedora Don Lupe (Verduras (lechuga, apio, pimiento)) \n")
		if opcion == "1":
			a = t.BodegaDonJulio()
			a .captura()
			for i in lista:
				if a.id == i.id:
					print("\nIdentificador existe")
					break
			else:
				lista.append(a)
		elif opcion == "2":
			b = t.AlmacenLaEsperanza()
			b.captura()
			for i in lista:
				if b.id == i.id:
					print("\nIdentificador existe")
    				break
			else:
				lista.append(b)
        elif opcion == "3":
			c = t.AbastecedoraLaUnion()
			c.captura()
			for i in lista:
				if c.id == i.id:
					print("\nIdentificador existe")
    				break
			else:
				lista.append(c)
        elif opcion == "4":
			d = t.SalsasDoniaMary()
			d.captura()
			for i in lista:
				if d.id == i.id:
					print("\nIdentificador existe")
    				break
			else:
				lista.append(d)
        elif opcion == "5":
			e = t.VerdurasMax()
		    e.captura()
			for i in lista:
				if e.id == i.id:
					print("\nIdentificador existe")
    				break
			else:
				lista.append(e)                        
        elif opcion == "6":
			f = t.AbastecedoraDonLupe()
			f.captura()
			for i in lista:
				if f.id == i.id:
					print("\nIdentificador existe")
    				break
			else:
				lista.append(f)


			
	elif opcionMenu=="2":
		print ("")
		id = input("\nIdentificador a borrar?")
		for i in lista:
			if id == i.id:
				print("\nIdentificador borrado")
				print(i.id)
				lista.remove(i)

	elif opcionMenu=="3":
		print("")
		id = input("\nIdentificador a cambiar?: ")
		for i in lista:
			if id == i.id:
				i.captura()
		else:
			print("\nIdentificador no encontrado")

	elif opcionMenu=="4":
		print("")
		for i in lista:
			print(i)
			
	elif opcionMenu=="5":
		print("\nGrabando ...")
		with open('sal.dat','wb') as fp:
			pickle.dump(lista,fp)
		
	elif opcionMenu=="6":
		print("\nLeyendo ...")
		if os.path.exists('sal.dat'):
			with open('sal.dat','rb') as fp:
				lista = pickle.load(fp)			
		else:
			print("\nError en la lectura archivo no existe ...")
						
	elif opcionMenu=="0":
		break

	else:
		print ("")
		input("\nNo has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")