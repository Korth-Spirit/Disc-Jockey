# Copyright (c) 2021 Johnathan P. Irvin
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
from korth_spirit import Instance
from korth_spirit.coords import Coordinates
from korth_spirit.data import CellObjectData, ObjectChangeData
from korth_spirit.sdk import aw_object_change, aw_wait

MIDIS = [
    "class1.mid",
    "class2.mid",
    "class3.mid",
    "class4.mid"
]

def find_speaker(bot: Instance, x: int, z: int, speak_description = "dj_speaker") -> CellObjectData:
    """
    Find the speaker object.

    Args:
        bot (Instance): The bot instance.
        x (int): The x coordinate.
        z (int): The z coordinate.

    Returns:
        CellObjectData: The speaker object.
    """
    print(f"Finding speaker at zone {x}, {z}")
    for obj in bot.query(x=x, z=z):
        if speak_description in obj.description:
            return obj

    raise Exception("Could not find speaker object.")

with Instance(name="Portal Mage") as bot:
    try:
        bot.login(
                citizen_number=(int(input("Citizen Number: "))),
                password=input("Password: ")
            ).enter_world(
                input("World: ")
            ).move_to(Coordinates(0, 0, 0))

        speaker = find_speaker(bot, 0, 0)
        print(f"Found speaker at {speaker.x}, {speaker.z}")

        while True:
            for midi in MIDIS:
                print(f"Playing {midi}")
                aw_object_change(
                    ObjectChangeData(
                        old_number = speaker.number,
                        old_x = speaker.x,
                        old_z = speaker.z,
                        owner = speaker.owner,
                        build_timestamp = speaker.build_timestamp,
                        x = speaker.x,
                        y = speaker.y,
                        z = speaker.z,
                        yaw = speaker.yaw,
                        tilt = speaker.tilt,
                        roll = speaker.roll,
                        model = speaker.model,
                        description = speaker.description,
                        action = f'create sound {midi}',
                        data = speaker.data,
                    )
                )
                aw_wait(5 * 60 * 1000)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

