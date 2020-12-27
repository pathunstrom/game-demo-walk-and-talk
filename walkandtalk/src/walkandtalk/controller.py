from dataclasses import dataclass

from ppb.systemslib import System
from ppb import GameEngine
from ppb.events import Update, KeyPressed, KeyReleased
from ppb.keycodes import W, A, S, D, Space

from walkandtalk import events as wtev

# TODO: Define actions
# TODO: Define Control Types
# TODO: Define events

@dataclass
class Controls:
    move_x: int
    move_y: int


class Controller(System):

    def __init__(self, engine: GameEngine,  **kwargs):
        engine.register(Update, self.extend_update)
        self.controls = Controls(0, 0)
        self.move_up = W
        self.move_down = S
        self.move_right = D
        self.move_left = A
        self.request_talk = Space

    def extend_update(self, event):
        event.controls = self.controls

    def on_key_pressed(self, event: KeyPressed, signal):
        if event.key is self.move_up:
            self.controls.move_y += 1
        elif event.key is self.move_down:
            self.controls.move_y -= 1
        elif event.key is self.move_right:
            self.controls.move_x += 1
        elif event.key is self.move_left:
            self.controls.move_x -= 1
        elif event.key is self.request_talk:
            signal(wtev.TalkControl())

    def on_key_released(self, event: KeyReleased, signal):
        if event.key is self.move_up:
            self.controls.move_y -= 1
        elif event.key is self.move_down:
            self.controls.move_y += 1
        elif event.key is self.move_right:
            self.controls.move_x -= 1
        elif event.key is self.move_left:
            self.controls.move_x += 1
