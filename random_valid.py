import os
from os.path import join
import sys
import shutil
import click
import random
train_dir="train"
valid_dir="valid"
@click.command()
@click.option('--count', default=10, help='Number of validation')
@click.option('--ctgry')
def hello(count, ctgry):
    src_dir=join(train_dir, ctgry) # train/cats
    dst_dir=join(valid_dir, ctgry) # valid/cats

    for x in range(count):
        filename=random.choice(os.listdir(src_dir))
        file_src=join(src_dir, filename)
        file_dst=join(dst_dir, filename)
        shutil.move(file_src, file_dst)

        


if __name__ == '__main__':
    hello()