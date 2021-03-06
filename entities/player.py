from __future__ import annotations
from typing import TYPE_CHECKING, List

from .entity import Entity, Types
if TYPE_CHECKING:
	from ..window.game import Game


class Player(Entity):
	"""Player class"""
	def __init__(
		self,
		game: Game,
		sprite: str = '#',
	):
		super().__init__(None, 10, 0, sprite)
		self.game = game
		self.type = Types.PLAYER
		
	@property
	def stats(self) -> List[str]:
		"""Returns dynamic statlist (WIP)"""
		attribs = self.game.attribs
		hpPerc = self.hp / self.maxHP # HP percentage
		fpPerc = self.fp / self.maxFP # FP percentage

		# green if hp over 50%, otherwise yellow if over 25%, otherwise red
		hpCol = attribs.green if (hpPerc > 0.5) else attribs.yellow if (hpPerc > 0.25) else attribs.red
		fpCol = attribs.green if (fpPerc > 0.5) else attribs.yellow if (fpPerc > 0.25) else attribs.red

		barLen = 10
		hpBar = "#" * (int(hpPerc * barLen)) + "-" * int(barLen - (hpPerc * barLen))
		fpBar = "#" * int(fpPerc * barLen) + "-" * int(barLen - (fpPerc * barLen))
		
		return [
			f"Hp ({self.hp}/{self.maxHP})",
			(hpBar, hpCol | attribs.bold),
			
			f"Fp ({self.fp}/{self.maxFP})",
			(fpBar, fpCol | attribs.bold),
			
			f"Att | 0",
			f"Def | 0",
			f"Str | 0",
			f"Dex | 0",
			f"Mag | 0",
			f"Lck | 0"
		]
	
	def interact(self, entity: Entity) -> None:
		# if entity.type == Types.FRIENDLY:
		# 	return
		# self.game.UI.addLog(f"Player was damaged for {entity.dmg} hp!")
		# self.damage(entity.dmg)
		pass