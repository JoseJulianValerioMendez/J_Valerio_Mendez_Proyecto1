import tkinter
import random
from tkinter import *

"""*********************************************************************
                    Instituto Tecnologico de Costa Rica
                        Ingenieria en Computadores
Lenguaje: Python 3.10.11
Descripción: Ventana principal que redirige a otras funciones
Autor: José Julián Valerio Méndez
Versión: 1.0
Fecha Última Modificación: Abril 20/2023
Entrada: Click del mouse y nombre colocado por el usuario
Restricciones: No presionar WASD y Espacio
Salidas: Redirección a nueva ventana
************************************************************************"""

Screen = tkinter.Tk()
Screen.geometry('1000x700')

class Game:
    def __init__(self): #Crea la ventana principal que nos permitirá realizar una serie de acciones(Nombre y Botones)
        self.BackG = tkinter.PhotoImage(file='Graphics/BackgroundTS.png')
        self.BG = Label(Screen, image=self.BackG)
        self.BG.place(x=0, y=0)
        
        self.Title = Label(Screen, text='Space Shooter', font=('ROG Fonts', 30))
        self.Title.place(x=280, y=20)
        
        self.Name = Label(Screen, text='Enter your name:(Press <ENTER> afterwards)', font=('ROG Fonts', 20), bg='black', fg='white')
        self.Name.place(x=70, y=170)
        self.NameEntry = Entry(Screen, font=('ROG Fonts', 20))
        self.NameEntry.place(x=300, y=220)
        self.NameEntry.bind('<Return>', self.save_name)

        
        self.ButtonStart = Button(Screen, text='Start', font=('ROG Fonts', 22), command=self.button_start, fg='purple')
        self.ButtonStart.pack()
        self.ButtonStart.place(x=425, y=100)
        
        self.ButtonScore = Button(Screen, text='Scoreboard', font=('ROG Fonts', 22), command=self.button_score, fg='blue')
        self.ButtonScore.pack()
        self.ButtonScore.place(x=360, y=350)
        
        self.ButtonAbout= Button(Screen, text='About', font=('ROG Fonts', 22), command=self.button_about, fg='red')
        self.ButtonAbout.pack()
        self.ButtonAbout.place(x=420, y=500)
        
        self.can_shoot = True #Variable que sirve en Shoot
        
        self.projectiles = [] #Lista para projectiles
        
        self.enemies = [] #Lista para enemigos
        self.enemy_projectiles = [] #Lista projectiles enemigos
        
        Screen.bind("<space>", self.shoot)
    
        """*********************************************************************
                        Instituto Tecnologico de Costa Rica
                            Ingenieria en Computadores
    Lenguaje: Python 3.10.11
    Descripción: Guarda el nombre
    Autor: José Julián Valerio Méndez
    Versión: 1.0
    Fecha Última Modificación: Abril 13/2023
    Entrada: nombre colocado por el usuario
    Restricciones: No tiene
    Salidas: Nada
    ************************************************************************"""

    def save_name(self, event): #Guarda el Nombre
        name = self.NameEntry.get()
        print(f'The name entered is: {name}')
    
        """*********************************************************************
                    Instituto Tecnologico de Costa Rica
                        Ingenieria en Computadores
    Lenguaje: Python 3.10.11
    Descripción: Boton que lleva a la sección de información
    Autor: José Julián Valerio Méndez
    Versión: 1.0
    Fecha Última Modificación: Abril 20/2023
    Entrada: Click del mouse
    Restricciones: 
    Salidas: Redirección a nueva ventana
    ************************************************************************"""

    def button_about(self): #Función para el boton "ButtonAbout"
        self.ButtonStart.destroy()
        self.ButtonScore.destroy()
        self.ButtonAbout.destroy()
        self.Title.destroy()
        
        
        self.Title = Label(Screen, text='Information', font=('ROG Fonts', 30))
        self.Title.pack(padx=20, pady=20)

        self.Info = Label(Screen, text='Instituto Tecnologico de Costa Rica', font=('ROG Fonts', 12))
        self.Info.pack()
        self.Info2 = Label(Screen, text='Ingeniería de Computadores: Taller de programación', font=('ROG Fonts', 12))
        self.Info2.pack()
        self.Info2 = Label(Screen, text='Professor: Milton Villegas Lemus', font=('ROG Fonts', 12))
        self.Info2.pack()
        self.Info4 = Label(Screen, text='Created by: José Julián Valerio (2023057544)', font=('ROG Fonts', 12))
        self.Info4.pack()
        self.Info5 = Label(Screen, text='Date and place of creation: April 2023, Costa Rica ', font=('ROG Fonts', 12))
        self.Info5.pack()
        self.Info6 = Label(Screen, text='Program version: Python.3.10', font=('ROG Fonts', 12))
        self.Info6.pack()
        
        
        self.Me_canvas = Canvas(Screen, width=300, height=400)
        self.Me_canvas.pack()
        self.Me = tkinter.PhotoImage(file='Graphics/Me.png')
        self.MePic= self.Me_canvas.create_image(0,0, anchor=NW, image= self.Me)

        self.ButtonBack = Button(Screen, text='Back', font=('ROG Fonts', 22), command=self.__init__, fg='red')
        self.ButtonBack.pack()
        self.ButtonBack.place(x=800, y=600)
        
        """*********************************************************************
                    Instituto Tecnologico de Costa Rica
                        Ingenieria en Computadores
Lenguaje: Python 3.10.11
Descripción: Boton que lleva a la ventana de Puntaje
Autor: José Julián Valerio Méndez
Versión: 1.0
Fecha Última Modificación: Abril 23/2023
Entrada: Click del mouse 
Restricciones: 
Salidas: Redirección a nueva ventana
************************************************************************"""
        
    def button_score(self): #Función del botón "ButtonScore"
        self.ButtonStart.destroy()
        self.ButtonScore.destroy()
        self.ButtonAbout.destroy()
        self.Title.destroy()

        self.ButtonBack = Button(Screen, text='Back', font=('ROG Fonts', 22), command=self.__init__, fg='red')
        self.ButtonBack.pack()
        self.ButtonBack.place(x=800, y=600)
    
    """*********************************************************************
                    Instituto Tecnologico de Costa Rica
                        Ingenieria en Computadores
Lenguaje: Python 3.10.11
Descripción: Boton que lleva a la ventana del juego
Autor: José Julián Valerio Méndez
Versión: 1.0
Fecha Última Modificación: Marzo 30/2023
Entrada: Click del mouse
Restricciones: 
Salidas: Ventana de juego
************************************************************************""" 
        
    def button_start(self): #Empieza el juego
        self.BG.destroy()
        self.Title.destroy()
        self.ButtonStart.destroy()
        self.ButtonScore.destroy()
        self.ButtonAbout.destroy()
        
        self.Ship_canvas = Canvas(Screen, width=1000, height=700, bg= 'black')
        self.Ship_canvas.pack()
        self.ShipImage = tkinter.PhotoImage(file='Graphics/SPV.png')
        self.ShipPic= self.Ship_canvas.create_image(50,320, anchor=NW, image= self.ShipImage)
        self.LivesImage = tkinter.PhotoImage(file='Graphics/Lives.png')
        self.LivesPic= self.Ship_canvas.create_image(30,30, anchor=NW, image= self.LivesImage)

        """**********************************************************
        Instituto Tecnologico de Costa Rica
                        Ingenieria en Computadores
Lenguaje: Python 3.10.11
Descripción: Conjunto de funciones que permite el movimiento de la nave
Autor: José Julián Valerio Méndez
Versión: 1.0
Fecha Última Modificación: Abril 15/2023
Entrada: Teclas WASD y coordenadas de ShipPic
Restricciones: No puede pasar de la mitad de la pantalla
Salidas: Movimiento de la nave
*****************************************************************************"""
        def up(event): #Cuando se apreta W, se mueve hacia arriba
            x=0
            y=-15
            move_ship(x, y)
            
        def down(event): #Cuando se apreta S, se mueve hacia abajo
            x=0
            y=15
            move_ship(x, y) 

        def front(event): #Cuando se apreta D, se mueve hacia la derecha
            x=15
            y=0
            move_ship(x,y)
        
        def back(event): #Cuando se apreta A, se mueve hacia la izquierda
            x=-15
            y=0
            move_ship(x, y)
            
        def move_ship(x, y): #Define las boundaries de la nave
            bbox = self.Ship_canvas.bbox(self.ShipPic)
            if bbox[1] + y < 0:  # Define la boudary de arriba
                y = -bbox[1]
            if bbox[3] + y > self.Ship_canvas.winfo_height():  # Define la boundary de abajo
                y = self.Ship_canvas.winfo_height() - bbox[3]
            if bbox[0] + x < 0:  # Define la boundary izquierda
                x = -bbox[0]
            if bbox[2] + x > self.Ship_canvas.winfo_width() / 2:  # Define la boundary derecha
                x = self.Ship_canvas.winfo_width() / 2 - bbox[2]
            self.Ship_canvas.move(self.ShipPic, x, y)
                    
        Screen.bind('<w>', up)
        Screen.bind('<s>', down)
        Screen.bind('<d>', front)
        Screen.bind('<a>', back)
        
        
        self.create_enemy()

    """**********************************************************
        Instituto Tecnologico de Costa Rica
                        Ingenieria en Computadores
Lenguaje: Python 3.10.11
Descripción: Funcion que crea un enemigo en un lugar "random" de la pantalla
Autor: José Julián Valerio Méndez
Versión: 1.0
Fecha Última Modificación: Abril 15/2023
Entrada: Imagenes y digitos random 
Restricciones: Tiene que aparecer del lado contrario de la nave
Salidas: Enemigo 
*****************************************************************************"""

    def create_enemy(self): #Crea un enemigo con una imagen en un punto al azar de la pantalla dentro de un rango
        enemy_image = tkinter.PhotoImage(file='Graphics/Enemy.png')
        enemy = self.Ship_canvas.create_image(1000, random.randint(0, 700), anchor=tkinter.E, image=enemy_image)
        self.enemies.append(enemy)
        
        Screen.after(7000, self.shoot_enemy, enemy)
        Screen.after(6000, self.create_enemy)
        enemy.pack()

    """**********************************************************  
        Instituto Tecnologico de Costa Rica
                        Ingenieria en Computadores
Lenguaje: Python 3.10.11
Descripción: Conjunto de funciones que crean y disparan un projectil
Autor: José Julián Valerio Méndez
Versión: 1.0
Fecha Última Modificación: Abril 15/2023
Entrada: 6000 ticks que le avisan a la funcion que tiene que disparar
Restricciones: 
Salidas: Projectil del enemigo 
*****************************************************************************"""

    def shoot_enemy(self, enemy): #Detecta cuando pasa x tiempo y crea una imagen de un projectil
        enemy_x, enemy_y, _, _ = self.Ship_canvas.bbox(enemy)
        enemy_projectile_image = tkinter.PhotoImage(file='Graphics/EnemyProjectile.png')
        enemy_projectile = self.Ship_canvas.create_image(enemy_x, enemy_y, anchor=tkinter.E, image=enemy_projectile_image)
        self.enemy_projectiles.append(enemy_projectile)
        self.move_enemyP(enemy_projectile, -10)
        
    def move_enemyP(self, projectile, speed): #Hace que el projectil se mueva hasta que choque con la nave o con el fin de la pantalla
        self.Ship_canvas.move(projectile, speed, 0)
        if self.Ship_canvas.coords(projectile)[0] < 0:
            self.Ship_canvas.delete(projectile)
            self.enemy_projectile = None
        elif self.Ship_canvas.find_overlapping(*self.Ship_canvas.bbox(projectile)):
            self.Ship_canvas.delete(projectile)
            self.enemy_projectiles.remove(projectile)
            self.Ship_canvas.create_text(500, 300, text="Game Over", font=("ROG Fonts", 50), fill="red")
            self.ButtonBack = Button(Screen, text='Back', font=('ROG Fonts', 22), command=self.__init__, fg='red')
            self.Ship_canvas.create_window(200, 200, window=self.ButtonBack)
            self.ButtonBack.pack()
        else:
            Screen.after(50, self.move_enemyP, projectile, speed)

        """**********************************************************
        Instituto Tecnologico de Costa Rica
                        Ingenieria en Computadores
Lenguaje: Python 3.10.11
Descripción: Conjunto de funciones que crea un projectil de la nave
Autor: Originalmente creado por José Julián Valerio y modificado por la herramienta digital ChatGPT para funcionamiento optimo
Versión: 1.0
Fecha Última Modificación: Abril 15/2023
Entrada: Tecla <Espacio>
Restricciones: Tiene que esperarse un tiempo antes de volver a disparar
Salidas: Projectil que se mueve continuamente
*****************************************************************************"""
        
    def shoot(self, event): #Detecta cuando se apreta Espacio y crea una imagen de projectil, ademas detecta si el projectil choca con el enemigo
        if self.can_shoot:
            self.can_shoot = False
            x0, y0, x1, y1 = self.Ship_canvas.bbox(self.ShipPic)
            self.projectile_image = tkinter.PhotoImage(file='Graphics/Projectile.png')
            if self.projectiles:
                self.Ship_canvas.delete(self.projectiles[0])
                self.projectiles.pop(0)
            self.projectile = self.Ship_canvas.create_image(x1, (y0 + y1) / 2, anchor=tkinter.W, image=self.projectile_image)
            self.projectiles.append(self.projectile)
            for enemy in self.enemies:
                if self.Ship_canvas.find_overlapping(*self.Ship_canvas.bbox(enemy)):
                    self.Ship_canvas.delete(enemy)
                    self.enemies.remove(enemy)
                    if self.projectile in self.projectiles:
                        self.can_shoot = True
                        self.projectiles.remove(self.projectile)
                        self.Ship_canvas.delete(self.projectile)
                    break
            else:
                self.move_projectile(self.projectile, 10)  
                self.cooldown()


    def move_projectile(self, projectile, speed): #Permite el movimiento del projectil de la nave
        self.Ship_canvas.move(projectile, speed, 0)
        if self.Ship_canvas.coords(projectile)[0] > 1000:
            if projectile in self.projectiles:
                self.can_shoot = True
                self.projectiles.remove(projectile)
                self.Ship_canvas.delete(projectile)
                
        else:
            Screen.after(50, self.move_projectile, projectile, speed +2)
            self.cooldown()
        """**********************************************************  
        Instituto Tecnologico de Costa Rica
                        Ingenieria en Computadores
Lenguaje: Python 3.10.11
Descripción: Funciones que permiten disparar el projectil despues de x tiempo
Autor: José Julián Valerio Méndez
Versión: 1.0
Fecha Última Modificación: Abril 15/2023
Entrada: Funciones anteriores
Restricciones: El projectil tiene que desaparecer
Salidas: Permite disparar de nuevo
*****************************************************************************"""
    def shoot_ready(self): #Le dice al codigo que la nave está lista para disparar de nuevo
        self.can_shoot = True


    def cooldown(self): #Llama a la función de shoot_ready despues de 1000 ticks
        Screen.after(1000, self.shoot_ready)

    

Game()     
Screen.mainloop()


