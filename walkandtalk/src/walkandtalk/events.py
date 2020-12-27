from dataclasses import dataclass

from ppb import BaseScene, Vector


@dataclass
class TalkControl:
    scene: BaseScene = None


@dataclass
class RequestThoughts:
    position: Vector
    scene: BaseScene = None


@dataclass
class DestroyText:
    scene: BaseScene = None
