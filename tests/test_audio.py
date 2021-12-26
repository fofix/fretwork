#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import pygame

from fretwork.audio import Audio
from fretwork.audio import Channel


class AudioTest(unittest.TestCase):

    def test_pre_open(self):
        audio = Audio()
        self.assertTrue(audio.pre_open())

    def test_open(self):
        audio = Audio()
        nb_channels = 10
        # init the pygame mixer and set channels
        audio_open = audio.open()
        self.assertTrue(audio_open)  # check return
        self.assertIsNotNone(pygame.mixer.get_init())  # check the mixer
        self.assertEqual(pygame.mixer.get_num_channels(), nb_channels)  # check channels
        # quit the mixer
        audio.close()

    def test_close(self):
        audio = Audio()
        # init the pygame mixer
        audio.open()
        # close the pygame mixer
        audio.close()
        self.assertIsNone(pygame.mixer.get_init())  # check the mixer

    def test_findChannel(self):
        audio = Audio()
        audio.open()
        channel = audio.findChannel()
        self.assertIsInstance(channel, pygame.mixer.ChannelType)

    def test_getChannel(self):
        audio = Audio()
        # init the pygame mixer
        audio.open()
        # get a channel
        channel_id = 1
        channel = audio.getChannel(channel_id)
        self.assertEqual(audio.getChannelCount(), 10)
        self.assertIs(type(channel), Channel)
