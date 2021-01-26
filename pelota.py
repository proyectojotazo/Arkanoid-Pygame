import pygame as pg
import settings
import palito

class Pelota:
    # Colección de imagenes para la animación de la explosión
    _explosion = [pg.image.load(f'imagenes/explosion0{i}.png') for i in range(8)]

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.tolerancia_colision = 10
        self.imagen = pg.image.load('imagenes/red_ball.png')

        self.settings = settings.Settings()

        # Variables para animación de explosión
        self.ix_explosion = 0
        self.muriendo = False
        self.velocidad_explosion = 10
        self.animación_explosion = 1000//self.settings.pantalla_FPS * self.velocidad_explosion
        self.frames_acumulados = 0

    @property
    def rect(self):
        """
        Propiedad que devolverá un objeto de tipo Rect
        """
        return self.imagen.get_rect(topleft=(self.x, self.y))

    def actualizar(self, dt, elemento, lista_bloques):
        """
        Método que actualizará la posición de la pelota.
        En caso de que 'muriendo' sea True, mostrará la animación de '__explosion()'
        """
        if self.muriendo:
            return self.__explosion(dt)
        else:
            self.__actualiza_posicion()
            self.__colision_pelota_elemento(elemento)
            self.__colision_pelota_bloques(lista_bloques)
            

    def __actualiza_posicion(self):
        """
        Método que actualizará la posición de la pelota en función de las colisiones
        con las paredes. En caso de que toque la parte inferior de la pantalla
        cambiará el estado de 'muriendo' a True
        """
        if self.rect.left <= 0 or self.rect.right >= self.settings.pantalla_width:
            self.vx = -self.vx
        if self.rect.top <= 0:
            self.vy = -self.vy
        if self.rect.bottom >= self.settings.pantalla_heigth:
            self.muriendo = True
            return

        self.x += self.vx
        self.y += self.vy

    def __colision_pelota_elemento(self, elemento):
        
        """
        Método encargado de la colisión de la pelota con el palo o con los bloques
        """
        if self.rect.colliderect(elemento.rect):
            if abs(elemento.rect.top - self.rect.bottom) < self.tolerancia_colision and self.vy > 0:
                # Aumento de velocidad cuando colision bola inf con palo sup
                # if isinstance(elemento, palito.Palito):
                #     self.vy += 0.1
                self.vy *= -1
            if abs(elemento.rect.bottom - self.rect.top) < self.tolerancia_colision and self.vy < 0:
                self.vy *= -1
            if abs(elemento.rect.right - self.rect.left) < self.tolerancia_colision and self.vx < 0:
                self.vx *= -1
            if abs(elemento.rect.left - self.rect.right) < self.tolerancia_colision and self.vx > 0:
                self.vx *= -1

    def __colision_pelota_bloques(self, lista_bloques):
        """
        Método encargado de la colisión con la lista de bloques
        En caso de colisión se eliminará el bloque pero antes producirá
        la colisión necesaria
        """
        if self.rect.collidelist(lista_bloques) != -1:
            bloque_colisionado = self.rect.collidelist(lista_bloques)
            self.__colision_pelota_elemento(lista_bloques[bloque_colisionado])
            lista_bloques.pop(bloque_colisionado)

    def __explosion(self, dt):
        """
        Método que 'creará' la animación de la explosión cambiando la imagen
        de la explosión.
        Una vez haya mostrado todas las imagenes el método devolverá True.
        """
        if self.ix_explosion >= len(self._explosion):
            return True
        self.imagen = self._explosion[self.ix_explosion]
        
        self.frames_acumulados += dt
        if self.frames_acumulados >= self.animación_explosion:
            self.ix_explosion += 1
            self.frames_acumulados = 0