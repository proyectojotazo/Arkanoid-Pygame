import pygame

class Settings:

    def __init__(self):
        # Configuraciones de la pantalla
        self.pantalla_width = 800
        self.pantalla_heigth = 600
        self.pantalla_FPS = 120

        # Patrones
        self.patron_bito = [
            ['XXXXX'],
            ['X-X-X'],
            ['-X-X-'],
            ['X---X'],
            ['XXXXX'],
            ['X---X'],
            ['X----'],
            ['XXXXX'],
            ['X----'],
            ['-XXX-'],
            ['X---X'],
            ['-XXX-']
        ]
        self.patron_mon = [
            ['XXXXX'],
            ['-X---'],
            ['--X--'],
            ['-X---'],
            ['XXXXX'],
            ['-XXX-'],
            ['X---X'],
            ['-XXX-'],
            ['XXXXX'],
            ['-X---'],
            ['--X--'],
            ['XXXXX']
        ]

