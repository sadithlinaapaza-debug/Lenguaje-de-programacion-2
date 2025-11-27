from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

angulo = 0.0

v1 = ( 0.0,  0.5)
v2 = (-0.5, -0.5)
v3 = ( 0.5, -0.5)

cx = (v1[0] + v2[0] + v3[0]) / 3.0
cy = (v1[1] + v2[1] + v3[1]) / 3.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

def display():
    global angulo
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glPushMatrix()
    glTranslatef(cx, cy, 0.0)
    glRotatef(angulo, 0.0, 0.0, 1.0)
    glTranslatef(-cx, -cy, 0.0)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(*v1)
    glVertex2f(*v2)
    glVertex2f(*v3)
    glEnd()

    glPopMatrix()
    glutSwapBuffers()

def special_keys(key, x, y):
    global angulo
    if key == GLUT_KEY_LEFT:
        angulo += 5.0
    elif key == GLUT_KEY_RIGHT:
        angulo -= 5.0
    angulo = angulo % 360.0
    glutPostRedisplay()

def keyboard(key, x, y):
    global angulo
    k = key.decode('utf-8') if isinstance(key, bytes) else key
    if k in ('q', 'Q', '\x1b'):
        sys.exit(0)
    elif k in ('a', 'A'):
        angulo = (angulo + 5.0) % 360.0
        glutPostRedisplay()
    elif k in ('d', 'D'):
        angulo = (angulo - 5.0) % 360.0
        glutPostRedisplay()

def idle():
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GL_DEPTH)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangulo rotante en OpenGL")

    init()
    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    glutMainLoop()

if __name__ == "__main__":
    main()
