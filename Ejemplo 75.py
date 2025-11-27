from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    # Texto "Hola Mundo"
    glRasterPos2f(-0.6, 0.1)
    for ch in "Hola Mundo":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

    # Texto "Puno"
    glRasterPos2f(-0.1, -0.2)
    for ch in "Puno":
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(ch))

    glFlush()

if __name__ == "__main__":
    glutInit(sys.argv)                               # antes: glotInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 200)
    glutCreateWindow(b"PyOpenGL - Hola Mundo y Puno")
    glClearColor(0.0, 0.0, 0.0, 1.0)                 # antes: glCrearColor()

    # Fijar una proyección 2D para posicionar el texto con glRasterPos2f
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

    glutDisplayFunc(display)
    glutMainLoop()
