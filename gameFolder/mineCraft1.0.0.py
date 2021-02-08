from ursina import *

class Test_Cube(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            color = color.white,
            texture= 'white_cube',
            rotation= Vec3(45,45,45)
        )
class test_button(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='cube',
            texture='brick',
            color=color.blue,
            highlight_color=color.white,
            pressed_colot=color.black
        )
    def input(self, key):
        if (self.hovered):
            if key =='left mouse down':
                print("Pressed")


def update():
    if held_keys['a']:
        test_shape.x -=1 * time.dt

app=Ursina()
test_shape=Entity(model='cube',color=color.red,scale=(1,4),position=(5,4))

sans=Entity(model='quad',texture='assets/master.jpeg')
test_cube=test_button()

app.run()