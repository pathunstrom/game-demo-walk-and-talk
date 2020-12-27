"""
A tiny game demo for ppb 0.11
"""
import ppb

from walkandtalk import controller
from walkandtalk import sprites


class WalkandTalk(ppb.BaseScene):
    def __init__(self, **props):
        super().__init__(**props)

        self.add(sprites.Player())
        self.add(sprites.NPC(
            position=(5, 0),
            message="I'm the first."
        ))
        self.add(sprites.NPC(
            position=(5, 1.5),
            message="I'm very close."
        ))
        self.add(sprites.NPC(
            position=(0, 5),
            message="I'm the second."
        ))
        self.add(sprites.NPC(
            position=(-5, 0),
            message="I'm the last."
        ))


def main():
    ppb.run(
        starting_scene=WalkandTalk,
        title='Walk and Talk',
        systems=[controller.Controller]
    )
