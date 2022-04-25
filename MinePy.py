from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('./assets/grass_block.png')
stone_texture = load_texture('./assets/stone_block.png')
brick_texture = load_texture('./assets/brick_block.png')
dirt_texture = load_texture('./assets/dirt_block.png')
sky_texture = load_texture('./assets/skybox.png')
arm_texture = load_texture('./assets/arm_texture.png')
punch_sound = Audio('./assets/punch_sound.wav', loop = False, autoplay = False)
block_pick = 1

window.exit_button.visible = False

def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
     
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),          
            scale = 0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
            if key == 'right mouse down':
                punch_sound.play() 
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3 (150, -10, 0),
            position =  Vec2(0.55, -0.6)
        )
    def active(self):
        self.position =  Vec2(0.4, -0.5)
    def passive(self):
        self.position =  Vec2(0.55, -0.6)


for z in range(8):
    for y in range(8):
        for x in range(8):
            if y == 0: 
                voxel = Voxel(position = (x,-y,z), texture = grass_texture) 
            elif 2 > y >= 1 :
                voxel = Voxel(position = (x,-y,z), texture = dirt_texture)
            elif y >= 2:
                voxel = Voxel(position = (x,-y,z), texture = stone_texture)

player = FirstPersonController()
sky = Sky()
hand = Hand()
app.run()

"""
from pyexpat import model
from turtle import position
from ursina import *;

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            position = (-3, -1),
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
        )
class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.red,
            highlight_color = color.blue,
            pressed_color = color.yellow
        )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                print('button pressed')
def update():
    if held_keys['a']:
        test_square.x -= 1 * time.dt
    if held_keys['d']:
        test_square.x += 1 * time.dt

app = Ursina()

{ El lugar de origen siempre es el centro de la pantalla. }

test_square = Entity(model = 'quad', color = color.red, scale = (1,4), position = (5,1))


sans_texture = load_texture('')
sans = Entity(model = 'quad', texture = sans_texture)


test_cube = Test_cube()
test_button = Test_button()

app.run()
"""