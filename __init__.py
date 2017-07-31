# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import pyautogui

__author__ = 'TREE'

LOGGER = getLogger(__name__)


class MatterMostSkill(MycroftSkill):
    def __init__(self):
        super(MatterMostSkill, self).__init__(name="MatterMostSkill")

    def initialize(self):
        mm_channel_down_intent = IntentBuilder("MMChannelDownIntent"). \
            require("MMChannelDownKeyword").build()
        self.register_intent(mm_channel_down_intent, self.handle_mm_channel_down_intent)

        mm_channel_up_intent = IntentBuilder("MMChannelUpIntent"). \
            require("MMChannelUpKeyword").build()
        self.register_intent(mm_channel_up_intent, self.handle_mm_channel_up_intent)

        mm_channel_switch_intent = IntentBuilder("MMChannelSwitchIntent"). \
            require("MMChannelSwitchKeyword").build()
        self.register_intent(mm_channel_switch_intent, self.handle_mm_channel_switch_intent)

        mm_direct_messages_intent = IntentBuilder("MMDirectMessagesIntent"). \
            require("MMDirectMessagesKeyword").build()
        self.register_intent(mm_direct_messages_intent, self.handle_mm_direct_messages_intent)


    def handle_mm_channel_down_intent(self, message):
        self.speak("moving down a channel")
        pyautogui.hotkey('alt', 'down')

    def handle_mm_channel_up_intent(self, message):
        self.speak("moving up a channel")
        pyautogui.hotkey('alt', 'up')

    def handle_mm_channel_switch_intent(self, message):
        self.speak("switching channels")
        pyautogui.hotkey('ctrl', 'k')

    def handle_mm_direct_messages_intent(self, message):
        self.speak("opening direct messages")
        pyautogui.hotkey('ctrl', 'shift', 'k')



    def stop(self):
        pass


def create_skill():
    return MatterMostSkill()
