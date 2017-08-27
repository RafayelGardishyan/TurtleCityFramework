import turtle
from time import sleep
try:
    import canvasvg
except ImportError:
    import pip
    pip.main(['install', 'canvasvg'])
    import canvasvg
# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF, renderPM
# from os import remove



class Drawer:

    t = turtle.Turtle()

    renderCount = 1
    PrevName = ""

    def DrawLine(self, distance):
        self.t.forward(distance)

    def TurnLeft(self, degrees):
        self.t.left(degrees)

    def TurnRight(self, degrees):
        self.t.right(degrees)

    def StopDrawing(self):
        self.t.penup()

    def StartDrawing(self):
        self.t.pendown()

    def PenColor(self, color):
        self.t.pencolor(color)

    def FillColor(self, color):
        self.t.fillcolor(color)

    def PenSize(self, size):
        self.t.pensize()

    def DrawCircle(self, size):
        realsize = size / 360
        for i in range(360):
            self.t.forward(realsize)
            self.t.left(1)

    def ChangeShape(self, shape):
        self.t.shape(shape)

    def DrawSquare(self, size):
        for i in range(4):
            self.t.forward(size)
            self.t.left(90)

    def DrawRectangle(self, LongSize, ShortSize):
        for i in range(2):
            self.t.forward(LongSize)
            self.t.left(90)
            self.t.forward(ShortSize)
            self.t.left(90)

    def RenderSVG(self, SceneName):
        self.t.hideturtle()
        if self.PrevName == SceneName:
            nameSav = SceneName + str(self.renderCount) + ".svg"
            ts = self.t.getscreen().getcanvas()
            canvasvg.saveall(nameSav, ts)
            self.renderCount += 1
            self.PrevName = SceneName
        else:
            self.renderCount = 1
            nameSav = SceneName + str(self.renderCount) + ".svg"
            ts = self.t.getscreen().getcanvas()
            canvasvg.saveall(nameSav, ts)
            self.renderCount += 1
            self.PrevName = SceneName
        self.t.showturtle()
    # def RenderPNG(self, SceneName):
    #     if self.PrevName == SceneName:
    #         nameSav = SceneName + str(self.renderCount) + ".svg"
    #         ts = self.t.getscreen().getcanvas()
    #         canvasvg.saveall(nameSav, ts)
    #         drawing = svg2rlg(nameSav)
    #         renderPM.drawToFile(drawing, SceneName + ".png")
    #         remove(nameSav)
    #         self.renderCount += 1
    #         self.PrevName = SceneName
    #     else:
    #         self.renderCount = 1
    #         nameSav = SceneName + str(self.renderCount) + ".svg"
    #         ts = self.t.getscreen().getcanvas()
    #         canvasvg.saveall(nameSav, ts)
    #         drawing = svg2rlg(nameSav)
    #         renderPM.drawToFile(drawing, SceneName + ".png")
    #         remove(nameSav)
    #         self.renderCount += 1
    #         self.PrevName = SceneName

    def Delay(self, seconds):
        sleep(seconds)

    def ClearScreen(self):
        self.t.reset()

    def SetSpeed(self, speed):
        self.t.speed(speed)

    def GetRoofLength(self, a):
        result = ((a * a) + (a * a)) ** 0.5
        return result

    def MoveUp(self, size):
        self.t.penup()
        self.t.setheading(90)
        self.t.forward(size)
        self.t.pendown()
        self.t.setheading(0)

    def MoveDown(self, size):
        self.t.penup()
        self.t.setheading(-90)
        self.t.forward(size)
        self.t.pendown()
        self.t.setheading(0)

    def MoveLeft(self, size):
        self.t.penup()
        self.t.setheading(180)
        self.t.forward(size)
        self.t.pendown()
        self.t.setheading(0)

    def MoveRight(self, size):
        self.t.penup()
        self.t.setheading(0)
        self.t.forward(size)
        self.t.pendown()
        self.t.setheading(0)

    def DrawRoofedHouse(self, size):
        Sub = size / 5
        self.t.setheading(0)
        self.t.pencolor('black')
        self.t.fillcolor('peru')
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(size)
            self.t.left(90)
        self.t.end_fill()
        self.t.penup()

        self.t.left(90)
        self.t.forward(size)
        self.t.pendown()
        self.t.pencolor('red')
        self.t.fillcolor('red')
        self.t.begin_fill()
        self.t.right(45)
        self.t.forward(self.GetRoofLength(size/2))
        self.t.right(90)
        self.t.forward(self.GetRoofLength(size/2))
        self.t.right(135)
        self.t.end_fill()
        self.t.forward(size)
        self.t.pencolor('black')
        self.t.penup()
        self.t.setheading(-90)
        self.t.forward(Sub*2)
        self.t.setheading(0)
        self.t.forward(Sub)
        self.t.pendown()

        def MoveWindow():
            self.t.penup()
            self.t.setheading(0)
            self.t.forward(Sub)
            self.t.pendown()

        def DrawWindow():
            self.t.fillcolor('lightcyan')
            self.t.begin_fill()
            for i in range(5):
                self.t.forward(Sub)
                self.t.left(90)
            self.t.end_fill()

        def GoToBegin():
            self.t.penup()
            self.t.setheading(180)
            self.t.forward(Sub*3)
            self.t.setheading(0)
            self.t.pendown()

        def MoveWindowDown():
            self.t.penup()
            self.t.setheading(-90)
            self.t.forward(Sub)
            self.t.pendown()

        DrawWindow()
        MoveWindow()
        DrawWindow()
        GoToBegin()
        MoveWindowDown()
        DrawWindow()
        MoveWindow()
        MoveWindow()
        MoveWindowDown()

        self.t.setheading(90)
        self.t.fillcolor('saddlebrown')
        self.t.begin_fill()
        self.t.forward(Sub * 2)
        self.t.right(90)
        self.t.forward(Sub)
        self.t.right(90)
        self.t.forward(Sub * 2)
        self.t.end_fill()
        self.t.setheading(180)
        self.t.forward(Sub * 4)


    def DrawFlat(self, size):
        Sub = size/5
        self.t.setheading(0)
        self.t.pencolor('black')
        self.t.fillcolor('gainsboro')
        self.t.begin_fill()
        for i in range(2):
            self.t.forward(size)
            self.t.left(90)
            self.t.forward(size*2)
            self.t.left(90)
        self.t.end_fill()

        self.t.penup()
        self.t.left(90)
        self.t.forward(size*2)
        self.t.backward(Sub*2)
        self.t.right(90)
        self.t.pendown()

        def GoToBegin():
            self.t.penup()
            self.t.setheading(180)
            self.t.forward(Sub*3)
            self.t.setheading(0)
            self.t.pendown()

        def MoveWindow():
            self.t.penup()
            self.t.setheading(0)
            self.t.forward(Sub)
            self.t.pendown()

        def MoveWindowDown():
            self.t.penup()
            self.t.setheading(-90)
            self.t.forward(Sub)
            self.t.pendown()

        def DrawWindow():
            self.t.fillcolor('lightcyan')
            self.t.begin_fill()
            for i in range(5):
                self.t.forward(Sub)
                self.t.left(90)
            self.t.end_fill()

        MoveWindow()
        for i in range(4):
            DrawWindow()
            MoveWindow()
            DrawWindow()
            MoveWindowDown()
            MoveWindowDown()
            GoToBegin()

        self.t.forward(size/5)
        self.t.setheading(90)
        self.t.fillcolor('gray')
        self.t.begin_fill()
        self.t.forward((Sub * 2) - (Sub/4))
        self.t.right(90)
        self.t.forward(Sub)
        self.t.right(90)
        self.t.forward((Sub * 2) - (Sub/4))
        self.t.setheading(180)
        self.t.end_fill()
        self.t.forward(Sub*3)

    def DrawSun(self, size):
        self.t.color('red', 'yellow')
        self.t.begin_fill()
        for i in range(36):
            self.t.forward(size)
            self.t.left(170)
        self.t.end_fill()
        self.t.penup()
        self.t.setheading(-90)
        self.t.forward(size/2)
        self.t.pendown()

    def tree(self, branchLen, t):
        if branchLen > 3:
            t.forward(branchLen)
            t.right(15)
            self.tree(branchLen - 7, t)
            self.t.left(30)
            self.tree(branchLen - 7, t)
            self.t.right(15)
            self.t.backward(branchLen)

    def DrawTree(self, size):
        self.t.setheading(90)
        self.t.color('green')
        self.tree(size, self.t)

    def DrawCar(self, size, color='red'):
        if size != 0:
            self.t.setheading(0)
            self.t.fillcolor(color)
            self.t.begin_fill()
            self.t.forward(5 * size)

            def WheelHolder():
                self.t.setheading(90)
                for i in range(180):
                    self.t.forward(0.2 * size)
                    self.t.right(1)

                self.t.setheading(0)

            WheelHolder()
            self.t.forward(15 * size)
            WheelHolder()
            self.t.forward(12.5 * size)
            self.t.setheading(90)
            for i in range(80):
                self.t.forward(0.375 * size)
                self.t.left(1)
            self.t.setheading(90)
            for i in range(180):
                self.t.forward(0.375 * size)
                self.t.left(1)
            self.t.setheading(180)
            for i in range(52):
                self.t.forward(0.625 * size)
                self.t.left(2)
            self.t.penup()
            self.t.end_fill()
            self.t.setheading(0)
            self.t.forward(7.5 * size)
            self.t.setheading(90)
            self.t.fillcolor('black')
            self.t.begin_fill()
            self.t.pendown()
            for i in range(360):
                self.t.forward(0.15 * size)
                self.t.right(1)
            self.t.setheading(0)
            self.t.penup()
            self.t.end_fill()
            self.t.fillcolor('gray')
            self.t.begin_fill()
            self.t.forward(3 * size)
            self.t.pendown()
            self.t.setheading(90)
            for i in range(360):
                self.t.forward(0.1 * size)
                self.t.right(1)
                self.t.penup()
            self.t.end_fill()
            self.t.setheading(180)
            self.t.forward(3 * size)
            self.t.setheading(0)
            self.t.forward((17.2 + 5.5 + 15) * size)
            self.t.setheading(90)
            self.t.fillcolor('black')
            self.t.begin_fill()
            self.t.pendown()
            for i in range(360):
                self.t.forward(0.15 * size)
                self.t.right(1)
            self.t.penup()
            self.t.end_fill()
            self.t.fillcolor('gray')
            self.t.begin_fill()
            self.t.setheading(0)
            self.t.forward(3 * size)
            self.t.pendown()
            self.t.setheading(90)
            for i in range(360):
                self.t.forward(0.1 * size)
                self.t.right(1)
            self.t.penup()
            self.t.end_fill()
            self.t.fillcolor('black')
            self.t.setheading(180)
            self.t.forward(5.5 * size)
            self.t.setheading(90)
            self.t.pendown()
            self.t.forward(22 * size)
            self.t.setheading(0)
            self.t.forward(18.5 * size)
            self.t.left(180)
            self.t.forward(43 * size)
            self.t.setheading(270)
            self.t.forward(0.5 * size)
            self.t.setheading(90)
            self.t.penup()
            self.t.pencolor('blue')
            self.t.fillcolor('LightBlue')
            self.t.begin_fill()
            self.t.pendown()
            for i in range(180):
                self.t.forward(0.375 * size)
                self.t.right(1)
            self.t.setheading(180)
            self.t.forward(43 * size)
            self.t.end_fill()
            self.t.backward(24.5 * size)
            self.t.setheading(90)
            self.t.forward(21.5 * size)
            self.t.setheading(-90)
            self.t.penup()
            self.t.forward((21.5 + 22) * size)
            self.t.setheading(180)
            self.t.forward((17.2 + 7.5 + 15) * size)
            self.t.setheading(-90)
            self.t.forward(8.6 * size)
            self.t.pendown()
        else:
            print("Enter a correct value for size")

    def DrawCloud(self, size, outerColor='blue', innerColor='lightblue'):
        self.t.pencolor(outerColor)
        self.t.fillcolor(innerColor)
        r = size / 2
        pi = 3.14
        result = (r * pi * 2) / 4
        self.t.begin_fill()
        self.t.setheading(180)
        for i in range(180):
            self.t.forward(result/180/2)
            self.t.right(1)

        self.t.setheading(90)

        for i in range(180):
            self.t.forward(result/180/2)
            self.t.right(1)

        self.t.setheading(0)

        for i in range(180):
            self.t.forward(result/180/2)
            self.t.right(1)

        self.t.setheading(180)
        self.t.forward(size/4)
        self.t.penup()
        self.t.end_fill()
        self.t.forward(size/8)
        self.t.pendown()


if __name__ == '__main__':
    Scene = Drawer()
    Scene.SetSpeed(0)
    Scene.DrawCloud(25)
    Scene.RenderSVG('CloudMovement')
    input()
