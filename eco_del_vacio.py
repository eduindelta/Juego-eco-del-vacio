print("\n------------ ECO DEL VACIO ------------\n")

print("Despiertas con un zumbido metálico en tus oídos. Estás en una sala tenuemente iluminada, con paredes de un material liso y oscuro que no reconoces. No recuerdas cómo llegaste aquí. Frente a ti, hay una consola central con un PANEL brillante y, sobre una mesa auxiliar, reposa un extraño DISPOSITIVO esférico.\n")

print("NIVEL 1: EL DESPERTAR\n")

decision_1 = input("¿Qué quieres investigar primero: el PANEL o el DISPOSITIVO?: ").upper()
if decision_1 == "PANEL" or decision_1 == "EL PANEL":
    print("\nTe acercas a la consola. La pantalla cobra vida y muestra tres símbolos alienígenas:\n")
    decision1_1 = input("Una ESTRELLA de ocho puntas \nUna LUNA fragmentada \nUn SOL negro. \n¿Cuál tocas?: ").upper()
    if decision1_1 == "ESTRELLA" or decision1_1 == "LA ESTRELLA": 
        print("\nUna puerta a tu izquierda se desliza silenciosamente, revelando dos caminos: \n")
        decision1_2 = input("una ARMERÍA llena de armas exóticas y un LABORATORIO médico con equipo avanzado. ¿A dónde te diriges?: ").upper()
        if decision1_2 == "ARMERIA" or decision1_2 == "LA ARMERIA":
            print("\nEntras y tomas un rifle de plasma. Es ligero y potente. De repente, escuchas pasos metálicos acercándose rápidamente. Las puertas se están cerrando. \nTienes tres opciones: \n")
            decision1_2_1 = input("1.DISPARAR a la consola de la puerta para mantenerla abierta.\n2.BUSCAR otra salida en la armeria.\n3.ESCONDERTE entre los estantes de armas.\nELIGE: ").upper()
            if decision1_2_1 == "DISPARA" or decision1_2_1 == "1" or decision1_2_1 == "DISPARAR A LA CONSOLA":
                print("\nApuntas el rifle de plasma a la consola de la puerta y disparas. El rayo de energía impacta con un estallido cegador, friendo los circuitos. La puerta se detiene a medio cerrar, ¡pero tu disparo también activa las defensas automáticas de la armería! Múltiples torretas bajan del techo y te apuntan. No tienes a dónde correr.\n")
                print("---Fin del juego. Una decisión impulsiva te ha costado la vida---\n")
            elif decision1_2_1 == "BUSCAR" or decision1_2_1 == "2" or decision1_2_1 == "BUSCAR OTRA SALIDA":
                print("\nEncuentras una rejilla de ventilación en el suelo. Parece lo suficientemente grande para que puedas pasar. Los pasos están casi en la puerta.\n")
                decision1_2_2 = input("¿Decides ENTRAR en el conducto o IGNORARLO y buscar otra cosa?: ").upper()
                if decision1_2_2 == "ENTRAR" or decision1_2_2 == "ENTRAR EN EL CONDUCTO":
                    print("\nAvanzas a gatas por el estrecho y oscuro conducto. El metal es frío y el eco de tus movimientos parece ensordecedor. Llegas a una bifurcación. El conducto de la izquierda parece ir hacia arriba, con un ligero zumbido, mientras que el de la derecha desciende y de él proviene un olor extraño.\n")
                    decision1_2_3 = input("---------- ¿ARRIBA O ABAJO? DECIDE ----------").upper()
                    if decision1_2_3 == "ARRIBA":
                        print("\nLlegas a una rejilla con vistas al puente de mando de la nave. Ves a la tripulación alienígena, y parecen estar en pánico, mirando una enorme nave hostil en la pantalla principal. Tienes una oportunidad única\n")
                        decision1_2_4 = input("Puedes OBSERVAR para entender qué pasa, o buscar una forma de SABOTEAR sus sistemas desde aquí: ").upper()
                        if decision1_2_4 == "OBSERVAR":
                            print("\nHaz descubierto su punto debil y te haz convertido en la clave para la supervivencia de tu gente\n")
                            print("--------------------FINAL A (EL ESPIA)-------------------")
            elif decision1_2_1 == "ESCONDERTE" or decision1_2_1 == "3":
                print("\nTe agachas detrás de un gran contenedor de armas justo cuando dos guardias robóticos entran. No te ven. Después de escanear la habitación, se van, pero activan un campo de fuerza en la entrada principal. Ves un terminal de seguridad en la pared.\n")      
                decision1_2_1_1 = input("¿Intentas DESACTIVAR el campo de fuerza desde el terminal o BUSCAR un punto débil para destruirlo?").upper() 
                if decision1_2_1_1 == "DESACTIVAR":
                    print("\nTe acercas al terminal. La pantalla muestra dos opciones de comando\n")
                    decision1_2_1_2 = input("SOBRECARGAR el emisor o REINICIAR el sistema de seguridad").upper()
                    if decision1_2_1_2 == "SOBRECARGAR":
                        print("\nEl campo de fuerza chisporrotea violentamente y explota hacia afuera, derribándote. La salida está despejada, pero el ruido atraerá guardias en segundos.\n")
                        print("\n--(Fin del juego. Creaste una salida, pero a un costo muy alto)--\n")
                    elif decision1_2_1_2 == "REINICIAR":
                        print("\nEl sistema se apaga por completo durante un ciclo de 10 segundos. El campo de fuerza desaparece en silencio. Es tu oportunidad de SALIR de la armería y seguir por el pasillo.\n")
                        print("\n--(Ruta desbloqueada. El sigilo y la inteligencia te abren el camino)--\n")
                elif decision1_2_1_1 == "BUSCAR":
                    print("\nInspeccionas el campo de fuerza y notas que toda la energía se canaliza desde un único conducto en el techo, que está expuesto. Tienes tu rifle de plasma.\n")
                    decision1_2_1_3 =
                     
            else:
                print("Error: Introduce una opcion valida ('DISPARAR O BUSCAR')")
    
    elif decision1_1 == "LUNA":
        print("\nLas luces de la sala parpadean y se vuelven rojas. Una alarma resuena. Una voz metálica anuncia 'Intruso detectado'. Tienes que actuar rápido. \n")
        decision1_3 = input("Puedes intentar FORZAR la puerta frente a ti o ESCONDERTE detrás de la consola: ").upper()
        if decision1_3 == "FORZAR":
            print("\nLa puerta no cede, pero tu forcejeo hace que un panel de control cercano eche chispas, revelando un manojo de cables. Es una oportunidad.\n")
            decision1_3_1 = input("Puedes GOLPEAR el panel para provocar un cortocircuito o ARRANCAR los cables directamente: ").upper()
            if decision1_3_1 == "GOLPEAR":
                print("\nEl golpe provoca una sobrecarga masiva. La puerta se abre con un estallido, pero una descarga eléctrica te alcanza, dejándote paralizado en el suelo mientras los guardias se acercan.\n")
                print("--(Fin del juego. La fuerza bruta no siempre es la solución)--\n")
            elif decision1_3_1 == "ARRANCAR":
                print("\nArrancas los cables con toda tu fuerza. Con una lluvia de chispas, la alarma se apaga y la puerta se abre. Frente a ti, un pasillo te da dos opciones claras.\n")
                decision1_3_1_1 = input("correr hacia las CÁPSULAS de escape o subir hacia el PUENTE de mando: ").upper()
                if decision1_3_1_1 == "CAPSULAS": 
                    print
        
        elif decision1_3 == "ESCONDERTE":
            print("\nTe ocultas tras la consola justo cuando dos guardias robóticos entran y vigilan la puerta. No te ven. Desde tu escondite, notas una rejilla de ventilación en el suelo. Es tu única vía de escape.\n")
            decision1_3_2 = input("Puedes intentar ABRIR la rejilla ahora o ESPERAR a que se vayan: ").upper()
            if decision1_3_2 == "ABRIR":
                print("")

elif decision_1 == "DISPOSITIVO" or decision_1 == "EL DISPOSITIVO":
    print("\nTomas la esfera metálica. Es fría al tacto. Al sostenerla, proyecta un holograma de un ser alienígena de aspecto pacífico que parece estar pidiendo ayuda en un idioma desconocido. De repente, el dispositivo te da dos opciones en tu propio idioma: RESPONDER al llamado o APAGAR el holograma.\n")
