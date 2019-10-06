# -*- coding: utf-8 -*-

"""
Name of the file : main.py
Description : The launch point of the program
"""

__author__ = 'koeman'
__copyright__ = ''
__credits__ = ['']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = ''
__email__ = ''
__status__ = ''

import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from frontend.launcher import launch_app

launch_app()
