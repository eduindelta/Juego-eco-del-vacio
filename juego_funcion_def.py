#----------------------"ECO DEL VACIO"--------------------------

#ESCENA RUTA PANEL

def escena_panel():
    print("\nTe acercas a la consola. La pantalla cobra vida y muestra tres símbolos alienígenas:\n")
    decision = input("Una ESTRELLA de ocho puntas \nUna LUNA fragmentada \nUn SOL negro. \n¿Cuál tocas?: ").upper()
    
    while True:
        if decision == "ESTRELLA":
            escena_estrella()
            break
        elif decision == "LUNA":
            escena_luna()
            break
        elif decision == "SOL":
            escena_sol()
            break
        else:
            print("Error: Introduce una opcion valida (ESTRELLA, LUNA o SOL)")
            
def escena_estrella():
    print("\nUna puerta a tu izquierda se desliza silenciosamente, revelando dos caminos: \n")
    decision = input("una ARMERÍA llena de armas exóticas y un LABORATORIO médico con equipo avanzado. ¿A dónde te diriges?: ").upper()
    
    while True:
        if decision == "ARMERIA":
            escena_armeria()
            break
        elif decision == "LABORATORIO":
            escena_laboratorio()
            break
        else:
            print("Error: Introduce una opcion valida (ARMERIA O LABORATORIO)")

def escena_armeria():
    print("\nEntras y tomas un rifle de plasma. Es ligero y potente. De repente, escuchas pasos metálicos acercándose rápidamente. Las puertas se están cerrando. \nTienes tres opciones: \n")
    decision = input("1.DISPARAR a la consola de la puerta para mantenerla abierta.\n2.BUSCAR otra salida en la armeria.\n3.ESCONDERTE entre los estantes de armas.\nELIGE: ").upper()
    
    while True:
        if decision == "DISPARAR" or decision == "1":
            print("\nApuntas el rifle de plasma a la consola de la puerta y disparas. El rayo de energía impacta con un estallido cegador, friendo los circuitos. La puerta se detiene a medio cerrar, ¡pero tu disparo también activa las defensas automáticas de la armería! Múltiples torretas bajan del techo y te apuntan. No tienes a dónde correr.\n")
            print("---Fin del juego. Una decisión impulsiva te ha costado la vida---\n")
            break
        elif decision == "BUSCAR":
            escena_armeria_buscar()
            break
        elif decision == "ESCONDERTE":
            escena_armeria_esconderte()
            break
        else:
            print("Error: Introduce una opcion valida (DISPARAR, BUSCAR o ESCONDERTE)")

def escena_armeria_buscar():
    print("\nEncuentras una rejilla de ventilación en el suelo. Parece lo suficientemente grande para que puedas pasar. Los pasos están casi en la puerta.\n")
    decision = input("¿Decides ENTRAR en el conducto o IGNORARLO y buscar otra cosa?: ").upper()
    
    while True:
        if decision == "ENTRAR":
            escena_armeria_buscar_entrar()
            break
        elif decision == "IGNORARLO":
            print("\nDecides que el conducto es una trampa o demasiado obvio y te apresuras a buscar otra salida en la armería. Pero ya es demasiado tarde. Mientras revisas un estante de armas, la puerta principal se abre de golpe y dos guardias robóticos te apuntan con sus rifles de plasma. No tienes a dónde correr ni tiempo para reaccionar.\n")
            print("--(Fin del juego. Dudaste un segundo de más y te costó la libertad)--\n")
            break
        else:
            print("Error: Introduce una opcion valida (ENTRAR O IGNORARLO)")

def escena_armeria_buscar_entrar():
    print("\nAvanzas a gatas por el estrecho y oscuro conducto. El metal es frío y el eco de tus movimientos parece ensordecedor. Llegas a una bifurcación. El conducto de la izquierda parece ir hacia arriba, con un ligero zumbido, mientras que el de la derecha desciende y de él proviene un olor extraño.\n")
    decision = input("---------- ¿ARRIBA O ABAJO? DECIDE ----------").upper()
    
    while True:
        if decision == "ARRIBA":
            escena_armeria_buscar_entrar_arriba()
            break
        elif decision == "ABAJO":
            escena_armeria_buscar_entrar_abajo()
            break
        else:
            print("Error: Introduce una opcion valida (ARRIBA o ABAJO)")

def escena_armeria_buscar_entrar_arriba():
    print("\nLlegas a una rejilla con vistas al puente de mando de la nave. Ves a la tripulación alienígena, y parecen estar en pánico, mirando una enorme nave hostil en la pantalla principal. Tienes una oportunidad única\n")
    decision = input("Puedes OBSERVAR para entender qué pasa, o buscar una forma de SABOTEAR sus sistemas desde aquí: ").upper()
    
    while True:
        if decision == "OBSERVA":
            print("\nHaz descubierto su punto debil y te haz convertido en la clave para la supervivencia de tu gente\n")
            print("-------------------- FINAL A (EL ESPIA) -------------------")
            break
        elif decision == "SABOTEAR":
            print("\nCausas una explosión que te incapacita, dejando tu destino incierto.")
            print("-------------------- FINAL B (EL SABOTEADOR) -------------------")
            break
        else:
            print("Error: Introduce una opcion valida (OBSERVAR O SABOTEAR)")

def escena_armeria_buscar_entrar_abajo():
    print("\nEl conducto termina abruptamente en una sala de carga. Ves varias cápsulas de escape. ¡Es tu oportunidad! Pero también ves a otro humano prisionero a punto de ser llevado por un guardia.\n")
    decision = input("¿Decides CORRER hacia una cápsula para salvarte, o intentas RESCATAR al otro prisionero?: ").upper()
    
    while True:
        if decision == "CORRER":
            print("\nEscapas solo, pero siempre te preguntarás qué fue del otro.\n")
            print("----- Final C (El Solitario) -----\n")
            break
        elif decision == "RESCATAR":
            print("\nEl rescate es peligroso, pero juntos tienen más posibilidades de sobrevivir y volver a casa.\n")
            print("----- Final D (El Héroe) -----\n")
            break
        else:
            print("Error: Introduce una opcion valida (CORRER o RESCATAR)")

def escena_armeria_esconderte():
    print("\nTe agachas detrás de un gran contenedor de armas justo cuando dos guardias robóticos entran. No te ven. Después de escanear la habitación, se van, pero activan un campo de fuerza en la entrada principal. Ves un terminal de seguridad en la pared.\n")
    decision = input("¿Intentas DESACTIVAR el campo de fuerza desde el terminal o BUSCAR un punto débil para destruirlo?: ").upper()
    
    while True:
        if decision == "DESACTIVAR":
            escena_armeria_esconderte_desactivar()
            break
        elif decision == "BUSCAR":
            escena_armeria_esconderte_buscar()
            break
        else:
            print("Error: Introduce una opcion valida (DESACTIVAR o BUSCAR)")

def escena_armeria_esconderte_desactivar():
    print("\nTe acercas al terminal. La pantalla muestra dos opciones de comando\n")
    decision = input("SOBRECARGAR el emisor o REINICIAR el sistema de seguridad: ").upper()
    
    while True:
        if decision == "SOBRECARGAR":
            print("\nEl campo de fuerza chisporrotea violentamente y explota hacia afuera, derribándote. La salida está despejada, pero el ruido atraerá guardias en segundos.\n")
            print("\n--(Fin del juego. Creaste una salida, pero a un costo muy alto)--\n")
            break
        elif decision == "REINICIAR":
            print("\nEl sistema se apaga por completo durante un ciclo de 10 segundos. El campo de fuerza desaparece en silencio. Es tu oportunidad de SALIR de la armería y seguir por el pasillo.\n")
            print("\n--(Ruta desbloqueada. El sigilo y la inteligencia te abren el camino)--\n")
            break
        else:
            print("Error: Introduce una opcion valida (SOBRECARGAR o REINICIAR)")

def escena_armeria_esconderte_buscar():
    pass

def escena_laboratorio():
    pass

def escena_luna():
    pass

def escena_sol():
    pass

# --- ESCENAS DE LA RUTA 'DISPOSITIVO' ---

def escena_dispositivo():
    pass

def start_game():
    print("---------- ECO DEL VACIO ----------")
    print("\nDespiertas con un zumbido metálico en tus oídos. Estás en una sala tenuemente iluminada, con paredes de un material liso y oscuro que no reconoces. No recuerdas cómo llegaste aquí. Frente a ti, hay una consola central con un PANEL brillante y, sobre una mesa auxiliar, reposa un extraño DISPOSITIVO esférico.\n")
    
    while True:
        decision_1 = input("¿Qué quieres investigar primero: el PANEL o el DISPOSITIVO?: ").upper()
        
        if decision_1 == "PANEL":
            escena_panel()
            break # Termina el bucle una vez que la ruta del panel concluye
        elif decision_1 == "DISPOSITIVO":
            escena_dispositivo()
            break
        else:
            print("Error: Introduce una opcion valida (PANEL O DISPOSITIVO)")

# --- INICIO DEL JUEGO ---
start_game()
print("\n------------ GRACIAS POR JUGAR ------------")