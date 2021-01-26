import pygame as pg
import sys, os
import pelota, palito, bloque, settings
import random

class Game:

    def __init__(self):
        # Configuración de la pantalla
        self.settings = settings.Settings()
        self.pantalla = pg.display.set_mode((self.settings.pantalla_width, self.settings.pantalla_heigth))
        pg.display.set_caption("Futuro Arkanoid")
        self.fondo = pg.image.load('imagenes/background.png')

        # Instancias
        self.pelota = pelota.Pelota(400, 300, 2, 2)
        self.palito = palito.Palito(((self.settings.pantalla_width-128)/2), 550)
        self.lista_obj = [self.pelota, self.palito]
        self.lista_bloques = self.__crea_bloques(self.settings.patron_bito)
        self.clock = pg.time.Clock()
        
    def bucle_principal(self):
        game_over = False
        while not game_over:
            dt = self.clock.tick(self.settings.pantalla_FPS)

            self.__eventos()
            if not self.pelota.muriendo:
                self.palito.moving_stick()
            game_over = self.pelota.actualizar(dt, self.palito, self.lista_bloques)         
            self.__pinta_pantalla()
            
            pg.display.flip()

    def __eventos(self):
        """
        Método encargado de comprobar eventos
        """
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def __pinta_pantalla(self):
        """
        Método semi-privado encargado de pintar:
        - El fondo
        - La pelota
        - El palito
        - El grupo de bloques
        """
        self.pantalla.blit(self.fondo, (0,0))
        for bloque in self.lista_bloques:
            self.pantalla.blit(bloque.imagen, (bloque.x,bloque.y))
        self.pantalla.blit(self.pelota.imagen, (self.pelota.x,self.pelota.y))
        self.pantalla.blit(self.palito.imagen, (self.palito.x,self.palito.y))
        
    def __crea_bloques(self, patron):
        """
        Método semi-privado encargado de crear el grupo de bloques.
        El argumento 'patron' debe ser una lista de listas como esta:
        [
            ['XX-X-'],
            ...
        ]
        La cual está diseñada de tal forma que la lista principal deberá contener
        un total de 12 listas y cada una de estas listas deberá de contener SÓLO 
        los carácteres 'X' o '-' siendo 'X'=<se_dibuja> y '-'=<no_se_dibuja>
        """
        c = 0
        f = 0
        l = []
        for patron in patron:
            for elemento in patron[f]:
                if elemento == 'X':
                    l.append(bloque.Bloque((16 + c * bloque.Bloque.w), (16 + f * bloque.Bloque.h)))
                f += 1
            f = 0
            c += 1
        return l

if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_principal()