# TurtleCityFramework

Docs for a specific version of this framework can be found in the wiki tab of this repository

Quick Link: [Wiki](https://github.com/RafayelGardishyan/TurtleCityFramework/wiki)

## Docs Latest Version
A framework to draw city attributes with turtle.
To work with this module you have to:
1. Download this module to your project dir
2. Import this module
3. Make a scene in the Drawer class.
4. Call a function from the function list

### Example Code:
```python
import TurtleInTheCity

Scene = TurtleInTheCity.Drawer()

Scene.DrawRoofedHouse(50, 'peru', 'red')
Scene.RenderSVG('test')
```


### Functions List:
* DrawRoofedHouse(size, color(optional), roofcolor(optional))
* DrawFlat(size, color(optional), windowcolor(optional))
* DrawSun(size, innercolor(optional), outercolor(optional))
* DrawTree(size, color(optional))
* DrawCar(size, color(optional))
* DrawClud(size, outerColor(optional), innerColor(optional))
* DrawLine(distance)
* DrawCircle(size, color(optional), fill(bool)(optional), fillcolor(optional))
* DrawSquare(size, color(optional), fill(bool)(optional), fillcolor(optional))
* DrawRectangle(size, color(optional), fill(bool)(optional), fillcolor(optional))
* DrawLetterA(size, color)
* DrawLetterB(size, color)
* Write(text, size, color)
* TurnLeft(degrees)
* TurnRight(degrees)
* StopDrawing()
* StartDrawing()
* PenColor(color)
* FillColor(color)
* PenSize(size)
* ChangeShape(shape)
* RenderSVG(SceneName)
* MoveUp(pixels)
* MoveDown(pixels)
* MoveRight(pixels)
* MoveLeft(pixels)
* SetSpeed(0-10)
* ClearScreen()
* Delay(seconds)

### Examples
![alt text](https://github.com/RafayelGardishyan/TurtleCityFramework/blob/master/Example2.png)
![alt text](https://github.com/RafayelGardishyan/TurtleCityFramework/blob/master/Example.gif)
![alt text](https://github.com/RafayelGardishyan/TurtleCityFramework/blob/master/Test.png)

### Render options
At this moment you can only render your canvas in a .svg file but soon you will be able to save it in a .png file!
