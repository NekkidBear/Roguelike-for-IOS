from scene import *
from PIL import Image
#from Sprite_parser import spritesheet

import sound
import random
import math
A = Action
dungeon_texture = Texture('sprites/roguelikeDungeon_transparent.png')
all_dungeon_textures[dungeon_texture.subtexture(n) for ]
class MyScene (Scene):
	def setup(self):

		self.background_color = '#394559'
		self.player = SpriteNode('plc:Character_Boy')
		self.player.position = self.size/2
		self.add_child(self.player)
		ground = Node(parent = self)
		ground_texture = dungeon_texture.subtexture(Rect(0,0,16,16))
		x=0
		y=0
		
		while x <= self.size.w + 16:
			tile = SpriteNode(ground_texture)
			ground.add_child(tile)
			x += 17
		
		pass
	
	def did_change_size(self):
		pass
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		x,y = touch.location
		move_action = Action.move_to(x,y,0.7, TIMING_SINODIAL)
		self.player.run_action(move_action)
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=True)
