#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import time

import pygame

from fretwork.audio import Audio
from fretwork.audio import Channel
from fretwork.audio import Music


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


class MusicTest(unittest.TestCase):

    def setUp(self):
        filename = "tests/guitar.ogg"
        self.audio = Audio()
        self.audio.open()
        self.music = Music(filename)

    def tearDown(self):
        self.music.stop()
        self.audio.close()

    def test_setEndEvent_with_event(self):
        event = pygame.USEREVENT
        Music.setEndEvent(event)
        self.assertEqual(pygame.mixer.music.get_endevent(), 24)

    def test_setEndEvent_without_event(self):
        Music.setEndEvent()
        self.assertEqual(pygame.mixer.music.get_endevent(), pygame.NOEVENT)

    def test_play(self):
        self.music.play()
        self.assertTrue(self.music.isPlaying())

    def test_stop(self):
        self.music.play()
        self.music.stop()
        self.assertFalse(self.music.isPlaying())

    def test_pause(self):
        self.music.play()
        time.sleep(0.2)
        self.music.pause()
        position = self.music.getPosition()
        time.sleep(0.2)
        self.assertEqual(self.music.getPosition(), position)

    def test_unpause(self):
        self.music.play()
        time.sleep(0.2)
        self.music.pause()
        position = self.music.getPosition()
        time.sleep(0.2)
        self.music.unpause()
        self.assertNotEqual(self.music.getPosition(), position)


class ChannelTest(unittest.TestCase):

    def test_init(self):
        audio = Audio()
        audio.open()

        channel_id = 1
        channel = Channel(channel_id)
        self.assertEqual(channel.id, channel_id)

        audio.close()
