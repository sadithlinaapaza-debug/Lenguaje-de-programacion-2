from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glPointSize(6)                    # Tamaño de los puntos (aumentado para mejor visibilidad)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)  # Vista ortográfica 2D

def dibujar_triangulo():
    """Dibuja 3 puntos formando un triángulo"""
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)  # Color rojo
    glBegin(GL_LINES)

    # Tres vértices del triángulo
    glVertex2f(-0.9, 0.2)    # Vértice superior
    glVertex2f(-0.9, -0.4)  # Vértice inferior izquierdo
    glVertex2f(-0.9, -0.4)
    glVertex2f(-0.5, -0.4)
    glVertex2f(-0.5, -0.4)# Vértice inferior derecho
    glVertex2f(-0.5, 0.2)
    glVertex2f(-0.3, -0.4)
    glVertex2f(-0.3, 0.2)
    glVertex2f(-0.3, 0.2)
    glVertex2f(0.2, -0.4)
    glVertex2f(0.2, -0.4)
    glVertex2f(0.2, 0.2)
    glVertex2f(0.4, -0.4)
    glVertex2f(0.6, 0.2)
    glVertex2f(0.6, 0.2)
    glVertex2f(0.8, -0.4)
    glVertex2f(0.46, -0.2)
    glVertex2f(0.74, -0.2)

    glEnd()
    glFlush()       #obliga para que todo funcione

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangulo de puntos en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutMainLoop()

if __name__ == "__main__":  # CORRECCIÓN: __name_ en lugar de name
    main()
