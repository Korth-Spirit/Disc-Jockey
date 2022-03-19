# Copyright (c) 2021-2022 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from typing import List

from korth_spirit import ConfigurableInstance
from korth_spirit.configuration import (AggregateConfiguration,
                                        InputConfiguration, JsonConfiguration)
from korth_spirit.data import CellObjectData
from korth_spirit.sdk import aw_wait


class DJInstance(ConfigurableInstance):
    def __init__(self, midis: List[str]):
        super().__init__(
            AggregateConfiguration(
                configurations={
                    JsonConfiguration: ('configuration.json',),
                    InputConfiguration: (),
                }
            )
        )
        self.midis = midis
        self._current_midi = 0
    
    def find_speaker(self, description = "dj_speaker") -> CellObjectData:
        """
        Find the speaker object.
        Raises:
            Exception: If the speaker object could not be found.

        Returns:
            CellObjectData: The speaker object.
        """
        x, _, z = self._configuration.get_world_coordinates()
        print(f"Looking for {description} at {x}, {z}")
        for obj in self.query(x=x, z=z):
            if description in obj.description:
                print(f"Found speaker at {obj.x}, {obj.z}")
                return obj

        raise Exception("Could not find speaker object.")

    def main_loop(self, timer: int = 100) -> None:
        while True:
            self.find_speaker().set(
                name="action",
                value=f"create sound {self.midis[self._current_midi]}"
            )
            print(f"Playing {self.midis[self._current_midi]}")

            self._current_midi = (self._current_midi + 1) % len(self.midis)
            aw_wait(timer)

with DJInstance([
    "class1.midi",
    "class2.midi",
    "class3.midi",
    "class4.midi"
]) as bot:
    bot.main_loop(5 * 60 * 1000)
