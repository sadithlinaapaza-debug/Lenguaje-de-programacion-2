from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# posición del triángulo (inicial)
posx = 0.0
posy = 0.0

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # vista ortográfica 2D
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)

def dibujar_triangulo():
    """Dibuja un triángulo y lo traslada según posx,posy"""
    global posx, posy
    glClear(GL_COLOR_BUFFER_BIT)

    # aplicar transformación de modelo (traslación)
    glPushMatrix()
    glTranslatef(posx, posy, 0.0)

    glColor3f(0.0, 1.0, 0.0)  # amarillo
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.5)    # Vértice superior
    glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
    glVertex2f(0.5, -0.5)   # Vértice inferior derecho
    glEnd()

    glPopMatrix()
    glFlush()

def keyboard_special(key, x, y):
    """Recibe teclas especiales (flechas) y mueve el triángulo"""
    global posx, posy
    paso = 0.05

    if key == GLUT_KEY_UP:
        posy += paso
    elif key == GLUT_KEY_DOWN:
        posy -= paso
    elif key == GLUT_KEY_LEFT:
        posx -= paso
    elif key == GLUT_KEY_RIGHT:
        posx += paso

    # limitar para que no se salga de la vista (opcional)
    max_coord = 1.5  # margen; el triángulo puede salirse parcialmente
    if posx > max_coord: posx = max_coord
    if posx < -max_coord: posx = -max_coord
    if posy > max_coord: posy = max_coord
    if posy < -max_coord: posy = -max_coord

    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangulo de puntos en OpenGL - mover con flechas")
    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutSpecialFunc(keyboard_special)  # callback para teclas especiales (flechas)
    glutMainLoop()

if __name__ == "__main__":
    main()
