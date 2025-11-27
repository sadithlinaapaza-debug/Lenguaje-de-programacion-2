from OpenGL.GL import * 
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glColor3f(1.0, 1.0, 1.0)          # Color blanco para ejes
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2, 2, -0.5, 2)        # ✅ Escala ajustada

def dibujar_texto(x, y, texto):
    """Dibuja texto en la posición (x, y)"""
    glRasterPos2f(x, y)
    for c in texto:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(c))

def dibujar_funcion():
    glClear(GL_COLOR_BUFFER_BIT)

    # === DIBUJAR CUADRÍCULA ===
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_LINES)
    for i in np.arange(-2, 2.1, 1):
        # Verticales
        glVertex2f(i, -0.5)
        glVertex2f(i, 2)
        # Horizontales
        glVertex2f(-2, i if i >= -0.5 else -0.5)
        glVertex2f(2, i if i >= -0.5 else -0.5)
    glEnd()

    # === DIBUJAR EJES ===
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    # Eje X
    glVertex2f(-2, 0.0)
    glVertex2f(2, 0.0)
    # Eje Y
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0, 2)
    glEnd()

    # === MARCAS EN LOS EJES ===
    glBegin(GL_LINES)
    for i in np.arange(-2, 2.1, 1):
        # Eje X
        glVertex2f(i, -0.03)
        glVertex2f(i, 0.03)
    for j in np.arange(0, 2.1, 0.5):
        # Eje Y
        glVertex2f(-0.03, j)
        glVertex2f(0.03, j)
    glEnd()

    # === NÚMEROS EN EL PLANO ===
    glColor3f(1.0, 1.0, 1.0)
    for i in range(-2, 3):
        if i != 0:
            dibujar_texto(i - 0.05, -0.12, f"{i}")  # Números eje X
    for j in range(1, 3):
        dibujar_texto(0.08, j - 0.05, f"{j}")      # Números eje Y

    # === DIBUJAR FUNCIÓN y = x^2 ===
    glColor3f(1.0, 0.4, 0.7)  # Rosa claro
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-1.5, 1.5, 400):
        y = x ** 2
        glVertex2f(x, y)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Plano Cartesiano con y = x^2")
    inicializar()
    glutDisplayFunc(dibujar_funcion)
    glutMainLoop()

if __name__ == "__main__":
    main()
