#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import time

import pygame
import pytest

from fretwork.audio import Audio
from fretwork.audio import Channel
from fretwork.audio import MicrophonePassthroughStream
from fretwork.audio import Music
from fretwork.audio import Sound
from fretwork.audio import StreamingSound
from .utils import TestEngine
from .utils import TestMicrophone


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
        self.assertEqual(pygame.mixer.music.get_endevent(), event)

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
        self.music.unpause()
        time.sleep(0.2)
        self.assertNotEqual(self.music.getPosition(), position)


class ChannelTest(unittest.TestCase):

    def test_init(self):
        audio = Audio()
        audio.open()

        channel_id = 1
        channel = Channel(channel_id)
        self.assertEqual(channel.id, channel_id)

        audio.close()


class SoundTest(unittest.TestCase):

    def setUp(self):
        filename = "tests/guitar.ogg"
        self.audio = Audio()
        self.audio.open()
        self.sound = Sound(filename)

    def tearDown(self):
        self.sound.stop()
        self.audio.close()

    def test_isPlaying(self):
        # check if the sound is not playing
        self.assertFalse(self.sound.isPlaying())
        # play the sound
        self.sound.play()
        # check if it is playing well
        self.assertTrue(self.sound.isPlaying())
        # stop the sound
        self.sound.stop()


class MicrophonePassthroughStreamTest(unittest.TestCase):

    def setUp(self):
        engine = TestEngine()
        mic = TestMicrophone()
        self.audio = Audio()
        self.audio.open()
        self.mic_passthrough_stream = MicrophonePassthroughStream(engine, mic)
        self.mic_passthrough_stream.channel = Channel(1)

    def tearDown(self):
        self.mic_passthrough_stream.stop()
        self.audio.close()

    def test_play_once(self):
        self.mic_passthrough_stream.play()
        self.assertTrue(self.mic_passthrough_stream.playing)

    def test_play_twice(self):
        self.mic_passthrough_stream.play()
        self.mic_passthrough_stream.play()
        self.assertTrue(self.mic_passthrough_stream.playing)

    def test_stop_once(self):
        self.mic_passthrough_stream.play()
        self.mic_passthrough_stream.stop()
        self.assertFalse(self.mic_passthrough_stream.playing)

    def test_stop_twice(self):
        self.mic_passthrough_stream.play()
        self.mic_passthrough_stream.stop()
        self.mic_passthrough_stream.stop()
        self.assertFalse(self.mic_passthrough_stream.playing)

    def test_setVolume(self):
        volume = 10
        self.mic_passthrough_stream.setVolume(volume)
        self.assertEqual(self.mic_passthrough_stream.volume, volume)
        # self.assertEqual(self.mic_passthrough_stream.get_volume(), volume)

    def test_run(self):
        self.mic_passthrough_stream.run(0)


class StreamingSoundTest(unittest.TestCase):

    def setUp(self):
        self.audio = Audio()
        self.audio.open()

        channel = Channel(1)
        filename = b"tests/guitar.ogg"
        self.streaming_sound = StreamingSound(channel, filename)

    def tearDown(self):
        self.streaming_sound.stop()
        self.audio.close()

    def test_play(self):
        self.streaming_sound.play()
        self.assertTrue(self.streaming_sound.isPlaying())

    def test_stop(self):
        self.streaming_sound.play()
        self.streaming_sound.stop()
        self.assertFalse(self.streaming_sound.isPlaying())

    def test_setVolume(self):
        self.streaming_sound.play()
        self.streaming_sound.setVolume(10)
        self.streaming_sound.stop()

    @pytest.mark.skip(reason="Not implemented")
    def test_fadeout(self):
        self.streaming_sound.play()
        self.streaming_sound.fadeout(0.5)
        time.sleep(0.2)
        self.assertTrue(self.streaming_sound.isPlaying())
        time.sleep(0.5)
        self.assertFalse(self.streaming_sound.isPlaying())

    def test_get_position(self):
        self.streaming_sound.play()
        time.sleep(0.2)
        position = self.streaming_sound.getPosition()
        self.assertGreater(position, 0)
        self.streaming_sound.stop()

    def test_set_position(self):
        position = 5
        new_position = self.streaming_sound.setPosition(position)

        self.streaming_sound.play()
        self.assertEqual(position, new_position)
        self.assertAlmostEqual(self.streaming_sound.getPosition(), new_position)
        self.streaming_sound.stop()

    def test_set_wrong_position(self):
        position = 1000
        new_position = self.streaming_sound.setPosition(position)
        self.assertEqual(new_position, -1)

        # XXX: not working
        # self.streaming_sound.play()
        # time.sleep(0.2)
        # self.assertGreater(self.streaming_sound.getPosition(), 0)
        # self.streaming_sound.stop()

    def test_setPitchBendSemitones(self):
        self.streaming_sound.play()
        self.streaming_sound.setPitchBendSemitones(10)
        self.streaming_sound.stop()

    def test_setSpeed(self):
        self.streaming_sound.play()
        self.streaming_sound.setSpeed(2)
        self.streaming_sound.stop()
