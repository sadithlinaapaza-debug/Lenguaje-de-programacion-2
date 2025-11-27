from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys

escala = 1.0
angulo = 0.0
posx = 0.0
posy = 0.0

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glPointSize(5)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def dibujar_triangulo():
    global escala, angulo, posx, posy
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    #  Transformaciones
    glTranslatef(posx, posy, 0.0)    
    glRotatef(angulo, 0.0, 0.0, 1.0) 
    glScalef(escala, escala, 1.0)    

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

    glFlush()

def keyboard(key, x, y):
    global escala, angulo
    if key == b'+':        
        escala += 0.1
    elif key == b'-':      
        escala = max(0.1, escala - 0.1)
    elif key == b'r':      
        angulo -= 10
    elif key == b'R':      
        angulo += 10
    elif key == b'\x1b':   
        glutLeaveMainLoop()
    glutPostRedisplay()

def special_keys(key, x, y):
    global posx, posy
    paso = 0.1
    if key == GLUT_KEY_UP:
        posy += paso
    elif key == GLUT_KEY_DOWN:
        posy -= paso
    elif key == GLUT_KEY_LEFT:
        posx -= paso
    elif key == GLUT_KEY_RIGHT:
        posx += paso
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangulo - Escala, Rotacion y Traslacion (OpenGL)")

    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutMainLoop()

if __name__ == "__main__":
    main()
