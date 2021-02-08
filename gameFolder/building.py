from ursina import *
from ursina import mouse, camera
from ursina.prefabs.first_person_controller import FirstPersonController
app=Ursina()
grass_texture=load_texture('assets/grass_block.png')
stone_texture=load_texture('assets/stone_block.png')
brick_texture=load_texture('assets/brick_block.png')
dirt_texture=load_texture('assets/dirt_block.png')
sky_texture=load_texture('assets/skybox.png')
arm_texture=load_texture('assets/arm_texture.png')
ss=Audio('assets/mineDestroy',loop=False,autoplay=False)
theme_song=Audio('assets/minecraft',loop=True,autoplay=True)
make_sound=Audio('assets/punch_sound',autoplay=False,loop=False)
BLOCK_PICK=1

window.fps_counter.enabled=False
window.exit_button.visible=False

def update():
    global BLOCK_PICK
    if held_keys['left mouse'] or held_keys['right mouse']:hand.normalHand()
    else:hand.workingHand()
    if held_keys['1'] : BLOCK_PICK = 1
    if held_keys['2'] : BLOCK_PICK = 2
    if held_keys['3'] : BLOCK_PICK = 3
    if held_keys['4'] : BLOCK_PICK = 4
class Voxel(Button):
    def __init__(self,position = (0,0,0),texture=grass_texture ):

        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.random_color(),
            scale=0.5)
    def input(self,key):
        if self.hovered:
            if key=='left mouse down':
                make_sound.play()
                if BLOCK_PICK==1:voxel=Voxel(position=self.position+ mouse.normal,texture=dirt_texture)
                if BLOCK_PICK==2:voxel=Voxel(position=self.position+ mouse.normal,texture=stone_texture)
                if BLOCK_PICK==3:voxel=Voxel(position=self.position+ mouse.normal,texture=grass_texture)
                if BLOCK_PICK==4:voxel=Voxel(position=self.position+ mouse.normal,texture=brick_texture)
                ss.stop()
            if key=='right mouse down':
                ss.play()
                destroy(self)

class sky(Entity):
    def __init__(self):
        super().__init__(
            position=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True)
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150,-10,0),
            position=Vec2(0.2,-0.6)
        )
    def normalHand(self):
        self.position=Vec2(0.1,-0.5)
    def workingHand(self):
        self.position=Vec2(0.2,-0.6)
for z in range(30):
    for x in range(30):
            vocel=Voxel((x,0,z))
theme_song.play()
player=FirstPersonController()
sky=sky()
hand=Hand()
app.run()