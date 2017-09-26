#!/usr/bin/env python2
# -*- coding: utf-8-*-

# Copyright 2017 g10dras.
__author__ = 'g10dras'

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def WelcomeMsg(screen):
    effects = [
        Cycle(
            screen,
            FigletText("ROBOCOP", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("cop without gun", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 20)], repeat=False)


if __name__ == "__main__":
    Screen.wrapper(WelcomeMsg)
