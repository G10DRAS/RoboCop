#!/usr/bin/env python2
# -*- coding: utf-8-*-

# Copyright 2017 g10dras
__author__ = 'g10dras'
__version__ = "0.0.7"


import os
import sys
import logging
import yaml
import argparse

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

parser = argparse.ArgumentParser(description='RoboCop Voice Control Center')
parser.add_argument('--consoleinput', action='store_true',
                    help='Use text input instead of a real microphone')
parser.add_argument('--yamlconfig', action='store_true',
                    help='Prefer YAML config over SQLite3DB config')
parser.add_argument('--configdb', action='store_true',
                    help='Prefer SQLite3DB over YAML config')
parser.add_argument('--lcd', action='store_true',
                    help='I2C LCD Display')
parser.add_argument('--bluetoothheadset', action='store_true',
                    help='Bluetooth Headset Support')
parser.add_argument('--bluealsa', action='store_true',
                    help='BlueAlsa Support')
parser.add_argument('--magicmirror', action='store_true',
                    help='RoboCop Magic Mirror Support')
args = parser.parse_args()


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
