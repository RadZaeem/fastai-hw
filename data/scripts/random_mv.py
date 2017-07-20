import os
from os.path import join
import sys
import shutil
import click
import random

@click.command()
@click.argument('src')
@click.argument('dst')
@click.argument('cnt')

def random_valid_set(src,dst,cnt):
    # mv x amount of random pictures from train to valid directory
    for x in range(int(cnt)):
        filename=random.choice(os.listdir(src))
        file_src=join(src, filename)
        file_dst=join(dst, filename)
        shutil.move(file_src, file_dst)

        


if __name__ == '__main__':
    random_valid_set()