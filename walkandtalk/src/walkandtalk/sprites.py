from ppb import Sprite, Vector
from ppb import events as ev
from ppb import Text, Font

from walkandtalk import events as wtev


class Player(Sprite):
    """The player character."""
    speed = 2

    def on_update(self, event: ev.Update, signal):
        self.position += Vector(event.controls.move_x, event.controls.move_y) * event.time_delta * self.speed

    def on_talk_control(self, event: wtev.TalkControl, signal):
        signal(wtev.RequestThoughts(self.position))


class NPC(Sprite):
    message = "This is a test message."
    nearby = 1.5
    text_render = None

    def on_update(self, event, signal):  # TODO: signal type hint
        player = next(event.scene.get(kind=Player))
        if self.text_render is not None and (player.position - self.position).length >= self.nearby:
            signal(wtev.DestroyText(), targets=[self.text_render])
            self.text_render = None

    def on_request_thoughts(self, event: wtev.RequestThoughts, signal):
        if (self.position - event.position).length <= self.nearby and self.text_render is None:
            self.text_render = TextBlob(message=self.message, position=self.position + Vector(0, -1))
            event.scene.add(self.text_render)


font = Font("walkandtalk/resources/Comfortaa_Bold.ttf", size=48)


class TextBlob(Sprite):
    _image = None
    message = "This is a debug message."
    height = 0.75
    layer = 2

    @property
    def image(self):
        if self._image is None:
            self._image = Text(self.message, font=font, color=(255, 255, 255))
        return self._image

    def on_destroy_text(self, event, signal):
        event.scene.remove(self)
