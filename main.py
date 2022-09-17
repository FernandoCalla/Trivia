import random
import time

iniciar_trivia = True

  
#colores
  
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

while iniciar_trivia == True:
  print("Bienvenido a mi trivia sobre futbol")
  print("Pondremos a prueba tus conocimientos")
  #variable que almacena el nombre
  nombre = input("Ingresa tu nombre: ")
  
  #variable que almacena el puntaje
  puntaje = random.randint(0, 10)
  
  print(BLUE,
      "\n Hola", nombre,
      "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n",RESET
  )
  time.sleep(1)
  print(YELLOW,
      "\n Recuerda que cada pregunta correcta suma una cantidad aleatoria de puntos y cada incorrecta resta 5 puntos, suerte. Si adivinas la respuesta secreta obtendras puntos extra:\n",RESET
  )
  time.sleep(1)
  print(CYAN,"Puntaje inicial: ", puntaje,RESET,"\n")
  time.sleep(1)
  for i in range (5,0,-1):
    print("La trivia comienza en ", i, "."*i ,"\n")
    time.sleep(1)
    
  #Pregunta 1
    
  print(MAGENTA,"En que pais se realizara este mundial?",RESET)
  print("a) China")
  print("b) Brasil")
  print("c) Rusia")
  print("d) Qatar")
  #Validacion de la respuesta de la pregunta 1
  respuesta1 = input("Ingresa la letra de la respuesta correcta: ")
  print("Cargando...\n")
  time.sleep(2)
  while respuesta1 not in ("a", "b", "c", "d", "g"):
      respuesta1 = input(
          "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if (respuesta1 == "d"):
      print(GREEN,"Correcto, el mundial se desarrollara en Qatar.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      numeroRandom= random.randint(0, 10)
      puntaje += numeroRandom
      print(CYAN,"Se le agregó", numeroRandom, "puntos.",RESET,"\n")
  elif (respuesta1 == "g"):      
      puntaje += 15
      print(YELLOW,"Encontraste la respuesta secreta. +15 puntos\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
  else:      
      print(RED,"No , el mundial se desarrollara en Qatar.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET) 
      puntaje -= 5
      print(CYAN,"Se le restó 5 puntos.",RESET,"\n")
  
  print(CYAN,"Puntaje actual: ", puntaje,RESET,"\n")
  
  #Pregunta 2
  
  print(MAGENTA,"Quien ganó el mundial Rusia 2018?",RESET)
  print("a) Francia")
  print("b) Brasil")
  print("c) Rusia")
  print("d) Argentina")
  #Validacion de la respuesta de la pregunta 2
  respuesta2 = input("Ingresa la letra de la respuesta correcta: ")
  print("Cargando...\n")
  time.sleep(2)
  while respuesta2 not in ("a", "b", "c", "d", "f"):
      respuesta2 = input(
          "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")    
  if (respuesta2 == "a"):
      print(GREEN,"Correcto.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      numeroRandom= random.randint(0, 10)
      puntaje += numeroRandom
      print(CYAN,"Se le agregó", numeroRandom, "puntos.",RESET,"\n")  
  elif (respuesta2 == "f"):      
      print(YELLOW,"Encontraste la respuesta secreta +15 puntos.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      puntaje += 15
  else:      
      print(RED,"No , el mundial lo ganó Francia.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      puntaje -= 5
      print(CYAN,"Se le restó 5 puntos.",RESET,"\n")
  
  print(CYAN,"Puntaje actual: ", puntaje,RESET,"\n")
  
  #Pregunta 3
  
  print(MAGENTA,"Perú clasifico al mundial de Qatar del 2022?",RESET)
  print("a) Si")
  print("b) No")
  #Validacion de la respuesta de la pregunta 3
  respuesta3 = input("Ingresa la letra de la respuesta correcta: ")
  print("Cargando...\n")
  time.sleep(2)
  while respuesta3 not in ("a", "b", "p"):
      respuesta3 = input(
          "Debes responder a, b. Ingresa nuevamente tu respuesta: ")
  if (respuesta3 == "b"):
      print(GREEN,"Correcto, Perú no clasifico al mundial de Qatar.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      numeroRandom= random.randint(0, 10)
      puntaje += numeroRandom
      print(CYAN,"Se le agregó", numeroRandom, "puntos.",RESET,"\n")
  elif (respuesta3 == "p"):
      print(YELLOW,"Encontraste la respuesta secreta +15 puntos.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      puntaje += 15
  else:
      print(RED,"No , Perú no clasifico al mundial de Qatar.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      puntaje -= 5
      print(CYAN,"Se le restó 5 puntos.",RESET,"\n")
  print(CYAN,"Puntaje actual: ", puntaje,RESET,"\n")
  
  #Pregunta 4
  
  print(MAGENTA,"En que año se realizó el primer mundial de futbol?",RESET)
  print("a) 1920")
  print("b) 1930")
  print("c) 1960")
  print("d) 2000")
  #Validacion de la respuesta de la pregunta 4
  respuesta4 = input("Ingresa la letra de la respuesta correcta: ")
  print("Cargando...\n")
  time.sleep(2)
  while respuesta4 not in ("a", "b", "c", "d", "q"):
      respuesta4 = input(
          "Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta: ")
  if (respuesta4 == "b"):
      print(GREEN,"Correcto.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      if(puntaje>0):
        puntaje = puntaje*2
      else:
        puntaje+=60
      print(CYAN,"Se duplicó sus puntos si su puntaje era mayor a 0, si era negativo se le sumaron 60 puntos.",RESET,"\n")
  elif (respuesta4 == "q"):
      print(YELLOW,"Encontraste la respuesta secreta + 15 puntos.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      puntaje += 15
  elif(respuesta4 == "a"):
      print(RED,"No , fue en 1930.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      puntaje += 5
      print(CYAN,"Se le aumento 5 puntos.",RESET,"\n")
  elif(respuesta4 == "c"):
      print(RED,"No , fue en 1930.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      puntaje -= 5
      print(CYAN,"Se le restó 5 puntos.",RESET,"\n")
  elif(respuesta4 == "d"):
      #print("Puntaje anterior",puntaje,"\n")
      print(RED,"No , fue en 1930.\n",RESET)
      print("Cargando puntaje...\n")
      time.sleep(3)
      print(CYAN,"Puntaje anterior",puntaje,"\n",RESET)
      puntaje = puntaje/2
      print(CYAN,"Se le dividio a la mitad.",RESET,"\n")
  print(CYAN,"Puntaje actual: ", puntaje,RESET,"\n")
  print("Gracias por participar", nombre,"\n")
  print(CYAN,"Tu puntaje final es: ", puntaje,RESET,"\n")
  print("Aqui no termina , ingresa un numero entre 1 y 10 , si aciertas el 3er numero aleatorio que salga tu puntaje se suma mas 50.")
  numero=int(input("Ingresa numero: "))
  while numero <1 or numero>10:
      numero = int(input(
          "Debes responder un numero entre 1 y 10. Ingresa nuevamente tu respuesta: "))
  for i in range(0,3):
    random1=random.randint(1, 10)
    print("Numero",i+1,"es",random1,"\n")
    if(i==2):
      if(numero==random1):
        puntaje+=50
        print(GREEN,"Suertudoooo.\n",RESET)
      else:
        print(RED,"No adivinaste.\n",RESET)
  
  print(CYAN,"Tu puntaje final es: ", puntaje,RESET,"\n")
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si": 
   print("\nEspero ",nombre," que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False 
        
