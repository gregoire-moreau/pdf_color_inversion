#!/usr/bin/env python3

import fitz
import sys
from PIL import Image
import os
import argparse
from inversion import invert


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start training of an agent')
    parser.add_argument('input',  help='Path to the input PDF file')
    parser.add_argument('-o', '--output')
    parser.add_argument('-n', '--name')
    args = parser.parse_args()

    doc = fitz.open(args.input)
    if args.output:
        output_path = args.output
    else:
        name = doc.metadata['title'] if not args.name else args.name
        if name[-4:] != '.pdf':
            name += '.pdf'
        output_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))) + '\\output\\' + name
    images = invert(doc)
    doc.close()

    if len(images) > 1:
        images[0].save(output_path, format='PDF', save_all=True, append_images=images[1:])
    else:
        images[0].save(output_path, format='PDF')
