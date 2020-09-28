import argparse
from conversion import ocr_dataset_creator, batch_convertor, text_to_image
from os.path import curdir

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands', dest='command')

txt2img_parser = subparsers.add_parser('txt2img', help="convert a font to image for given text")
txt2img_parser.add_argument('--text', required=True, action='store', type=str, help='text you want to convert')
txt2img_parser.add_argument('--font_path', '-fp', action='store', default='default font', type=str, help='absolute '
                                                                                                         'path of font'
                                                                                                         ' file')
txt2img_parser.add_argument('--text_color', '-c', action='store', default='black', type=str, help='color for text')
txt2img_parser.add_argument('--background_color', '-bg', action='store', default='white', type=str,
                            help='color of background')
txt2img_parser.add_argument('--size', '-s', action='store', default=(128, 128), type=tuple, help='size of the image')


batch_convert_parser = subparsers.add_parser('batch_convert',
                                             help='convert all ttf files to images for the given folder for '
                                                  'every character')
batch_convert_parser.add_argument('folder_path', action='store', type=str, help='directory absolute path')


create_dataset_parser = subparsers.add_parser('create_dataset',
                                              help='convert given ttf file to images for the given folder for '
                                                   'every character')
create_dataset_parser.add_argument('--font_path', '-fp', required=True, action='store', type=str, )
create_dataset_parser.add_argument('--storage_path', '-sp', action='store', default=curdir, type=str, )
create_dataset_parser.add_argument('--text_color', '-c', action='store', default='black', type=str,
                                   help='color for text')
create_dataset_parser.add_argument('--background_color', '-bg', action='store', default='white', type=str,
                                   help='color of background')
create_dataset_parser.add_argument('--size', '-s', action='store', default=(128, 128), type=tuple,
                                   help='size of the image')

args = parser.parse_args()

if args.command == 'txt2img':
    text_to_image(args.text, path_to_ttf=args.font_path, text_color=args.text_color, bg=args.background_color,
                  size=args.size)
elif args.command == 'batch':
    batch_convertor(args.folder_path)
elif args.command == 'dataset':
    ocr_dataset_creator(args.font_path,)
else:
    print("Enter a valid argument")
