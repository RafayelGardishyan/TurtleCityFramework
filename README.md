# TurtleCityFramework

Docs for a specific version of this framework can be found in the wiki tab of this repository

Quick Link: [Wiki](https://github.com/RafayelGardishyan/TurtleCityFramework/wiki)

## Docs Latest Version (v1.3.2.4)
A framework to draw easier with turtle.
To work with this module you have to:
1. Download source or release archive(then unzip)
2. Make a new file in the same dir
3. Import this module in the file
4. Make a scene in the Drawer class.
5. Call a function from the function list

### Example Code:
```
File Tree:
dir/
   /TurtleInTheCity.py
   /MyFile.py
```
```python
# MyFile.py

import TurtleInTheCity

Scene = TurtleInTheCity.Drawer()

Scene.DrawRoofedHouse(50, 'peru', 'red')
Scene.RenderSVG('test')
```


### Functions List:
* DrawRoofedHouse(size, color(optional), roofcolor(optional), windowcolor(optional), doorcolor(optional))
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
* DrawLetterW(size, color)
* DrawLetterY(size, color)
* DrawLetterX(size, color)
* DrawLetterZ(size, color)
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
