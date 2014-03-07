#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from ui import *

def main():
    app = QtGui.QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

