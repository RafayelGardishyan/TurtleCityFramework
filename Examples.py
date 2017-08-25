import TurtleInTheCity

'''
Scene.:
.DrawRoofedHouse(size)
.DrawFlet(size)
.DrawSun(size)
.DrawTree(size)
.MoveUp(pixels)
.MoveDown(pixels)
.MoveRight(pixels)
.MoveLeft(pixels)
.SetSpeed(0-10)
.ClearScreen()
.Delay(seconds)
'''

if __name__ == '__main__':
    Scene = TurtleInTheCity.Drawer()
    Scene.SetSpeed(0)
    Scene.MoveLeft(370)
    Scene.MoveDown(310)
    Scene.DrawRoofedHouse(75)
    Scene.MoveRight(100)
    Scene.DrawFlat(75)
    Scene.MoveRight(100)
    Scene.DrawCar(0.75, 'green')
    Scene.MoveRight(150)
    Scene.DrawTree(40)
    Scene.MoveRight(20)
    Scene.MoveUp(500)
    Scene.DrawSun(75)
    Scene.Render('Test')
    input()
