from __future__ import annotations
from typing import TYPE_CHECKING

from .entity import Entity, Types

if TYPE_CHECKING:
	from map import Map

class Enemy(Entity):
	def __init__(
		self,
		colour: int,
		sprite: str,
		x: int,
		y: int
	) -> None:
		super().__init__(map, sprite, colour)
		self.type = Types.ENEMY
		self.set_pos(x, y)
	
	def interact(self, entity: Entity):
		"""How another entity interacts with this enemy"""
		# if entity.type == Types.FRIENDLY:
		# 	return
		# self.map.game.UI.addLog(f"enemy was damaged for {entity.dmg} hp!")
		# self.damage(entity.dmg)
		pass