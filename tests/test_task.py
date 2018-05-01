#!/usr/bin/python
# -*- coding: utf-8 -*-

# FoFiX
# Copyright (C) 2017 FoFiX team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import unittest

from fretwork.task import Task
from fretwork.task import TaskEngine


class Tasker(Task):
    """ Task for tests """
    starting = False
    running = False
    ticking = None

    def started(self):
        self.started = True

    def stopped(self):
        self.started = False

    def run(self, ticks):
        Task().run(ticks)  # needed to cover Task.run
        self.running = True
        self.ticking = ticks


class TaskEngineTest(unittest.TestCase):

    def setUp(self):
        self.engine = object
        self.task_engine = TaskEngine(self.engine)

    def test_checkTask(self):
        # no task
        no_task = "no task"
        self.assertFalse(self.task_engine.checkTask(no_task))  # no task

        # one task
        task = Task()
        self.task_engine.tasks.append({'task': task})
        self.assertTrue(self.task_engine.checkTask(task))  # one task

    def test_addTask(self):
        task = Tasker()
        self.task_engine.addTask(task)
        self.assertTrue(self.task_engine.checkTask(task))  # one task
        self.assertTrue(task.started)  # started

    def test_removeTask(self):
        # add one task
        task = Tasker()
        self.task_engine.addTask(task)
        self.assertTrue(self.task_engine.checkTask(task))  # one task
        self.assertTrue(task.started)  # started

        # remove the task
        self.task_engine.removeTask(task)
        self.assertFalse(self.task_engine.checkTask(task))  # no task
        self.assertFalse(task.started)  # stopped

    def test_pauseTask(self):
        task = Task()
        self.task_engine.addTask(task)
        self.task_engine.pauseTask(task)
        self.assertTrue(self.task_engine.tasks[0]['paused'])  # paused

    def test_resumeTask(self):
        task = Task()
        self.task_engine.addTask(task)
        self.task_engine.pauseTask(task)  # paused
        self.task_engine.resumeTask(task)  # resumed
        self.assertFalse(self.task_engine.tasks[0]['paused'])  # resumed

    def test_exit(self):
        # add tasks
        task0 = Task()
        task1 = Task()
        self.task_engine.addTask(task0)
        self.task_engine.addTask(task1)

        # remove all tasks
        self.task_engine.exit()
        self.assertFalse(self.task_engine.checkTask(task0))
        self.assertFalse(self.task_engine.checkTask(task1))
