import pygame as pg

class Bloque:
    # Tamaño de las imagenes por defecto
    w = 64
    h = 32

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.imagen = pg.image.load('imagenes/red_brick.png')
    
    @property
    def rect(self):
        """
        Propiedad que devolverá un objeto de tipo Rect
        """
        return self.imagen.get_rect(topleft=(self.x, self.y))

    