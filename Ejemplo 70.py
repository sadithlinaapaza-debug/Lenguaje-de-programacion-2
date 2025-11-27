from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Fondo blanco
    glPointSize(6.0)                  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.5, 2.5, -0.5, 5.5, -1.0, 1.0)  # Rango visible (x,y)

def texto(x, y, texto):
    """Dibuja texto en pantalla"""
    glRasterPos2f(x, y)
    for ch in texto:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))

def dibujar_funcion():
    glClear(GL_COLOR_BUFFER_BIT)

    # ============================
    # Ejes X y Y
    # ============================
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-2.5, 0.0)
    glVertex2f(2.5, 0.0)   # Eje X
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0, 5.5)   # Eje Y
    glEnd()

    # --- Marcas en el eje X ---
    for i in range(-2, 3):
        glBegin(GL_LINES)
        glVertex2f(i, -0.05)
        glVertex2f(i, 0.05)
        glEnd()
        if i != 0:
            texto(i - 0.05, -0.25, str(i))

    # --- Marcas en el eje Y ---
    for j in range(0, 6):
        glBegin(GL_LINES)
        glVertex2f(-0.05, j)
        glVertex2f(0.05, j)
        glEnd()
        if j != 0:
            texto(0.1, j - 0.05, str(j))

    # ============================
    # Función y = x²
    # ============================

    # Línea azul que une los puntos
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    x = -2.0
    while x <= 2.0:
        y = x * x
        glVertex2f(x, y)
        x += 0.05
    glEnd()

    # Puntos rojos y coordenadas
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    x = -2.0
    while x <= 2.0:
        y = round(x * x, 2)
        glVertex2f(x, y)
        x += 0.5
    glEnd()

    # Mostrar coordenadas (x, y)
    x = -2.0
    while x <= 2.0:
        y = round(x * x, 2)
        texto(x + 0.05, y + 0.1, f"({x:.1f},{y:.1f})")
        x += 0.5

    # Etiquetas
    glColor3f(0.0, 0.0, 0.0)
    texto(2.1, -0.3, "X")
    texto(-0.2, 5.2, "Y")
    texto(0.5, 4.8, "y = x²")

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Grafico de y = x^2 con coordenadas")
    inicializar()
    glutDisplayFunc(dibujar_funcion)
    glutMainLoop()

if __name__ == "__main__":
    main()
