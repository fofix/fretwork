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


class TaskEngineTest(unittest.TestCase):

    def setUp(self):
        self.engine = object
        self.task_engine = TaskEngine(self.engine)

    def test_checkTask(self):
        # no task
        no_task = "no task"
        self.assertFalse(self.task_engine.checkTask(no_task))

        # one task
        task = Task()
        self.task_engine.tasks.append({'task': task})
        self.assertTrue(self.task_engine.checkTask(task))

    def test_addTask(self):
        task = Task()
        self.task_engine.addTask(task)
        self.assertTrue(self.task_engine.checkTask(task))

    def test_removeTask(self):
        # add one task
        task = Task()
        self.task_engine.addTask(task)
        self.assertTrue(self.task_engine.checkTask(task))

        # remove the task
        self.task_engine.removeTask(task)
        self.assertFalse(self.task_engine.checkTask(task))

    def test_pauseTask(self):
        task = Task()
        self.task_engine.addTask(task)
        self.task_engine.pauseTask(task)
        self.assertTrue(self.task_engine.tasks[0]['paused'])

    def test_resumeTask(self):
        task = Task()
        self.task_engine.addTask(task)
        self.task_engine.pauseTask(task)
        self.task_engine.resumeTask(task)
        self.assertFalse(self.task_engine.tasks[0]['paused'])

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
