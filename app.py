# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from tools.manager import AppManager


def main():
    app_manager = AppManager()
    app_manager.show_head()

    img_path = app_manager.get_image_path()
    save_folder = app_manager.get_save_folder()

    app_manager.printer.echo()
    print(f'Path to image file: {img_path}')
    app_manager.printer.echo()
    print(f'Path to the folder to save the final file: {save_folder}')
    app_manager.printer.echo()

    app_manager.show_footer()


if __name__ == '__main__':
    main()
