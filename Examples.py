import TurtleInTheCity

if __name__ == '__main__':
    Scene = TurtleInTheCity.Drawer()
    Scene.SetSpeed(0)
    Scene.MoveLeft(370)
    Scene.MoveDown(310)
    Scene.DrawRoofedHouse(75)
    Scene.MoveRight(100)
    Scene.DrawFlat(75)
    Scene.MoveRight(100)
    Scene.DrawCar(75,)
    Scene.MoveRight(150)
    Scene.DrawTree(40)
    Scene.MoveRight(20)
    Scene.MoveUp(500)
    Scene.DrawSun(75)
    Scene.MoveLeft(125)
    Scene.DrawCloud(125)
    Scene.MoveLeft(125)
    Scene.DrawCloud(75)
    Scene.MoveDown(75)
    Scene.Write('ABXY WZ', 50, 'green')
    Scene.RenderSVG('Example')
    input()
