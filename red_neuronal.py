import random

'''
Red Neuronal Supervisada:
	- Supervisamos a la red en su aprendizaje
	- Indicandole las respuestas correctas cuando este falla para su aprendizaje
'''
class red_neuronal_PerceptronSimple_AND_OR():
	# Red neuronal de discriminacion lineal, discrimina por regiones
		# And - Or 
	def __init__( self ):
		self.nodos_entrada = []
		self.nodos_salida = []

	def define_nodos_capa_entrada( self , cant_nodos ):
		return [ nodo_Neurona() for x in range(cant_nodos) ]

	def define_nodos_capa_salida(self , cant_nodos ):
		return [ nodo_Neurona() for x in range(cant_nodos) ]

	def define_nodos_capa_oculta(self , cant_nodos ):
		return [ nodo_Neurona() for x in range(cant_nodos) ]
	
	def uniendo_capas( self , capa_nodos_entrada , capa_nodos_salida ):
		for obj_nodo_salida in capa_nodos_salida:
			for obj_nodo_entrada in capa_nodos_entrada:
				obj_nodo_salida.add_nodos_entrada( obj_nodo_entrada , random.random() )

	def entrenamiento_red( self , lista_datos ):
		list_pos_tomadas = []
		while len(list_pos_tomadas) != len(lista_datos):
			# Tomamos un dato aleatorio de la lista ------------->>>>>>>>>
			pos_dato = random.randint( 0 , len(lista_datos)-1 )
			while pos_dato in list_pos_tomadas:
				pos_dato = random.randint( 0 , len(lista_datos)-1 )

			list_pos_tomadas.append( pos_dato ) #LLevamos registro de los datos ya seleccionados
			dato = lista_datos[pos_dato]
			# -------------------------------------->>>>>>>>>>

			# Ingresamos los valores de entrada a los nodos ->
			self.nodos_entrada[0].peso_salida = dato["Entrada"][0] # 1
			self.nodos_entrada[1].peso_salida = dato["Entrada"][1] # 0
			# -------------------------------------->>>>>>>>>>

			# Calculamos el peso de salida --------->>>>>>>>>>
			self.nodos_salida[0].funcion_peso() #Calcula la salida de la neurona salida
			# -------------------------------------->>>>>>>>>>

			cont_salida = 0
			while self.nodos_salida[0].peso_salida != dato["Salida"][0] and cont_salida != 100: #Mientras la salida neuronal no coincida con salida correcta
				
				self.nodos_salida[0].funcion_recalculo_pesos_sinapticos_neurona( dato["Salida"][0] ) #Recalculamos los pesos de la neurona indicando el correcto
				self.nodos_salida[0].funcion_peso() #Calculamos la salida con los pesos modificados

				if self.nodos_salida[0].peso_salida == dato["Salida"][0]:
					list_pos_tomadas = [ pos_dato ]

			if cont_salida == 100:
				print( "Salida por Contador_Salida; fallo al recalculo de pesos sinapticos" )
				return None

	def testeo( self , lista_datos ):
		list_pos_tomadas = []
		for x in range( len(lista_datos) ):
	
			# Tomamos un dato aleatorio ------------->>>>>>>>>
			pos_dato = random.randint( 0 , len(lista_datos)-1 )
			while pos_dato in list_pos_tomadas:
				pos_dato = random.randint( 0 , len(lista_datos)-1 )

			list_pos_tomadas.append( pos_dato )
			dato = lista_datos[pos_dato]
			# -------------------------------------->>>>>>>>>>

			# Ingresamos los valores de entrada a los nodos ->
			self.nodos_entrada[0].peso_salida = dato["Entrada"][0] # 1
			self.nodos_entrada[1].peso_salida = dato["Entrada"][1] # 0
			# -------------------------------------->>>>>>>>>>

			self.nodos_salida[0].funcion_peso() #Calcula la salida de la neurona
			print( "Entrada: ", dato["Entrada"] ," - Salida Neuronal: ", self.nodos_salida[0].peso_salida , '- Salida_Correcta: ', dato["Salida"]  )

		print( "Pesos Sinapticos Red --------------->>>>>>>>>>" )
		print( self.nodos_salida[0].nodos_entrada[0]["W"] , self.nodos_salida[0].nodos_entrada[1]["W"] )
		print( "------------------------------------>>>>>>>>>>" )

	def red_neuronal( self , lista_datos ):
		self.nodos_entrada = self.define_nodos_capa_entrada( 2 ) # 1-0 ; 0-1 ; siempre son 2 entradas
		self.nodos_salida = self.define_nodos_capa_salida( 1 )
		self.uniendo_capas( self.nodos_entrada , self.nodos_salida ) #( entrada , salida )
		self.entrenamiento_red( lista_datos )
		print("Proceso de Entrenamiento Terminado ---->>>")
		self.testeo( lista_datos )

class red_neuronal_PerceptronSimple_XOR():
	
	def __init__( self ):
		self.nodos_entrada = []
		self.nodos_capa_oculta = []
		self.nodos_salida = []
	
	def define_nodos_capa( self , cant_nodos ):
		return [ nodo_Neurona() for x in range(cant_nodos) ]

	def uniendo_capas( self , capa_nodos_entrada , capa_nodos_salida ):
		for obj_nodo_salida in capa_nodos_salida:
			for obj_nodo_entrada in capa_nodos_entrada:
				obj_nodo_salida.add_nodos_entrada( obj_nodo_entrada , random.random() )
	
	def entrenamiento_red( self , lista_datos ):
		list_pos_tomadas = []
		while len(list_pos_tomadas) != len(lista_datos):
			# Tomamos un dato aleatorio de la lista ------------->>>>>>>>>
			pos_dato = random.randint( 0 , len(lista_datos)-1 )
			while pos_dato in list_pos_tomadas:
				pos_dato = random.randint( 0 , len(lista_datos)-1 )

			list_pos_tomadas.append( pos_dato ) #LLevamos registro de los datos ya seleccionados
			dato = lista_datos[pos_dato]
			# -------------------------------------->>>>>>>>>>

			# Ingresamos los valores de entrada a los nodos ->
			self.nodos_entrada[0].peso_salida = dato["Entrada"][0] # 1
			self.nodos_entrada[1].peso_salida = dato["Entrada"][1] # 0
			# -------------------------------------->>>>>>>>>>

			# Calculamos el peso de salida --------->>>>>>>>>>
			self.nodos_salida[0].funcion_peso() #Calcula la salida de la neurona salida
			# -------------------------------------->>>>>>>>>>

			cont_salida = 0
			while self.nodos_salida[0].peso_salida != dato["Salida"][0] and cont_salida != 100: #Mientras la salida neuronal no coincida con salida correcta
				
				self.nodos_salida[0].funcion_recalculo_pesos_sinapticos_neurona( dato["Salida"][0] ) #Recalculamos los pesos de la neurona indicando el correcto
				self.nodos_salida[0].funcion_peso() #Calculamos la salida con los pesos modificados

				if self.nodos_salida[0].peso_salida == dato["Salida"][0]:
					list_pos_tomadas = [ pos_dato ]

			if cont_salida == 100:
				print( "Salida por Contador_Salida; fallo al recalculo de pesos sinapticos" )
				return None

	def red_neuronal( self , lista_datos ):
		self.nodos_entrada = self.define_nodos_capa(2)
		self.nodos_capa_oculta = self.define_nodos_capa(1)
		self.nodos_salida = self.define_nodos_capa(1)

		self.uniendo_capas( self.nodos_entrada , self.nodos_capa_oculta )
		self.uniendo_capas( self.nodos_capa_oculta , self.nodos_salida )

		self.entrenamiento_red( lista_datos )



class nodo_Neurona():

	def __init__( self ):
		self.nodos_entrada = []
		self.peso_salida = 0.001 #El valor es muy cercano a 0 pero no 0
		self.umbral = random.randint( 2,5 ) #El humbral en la funcion escalon toma mucha importancia H( (w1*x1 + w2*x2) - umbral )

	def add_nodos_entrada( self , obj_nodo , peso_sinaptico ):
		# W = peso sinaptico
		# obj_nodo = referencia al nodo
		self.nodos_entrada.append( { 'obj_nodo':obj_nodo , 'W':peso_sinaptico } ) 

	def funcion_peso( self ):
		peso_salida_nodo = 0
		for nodo in self.nodos_entrada:
			peso_salida_nodo += self.funcion_sinaptica_peso( nodo['obj_nodo'].peso_salida , nodo['W'] )
		peso_salida_nodo = (peso_salida_nodo - self.umbral)
		
		self.peso_salida = self.funcion_de_activacion_Escalon( peso_salida_nodo )
	
	def funcion_sinaptica_peso( self , peso_entrada , Wi ):
		return peso_entrada * Wi

	# --------------------->>>
	# Funciones de activacion
	# --------------------->>>
	def funcion_de_activacion_Escalon( self , peso ):
		if peso>=0:
			return 1
		else: #peso < 0
			return 0
		#return peso #La funcion de activacion es la identidad
	
	def funcion_de_activacion_Identidad( self , peso ):
		return peso #La funcion de activacion es la identidad
	# --------------------->>>
	# --------------------->>>

	def funcion_salida( self , peso ):
		return peso #La funcion de salida es la identidad

	def get_neuronas_de_entradas( self ):
		for nodo in self.nodos_entrada:
			print( nodo['obj_nodo'].peso_salida )
	
	def funcion_recalculo_pesos_sinapticos_neurona( self , salida_verdadera ):
		e = 0.5 #ritmo de aprendizaje
		for nodo in self.nodos_entrada:
			dif_W = salida_verdadera * nodo['obj_nodo'].peso_salida   
			nodo['W'] = nodo['W'] + dif_W

#Redes Neuronales Supervisadas
#Datos entrenamiento ------------>>>>
Lista_Datos = [ 
		{'Entrada':[0,0] , "Salida":[0]},
		{'Entrada':[0,1] , "Salida":[1]},
		{'Entrada':[1,0] , "Salida":[1]},
		{'Entrada':[1,1] , "Salida":[1]}
	]
#-------------------------------->>>>

'''
red_And = red_neuronal_PerceptronSimple_AND_OR()
red_And.red_neuronal( Lista_Datos )
'''