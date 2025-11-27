from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import sys

class CuboConBMP:
    def __init__(self):
        self.angle_x = 0
        self.angle_y = 0
        self.texturas = [0]*6
        self.init_window()

    def cargar_textura_bmp(self, ruta):
        """Lee BMP (24 o 32 bits, sin compresión) y crea una textura OpenGL.
           Devuelve tex_id (int) o 0 si falla."""
        try:
            with open(ruta, "rb") as f:
                header = f.read(54)
                if len(header) < 54 or header[0:2] != b'BM':
                    print(f"[ERROR] {ruta} no es un BMP válido.")
                    return 0

                data_offset = int.from_bytes(header[10:14], "little")
                width = int.from_bytes(header[18:22], "little", signed=False)
                height = int.from_bytes(header[22:26], "little", signed=True)
                bpp = int.from_bytes(header[28:30], "little")
                compression = int.from_bytes(header[30:34], "little")
                if compression != 0:
                    print(f"[ERROR] {ruta} BMP comprimido no soportado.")
                    return 0

                top_down = False
                if height < 0:
                    top_down = True
                    height = abs(height)

                # bytes por pixel
                if bpp == 24:
                    bytes_per_pixel = 3
                elif bpp == 32:
                    bytes_per_pixel = 4
                else:
                    print(f"[ERROR] {ruta} BPP {bpp} no soportado (usar 24 o 32).")
                    return 0

                f.seek(data_offset)
                # filas alineadas a 4 bytes
                row_padded = ((width * bytes_per_pixel + 3) // 4) * 4
                raw = f.read(row_padded * height)
                if len(raw) < row_padded * height:
                    print(f"[ERROR] {ruta} datos incompletos.")
                    return 0

                # construir buffer RGB(A) sin padding, en orden R,G,B,(A)
                img = bytearray()
                for row in range(height):
                    if top_down:
                        src_row = row
                    else:
                        src_row = height - 1 - row
                    row_start = src_row * row_padded
                    for col in range(width):
                        px_start = row_start + col * bytes_per_pixel
                        b = raw[px_start]
                        g = raw[px_start + 1]
                        r = raw[px_start + 2]
                        img.extend((r, g, b))
                        if bytes_per_pixel == 4:
                            a = raw[px_start + 3]
                            img.append(a)

            # crear textura
            tex_id = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, tex_id)
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

            if bytes_per_pixel == 3:
                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0,
                             GL_RGB, GL_UNSIGNED_BYTE, bytes(img))
            else:
                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                             GL_RGBA, GL_UNSIGNED_BYTE, bytes(img))

            # generar mipmaps para mejor calidad al escalar (si está disponible)
            try:
                glGenerateMipmap(GL_TEXTURE_2D)
            except Exception:
                pass

            print(f"[OK] Cargada {ruta} ({width}x{height}, {bpp}bpp) -> tex {tex_id}")
            return tex_id

        except FileNotFoundError:
            print(f"[ERROR] Archivo no encontrado: {ruta}")
            return 0
        except Exception as e:
            print(f"[ERROR] Falló al cargar {ruta}: {e}")
            return 0

    def init_window(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(700, 700)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(b"Cubo 3D con BMP - E:\\SELECCIONAR\\Nueva carpeta\\I1..I6.bmp")

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glClearColor(0.1, 0.1, 0.1, 1.0)

        # RUTA BASE y archivos
        base = r"E:\SELECCIONAR\Nueva carpeta"
        archivos = ["I1.bmp", "I2.bmp", "I3.bmp", "I4.bmp", "I5.bmp", "I6.bmp"]

        for i, imgname in enumerate(archivos):
            ruta = os.path.join(base, imgname)
            tex = self.cargar_textura_bmp(ruta)
            if tex == 0:
                # si falla, dejamos 0 y se dibujará un color sólido
                print(f"[WARN] Usando color solido para la cara {i+1}")
            self.texturas[i] = tex

        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutSpecialFunc(self.keyboard_special)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1.0, 1.0, 50.0)
        glMatrixMode(GL_MODELVIEW)

        glutMainLoop()

    def draw_face_textured_or_colored(self, texture_id, color_on_fail=(0.8,0.2,0.2)):
        """Si texture_id != 0 dibuja la cara con textura;
           si es 0 dibuja un quad con 1 solo color (evita fallos)."""
        if texture_id:
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glBegin(GL_QUADS)
            glTexCoord2f(0.0, 0.0); glVertex3f(-1, -1, 0)
            glTexCoord2f(1.0, 0.0); glVertex3f( 1, -1, 0)
            glTexCoord2f(1.0, 1.0); glVertex3f( 1,  1, 0)
            glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1, 0)
            glEnd()
        else:
            glBindTexture(GL_TEXTURE_2D, 0)
            glColor3fv(color_on_fail)
            glBegin(GL_QUADS)
            glVertex3f(-1, -1, 0)
            glVertex3f( 1, -1, 0)
            glVertex3f( 1,  1, 0)
            glVertex3f(-1,  1, 0)
            glEnd()
            glColor3f(1,1,1)  # reset color

    def draw_cube(self):
        # Frente (I1)
        glPushMatrix()
        glTranslatef(0, 0, 1)
        self.draw_face_textured_or_colored(self.texturas[0], (1,0,0))
        glPopMatrix()

        # Atrás (I2)
        glPushMatrix()
        glRotatef(180, 0, 1, 0)
        glTranslatef(0, 0, 1)
        self.draw_face_textured_or_colored(self.texturas[1], (0,1,0))
        glPopMatrix()

        # Izquierda (I3)
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(0, 0, 1)
        self.draw_face_textured_or_colored(self.texturas[2], (0,0,1))
        glPopMatrix()

        # Derecha (I4)
        glPushMatrix()
        glRotatef(-90, 0, 1, 0)
        glTranslatef(0, 0, 1)
        self.draw_face_textured_or_colored(self.texturas[3], (1,1,0))
        glPopMatrix()

        # Arriba (I5)
        glPushMatrix()
        glRotatef(-90, 1, 0, 0)
        glTranslatef(0, 0, 1)
        self.draw_face_textured_or_colored(self.texturas[4], (1,0,1))
        glPopMatrix()

        # Abajo (I6)
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        glTranslatef(0, 0, 1)
        self.draw_face_textured_or_colored(self.texturas[5], (0.5,0.5,0.5))
        glPopMatrix()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -6.0)
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)

        self.draw_cube()
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
    CuboConBMP()
