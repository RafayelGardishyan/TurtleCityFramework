import turtle

class Drawer:

    t = turtle.Turtle()

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
        for i in range(4):
            self.t.forward(size)
            self.t.left(90)

        self.t.penup()

        self.t.left(90)
        self.t.forward(size)
        self.t.pendown()
        self.t.pencolor('red')
        self.t.right(45)
        self.t.forward(self.GetRoofLength(size/2))
        self.t.right(90)
        self.t.forward(self.GetRoofLength(size/2))
        self.t.right(135)
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
            for i in range(5):
                self.t.forward(Sub)
                self.t.left(90)

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
        self.t.forward(Sub * 2)
        self.t.right(90)
        self.t.forward(Sub)
        self.t.right(90)
        self.t.forward(Sub * 2)
        self.t.setheading(180)
        self.t.forward(Sub * 4)


    def DrawFlet(self, size):
        Sub = size/5
        self.t.setheading(0)
        self.t.pencolor('black')
        for i in range(2):
            self.t.forward(size)
            self.t.left(90)
            self.t.forward(size*2)
            self.t.left(90)

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
            for i in range(5):
                self.t.forward(Sub)
                self.t.left(90)

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
        self.t.forward((Sub * 2) - (Sub/4))
        self.t.right(90)
        self.t.forward(Sub)
        self.t.right(90)
        self.t.forward((Sub * 2) - (Sub/4))
        self.t.setheading(180)
        self.t.forward(Sub*3)

    def DrawSun(self, size):
        self.t.color('red', 'yellow')
        self.t.begin_fill()
        for i in range(36):
            self.t.forward(size)
            self.t.left(170)
        self.t.end_fill()

    def tree(self, branchLen, t):
        if branchLen > 5:
            t.forward(branchLen*2)
            t.right(20)
            self.tree(branchLen - 5, t)
            self.t.left(40)
            self.tree(branchLen - 5, t)
            self.t.right(20)
            self.t.backward(branchLen*2)

    def DrawTree(self, size):
        self.t.setheading(90)
        self.t.color('green')
        self.tree(size, self.t)

    def DrawCar(self, size):
        print("Coming Soon!")


if __name__ == '__main__':
    Scene = Drawer()
    Scene.SetSpeed(10)
    Scene.MoveLeft(350)
    Scene.MoveDown(300)
    Scene.DrawRoofedHouse(100)
    Scene.MoveRight(150)
    Scene.DrawFlet(100)
    Scene.MoveRight(200)
    Scene.DrawTree(30)
    Scene.MoveUp(500)
    Scene.MoveRight(200)
    Scene.DrawSun(150)

    input()
