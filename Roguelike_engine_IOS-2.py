from scene import *
from PIL import Image

import sound
import random
import math
A = Action


class MyScene (Scene):
	def setup(self):

		self.background_color = '#394559'
		#self.dungeon_texture = SpriteNode(Texture('sprites/roguelikeSheet_transparent.png'), scale = 2, position = (0,0), parent = self)
		self.player = SpriteNode('plc:Character_Boy')
		self.player.position = self.size/2
		self.add_child(self.player)
		ground = Node(parent = self)
		#ground_texture = self.dungeon_texture.subtexture(Rect(0,0,0.0625, 0.0625)).anchor_point=(0,0)
		x=0
		y=0
		
		while y <= self.size.h + 0.0625:
			while x <= self.size.w + 0.0625:
				tile = SpriteNode('plc:Dirt_Block')
				#tile = SpriteNode(Texture(self.dungeon_texture).subtexture(Rect(0.0625,0.0625,0.0625,0.0625)), position = (0,0), scale = 2)
				ground.add_child(tile)
				x += 0.0625
			y += 0.0625
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
