from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(1.0, 1.0, 1.0, 1.0)  
    glPointSize(10)                    # Tamaño de los puntos (aumentado para mejor visibilidad)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)  # Vista ortográfica 2D

def dibujar_zorro():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.1, 0.1, 0.1)  
    glBegin(GL_LINE_STRIP)
 
    glVertex2f(-0.7, 0.1)
    glVertex2f(-0.8, -0.2)
    glVertex2f(-0.9, -0.6)
    glVertex2f(-0.8, -0.7)
    glVertex2f(-0.7, -0.6)
    glVertex2f(-0.4, -0.9)
    glVertex2f(-0.1, -0.98)
    glVertex2f(0.1, -0.98)
    glVertex2f(0.4, -0.9)  
    glVertex2f(0.7, -0.6)
    glVertex2f(0.8, -0.7)
    glVertex2f(0.9, -0.7)
    glVertex2f(0.8, -0.3)
    glVertex2f(0.7, 0.1)
    glVertex2f(0.3, 0.4)
    glVertex2f(0.0, 0.1)
    glVertex2f(-0.3, 0.4)
    glVertex2f(-0.7, 0.1)
    glVertex2f(-0.8, 0.4)
    glVertex2f(-0.9, 0.7)
    glVertex2f(-0.8, 0.95)
    glVertex2f(-0.7, 0.95)
    glVertex2f(-0.5, 0.9)
    glVertex2f(-0.3, 0.7)
    glVertex2f(-0.2, 0.6)
    glVertex2f(0.0, 0.7)
    glVertex2f(0.2, 0.6)
    glVertex2f(0.3, 0.7)
    glVertex2f(0.5, 0.9)
    glVertex2f(0.7, 0.95)
    glVertex2f(0.8, 0.95)
    glVertex2f(0.9, 0.7)
    glVertex2f(0.7, 0.1)
    
    glEnd()
    glFlush()       #obliga para que todo funcione

    
# Osico
    glColor3f(0.1, 0.1, 0.1)  
    glBegin(GL_POLYGON)

    glVertex2f(-0.1, -0.8)
    glVertex2f(-0.2, -0.6)
    glVertex2f(-0.1, -0.5)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.2, -0.6)
    glVertex2f(0.1, -0.8)

    glEnd()
    glFlush()
#Orejas
    glColor3f(1.0, 0.713, 0.756)  
    glBegin(GL_POLYGON)

    glVertex2f(-0.4, 0.6)
    glVertex2f(-0.7, 0.9)
    glVertex2f(-0.7, 0.4)
    glVertex2f(-0.6, 0.3)
    glVertex2f(-0.4, 0.5)

    glEnd()
    glFlush()

    glColor3f(1.0, 0.713, 0.756)  
    glBegin(GL_POLYGON)

    glVertex2f(0.4, 0.6)
    glVertex2f(0.7, 0.9)
    glVertex2f(0.7, 0.4)
    glVertex2f(0.6, 0.3)
    glVertex2f(0.4, 0.5)

    glEnd()
    glFlush()
    #Ojos
    glColor3f(0.1, 0.1, 0.1)  
    glBegin(GL_LINE_STRIP)

    glVertex2f(-0.5, 0.0)
    glVertex2f(-0.4, 0.0)
    glVertex2f(-0.2, -0.1)
    glVertex2f(-0.4, -0.1)
    glVertex2f(-0.5, 0.0)
    
    glEnd()
    glFlush()

    glColor3f(0.1, 0.1, 0.1)  
    glBegin(GL_LINE_STRIP)

    glVertex2f(0.5, 0.0)
    glVertex2f(0.4, 0.0)
    glVertex2f(0.2, -0.1)
    glVertex2f(0.4, -0.1)
    glVertex2f(0.5, 0.0)
    
    glEnd()
    glFlush()

    glColor3f(0.1, 0.1, 0.1)  
    glBegin(GL_TRIANGLES)

    glVertex2f(-0.4, 0.0)    
    glVertex2f(-0.4, -0.1)  
    glVertex2f(-0.3, -0.1)   

    glEnd()
    glFlush()

    glColor3f(0.1, 0.1, 0.1)  
    glBegin(GL_TRIANGLES)

    glVertex2f(0.4, 0.0)    
    glVertex2f(0.4, -0.1)  
    glVertex2f(0.3, -0.1)   

    glEnd()
    glFlush()

    #Nariz
    glBegin(GL_LINE_STRIP)

    glVertex2f(-0.1, 0.0)
    glVertex2f(-0.2, -0.4)
    glVertex2f(-0.3, -0.6)
    glVertex2f(-0.3, -0.7)
    glVertex2f(-0.1, -0.8)
    
    glEnd()
    glFlush()

    glBegin(GL_LINE_STRIP)

    glVertex2f(0.1, 0.0)
    glVertex2f(0.2, -0.4)
    glVertex2f(0.3, -0.6)
    glVertex2f(0.3, -0.7)
    glVertex2f(0.1, -0.8)
    
    glEnd()
    glFlush()
    
    glColor3f(0.1, 0.1, 0.1)  
    glBegin(GL_LINES)

    glVertex2f(-0.5, -0.3)
    glVertex2f(-0.3, -0.7)

    glVertex2f(0.5, -0.3)
    glVertex2f(0.3, -0.7)
    
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Retrato de Zorro en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_zorro)
    glutMainLoop()

if __name__ == "__main__":  # CORRECCIÓN: __name_ en lugar de name
    main()
