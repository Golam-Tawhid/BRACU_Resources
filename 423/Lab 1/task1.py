from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

vertices = [
    #body
    [-1, -1, 0], [1, -1, 0], [1, .5, 0], [-1, .5, 0],
    #roof
    [-1, .5, 0], [1, .5, 0], [0, 1.5, 0]
]

triangles = [
    #body
    (0, 1, 2), (0, 2, 3),
    #roof
    (4, 5, 6)
]

total_raindrops = 200
raindrops = [[random.uniform(-3, 3), random.uniform(1.5, 4), 0] for i in range(total_raindrops)]
speed = 0.05
bending = 0.0

bg_color = [0.0, 0.0, 0.0]
bg_change_speed = 0.01

def draw_house():
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.35, 0.05)
    for triangle in triangles[:2]:
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.0, 0.0)
    for triangle in triangles[2:]:
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_raindrops():
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 1.0)
    for drop in raindrops:
        glVertex3fv(drop)
    glEnd()

def update_raindrops():
    for drop in raindrops:
        drop[1] -= speed
        drop[0] += bending
        if drop[1] < -1:
            drop[1] = random.uniform(1, 4)
            drop[0] = random.uniform(-3, 3)

def bg_update(direction):
    global bg_color
    if direction == "day":
        bg_color = [min(k + bg_change_speed, 1.0) for k in bg_color]
    elif direction == "night":
        bg_color = [max(k - bg_change_speed, 0.0) for k in bg_color]

def display():
    glClearColor(*bg_color, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    draw_house()
    draw_raindrops()
    update_raindrops()
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global bending
    if key == b'\x1b':
        glutLeaveMainLoop()
    elif key == GLUT_KEY_LEFT:
        bending -= 0.001
    elif key == GLUT_KEY_RIGHT:
        bending += 0.001
    elif key == b'n':
        bg_update("night")
    elif key == b'd':
        bg_update("day")

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Task 1: Building a House in Rainfall")

    glEnable(GL_DEPTH_TEST)
    glPointSize(3)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(keyboard)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(0, timer, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
