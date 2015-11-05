# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:59:26 2015

@author: lilun
"""

import sys
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        
        
        
        self.menuFile=self.menuBar().addMenu("&File")
        self.actionSaveAs=QAction("&Save as",self)
        self.connect(self.actionSaveAs, SIGNAL("TRIGGERED()"),self.saveas)
        self.actionExit=QAction("&Exit",self)
        self.connect(self.actionExit,SIGNAL("triggered()"),self.close)
        self.menuFile.addActions([self.actionSaveAs,self.actionExit])
        
        
        self.menuHelp=self.menuBar().addMenu("&Help")
        self.actionAbout=QAction("&About",self)
        self.connect(self.actionAbout,SIGNAL("triggered()"),self.about)
        self.menuHelp.addActions([self.actionAbout])
        
        
        self.form=Form()
        self.setCentralWidget(self.form)
        
    def saveas(self):
        fname=unicode(QFileDialog.getSaveFileName(self,"Save as..."))
        
    def about(self):
        QMessageBox.about(self,"About Function,Evaluator","this is my help message.")
        
class Form(QDialog) :
    def __init__(self, parent=None) :
        super(Form, self).__init__(parent)
        self.plot = MatplotlibCanvas()
        function_list = ["np.sin(x)", "np.cos(x)", "pow(x,2)"]
        self.function_edit = QComboBox(parent=None)
        self.function_edit.setEditable(True)
        self.function_edit.addItems(function_list)
        self.parameter_edit = QLineEdit("x=...")
        self.parameter_edit.selectAll()
        self.output_edit = QLineEdit("output=...")
        self.output_edit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.plot)
        layout.addWidget(self.function_edit)
        layout.addWidget(self.parameter_edit)
        layout.addWidget(self.output_edit)
        self.setLayout(layout)
        self.function_edit.setFocus()
        self.connect(self.output_edit,SIGNAL("returnPressed()"),self.updateUI)
        self.setWindowTitle("function evaluator")

    def updateUI(self) :

        try :
            x = np.array(eval(str(self.parameter_edit.text())))
            f = eval(str(self.function_edit.currentText()))
            f_s = str(f).replace("[","").replace("]","")#.replace(" ",",")
            self.output_edit.setText(f_s)
            self.plot.update_figure(x,f)
        except:
            self.output_edit.setText("I can't code")

class MatplotlibCanvas(FigureCanvas):
    def __init__(self,parent=None,width=5,height=4,dpi=100):
        self.fig=Figure(figsize=(width,height),dpi=dpi)
        self.axes=self.fig.add_subplot(111)
        self.axes.hold(False)
        self.compute_initial_figure()
        FigureCanvas.__init__(self,self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
    def compute_initial_figure(self):
        t=np.arange(0.0,3.0,0.01)
        f=np.sin(2*np.pi*t)
#        x=Form.updateUI.x
#        f=Form.updateUI.f
        self.axes.plot(t,f)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('f(t)')
    
    def update_figure(self, t, f):
        self.axes.plot(t, f)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('f(t)')
        self.draw()
        
app=QApplication(sys.argv)
main=MainWindow()
main.show()
app.exec_()