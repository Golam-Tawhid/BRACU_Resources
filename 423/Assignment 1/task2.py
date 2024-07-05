from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import sys
import time

width = 800
height = 600
size = 10.0
speed = 0.03
speed_increment = 0.02
blink = 1.0

points = []
frozen = False

def initGL():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(size)

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def drawPoint(x, y, color, blink, blink_start_time):
    current_time = time.time()
    if blink:
        elapsed_time = current_time - blink_start_time
        if elapsed_time < blink:
                glColor3f(1.0, 1.0, 1.0)
        else:
            glColor3f(color[0], color[1], color[2])
    else:
        glColor3f(color[0], color[1], color[2])

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def mouse(button, state, x, y):
    if not frozen and state == GLUT_DOWN:
        if button == GLUT_RIGHT_BUTTON:
            color = (random.random(), random.random(), random.random())
            direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])
            points.append({
                'x': x,
                'y': height - y,
                'color': color,
                'direction': direction,
                'blink': False,
                'blink_start_time': 0
            })
            #print(f"Point at ({x}, {height - y}), color {color}, direction {direction}")
        elif button == GLUT_LEFT_BUTTON:
            current_time = time.time()
            for point in points:
                point['blink'] = True
                point['blink_start_time'] = current_time

def updatePoints():
    if not frozen:
        for point in points:
            point['x'] += point['direction'][0] * speed
            point['y'] += point['direction'][1] * speed

            if point['x'] <= 0 or point['x'] >= width:
                point['direction'] = (-point['direction'][0], point['direction'][1])
            if point['y'] <= 0 or point['y'] >= height-10:
                point['direction'] = (point['direction'][0], -point['direction'][1])

def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    for point in points:
        point = drawPoint(point['x'], point['y'], point['color'], point['blink'], point['blink_start_time'])

    glutSwapBuffers()

def idle():
    updatePoints()
    glutPostRedisplay()

def keyboard(key, x, y):
    global speed, frozen
    if key == GLUT_KEY_UP:
        if not frozen:
            speed += speed_increment
            #print(f"Speed increased to {speed}")
    elif key == GLUT_KEY_DOWN:
        if not frozen:
            speed = max(0, speed - speed_increment)
            #print(f"Speed decreased to {speed}")

def normalKeyboard(key, x, y):
    global frozen
    if key == b' ':
        frozen = not frozen
        if frozen:
            print("Points frozen")
        else:
            print("Points unfrozen")

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Task 2: Building the Amazing Box")

    initGL()
    glutDisplayFunc(drawScene)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutIdleFunc(idle)
    glutSpecialFunc(keyboard)
    glutKeyboardFunc(normalKeyboard)

    glutMainLoop()

if __name__ == '__main__':
    main()