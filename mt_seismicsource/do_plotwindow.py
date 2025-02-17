# -*- coding: utf-8 -*-
"""
SHARE Seismic Source Toolkit

Dialog for plot window.

Author: Fabian Euchner, fabian@sed.ethz.ch
"""

############################################################################
#    This program is free software; you can redistribute it and/or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################

import numpy
import shapely.geometry
# import shapely.ops

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *

import utils
from ui_plotwindow import Ui_PlotWindow

class PlotWindow(QDialog, Ui_PlotWindow):
    """This class represents the plot window dialog."""

    def __init__(self, iface):

        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)
