import pygame as pg
from pygame.locals import *

class Palito:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 5

        self.imagen = pg.image.load('imagenes/regular_racket.png')

    @property
    def rect(self):
        """
        Propiedad que devolverá un objeto de tipo Rect
        """
        return self.imagen.get_rect(topleft=(self.x, self.y))

    def moving_stick(self):
        """
        Método que comprobará si se pulsan la flecha izquierda 'K_RIGHT'
        o la flecha derecha 'K_RIGHT'. En caso de ser pulsadas el palito
        se moverá en dicha dirección.
        """
        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[K_RIGHT] and self.rect.right <= 798:
            # self.vx = 5
            self.x += self.vx
        elif teclas_pulsadas[K_LEFT] and self.rect.left > 1:
            # self.vx = 5
            self.x -= self.vx
        # else:
        #     self.vx = 0