# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
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
