from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Piramide3D:
    def __init__(self):
        self.angle_x = 0
        self.angle_y = 0
        self.init_window()

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(600, 600)
        glutCreateWindow(b"Piramide 3D con colores por vertice")

        glEnable(GL_DEPTH_TEST)
        glClearColor(0.1, 0.1, 0.1, 1.0)

        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutSpecialFunc(self.keyboard_special)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 1, 50)
        glMatrixMode(GL_MODELVIEW)

        glutMainLoop()

    def draw_colored_pyramid(self):
        glBegin(GL_TRIANGLES)

        # Vértices de la pirámide
        top = [0.0, 1.0, 0.0]
        v1 = [-1.0, -1.0, 1.0]
        v2 = [1.0, -1.0, 1.0]
        v3 = [1.0, -1.0, -1.0]
        v4 = [-1.0, -1.0, -1.0]

        # --- Caras laterales (4 triángulos) ---
        # Frente
        glColor3f(1.0, 0.0, 0.0)  # rojo
        glVertex3fv(top)
        glColor3f(0.0, 1.0, 0.0)  # verde
        glVertex3fv(v1)
        glColor3f(0.0, 0.0, 1.0)  # azul
        glVertex3fv(v2)

        # Derecha
        glColor3f(1.0, 0.0, 0.0)  # rojo
        glVertex3fv(top)
        glColor3f(0.0, 0.0, 1.0)  # azul
        glVertex3fv(v2)
        glColor3f(1.0, 1.0, 0.0)  # amarillo
        glVertex3fv(v3)

        # Atrás
        glColor3f(1.0, 0.0, 0.0)  # rojo
        glVertex3fv(top)
        glColor3f(1.0, 1.0, 0.0)  # amarillo
        glVertex3fv(v3)
        glColor3f(1.0, 0.0, 1.0)  # magenta
        glVertex3fv(v4)

        # Izquierda
        glColor3f(1.0, 0.0, 0.0)  # rojo
        glVertex3fv(top)
        glColor3f(1.0, 0.0, 1.0)  # magenta
        glVertex3fv(v4)
        glColor3f(0.0, 1.0, 0.0)  # verde
        glVertex3fv(v1)

        glEnd()

        # --- Base cuadrada ---
        glBegin(GL_QUADS)
        glColor3f(0.3, 0.3, 0.3)  # gris suave
        glVertex3fv(v1)
        glVertex3fv(v2)
        glVertex3fv(v3)
        glVertex3fv(v4)
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, -6.0)
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)

        self.draw_colored_pyramid()
        glutSwapBuffers()

    def keyboard_special(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            self.angle_y += 5
        elif key == GLUT_KEY_LEFT:
            self.angle_y -= 5
        elif key == GLUT_KEY_UP:
            self.angle_x -= 5
        elif key == GLUT_KEY_DOWN:
            self.angle_x += 5
        glutPostRedisplay()


if __name__ == "__main__":
    Piramide3D()
