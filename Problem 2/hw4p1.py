# Created by Derek Black
# Created Oct. 18, 2015

import sys
import numpy as np
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Form(QtGui.QWidget) :
    def __init__(self):
        super(Form, self).__init__()
        self.plot = MatplotlibCanvas()
        
        # Text Boxes & Labels
        self.function_select = QtGui.QComboBox()
        self.label = QtGui.QLabel('Select Function', self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.function_select.addItem("Sin", 'np.sin')
        self.function_select.addItem("Cos", 'np.cos')
        self.function_select.addItem("Tan", 'np.tan')
        self.label2 = QtGui.QLabel('x Range:', self)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter = QtGui.QLineEdit("x = Start, Stop, Increment")
        self.parameter.setFocus()
        self.parameter.selectAll()
        
        self.label3 = QtGui.QLabel('Incremental Output =', self)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.output = QtGui.QLineEdit("y(xi)")
        self.function_eval = QtGui.QLineEdit("y(x)")
        self.label4 = QtGui.QLabel('y(x) = ', self)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        
        #Appearance
        self.spacer = QtGui.QLabel('', self)
        self.spacer.setAlignment(QtCore.Qt.AlignCenter)
        
        # Push Buttons
        self.run = QtGui.QPushButton('RUN', self)
        self.run.clicked.connect(self.updateUI)
        self.clear = QtGui.QPushButton('CLEAR', self)
        self.clear.clicked.connect(self.clearall)

        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.plot)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.function_select)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.parameter)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.label4)
        self.layout.addWidget(self.function_eval)
        self.layout.addWidget(self.spacer)
        self.layout.addWidget(self.run)
        self.layout.addWidget(self.clear)
         
        self.setLayout(self.layout)
        self.setWindowTitle("Function Evaluator")
  
    def updateUI(self) :
        
        get_x = self.parameter.text()
        if get_x == 'x = Start, Stop, Increment':
            self.output.setText(str('x = Start, Stop, Increment'))
        else:
            xlist = get_x.split(",")
            xlist = map(str,xlist)
            count = -1
            for i in xlist:
                count = count + 1
                if i.isdigit() == False:
                    xlist[count] = eval(xlist[count])
            xlist_new = map(float,xlist)
            x = np.linspace(xlist_new[0],xlist_new[1],xlist_new[2])
        
            f_get = self.function_select.itemData(self.function_select.currentIndex())
            if f_get == 'np.sin':
                f = np.sin(x)
                f_eval = np.sin(xlist_new[1])
            elif f_get == 'np.cos':
                f = np.cos(x)
                f_eval = np.cos(xlist_new[1])
            else:
                f = np.tan(x)
                f_eval = np.tan(xlist_new[1])
        
            self.output.setText(str(f))
            self.function_eval.setText(str(f_eval))
            
            
            self.plot.axes.plot(x,f)
            self.plot.draw()
        
        
    def clearall(self):
        self.output.setText('y(xi)')
        self.parameter.setText('x = Start, Stop, Increment')
        self.function_eval.setText('y(x)')
        
        
       
class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100) :
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(False)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        t =np.arange(0.0,3.0,0.01)
        f = np.sin(2*np.pi*t)
        self.axes.plot(t,f)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('f(f)')
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()