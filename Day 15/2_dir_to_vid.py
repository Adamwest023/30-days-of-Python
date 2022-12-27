import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
thumbnail_per_half_second_dir = os.path.join(
    SAMPLE_OUTPUTS, "thumbnails-per-half-second")
output_video = os.path.join(SAMPLE_OUTPUTS, "thumbs.mp4")


this_dir = os.listdir(thumbnail_dir)
# sending to the path if a file is a certain type
# inline iteration
filepaths = [os.path.join(thumbnail_dir, fname)
             for fname in this_dir if fname.endswith("jpg")]

print(filepaths)
clip = ImageSequenceClip(filepaths, fps=4)
clip.write_videofile(output_video)
