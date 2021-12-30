#!/usr/bin/python

class TestEngine:
    """An engine-ish for tests only"""
    tickDelta = 10

    def addTask(self, task, synced=True):
        pass

    def removeTask(self, task):
        pass


class TestMicrophone:
    """A microphone-ish for tests only"""
    passthroughQueue = []
