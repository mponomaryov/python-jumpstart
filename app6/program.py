import os
import platform
import subprocess

import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('--------------------')
    print('    CATS FACTORY')
    print('--------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    full_path = os.path.join(base_folder, 'cats_pictures')
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cats_count = 8
    for i in range(1, cats_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)
    print('Done.')


def display_cats(folder):
    print('Displaying cats in OS window.')
    system = platform.system()
    if system == 'Darwin':
        cmd = 'open'
    elif system == 'Windows':
        cmd = 'explorer'
    elif system == 'Linux':
        cmd = 'xdg-open'
    else:
        print('We don\'t support your OS: {}'.format(system))
        return
    subprocess.call([cmd, folder])


if __name__ == '__main__':
    main()
