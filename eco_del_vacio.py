print("\n------------ ECO DEL VACIO ------------\n")

print("Despiertas con un zumbido metálico en tus oídos. Estás en una sala tenuemente iluminada, con paredes de un material liso y oscuro que no reconoces. No recuerdas cómo llegaste aquí. Frente a ti, hay una consola central con un PANEL brillante y, sobre una mesa auxiliar, reposa un extraño DISPOSITIVO esférico.\n")


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
            if decision1_2_1 == "DISPARAR" or decision1_2_1 == "1" or decision1_2_1 == "DISPARAR A LA CONSOLA":
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
                            print("-------------------- FINAL A (EL ESPIA) -------------------")
                        else:
                            print("Introduce una opcion valida")
                    elif decision1_2_3 == "ABAJO":
                        print("\nEl conducto termina abruptamente en una sala de carga. Ves varias cápsulas de escape. ¡Es tu oportunidad! Pero también ves a otro humano prisionero a punto de ser llevado por un guardia.\n")
                        decision1_2_3_1 = input("¿Decides CORRER hacia una cápsula para salvarte, o intentas RESCATAR al otro prisionero?: ").upper()
                        if decision1_2_3_1 == "CORRER":
                            print("\nEscapas solo, pero siempre te preguntarás qué fue del otro.\n")
                            print("----- Final C (El Solitario) -----\n")
                        elif decision1_2_3_1 == "RESCATAR":
                            print("\nEl rescate es peligroso, pero juntos tienen más posibilidades de sobrevivir y volver a casa.\n")
                            print("----- Final D (El Héroe) -----\n")
                        else:
                            print("Error: Introduce una opcion valida")
                    else:
                        print("Error: Introduce una opcion valida")
                elif decision1_2_2 == "IGNORARLO":
                    print("\nDecides que el conducto es una trampa o demasiado obvio y te apresuras a buscar otra salida en la armería. Pero ya es demasiado tarde. Mientras revisas un estante de armas, la puerta principal se abre de golpe y dos guardias robóticos te apuntan con sus rifles de plasma. No tienes a dónde correr ni tiempo para reaccionar.\n")
                    print("--(Fin del juego. Dudaste un segundo de más y te costó la libertad)--\n")
                else:
                    print("Error: Introduce una opcion valida")        
            elif decision1_2_1 == "ESCONDERTE" or decision1_2_1 == "3":
                print("\nTe agachas detrás de un gran contenedor de armas justo cuando dos guardias robóticos entran. No te ven. Después de escanear la habitación, se van, pero activan un campo de fuerza en la entrada principal. Ves un terminal de seguridad en la pared.\n")      
                decision1_2_1_1 = input("¿Intentas DESACTIVAR el campo de fuerza desde el terminal o BUSCAR un punto débil para destruirlo?: ").upper() 
                if decision1_2_1_1 == "DESACTIVAR":
                    print("\nTe acercas al terminal. La pantalla muestra dos opciones de comando\n")
                    decision1_2_1_2 = input("SOBRECARGAR el emisor o REINICIAR el sistema de seguridad: ").upper()
                    if decision1_2_1_2 == "SOBRECARGAR":
                        print("\nEl campo de fuerza chisporrotea violentamente y explota hacia afuera, derribándote. La salida está despejada, pero el ruido atraerá guardias en segundos.\n")
                        print("\n--(Fin del juego. Creaste una salida, pero a un costo muy alto)--\n")
                    elif decision1_2_1_2 == "REINICIAR":
                        print("\nEl sistema se apaga por completo durante un ciclo de 10 segundos. El campo de fuerza desaparece en silencio. Es tu oportunidad de SALIR de la armería y seguir por el pasillo.\n")
                        print("\n--(Ruta desbloqueada. El sigilo y la inteligencia te abren el camino)--\n")
                    else:
                        print("Introduce una opcion valida")
                elif decision1_2_1_1 == "BUSCAR":
                    print("\nInspeccionas el campo de fuerza y notas que toda la energía se canaliza desde un único conducto en el techo, que está expuesto. Tienes tu rifle de plasma.\n")
                    decision1_2_1_3 = input("Puedes DISPARAR al conducto o IGNORARLO y volver al terminal: ").upper()
                    if decision1_2_1_3 == "DISPARAR":
                        print("\nEl disparo preciso hace que el conducto explote, desactivando el campo de fuerza. Sin embargo, los restos del conducto caen y bloquean la puerta principal. Has abierto una brecha en la pared que da a las bodegas de carga. Es una nueva ruta de escape.\n")
                        print("\n--(Ruta desbloqueada. La destrucción creativa te ha abierto un nuevo camino)--\n")
                    elif decision1_2_1_3 == "IGNORARLO":
                        print("\nTe das cuenta de que cualquier intento de destrucción será demasiado ruidoso. Decides que no es una opción viable y vuelves a examinar el TERMINAL de seguridad.\n")
                        print("\n--(Vuelves a la decisión anterior: DESACTIVAR)--\n")
                    else:
                        print("Introduce una opcion valida")       
            else:
                print("Error: Introduce una opcion valida ('DISPARAR O BUSCAR')")
        elif decision1_2 == "LABORATORIO":
            print("\nEl laboratorio está impecable. En una mesa central, hay una jeringa con un líquido verde brillante. Una pantalla muestra datos biológicos de una criatura desconocida.\n")
            decision1_2_5 = input("Puedes ANALIZAR los datos en la pantalla, IGNORAR todo e irte, o TOMAR la jeringa: ").upper()
            if decision1_2_5 == "ANALIZAR":
                print("\nLa pantalla muestra que el líquido es un potente estimulante neuronal, pero es inestable. De repente, una alarma suena en el pasillo. Los datos te dan una idea\n")
                decision1_2_5_1 = input("puedes usar el estimulante para MEJORAR tus reflejos o para SOBRECARGAR un sistema eléctrico cercano y crear una distracción: ").upper()
                if decision1_2_5_1 == "MEJORAR":
                    print("\nTe inyectas el líquido, tus sentidos se agudizan y escapas por el pasillo a una velocidad increíble.\n")  
                    print("----- Final M (El Aumento) -----")         
                elif decision1_2_5_1 == "SOBRECARGAR":
                    print("\nViertes el líquido en una consola, causando una explosión que te permite escabullirte sin ser visto.\n")
                    print("----- Final N (El Estratega) -----")
                else:
                    print("\nError: Introduce una opcion valida\n")
            elif decision1_2_5 == "IGNORAR":
                print("\nDecides que es demasiado arriesgado y te das la vuelta para salir. Al cruzar la puerta, esta se cierra de golpe detrás de ti, sellando el laboratorio para siempre. Estás de nuevo en el pasillo, pero ahora oyes guardias acercándose. Tu única opción es CORRER.\n")
                print("\nRuta Desbloqueada: La falta de curiosidad te obliga a una huida desesperada por los pasillos de la nave.\n")
            elif decision1_2_5 == "TOMAR":
                print("\nGuardas la jeringa en tu bolsillo. Es fría al tacto. Al salir del laboratorio, te topas con un guardia alienígena solitario.\n")
                decision1_2_5_2 = input("Puedes intentar LUCHAR contra él o INYECTARLE el líquido para ver qué pasa: ").upper()
                if decision1_2_5_2 == "LUCHAR":
                    print("\nTe enfrentas al guardia en un combate incierto.\n")
                    print("----- Final O (El Luchador) -----\n")
                elif decision1_2_5_2 == "INYECTARLE":
                    print("\nLe clavas la jeringa al guardia, que cae convulsionando, dándote tiempo para escapar.\n")
                    print("----- Final P (El Experimentador) -----\n")
                else:
                    print("\nError: Introduce una opcion valida\n")
            else:
                print("\nError: Introduce una opcion valida\n")
    
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
                    print("\nCorres hacia las cápsulas, logrando escapar de la nave por poco.\n")
                    print("----- Final I (El Escape)-----\n")
                else:
                    print("\nError: Introduce una opcion valida\n")
            else:
                print("\nError: Introduce una opcion valida\n")      
        elif decision1_3 == "ESCONDERTE":
            print("\nTe ocultas tras la consola justo cuando dos guardias robóticos entran y vigilan la puerta. No te ven. Desde tu escondite, notas una rejilla de ventilación en el suelo. Es tu única vía de escape.\n")
            decision1_3_2 = input("Puedes intentar ABRIR la rejilla ahora o ESPERAR a que se vayan: ").upper()
            if decision1_3_2 == "ABRIR":
                print("\nLa abres con sigilo y te deslizas dentro. El conducto es oscuro, pero un mapa de mantenimiento en la pared ilumina dos rutas\n")
                decision1_3_2_1 = input("Una hacia el MOTOR y otra hacia las BODEGAS de carga: ").upper()
                if decision1_3_2_1 == "MOTOR":
                    print("\nTe diriges al motor para inutilizar la nave y crear una distracción.\n")
                    print("----- Final K (El Saboteador) -----")
                elif decision1_3_2_1 == "BODEGAS":
                    print("\nVas a las bodegas, esperando encontrar una nave de carga en la que puedas esconderte para escapar.\n")
                    print("----- Final L (El Polizón) -----")
                else:
                    print("Error: Introduce un codigo valido")
            elif decision1_3_2 == "ESPERAR":
                print("\nEsperas varios minutos, pero los guardias no se mueven. De repente, uno de ellos gira y realiza un escaneo térmico de la sala, detectando tu calor corporal. No tienes a dónde huir.\n")
                print("--(Fin del juego. La paciencia no siempre es una virtud)--\n")
            else:
                print("Error: Introduce una opcion valida")
    elif decision1_1 == "SOL":
        print("\nLa pantalla muestra un mapa estelar de la galaxia, con una ruta parpadeante que conduce a un sistema desconocido. Te da tres opciones\n")
        decision1_4 = input("DESCARGAR el mapa a tu brazalete, MEMORIZAR la ruta o CERRAR el mapa: ").upper()
        if decision1_4 == "DESCARGAR":
            print("\nConectas tu brazalete y la transferencia de datos comienza. Justo cuando termina, la consola detecta la descarga no autorizada y activa una alarma silenciosa. La puerta se sella, pero ahora tienes el mapa. Ves un conducto de ventilación en el suelo. Es tu única salida.\n")
            print("--Ruta Desbloqueada: Tienes la información clave para volver a casa, pero ahora debes escapar de una nave que te busca activamente.--\n")
        elif decision1_4 == "MEMORIZAR":
            print("\nTe concentras en la pantalla, intentando grabar cada coordenada y cada giro de la ruta en tu mente. Mientras lo haces, las luces de la sala se apagan de golpe, dejándote en total oscuridad. La pantalla se ha ido. ¿Crees recordar la ruta?\n")
            decision1_4_1 = input("Puedes CONFIAR en tu memoria y buscar una salida o ESPERAR a que vuelva la luz: ").upper()
            if decision1_4_1 == "CONFIAR":
                print("\nSi confías en tu memoria, tu escape dependerá de qué tan bien recuerdes el camino.\n")
                print("----- Final Q (El Navegante Incierto) -----\n")
            elif decision1_4_1 == "ESPERAR":
                print("Si esperas, los guardias llegan antes de que la energía se restablezca.\n")
                print("----- Final R (La Presa Paciente) -----")
            else:
                print("Error: Introduce una opcion valida")
        elif decision1_4 == "CERRRAR":
            print("\nDecides que la información es un riesgo innecesario y cierras el mapa. En ese instante, la puerta detrás de ti se abre, revelando a un ser alienígena alto y delgado que te observa con curiosidad, no con hostilidad.\n")
            decision1_4_2 = input("Te hace un gesto para que lo SIGAS o te quedes y ESPERES: ").upper()
            if decision1_4_2 == "SEGUIR" or decision1_4_2 == "SIGAS":
                print("\nSi lo sigues, aceptas un destino desconocido de la mano de tu captor.\n")
                print("----- Final S (El Invitado) -----")
            elif decision1_4_2 == "ESPERAR" or decision1_4_2 == "ESPERES":
                print("\nSi esperas, el alienígena se encoge de hombros y vuelve a sellar la puerta, dejándote encerrado.\n")
                print("----- Final T (El Prisionero) -----")
            else:
                print("Error: Introduce una opcion valida")
        else:
            print("Error: Introduce una opcion valida")
    else:
        print("Error: Introduce una opcion valida")
elif decision_1 == "DISPOSITIVO" or decision_1 == "EL DISPOSITIVO":
    print("\nTomas la esfera metálica. Es fría al tacto. Al sostenerla, proyecta un holograma de un ser alienígena de aspecto pacífico que parece estar pidiendo ayuda en un idioma desconocido. De repente, el dispositivo te da dos opciones en tu propio idioma: \n")
    decision_1_2 = input("RESPONDER al llamado o APAGAR el holograma o ANALIZAR el dispositivo: ").upper()
    if decision_1_2 == "RESPONDER":
        print("\nSientes una conexión mental con el ser holográfico. Te inunda una sensación de gratitud y te muestra tres imágenes clave para que elijas una:\n")
        decision_1_2_1 = input("un CRISTAL de energía, las coordenadas de una NEBULOSA o la imagen de un guerrero ENEMIGO: ").upper()
        if decision_1_2_1 == "CRISTAL":
            print("\nSi eliges el CRISTAL, te muestra cómo usarlo para sobrecargar el motor de la nave y provocar un escape masivo.\n")
            print("----- Final U (El Ingeniero) -----")
        elif decision_1_2_1 == "NEBULOSA":
            print("\nSi eliges la NEBULOSA, te revela una ruta de escape segura a través de ella, donde las naves más grandes no pueden seguirte.\n")
            print("----- Final V (El Piloto) -----")
        elif decision_1_2_1 == "ENEMIGO":
            print("\nSi eliges al ENEMIGO, te muestra un punto débil en su armadura, dándote una ventaja crucial si tienes que luchar.\n")
            print("----- Final Y (El Táctico) -----\n")
        else:
            print("Error: Introduce una opcion valida")
    elif decision_1_2 == "APAGAR":
        print("\nEl holograma se desvanece y la esfera emite un fuerte pitido que alerta a los guardias. Escuchas pasos metálicos acercándose rápidamente. Debes actuar ya.\n")
        decision_1_2_2 = input("Puedes LANZAR el dispositivo lejos, ESCONDERTE con él o intentar MODIFICARLO rápidamente.").upper()
        if decision_1_2_2 == "LANZAR":
            print("\nLanzas la esfera al otro lado de la sala. Los guardias entran y van a investigar el objeto, dándote una oportunidad de oro para escabullirte por la puerta.\n")
            print("----- Final W (La Distracción) -----")
        elif decision_1_2_2 == "ESCONDERTE":
            print("\nTe escondes, pero los guardias entran con escáneres avanzados que detectan el dispositivo y a ti casi al instante. No hay escapatoria.\n")
            print("----- Final X (La Rata Acorralada) -----")
        elif decision_1_2_2 == "MODIFICARLO":
            print("\nManipulas la esfera justo cuando entran los guardias, haciendo que emita un pulso sónico que los aturde y te permite escapar.\n")
            print("----- Final Z (El Improvisador) ----- ")
        else:
            print("Error: Introduce una opcion valida")
    elif decision_1_2 == "ANALIZAR":
        print("\nIgnoras el holograma y examinas la esfera. Descubres una pequeña fisura que parece ser un panel de acceso. El holograma parpadea, como si esperara tu decisión.")
        decision_1_2_3 = input("Puedes intentar ABRIR el panel, DEJARLO y responder al holograma, o GOLPEARLO contra la mesa para ver qué pasa: ").upper()
        if decision_1_2_3 == "ABRIR":
            print("\nSi eliges ABRIR, revelas una fuente de energía que podrías usar a tu favor.\n")
            print("----- Ruta Desbloqueada -----\n")
        elif decision_1_2_3 == "DEJARLO":
            print("\nSi decides DEJARLO, puedes volver a RESPONDER o APAGAR.\n")
            print("----- Vuelves a la decisión anterior -----\n")
        elif decision_1_2_3 == "GOLPEARLO":
            print("\nSi lo GOLPEAS, el dispositivo explota con la fuerza de una granada. Un error fatal.\n")
            print("----- Fin del Juego -----")
        else:
            print("Error: Introduce una opcion valida")
    else:
        print("Error: Introduce una opcion valida")


