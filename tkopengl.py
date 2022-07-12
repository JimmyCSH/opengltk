# R&D Project Code
#
# Author: James Shaw
# Date: 12.07.22
# Version: 1.0
#
# This is an OpenGL GUI application that allows users to view and manipulate a 3-dimensional
# wireframe object using buttons.
#
# Resources:
# https://github.com/jonwright/pyopengltk
# https://pypi.org/project/pyopengltk/

import tkinter
from tkinter import filedialog
from pyopengltk import OpenGLFrame
from OpenGL import GL
from OpenGL import GLU

root = tkinter.Tk()
root.resizable(width = False, height = False)
root.title("3D Model Viewer")

# Cube Vertices
vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
)

# Cube Edges
edges = (
    (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), 
    (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
)

def Cube():
    GL.glBegin(GL.GL_LINES)
    for edge in edges:
        for vertex in edge:
            GL.glVertex3fv(vertices[vertex])
    GL.glEnd()

# Rotate the object along the x-axis...
def rotateX():
    GL.glRotatef(2, 1, 0, 0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    Cube()

# Rotate the object along the y-axis...
def rotateY():
    GL.glRotatef(2, 0, 1, 0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    Cube()

# Rotate the object along the z-axis...
def rotateZ():
    GL.glRotatef(2, 0, 0, 1)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    Cube()

class CubeGL(OpenGLFrame):
    # Initialize the OpenGL window...
    def initgl(self):
        GL.glLoadIdentity()
        GLU.gluPerspective(90, (self.width / self.height), 0.1, 50.0)
        GL.glTranslatef(0.0, 0.0, -5)

    # Redraw the OpenGL window...
    def redraw(self):
        GL.glRotatef(0, 0, 0, 0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        Cube()

def add():
    # Allows user to access file from the desktop to upload to application...
    file = filedialog.askopenfilename(initialdir = "/", title = "Select C3D File",
        filetypes = (("executables", "*.exe"), ("all files", "*.*")))

def main():
    # Main frame with OpenGL window...
    screen = CubeGL(height = 700, width = 1000)
    screen.animate = 10
    screen.pack()

    logicFrame = tkinter.Frame(root, bg = "#3D426B")
    logicFrame.place(relwidth = 0.2, relheight = 1.0, rely = 0.0, relx = 0.0)

    openFile = tkinter.Button(logicFrame, text = "Import Model", padx = 40, pady = 6, fg = "white", 
    bg = "#FFB247", borderwidth = 0, command = add)
    openFile.pack(pady = 36)

    rotatex = tkinter.Button(logicFrame, text = "Rotate X", padx = 54, pady = 6, fg = "white", 
    bg = "#FFB247", borderwidth = 0, command = rotateX)
    rotatex.pack()

    rotatey = tkinter.Button(logicFrame, text = "Rotate Y", padx = 54, pady = 6, fg = "white", 
    bg = "#FFB247", borderwidth = 0, command = rotateY)
    rotatey.pack(pady = 36)

    rotatez = tkinter.Button(logicFrame, text = "Rotate Z", padx = 54, pady = 6, fg = "white", 
    bg = "#FFB247", borderwidth = 0, command = rotateZ)
    rotatez.pack()

    otherframe = tkinter.Frame(root, bg = "#565c8f")
    otherframe.place(relwidth = 0.8, relheight = 0.05, rely = 0.0, relx = 0.2)

    apptitle = tkinter.Button(otherframe, text = "3D Object Data Viewer", padx = 0, pady = 60, fg = "white", 
    bg = "#565c8f", borderwidth = 0)
    apptitle.pack()

    vertexviewer = tkinter.Frame(root, bg = "#757a9e")
    vertexviewer.place(relwidth = 0.15, relheight = 0.95, rely = 0.05, relx = 0.85)

    vertextitle = tkinter.Button(vertexviewer, text = "Vertices", padx = 54, pady = 6, fg = "black", 
    bg = "white", borderwidth = 0)
    vertextitle.pack()

    return root.mainloop()

if __name__=="__main__":
    main()