from PIL import Image, ImageFont, ImageDraw, ImageColor
from characterDictionary import character_dictionary
from os import mkdir, listdir, curdir
from os.path import join, isfile, dirname


def batch_convertor(directory_name):
    ttf_files = [files for files in listdir(directory_name) if
                 isfile(join(directory_name, files)) and files.endswith(".ttf")]
    batch_dir = f"{directory_name}/{ttf_files[0].split('-')[0]}"
    try:
        mkdir(batch_dir)
        print('Converting...........')

        for i in range(33, 126):
            if chr(i).isalnum():
                char_folder_name = f"{batch_dir}/{chr(i)}"
            else:
                char_folder_name = f"{batch_dir}/{character_dictionary[chr(i)]}"
            mkdir(char_folder_name)
            for font in ttf_files:
                path_of_font = f"{directory_name}/{font}"
                image_name_prefix = font.split('-')[1].replace('.ttf', "")
                im = Image.new(mode='P', size=(128, 128), color=ImageColor.getrgb(color='white'))
                draw = ImageDraw.ImageDraw(im)
                font = ImageFont.truetype(path_of_font, size=128)
                w, h = draw.textsize(chr(i), font=font)
                draw.text(((128 - w) / 2, (128 - h) / 2), chr(i), font=font, fill=ImageColor.getrgb("black"))
                if chr(i).isalnum():
                    im.save(f"{char_folder_name}/{image_name_prefix}-{chr(i)}.png")
                else:
                    im.save(f"{char_folder_name}/{image_name_prefix}-{character_dictionary[chr(i)]}.png")
        print('Task Completed.....')
        print(f'File Location : {batch_dir}')
    except FileExistsError:
        print("Already a file exists...")


def text_to_image(text, path_to_ttf, text_color, bg, size):
    width, height = size
    mode = 'P'
    if text_color != "black":
        mode = 'RGB'
    im = Image.new(mode=mode, size=size, color=ImageColor.getrgb(color=bg))
    draw = ImageDraw.ImageDraw(im)
    if path_to_ttf != "default font":
        try:
            font = ImageFont.truetype(path_to_ttf, size=width)
            w, h = draw.textsize(text, font=font)
            draw.text(((width - w) / 2, (height - h) / 2), text, font=font, fill=ImageColor.getrgb(text_color))
            im.save(f"{dirname(path_to_ttf)}/{text[0:5]}.png")
        except OSError:
            print("Enter valid font file location")
    else:
        w, h = draw.textsize(text)
        draw.text(((width - w) / 2, (height - h) / 2), text, fill=ImageColor.getrgb(text_color))
        im.save(f"{curdir}/{text[0:5]}.png")


def ocr_dataset_creator(path_to_ttf, path_to_store=curdir, text_color="black", bg="white",
                        size=(128, 128)):
    width, height = size
    mode = 'P'
    if text_color != "black":
        mode = 'RGB'
    for i in range(33, 126):
        im = Image.new(mode=mode, size=size, color=ImageColor.getrgb(color=bg))
        draw = ImageDraw.ImageDraw(im)
        font = ImageFont.truetype(path_to_ttf, size=width)
        w, h = draw.textsize(chr(i), font=font)
        draw.text(((width - w) / 2, (height - h) / 2), chr(i), font=font, fill=ImageColor.getrgb("black"))
        try:
            if chr(i).isalnum():
                im.save(f"{path_to_store}/{chr(i)}.png")
            else:
                im.save(f"{path_to_store}/{character_dictionary[chr(i)]}.png")
        except FileNotFoundError:
            print(chr(i))
