# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os

from tools.config import AppConfig
from tools.printer import SmartPrinter


class AppManager:

    def __init__(self):
        self.config = AppConfig()
        self.printer = SmartPrinter()

    def show_head(self):
        self.printer.echo(char='*')
        self.printer.echo(text=self.config.app_name)

    def show_footer(self):
        self.printer.echo(text=self.config.copyright_, char='|')
        self.printer.echo(text=self.config.url, char='=')

    @staticmethod
    def get_image_path():
        while 1:
            image_file_path = input('Enter the path to the image in *.png format: ')
            if not os.path.isfile(image_file_path):
                print(f'ERROR! File not found.')
                continue
            if not image_file_path.endswith('.png'):
                print(f'ERROR! Invalid file format. Specify the path to the file in *.png format.')
                continue
            return image_file_path

    @staticmethod
    def get_save_folder():
        while 1:
            directory_path = input(f'Enter the path to the folder to save the received file: ')
            if not os.path.exists(directory_path):
                print("ERROR! The specified directory does not exist.")
                continue
            return directory_path
