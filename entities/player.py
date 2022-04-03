from __future__ import annotations
from typing import TYPE_CHECKING

from entities.entity import Entity

if TYPE_CHECKING:
	from window.screen import Screen


class Player(Entity):
	"""Player class"""
	def __init__(
		self,
		screen: Screen,
		sprite: str = '#',
	):
		super().__init__(screen, sprite)
		self.set_pos()
	
	def handle_movement(self) -> None:
		"""Handles player movement"""
		ch = self.screen.getch()
		match ch: # probably a better way of doing this, however i am lazy
			case 27: #escape key
				self.screen.loadMenu("options") # loads the escape menu
			
			case 259 | 119: # up arrow | w
				ent = self.screen.entityInPos(self.x, self.y-1)
				if ent and ent.block:
					ent.interact()
					return
				self.y -= 1
				
			case 258 | 115: # down arrow | s
				ent = self.screen.entityInPos(self.x, self.y+1)
				if ent and ent.block:
					ent.interact()
					return
				self.y += 1
				
			case 260 | 97: # left arrow | a
				ent = self.screen.entityInPos(self.x-1, self.y)
				if ent and ent.block:
					ent.interact()
					return
				self.x -= 1
				
			case 261 | 100: # right arrow | d
				ent = self.screen.entityInPos(self.x+1, self.y)
				if ent and ent.block:
					ent.interact()
					return
				self.x += 1

		# makes sure the positions are all ok
		self.inside_border_check()
	
	def interact(self) -> None:
		pass