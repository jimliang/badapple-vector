
import os
import sys
import time

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees


def main():
    fps = 10
    root_dir = '/Volumes/temp/images10'
    images = os.listdir(root_dir)
    screen_datas = map(lambda image: anki_vector.screen.convert_image_to_screen_data(
        Image.open(os.path.join(root_dir, image))
    ), images)
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
            robot.behavior.say_text("Bad apple")
            robot.behavior.set_head_angle(degrees(45.0))
            robot.behavior.set_lift_height(0.0)
            i = 0
            for screen_data in screen_datas:
                i += 1
                print(i, images[i])
                robot.screen.set_screen_with_image_data(screen_data,  1 / fps)
                # time.sleep(1000 / fps)
            


if __name__ == "__main__":
    main()
