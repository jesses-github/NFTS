import imageio
import os
from PIL import Image, ImageSequence

OUTPUT_FILENAME = 'trashgif.gif'
OUTPUT_SIZE = 2000, 2000
FRAME_DURATION = 0.25
SOURCE_FOLDER = 'gif_generator_folder'

def thumbnails(frames, size):
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size, Image.ANTIALIAS)
        yield thumbnail

def compile_uncompressed_gif():
    images = []
    for filename in os.listdir(SOURCE_FOLDER):
        images.append(imageio.imread(os.path.join(SOURCE_FOLDER, filename)))
    imageio.mimsave(OUTPUT_FILENAME, images, duration=FRAME_DURATION)

def compress_gif(filename=OUTPUT_FILENAME, size=OUTPUT_SIZE):
    im = Image.open(filename)
    frames = ImageSequence.Iterator(im)
    frames = thumbnails(frames, size)
    om = next(frames)
    om.info = im.info
    om.save(filename, save_all=True, append_images=list(frames), loop=0)

def compile_compressed_gif():
    pass


if __name__ == '__main__':
    compile_uncompressed_gif()
    compress_gif()
