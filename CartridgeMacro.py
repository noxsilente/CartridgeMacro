#################################################################################################
#                                            CartridgeMacro   ---   for FreeCAD
#       
#    Author: NoxSilente
#    Github: https://github.com/noxsilente/CartridgeMacro    --------- GNU V.3 Licence
#    E-Mail: cguiproject@gmail.com 
#       
#     The purpose of this macro is to simplify the creation of cases for firearms'cartridges 
#     Available types are:
#           - Bottleneck (rimless, rimmed, belted)
#           - Straight (rimless, rimmed, belted)
#       
#    The user have to give several dimensions for create the final object, after that, the user can modify the sketch if needed.
#    I created this macro by the needing a faster way to make cartridges (maybe I'll add the possibility to create bullets too).
#    This macro is in 'alpha' version, intended to be improved (I'm already working on a version using Tkinter library), so
#    some issues can occur during the creation of objects. Please report via email or modify the script if needed 
#      
# I tried to make the script easier using my knowledge (quite basic)
#
#################################################################################################


__title__ = "CartridgeMacro"
__version__ = "0.1"
# importing libraries
import FreeCAD
from PySide.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QGridLayout, QCheckBox, QRadioButton, QMessageBox
#creating constant values
sb = -2.225 #small boxer
lb = -2.665 #large boxer
# creating a list which have to handle input data
V_list = ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
check_list = [0, 0, 0, 1, 0, 0]
# other values
trim_vals = 0,
n = 0
# if the macro doesn't load the FreeCAD library it try again, and if it doesn't for the second time, a message will occur
# If it doesn't load the library reopening the macro, the user have to create a fake object and,
# in the next opening, it will be possible to operate 
try:
    print(Part)
except:
    print('FreeCAD not loaded.. retrying')
    try: 
        import FreeCAD
        print(Part)
    except:
        err=QMessageBox()
        err.setIcon(QMessageBox.Critical)
        err.setInformativeText('FreeCad not loaded - try to create an object then restart macro')
        err.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        if err.exec() == QMessageBox.Close:
            sys.exit()
        else:
            pass
        err.show()
# If there is no document opened, it will be created a new one
try:
    _Doc_  =App.getDocument(App.ActiveDocument.Name).Name #'proiettili2'
    #print(_Doc_)
except:
    App.newDocument('NewDocument')
    _Doc_  =App.getDocument(App.ActiveDocument.Name).Name
    #print(_Doc_)
# Creating Classes:
# All classes have an __init__ def where it will appear the offset.
# Every offset is intended to ask the necessary values for the creation of the desired object
# with the def 'get_values', all inputs will be processed and inserted in 'V_list'. 
#
# All classes are called from the main class after triggering a specific RadioButton
####################################################################################
#                                        BOTTLENECK
####################################################################################
class Bottleneck(QWidget):        
    def __init__(self):
        super(Bottleneck, self).__init__()
        def get_values():
#    First value = name of the object. If no name is given it will be 'NoName'
#    First range values = Diameter dimensions. 
#                                 They are half of the value and in the negative side of the plane (not essensial choice)
#    Second range values = Length dimensions.
#                                 They are intended just to define the lengths of the object
            V_list[0] = v_list[0].text() if v_list[0].text() != '' else 'NoName' 
            if (v_list[9].text() == '') or (v_list[9]=='0'):
                v_list[9] = v_list[8]
            for i in range(1,7):
                V_list[i] = float(v_list[i].text()) if v_list[i].text() !='' else '0'
            for i in range(7,14):
                V_list[i] = -(float(v_list[i].text())/2) if v_list[i].text() !='' else '0'
            print(V_list)

        Vlayout = QVBoxLayout()
        Hlayout=QHBoxLayout()
        group = QGroupBox()    
        layout = QGridLayout(group)
        layout.setHorizontalSpacing(10)
        l_list=[QLabel("NOME:"), QLabel("L1"), QLabel("L2"), QLabel("L3"), QLabel("Lrim"), QLabel('lRIM'), QLabel('LRIM'), QLabel("Ø Proiettile"), QLabel("Ø Collo"), QLabel("Ø Base Collo"), QLabel("Ø Spalla"), QLabel("Ø Base"), QLabel("ø Fondello "), QLabel("Ø Fondello")]
        v_list =[QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(), QLineEdit()]    
        Hlayout.addWidget(l_list[0])
        Hlayout.addWidget(v_list[0])
        layout.addLayout(Hlayout,0,0)
# the range is defined based on the number of values:
# after the firs 'V_list' element, others are defined in couples
# (only for a better arrangement of the offset)
        for i in range(1,12, 2):
            Hlayout=QHBoxLayout()
            v_list[i].setFixedWidth(50)
            v_list[i+1].setFixedWidth(50)
            Hlayout.addWidget(l_list[i])
            Hlayout.addWidget(v_list[i])
            Hlayout.addWidget(l_list[i+1])
            Hlayout.addWidget(v_list[i+1])
            layout.addLayout(Hlayout,i,0)
# if a value exceed from the couples it will be added 'manually'
        Hlayout=QHBoxLayout()
        Hlayout.addWidget(l_list[-1])
        Hlayout.addWidget(v_list[-1])
        layout.addLayout(Hlayout, 13, 0)
# adding the group (BoxLayout) to the widget
        Vlayout.addWidget(group)               
        button = QPushButton('OK')     
        button.clicked.connect(get_values)
        Vlayout.addWidget(button) 
        self.setLayout(Vlayout)
####################################################################################
#                                        #BOTTLENECK - RIMMMED
####################################################################################
class B_Rimmed(QWidget):        
    def __init__(self):
        super(B_Rimmed, self).__init__()
        def get_values():
            print(check_list)
            V_list[0] = v_list[0].text() if v_list[0].text() != '' else 'NoName' 
            if (v_list[7].text() == '') or (v_list[7]=='0'):
                v_list[7] = v_list[6]
            for i in range(1,5):
                V_list[i] = float(v_list[i].text()) if v_list[i].text() !='' else '0'
            for i in range(5,11):
                V_list[i] = -(float(v_list[i].text())/2) if v_list[i].text() !='' else '0'
            print(V_list)
    
        Vlayout = QVBoxLayout()
        Hlayout=QHBoxLayout()
        group = QGroupBox()    
        layout = QGridLayout(group)
        layout.setHorizontalSpacing(10)
        l_list=[QLabel("NOME:"), QLabel("L1"), QLabel("L2"), QLabel("L3"), QLabel("Lrim"), QLabel("Ø Proiettile"), QLabel("Ø Collo"),QLabel("Ø Base Collo"), QLabel("Ø Spalla"), QLabel("Ø Base"), QLabel("Ø Fondello")]
        v_list =[QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(), QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit()]    
        Hlayout.addWidget(l_list[0])
        Hlayout.addWidget(v_list[0])
        layout.addLayout(Hlayout,0,0)
    
        for i in range(1,10, 2):
            Hlayout=QHBoxLayout()
            v_list[i].setFixedWidth(50)
            v_list[i+1].setFixedWidth(50)
            Hlayout.addWidget(l_list[i])
            Hlayout.addWidget(v_list[i])
            Hlayout.addWidget(l_list[i+1])
            Hlayout.addWidget(v_list[i+1])
            layout.addLayout(Hlayout,i,0)
#        Hlayout=QHBoxLayout()
#        Hlayout.addWidget(l_list[-1])
#        Hlayout.addWidget(v_list[-1])
#        layout.addLayout(Hlayout, 8, 0)
    
        Vlayout.addWidget(group)               
        button = QPushButton('OK')     
        button.clicked.connect(get_values)
        Vlayout.addWidget(button) 
        self.setLayout(Vlayout)
####################################################################################
#                                        BOTTLENECK - BELTED
####################################################################################
class B_Belted(QWidget):        
    def __init__(self):
        super(B_Belted, self).__init__()
        def get_values():
            print(check_list)
            V_list[0] = v_list[0].text() if v_list[0].text() != '' else 'NoName'
            if (v_list[9].text() == '') or (v_list[9]=='0'):
                v_list[9] = v_list[8]
            for i in range(1,7):
                V_list[i] = float(v_list[i].text()) if v_list[i].text() !='' else '0'
            for i in range(7,15):
                V_list[i] = -(float(v_list[i].text())/2) if v_list[i].text() !='' else '0'
            print(V_list)
    
        Vlayout = QVBoxLayout()
        Hlayout=QHBoxLayout()
        group = QGroupBox()    
        layout = QGridLayout(group)
        layout.setHorizontalSpacing(10)
        l_list=[QLabel("NOME:"), QLabel("L1"), QLabel("L2"), QLabel("L3"), QLabel("Lrim"), QLabel('lRIM'), QLabel('LRIM'), QLabel("Ø Proiettile"), QLabel("Ø Collo"), QLabel("Ø Base Collo"), QLabel("Ø Spalla"), QLabel("Ø Base"),  QLabel("Ø Cinturino"), QLabel("ø Fondello "), QLabel("Ø Fondello")]
        v_list =[QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(), QLineEdit()]    
        Hlayout.addWidget(l_list[0])
        Hlayout.addWidget(v_list[0])
        layout.addLayout(Hlayout,0,0)
    
        for i in range(1,14, 2):
            Hlayout=QHBoxLayout()
            v_list[i].setFixedWidth(50)
            v_list[i+1].setFixedWidth(50)
            Hlayout.addWidget(l_list[i])
            Hlayout.addWidget(v_list[i])
            Hlayout.addWidget(l_list[i+1])
            Hlayout.addWidget(v_list[i+1])
            layout.addLayout(Hlayout,i,0)

    
        Vlayout.addWidget(group)               
        button = QPushButton('OK')     
        button.clicked.connect(get_values)
        Vlayout.addWidget(button) 
        self.setLayout(Vlayout)
####################################################################################
#                                        STRAIGHT - RIMMED
####################################################################################
class S_Rimmed(QWidget):        
    def __init__(self):
        super(S_Rimmed, self).__init__()   
        def get_values():
            if (v_list[5].text() == '') or (v_list[5]=='0'):
                v_list[5] = v_list[4]
            print(check_list)
            V_list[0] = v_list[0].text() if v_list[0].text() != '' else 'NoName' 
            V_list[1] = float(v_list[1].text()) if v_list[1].text() !='' else '0'
            V_list[2] = float(v_list[2].text()) if v_list[2].text() !='' else '0'
            for i in range(3,7):
                V_list[i] = -(float(v_list[i].text())/2) if v_list[i].text() !='' else '0'
            print(V_list)
    
        Vlayout = QVBoxLayout()
        Hlayout=QHBoxLayout()
        group = QGroupBox()    
        layout = QGridLayout(group)
        layout.setHorizontalSpacing(10)
        l_list=[QLabel("NOME:"), QLabel("L1"), QLabel("Lrim"),  QLabel("Ø Proiettile"), QLabel("Ø Collo"), QLabel("Ø Base"), QLabel("Ø Fondello")]
        v_list =[QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit()]    
        Hlayout.addWidget(l_list[0])
        Hlayout.addWidget(v_list[0])
        layout.addLayout(Hlayout,0,0)
    
        for i in range(1,6, 2):
            Hlayout=QHBoxLayout()
            v_list[i].setFixedWidth(50)
            v_list[i+1].setFixedWidth(50)
            Hlayout.addWidget(l_list[i])
            Hlayout.addWidget(v_list[i])
            Hlayout.addWidget(l_list[i+1])
            Hlayout.addWidget(v_list[i+1])
            layout.addLayout(Hlayout,i,0)
    
        Vlayout.addWidget(group)               
        button = QPushButton('OK')     
        button.clicked.connect(get_values)
        Vlayout.addWidget(button) 
        self.setLayout(Vlayout)
####################################################################################
#                                            STRAIGHT
####################################################################################
class Straight(QWidget):        
    def __init__(self):
        super(Straight, self).__init__()   
        def get_values():
            if (v_list[7].text() == '') or (v_list[7]=='0'):
                v_list[7] = v_list[6]
            print(check_list)
            V_list[0] = v_list[0].text() if v_list[0].text() != '' else 'NoName' 
            for i in range(1,5):
                V_list[i] = float(v_list[i].text()) if v_list[i].text() !='' else '0'
            for i in range(5,10):
                V_list[i] = -(float(v_list[i].text())/2) if v_list[i].text() !='' else '0'
            print(V_list)

        Vlayout = QVBoxLayout()
        Hlayout=QHBoxLayout()
        group = QGroupBox()    
        layout = QGridLayout(group)
        layout.setHorizontalSpacing(10)
        l_list=[QLabel("NOME:"), QLabel("L1"), QLabel("Lrim"), QLabel('lRIM'), QLabel('LRIM'), QLabel("Ø Proiettile"), QLabel("Ø Collo"), QLabel("Ø Base"), QLabel("ø Fondello "), QLabel("Ø Fondello")]
        v_list =[QLineEdit(),QLineEdit(), QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit()]    
        Hlayout.addWidget(l_list[0])
        Hlayout.addWidget(v_list[0])
        layout.addLayout(Hlayout,0,0)

        for i in range(1,8,2):
            Hlayout=QHBoxLayout()
            v_list[i].setFixedWidth(50)
            v_list[i+1].setFixedWidth(50)
            Hlayout.addWidget(l_list[i])
            Hlayout.addWidget(v_list[i])
            Hlayout.addWidget(l_list[i+1])
            Hlayout.addWidget(v_list[i+1])
            layout.addLayout(Hlayout,i,0)
        Hlayout=QHBoxLayout()
        Hlayout.addWidget(l_list[-1])
        Hlayout.addWidget(v_list[-1])
        layout.addLayout(Hlayout, 8,0 )

        Vlayout.addWidget(group)               
        button = QPushButton('OK')     
        button.clicked.connect(get_values)
        Vlayout.addWidget(button) 
        self.setLayout(Vlayout)
####################################################################################
#                                        STRAIGHT BELTED
####################################################################################
class B_Straight(QWidget):
    def __init__(self):
        super(B_Straight, self).__init__()   
        def get_values():
            if (v_list[7].text() == '') or (v_list[7]=='0'):
                v_list[7] = v_list[6]
            print(check_list)
            V_list[0] = v_list[0].text() if v_list[0].text() != '' else 'NoName' 
            for i in range(1,5):
                V_list[i] = float(v_list[i].text()) if v_list[i].text() !='' else '0'
            for i in range(5,11):
                V_list[i] = -(float(v_list[i].text())/2) if v_list[i].text() !='' else '0'
            print(V_list)

        Vlayout = QVBoxLayout()
        Hlayout=QHBoxLayout()
        group = QGroupBox()    
        layout = QGridLayout(group)
        layout.setHorizontalSpacing(10)
        l_list=[QLabel("NOME:"), QLabel("L1"), QLabel("Lrim"), QLabel('lRIM'), QLabel('LRIM'), QLabel("Ø Proiettile"), QLabel("Ø Collo"), QLabel("Ø Base"), QLabel("Ø Cinturino"),QLabel("ø Fondello "), QLabel("Ø Fondello")]
        v_list =[QLineEdit(),QLineEdit(), QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit()]    
        Hlayout.addWidget(l_list[0])
        Hlayout.addWidget(v_list[0])
        layout.addLayout(Hlayout,0,0)

        for i in range(1,10,2):
            Hlayout=QHBoxLayout()
            v_list[i].setFixedWidth(50)
            v_list[i+1].setFixedWidth(50)
            Hlayout.addWidget(l_list[i])
            Hlayout.addWidget(v_list[i])
            Hlayout.addWidget(l_list[i+1])
            Hlayout.addWidget(v_list[i+1])
            layout.addLayout(Hlayout,i,0)
    
    
        Vlayout.addWidget(group)               
        button = QPushButton('OK')     
        button.clicked.connect(get_values)
        Vlayout.addWidget(button) 
        self.setLayout(Vlayout)
####################################################################################
#                                        MAIN CLASS
####################################################################################
class AmmoMaker(QWidget):       
    def __init__(self):
        super(AmmoMaker, self).__init__()
        self.setWindowTitle('CartridgeMaker')
# Defining all the buttons and relative groups
        self.group = QGroupBox()
        self.group2 = QGroupBox()
        self.group3 = QGroupBox()
        self.gp = QGridLayout(self.group)
        self.gp2 = QGridLayout(self.group2)
        self.gp3 = QGridLayout(self.group3)
        self.opt1 = QRadioButton('Small')
        self.opt2 = QRadioButton('Large')
        self.opt3 = QRadioButton('Rimfire')
        self.ck1 = QRadioButton('Boxer',)
        self.ck2 = QRadioButton('Berdan') 
        self.form1 = QRadioButton('Bottleneck')
        self.form2 = QRadioButton('Straight')
        self.form3 = QRadioButton('Rimmed')
        self.form4 = QRadioButton('Belted')
        self.form5 = QRadioButton('Rimmed')
        self.form6 = QRadioButton('Belted')
# connecting the buttons to specific functions
        self.ck1.clicked.connect(self.check)
        self.ck2.clicked.connect(self.check)
        self.opt1.clicked.connect(self.check2)
        self.opt2.clicked.connect(self.check2)
        self.opt3.clicked.connect(self.check2)
        self.form1.clicked.connect(self.class_value)
        self.form2.clicked.connect(self.class_value)
        self.form3.clicked.connect(self.class_value)
        self.form4.clicked.connect(self.class_value)
        self.form5.clicked.connect(self.class_value)
        self.form6.clicked.connect(self.class_value)
# adjusting the offset using a grid
        self.gp.addWidget(self.form1, 0, 0)
        self.gp.addWidget(self.form2, 0, 1)
        self.gp.addWidget(self.form3, 1, 0)
        self.gp.addWidget(self.form5, 1, 1)
        self.gp.addWidget(self.form4, 2, 0)
        self.gp.addWidget(self.form6, 2, 1)
        self.gp2.addWidget(self.opt1, 0, 0)
        self.gp2.addWidget(self.opt2, 0, 1)
        self.gp2.addWidget(self.opt3, 1, 0)
        self.gp3.addWidget(self.ck1, 0, 0)
        self.gp3.addWidget(self.ck2, 0, 1)
# defining an error message which will raise if a sketch or an object is unable to be created
        self.error_msg = QMessageBox()
        self.error_msg.setIcon(QMessageBox.Critical)
        self.error_msg.setText('Wrong settings')
        self.error_msg.setWindowTitle('Error')

        self.group_layout = QGridLayout(self.group)
        self.button = QPushButton('Crea!')
        self.button.clicked.connect(self.get_elements)
        self.group_layout.addWidget(self.group, 0, 0)
        self.group_layout.addWidget(self.group2, 0, 1)
        self.group_layout.addWidget(self.group3, 1, 1)
        self.group_layout.addWidget(self.button, 2, 1)
        self.group_layout.addWidget(Bottleneck(), 1, 0)
        self.setLayout(self.group_layout)
        self.show()
# if a cartridge class is called, the last element of the grid will be deleted recreating the wanted class' offset
    def class_value(self):
        if (self.form1.isChecked()): #Bottleneck  
            self.group_layout.itemAt(4).widget().deleteLater()
            self.group_layout.addWidget(Bottleneck(), 1, 0)
            check_list[3] = 1
        elif (self.form2.isChecked()): #Straight
            check_list[3] = 2
            self.group_layout.itemAt(4).widget().deleteLater()
            self.group_layout.addWidget(Straight(), 1, 0)
        elif(self.form3.isChecked()):  #Bottleneck_Rimmed
            check_list[3] = 3
            self.group_layout.itemAt(4).widget().deleteLater()
            self.group_layout.addWidget(B_Rimmed(), 1,0)
        elif(self.form4.isChecked()):  #Bottleneck_Belted
            check_list[3] = 4
            self.group_layout.itemAt(4).widget().deleteLater()
            self.group_layout.addWidget(B_Belted(), 1,0)
        elif(self.form5.isChecked()):  #Straight_Rimmed
            check_list[3] = 5
            self.group_layout.itemAt(4).widget().deleteLater()
            self.group_layout.addWidget(S_Rimmed(), 1,0)        
        elif(self.form6.isChecked()):  #Straight_Belted
            check_list[3] = 6
            self.group_layout.itemAt(4).widget().deleteLater()
            self.group_layout.addWidget(B_Straight(), 1,0)

    def check(self):
        if self.ck1.isChecked():
            check_list[1] = 0
        elif self.ck2.isChecked():
            check_list[1] = 1
    def check2(self):
        if self.opt1.isChecked():
            check_list[0] = 1
        elif self.opt2.isChecked():
            check_list[0] = 2
        elif self.opt3.isChecked():
            check_list[0] = 0

              
    def get_elements(self):

        print(check_list)
        print(V_list, end=' + ')
        print(_Doc_)
        ints=[str(i) for i in range(10)]
        if (V_list[0][:1]=='.') or (V_list[0][:1] in ints ) :  
            new_val =  'Cartridge'
        else:
             new_val = V_list[0]
        
        #Origin='Origin'+str(t)+'.'+Plane+'.'
        sketch_name= new_val+'_base'#time.strftime('_%H:%M:%S')

        obj = App.activeDocument().addObject("PartDesign::Body",new_val)
        Gui.activateView('Gui::View3DInventor', True) 
        #Gui.ActiveDocument.ActiveView.getActiveObject('pdbody')
        Gui.activeView().setActiveObject('pdbody',obj)
        Gui.Selection.clearSelection()
        Gui.Selection.addSelection(obj)
        App.ActiveDocument.recompute()
        #Gui.Selection.addSelection(_Doc_,new_val,Origin)
        #print(_Doc_ + ' ' + new_val + ' ' + Origin)
        plane= [o.Label for o in obj.Origin.OriginFeatures if o.Role == 'XZ_Plane'][0]
        #obj.newObject('Sketcher::SketchObject',sketch_name)
        App.getDocument(_Doc_).getObject(new_val).newObject('Sketcher::SketchObject',sketch_name)
        App.getDocument(_Doc_).getObject(sketch_name).Support = (App.getDocument(_Doc_).getObject(plane),[''])
        App.getDocument(_Doc_).getObject(sketch_name).MapMode = 'FlatFace'
        App.getDocument(_Doc_).getObject(new_val).Label = V_list[0]
        App.ActiveDocument.recompute()

####################################################################################
#
#                                                         Bottleneck Rimless    
#
####################################################################################
#      1  2  3     
        if check_list[3] == 1:        
            if V_list[2]<V_list[3]:
                V_list[2]= V_list[1]-V_list[2]
                print(V_list[2])
            else:
                pass
            k= V_list[8]-V_list[7]
            ExtGeoList = [
            Part.LineSegment(App.Vector(V_list[7], V_list[1]), App.Vector(V_list[8], V_list[1])),
            Part.LineSegment(App.Vector(V_list[8], V_list[1]), App.Vector(V_list[9], V_list[2])),
            Part.LineSegment(App.Vector(V_list[9], V_list[2]), App.Vector(V_list[10], V_list[3])),
            Part.LineSegment(App.Vector(V_list[10], V_list[3]), App.Vector(V_list[11], V_list[6])),
            Part.LineSegment(App.Vector(V_list[11], V_list[6]), App.Vector(V_list[12], (V_list[4]+V_list[5]))),
            Part.LineSegment(App.Vector(V_list[12], (V_list[4]+V_list[5])), App.Vector(V_list[12], V_list[4])),
            Part.LineSegment(App.Vector(V_list[12], V_list[4]), App.Vector(V_list[13], V_list[4])),
            Part.LineSegment(App.Vector(V_list[13], V_list[4]),App.Vector(V_list[13],0))
            ]
            
            ExtConstList = [
            Sketcher.Constraint('Horizontal',0), Sketcher.Constraint('Coincident',0,2,1,1),
            Sketcher.Constraint('Coincident',1,2,2,1), Sketcher.Constraint('Coincident',2,2,3,1),
            Sketcher.Constraint('Vertical',3), Sketcher.Constraint('Coincident',3,2,4,1), 
            Sketcher.Constraint('Coincident',4,2,5,1), Sketcher.Constraint('Coincident',5,2,6,1),
            Sketcher.Constraint('Vertical',5),Sketcher.Constraint('Horizontal',6),Sketcher.Constraint('Vertical',7),
            Sketcher.Constraint('Coincident',6,2,7,1), Sketcher.Constraint('Coincident', 7,2,8,1),
            ]
            if check_list[0] == 1:    
                a = sb
            elif check_list[0] == 2:
                a = lb
            else:
                 self.error_msg.setInformativeText('Rimless cannot be Rimfire')
                 self.error_msg.show()
                 App.getDocument(_Doc_).getObject(new_val).removeObjectsFromDocument()
                 App.getDocument(_Doc_).removeObject(new_val)

            if check_list[1] == 0:          
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[13], 0), App.Vector(a, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(a, 0), App.Vector(a, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(a, 2.7), App.Vector(-1.5, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, 2.7), App.Vector(-1.5, V_list[6])))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, V_list[6]), App.Vector(V_list[11]-(V_list[10]-V_list[9]), V_list[6])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[11]-(V_list[10]-V_list[9]), V_list[6]), App.Vector(V_list[10]-k, V_list[3])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10]-k, V_list[3]), App.Vector(V_list[9]-k, V_list[2])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[9]-k, V_list[2]), App.Vector(V_list[7], V_list[1])))
                ExtConstList.append( Sketcher.Constraint('Coincident',8,2,9,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',9,2,10,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',10,2,11,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',11,2,12,1))    
                ExtConstList.append( Sketcher.Constraint('Coincident',12,2,13,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',13,2,14,1))   
                ExtConstList.append(Sketcher.Constraint('Coincident',14,2,15,1))  
                ExtConstList.append(Sketcher.Constraint('Coincident',15,2,0,1))     
            elif check_list[1] == 1:
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[13], 0), App.Vector(a, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(a, 0), App.Vector(a, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(a, 2.7), App.Vector(-1.5, 2.7)))
                ExtGeoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(0,2.7,0),App.Vector(0,0,1),1.5),3.141593,4.716321))
                ExtGeoList.append(Part.LineSegment(App.Vector(0, 1.2), App.Vector(0, V_list[6])))
                ExtGeoList.append(Part.LineSegment(App.Vector(0, V_list[6]), App.Vector(a, V_list[6])))
                ExtGeoList.append(Part.LineSegment(App.Vector(a, V_list[6]), App.Vector(V_list[10]-k, V_list[3]/2)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10]-k, V_list[3]/2),App.Vector(V_list[10]-k, V_list[3])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10]-k, V_list[3]), App.Vector(V_list[9]-k, V_list[2])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[9]-k, V_list[2]), App.Vector(V_list[7], V_list[1])))
                ExtConstList.append( Sketcher.Constraint('Coincident',8,2,9,1))
                ExtConstList.append( Sketcher.Constraint('Coincident',9,2,10,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',10,2,11,1))
                ExtConstList.append( Sketcher.Constraint('Coincident',11,2,12,1))
                ExtConstList.append( Sketcher.Constraint('Coincident',12,2,13,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',13,2,14,1))   
                ExtConstList.append(Sketcher.Constraint('Coincident',14,2,15,1))  
                ExtConstList.append(Sketcher.Constraint('Coincident',15,2,16,1))  
                ExtConstList.append(Sketcher.Constraint('Coincident',16,2,17,1))   
                ExtConstList.append(Sketcher.Constraint('Coincident',17,2,0,1)) 
                ExtConstList.append(Sketcher.Constraint('PointOnObject',11,2,-2))                
                print('all constrs done')         
            trim_vals = 7,8,(V_list[13], V_list[4]/3), (V_list[12],0)
                #ExtGeoList.append(Part.LineSegment(App.Vector(V_list[12], 0), App.Vector(0, 0)))

######################
#     Straight Rimless     
######################   
#      1  2  3 
        elif check_list[3] == 2:
            ExtGeoList = [
            Part.LineSegment(App.Vector(V_list[5], V_list[1]), App.Vector(V_list[6], V_list[1])),
            Part.LineSegment(App.Vector(V_list[6], V_list[1]), App.Vector(V_list[7], V_list[4])),
            Part.LineSegment(App.Vector(V_list[7], V_list[4]), App.Vector(V_list[8], (V_list[2]+V_list[3]))),
            Part.LineSegment(App.Vector(V_list[8], (V_list[2]+V_list[3])), App.Vector(V_list[8], V_list[2])),
            Part.LineSegment(App.Vector(V_list[8], V_list[2]), App.Vector(V_list[9], V_list[2])),
            Part.LineSegment(App.Vector(V_list[9], V_list[2]), App.Vector(V_list[9], 0)),
            ]
            ExtConstList = [
            Sketcher.Constraint('Coincident',0,2,1,1), Sketcher.Constraint('Coincident',1,2,2,1), 
            Sketcher.Constraint('Coincident',2,2,3,1), Sketcher.Constraint('Coincident',3,2,4,1),
            Sketcher.Constraint('Coincident',4,2,5,1)
            ]
            if check_list[0] == 1:
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[9], 0), App.Vector(sb, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 0), App.Vector(sb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 2.7), App.Vector(-1.5, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, 2.7), App.Vector(-1.5, V_list[4]+1)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, V_list[4]+1), App.Vector(V_list[6]/2 , V_list[1]/4)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[6]/2 , V_list[1]/4), App.Vector(V_list[5], V_list[1]/4)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[5] , V_list[1]/4), App.Vector(V_list[5], V_list[1])))
                ExtConstList.append(Sketcher.Constraint('Coincident',5,2,6,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',6,2,7,1)) 
                ExtConstList.append(Sketcher.Constraint('Coincident',7,2,8,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',8,2,9,1)) 
                ExtConstList.append(Sketcher.Constraint('Coincident',9,2,10,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',10,2,11,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',11,2,12,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',12,2,0,1)) 
            elif check_list[0] == 2:
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[9], 0), App.Vector(lb, 0)))
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 0),App.Vector(lb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 2.7), App.Vector(-1.5, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, 2.7), App.Vector(-1.5, V_list[4]+1)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, V_list[4]+1), App.Vector(V_list[6]/2 , V_list[1]/4)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[6]/2 , V_list[1]/4), App.Vector(V_list[5], V_list[1]/4)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[5] , V_list[1]/4), App.Vector(V_list[5], V_list[1])))
                ExtConstList.append(Sketcher.Constraint('Coincident',5,2,6,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',6,2,7,1)) 
                ExtConstList.append(Sketcher.Constraint('Coincident',7,2,8,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',8,2,9,1)) 
                ExtConstList.append(Sketcher.Constraint('Coincident',9,2,10,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',10,2,11,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',11,2,12,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',12,2,0,1)) 
            else:
                 self.error_msg.setInformativeText('Rimless cannot be Rimfire')
                 self.error_msg.show()
                 App.getDocument(_Doc_).getObject(new_val).removeObjectsFromDocument()
                 App.getDocument(_Doc_).removeObject(new_val)
                #ExtGeoList.append(Part.LineSegment(App.Vector(V_list[9], 0), App.Vector(0, 0)))
            trim_vals = 5,6,(V_list[9], V_list[2]/3), (V_list[8],0)

#######################
#     Bottleneck Rimmed    
#######################
#      1  2  3        
        if check_list[3] == 3:        
            if V_list[2]<V_list[3]:
                V_list[2]= V_list[1]-V_list[2]
            else:
                pass
            ExtGeoList = [
            Part.LineSegment(App.Vector(V_list[5], V_list[1]), App.Vector(V_list[6], V_list[1])),
            Part.LineSegment(App.Vector(V_list[6], V_list[1]), App.Vector(V_list[7], V_list[2])),
            Part.LineSegment(App.Vector(V_list[7], V_list[2]), App.Vector(V_list[8], V_list[3])),
            Part.LineSegment(App.Vector(V_list[8], V_list[3]), App.Vector(V_list[9], V_list[4])),
            Part.LineSegment(App.Vector(V_list[9], V_list[4]), App.Vector(V_list[10], V_list[4])),
            Part.LineSegment(App.Vector(V_list[10], V_list[4]), App.Vector(V_list[10], 0)),
            ]
            
            ExtConstList = [
            Sketcher.Constraint('Coincident',0,2,1,1), Sketcher.Constraint('Coincident',1,2,2,1), 
            Sketcher.Constraint('Coincident',2,2,3,1), Sketcher.Constraint('Coincident',3,2,4,1), 
            Sketcher.Constraint('Coincident',4,2,5,1)
            ]
            if check_list[0] == 1:
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10], 0), App.Vector(sb, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 0), App.Vector(sb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 2.7), App.Vector(-(4.45/3), 2.7))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(-(4.45/3), 2.7), App.Vector(-(4.45/3), 4.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-(4.45/3), 4.7), App.Vector(V_list[8]-(V_list[7]-V_list[6]), 4.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[8]-(V_list[7]-V_list[6]), 4.7), App.Vector(V_list[8]-(V_list[7]-V_list[5]), V_list[3])))                
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[8]-(V_list[7]-V_list[5]), V_list[3]), App.Vector(V_list[7]-(V_list[7]-V_list[5]), V_list[2])))                
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[7]-(V_list[7]-V_list[5]), V_list[2]), App.Vector(V_list[5], V_list[1])))                
                ExtConstList.append( Sketcher.Constraint('Coincident',5,2,6,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',6,2,7,1))   
                ExtConstList.append( Sketcher.Constraint('Coincident',7,2,8,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',8,2,9,1)) 
                ExtConstList.append( Sketcher.Constraint('Coincident',9,2,10,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',10,2,11,1)) 
                ExtConstList.append( Sketcher.Constraint('Coincident',11,2,12,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',12,2,13,1))     
                ExtConstList.append(Sketcher.Constraint('Coincident',13,2,0,1))     

            elif check_list[0] == 2:
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10], 0), App.Vector(lb, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 0), App.Vector(lb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 2.7), App.Vector(-(4.45/3), 2.7))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(-(4.45/3), 2.7), App.Vector(-(4.45/3), 4.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-(4.45/3), 4.7), App.Vector(V_list[8]-(V_list[7]-V_list[6]), 4.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[8]-(V_list[7]-V_list[6]), 4.7), App.Vector(V_list[8]-(V_list[7]-V_list[5]), V_list[3])))                
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[8]-(V_list[7]-V_list[5]), V_list[3]), App.Vector(V_list[7]-(V_list[7]-V_list[5]), V_list[2])))                
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[7]-(V_list[7]-V_list[5]), V_list[2]), App.Vector(V_list[5], V_list[1])))                
                ExtConstList.append( Sketcher.Constraint('Coincident',5,2,6,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',6,2,7,1))   
                ExtConstList.append( Sketcher.Constraint('Coincident',7,2,8,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',8,2,9,1)) 
                ExtConstList.append( Sketcher.Constraint('Coincident',9,2,10,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',10,2,11,1)) 
                ExtConstList.append( Sketcher.Constraint('Coincident',11,2,12,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',12,2,13,1))     
                ExtConstList.append(Sketcher.Constraint('Coincident',13,2,0,1))                  
            else:
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10], 0), App.Vector(0, 0)))
                ExtGeoList.append(Part.LineSegment(App.Vector(0,0), App.Vector(0,  V_list[4]/3)))
                ExtGeoList.append(Part.LineSegment(App.Vector(0,V_list[4]/3), App.Vector(V_list[10]-(V_list[10]-V_list[8]),  V_list[4]/3)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10]-(V_list[10]-V_list[8]),V_list[4]/3), App.Vector(V_list[8] - (V_list[7]-V_list[5]), V_list[3])))
                ExtGeoList.append(Part.LineSegment(App.Vector(App.Vector(V_list[8] - (V_list[7]-V_list[5]), V_list[3])), App.Vector(V_list[7]-(V_list[7]-V_list[5]), V_list[2])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[7]-(V_list[7]-V_list[5]), V_list[2]), App.Vector(V_list[5], V_list[1])))
                ExtConstList.append( Sketcher.Constraint('Coincident',5,2,6,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',6,2,7,1))   
                ExtConstList.append( Sketcher.Constraint('Coincident',7,2,8,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',8,2,9,1)) 
                ExtConstList.append(Sketcher.Constraint('Coincident',9,2,10,1)) 
                ExtConstList.append(Sketcher.Constraint('Coincident',10,2,11,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',11,2,0,1))  
            trim_vals = 5,6,(V_list[10], V_list[4]/3), (V_list[9],0)

#######################
#     Bottleneck Belted
#######################   
#      1  2  3     
        if check_list[3] == 4:        
            if V_list[2]<V_list[3]:
                V_list[2]= V_list[1]-V_list[2]
            else:
                pass
            ExtGeoList = [
            Part.LineSegment(App.Vector(V_list[7], V_list[1]), App.Vector(V_list[8], V_list[1])),
            Part.LineSegment(App.Vector(V_list[8], V_list[1]), App.Vector(V_list[9], V_list[2])),
            Part.LineSegment(App.Vector(V_list[9], V_list[2]), App.Vector(V_list[10], V_list[3])),
            Part.LineSegment(App.Vector(V_list[10], V_list[3]), App.Vector(V_list[11], V_list[6])),
            Part.LineSegment(App.Vector(V_list[11], V_list[6]), App.Vector(V_list[12], V_list[6])),
            Part.LineSegment(App.Vector(V_list[12], V_list[6]), App.Vector(V_list[12], V_list[6]-(V_list[6]/3))), #App.Vector(V_list[12], (V_list[6]-V_list[5]-V_list[4])/2))
            Part.LineSegment(App.Vector(V_list[12], V_list[6]-(V_list[6]/3)), App.Vector(V_list[13], V_list[5]+ V_list[4])),
            Part.LineSegment(App.Vector(V_list[13], V_list[5]+ V_list[4]), App.Vector(V_list[13], V_list[4])),
            Part.LineSegment(App.Vector(V_list[13], V_list[4]), App.Vector(V_list[14], V_list[4])),
            Part.LineSegment(App.Vector(V_list[14], V_list[4]), App.Vector(V_list[14], 0))
            ]
            
            ExtConstList = [
            Sketcher.Constraint('Coincident',0,2,1,1), Sketcher.Constraint('Coincident',1,2,2,1), 
            Sketcher.Constraint('Coincident',2,2,3,1), Sketcher.Constraint('Coincident',3,2,4,1), 
            Sketcher.Constraint('Coincident',4,2,5,1), Sketcher.Constraint('Coincident',5,2,6,1),
            Sketcher.Constraint('Coincident',6,2,7,1), Sketcher.Constraint('Coincident',7,2,8,1),
            Sketcher.Constraint('Coincident',8,2,9,1)
            ]
            if check_list[0] == 1:
                k = V_list[8] -V_list[7]
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[14], 0), App.Vector(sb, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 0), App.Vector(sb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 2.7), App.Vector(-1.5, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, 2.7), App.Vector(-1.5, V_list[6])))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, V_list[6]), App.Vector(V_list[11]-(V_list[10]-V_list[9]), V_list[6])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[11]-(V_list[10]-V_list[9]), V_list[6]), App.Vector(V_list[10]-k, V_list[3])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10]-k, V_list[3]), App.Vector(V_list[9]-k, V_list[2])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[9]-k, V_list[2]), App.Vector(V_list[7], V_list[1])))               
                ExtConstList.append( Sketcher.Constraint('Coincident',9,2,10,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',10,2,11,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',11,2,12,1))    
                ExtConstList.append( Sketcher.Constraint('Coincident',12,2,13,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',13,2,14,1))    
                ExtConstList.append( Sketcher.Constraint('Coincident',14,2,15,1))      
                ExtConstList.append( Sketcher.Constraint('Coincident',15,2,16,1))    
                ExtConstList.append( Sketcher.Constraint('Coincident',16,2,17,1))      
                ExtConstList.append( Sketcher.Constraint('Coincident',17,2,0,1))    
               
            elif check_list[0] == 2:
                k = V_list[8] -V_list[7]
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[14], 0), App.Vector(lb, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 0), App.Vector(lb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 2.7), App.Vector(-1.5, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, 2.7), App.Vector(-1.5, V_list[6])))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, V_list[6]), App.Vector(V_list[11]-(V_list[10]-V_list[9]), V_list[6])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[11]-(V_list[10]-V_list[9]), V_list[6]), App.Vector(V_list[10]-k, V_list[3])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10]-k, V_list[3]), App.Vector(V_list[9]-k, V_list[2])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[9]-k, V_list[2]), App.Vector(V_list[7], V_list[1])))               
                ExtConstList.append( Sketcher.Constraint('Coincident',9,2,10,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',10,2,11,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',11,2,12,1))    
                ExtConstList.append( Sketcher.Constraint('Coincident',12,2,13,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',13,2,14,1))    
                ExtConstList.append( Sketcher.Constraint('Coincident',14,2,15,1))      
                ExtConstList.append( Sketcher.Constraint('Coincident',15,2,16,1))    
                ExtConstList.append( Sketcher.Constraint('Coincident',16,2,17,1))      
                ExtConstList.append( Sketcher.Constraint('Coincident',17,2,0,1))        
            else:
                 self.error_msg.setInformativeText('Belted cannot be Rimfire')
                 self.error_msg.show()
                 App.getDocument(_Doc_).getObject(new_val).removeObjectsFromDocument()
                 App.getDocument(_Doc_).removeObject(new_val)
            trim_vals = 9,10,(V_list[14], V_list[4]/3), (V_list[13],0)
                #ExtGeoList.append(Part.LineSegment(App.Vector(V_list[14], 0), App.Vector(0, 0)))

#######################
#     Straight Belted   
#######################  
#      1  2  3 
        if check_list[3] == 6:     
            ExtGeoList = [
            Part.LineSegment(App.Vector(V_list[5], V_list[1]), App.Vector(V_list[6], V_list[1])),
            Part.LineSegment(App.Vector(V_list[6], V_list[1]), App.Vector(V_list[7], V_list[4])),
            Part.LineSegment(App.Vector(V_list[7], V_list[4]), App.Vector(V_list[8], V_list[4])),
            Part.LineSegment(App.Vector(V_list[8], V_list[4]), App.Vector(V_list[8], V_list[4]-(V_list[4]/3))),
            Part.LineSegment(App.Vector(V_list[8], V_list[4]-(V_list[4]/3)), App.Vector(V_list[9], V_list[3]+V_list[2])),
            Part.LineSegment(App.Vector(V_list[9], V_list[3]+V_list[2]), App.Vector(V_list[9], V_list[2])),
            Part.LineSegment(App.Vector(V_list[9], V_list[2]), App.Vector(V_list[10], V_list[2])),
            Part.LineSegment(App.Vector(V_list[10], V_list[2]), App.Vector(V_list[10], 0)),
            ]
            ExtConstList = [
            Sketcher.Constraint('Coincident',0,2,1,1), Sketcher.Constraint('Coincident',1,2,2,1), 
            Sketcher.Constraint('Coincident',2,2,3,1), Sketcher.Constraint('Coincident',3,2,4,1), 
            Sketcher.Constraint('Coincident',4,2,5,1), Sketcher.Constraint('Coincident',5,2,6,1), 
            Sketcher.Constraint('Coincident',6,2,7,1), Sketcher.Constraint('Coincident',7,2,8,1), 
            ]
            if check_list[0] == 1:
                k = V_list[6] -V_list[5]
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10], 0), App.Vector(sb, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 0), App.Vector(sb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 2.7), App.Vector(-1.5, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, 2.7), App.Vector(-1.5, V_list[4]-(V_list[4]/3))))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, V_list[4]-V_list[4]/3),  App.Vector(V_list[7]/2, V_list[4])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[7]/2, V_list[4]), App.Vector(V_list[7]-k, V_list[4])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[7]-k, V_list[4]), App.Vector(V_list[5], V_list[1])))                 
                ExtConstList.append( Sketcher.Constraint('Coincident',8,2,9,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',10,2,11,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',11,2,12,1))    
                ExtConstList.append( Sketcher.Constraint('Coincident',12,2,13,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',13,2,14,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',14,2,0,1))  
               
            elif check_list[0] == 2:
                k = V_list[6] -V_list[5]
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[10], 0), App.Vector(lb, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 0), App.Vector(lb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 2.7), App.Vector(-1.5, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, 2.7), App.Vector(-1.5, V_list[4])))
                ExtGeoList.append(Part.LineSegment(App.Vector(-1.5, V_list[4]),  App.Vector(V_list[7]-k, V_list[4])))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[7]-k, V_list[4]), App.Vector(V_list[5], V_list[1])))               
                ExtConstList.append( Sketcher.Constraint('Coincident',8,2,9,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',10,2,11,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',11,2,12,1))    
                ExtConstList.append( Sketcher.Constraint('Coincident',12,2,13,1))       
                ExtConstList.append( Sketcher.Constraint('Coincident',13,2,0,1))       
            else:
                 self.error_msg.setInformativeText('Belted cannot be Rimfire')
                 self.error_msg.show()
                 App.getDocument(_Doc_).getObject(new_val).removeObjectsFromDocument()
                 App.getDocument(_Doc_).removeObject(new_val)
            trim_vals = 7,8,(V_list[9], V_list[2]/3), (V_list[10],0)
                #ExtGeoList.append(Part.LineSegment(App.Vector(V_list[14], 0), App.Vector(0, 0)))


#######################
#     Straight Rimmed   
#######################  
#      1  2  3 
        elif check_list[3] == 5:
            ExtGeoList = [
            Part.LineSegment(App.Vector(V_list[3], V_list[1]), App.Vector(V_list[4], V_list[1])),
            Part.LineSegment(App.Vector(V_list[4], V_list[1]), App.Vector(V_list[5], V_list[2])),
            Part.LineSegment(App.Vector(V_list[5], V_list[2]), App.Vector(V_list[6], V_list[2])),
            Part.LineSegment(App.Vector(V_list[6], V_list[2]), App.Vector(V_list[6], 0)),
            ]
            ExtConstList = [
            Sketcher.Constraint('Coincident',0,2,1,1), Sketcher.Constraint('Coincident',1,2,2,1), 
            Sketcher.Constraint('Coincident',2,2,3,1)
            ]
            if check_list[0] == 1:
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[6], 0), App.Vector(sb, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 0), App.Vector(sb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(sb, 2.7), App.Vector( -(4.45/3), 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-(4.45/3), 2.7), App.Vector(-(4.45/3), 4.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-(4.45/3), 4.7), App.Vector(V_list[3], 4.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[3], 4.7), App.Vector(V_list[3], V_list[1])))
                ExtConstList.append(Sketcher.Constraint('Coincident',3,2,4,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',4,2,5,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',5,2,6,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',6,2,7,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',7,2,8,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',8,2,9,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',9,2,0,1)) 
            elif check_list[0] == 2:
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[6], 0), App.Vector(lb, 0))) 
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 0), App.Vector(lb, 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(lb, 2.7), App.Vector( -(5.33/3), 2.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-(5.33/3), 2.7), App.Vector(-(5.33/3), 4.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(-(5.33/3), 4.7), App.Vector(V_list[3], 4.7)))
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[3], 4.7), App.Vector(V_list[3], V_list[1])))
                ExtConstList.append(Sketcher.Constraint('Coincident',3,2,4,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',4,2,5,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',5,2,6,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',6,2,7,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',7,2,8,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',8,2,9,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',9,2,0,1)) 
            else:
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[6], 0), App.Vector(0, 0)))
                ExtGeoList.append(Part.LineSegment(App.Vector(0, 0), App.Vector( 0, V_list[2]/2)))
                ExtGeoList.append(Part.LineSegment(App.Vector(0, V_list[2]/2), App.Vector(V_list[3], V_list[2]/2)))   
                ExtGeoList.append(Part.LineSegment(App.Vector(V_list[3], V_list[2]/2), App.Vector(V_list[3], V_list[1]))) 
                ExtConstList.append(Sketcher.Constraint('Coincident',3,2,4,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',4,2,5,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',5,2,6,1))
                ExtConstList.append(Sketcher.Constraint('Coincident',6,2,7,1))   
                ExtConstList.append(Sketcher.Constraint('Coincident',7,2,0,1))     
            trim_vals = 3,4,(V_list[6], V_list[2]/3), (V_list[5],0)       
        
        Rev = sketch_name+'_revolution'
        try:
            App.getDocument(_Doc_).getObject(sketch_name).addGeometry(ExtGeoList,False)            
            App.getDocument(_Doc_).getObject(sketch_name).addConstraint(ExtConstList)
            try:
                App.getDocument(_Doc_).getObject(sketch_name).addGeometry(Part.LineSegment(App.Vector(trim_vals[2][0],trim_vals[2][1]+.1), App.Vector(trim_vals[3][0]+.1,0)),False)
                App.getDocument(_Doc_).getObject(sketch_name).trim(trim_vals[0], App.Vector(trim_vals[2][0], trim_vals[2][1],0))
                App.getDocument(_Doc_).recompute()
                App.getDocument(_Doc_).getObject(sketch_name).trim(trim_vals[1], App.Vector(trim_vals[3][0], trim_vals[3][1],0))
                App.getDocument(_Doc_).recompute()
            except:
                pass
            App.getDocument(_Doc_).getObject(new_val).newObject('PartDesign::Revolution',Rev)
            App.ActiveDocument.recompute()
            FreeCAD.ActiveDocument.recompute()  
        except:
            self.error_msg.setText('Error while creating sketch, control data!')
            self.error_msg.show()
        try:
            FreeCAD.getDocument(_Doc_).getObject(Rev).Profile = FreeCAD.getDocument(_Doc_).getObject(sketch_name)
            App.getDocument(_Doc_).getObject(Rev).ReferenceAxis = (App.getDocument(_Doc_).getObject(sketch_name),['V_Axis'])
            App.getDocument(_Doc_).getObject(Rev).Angle =360.0
            App.getDocument(_Doc_).getObject(sketch_name).Visibility = False
            #App.ActiveDocument.recompute()
            App.getDocument(_Doc_).getObject(Rev).ViewObject.ShapeColor=getattr(App.getDocument(_Doc_).getObject(new_val).getLinkedObject(True).ViewObject,'ShapeColor',App.getDocument(_Doc_).getObject(Rev).ViewObject.ShapeColor)
            App.getDocument(_Doc_).getObject(Rev).ViewObject.LineColor=getattr(App.getDocument(_Doc_).getObject(new_val).getLinkedObject(True).ViewObject,'LineColor',App.getDocument(_Doc_).getObject(Rev).ViewObject.LineColor)
            App.getDocument(_Doc_).getObject(Rev).ViewObject.PointColor=getattr(App.getDocument(_Doc_).getObject(new_val).getLinkedObject(True).ViewObject,'PointColor',App.getDocument(_Doc_).getObject(Rev).ViewObject.PointColor)
            App.getDocument(_Doc_).getObject(Rev).ViewObject.Transparency=getattr(App.getDocument(_Doc_).getObject(new_val).getLinkedObject(True).ViewObject,'Transparency',App.getDocument(_Doc_).getObject(Rev).ViewObject.Transparency)
            App.getDocument(_Doc_).getObject(Rev).ViewObject.DisplayMode=getattr(App.getDocument(_Doc_).getObject(new_val).getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument(_Doc_).getObject(Rev).ViewObject.DisplayMode)
            App.getDocument(_Doc_).getObject(Rev).Angle = 360.000000
            App.getDocument(_Doc_).getObject(Rev).ReferenceAxis = (App.getDocument(_Doc_).getObject(sketch_name), ['V_Axis'])
            App.getDocument(_Doc_).getObject(Rev).Midplane = 0
            App.getDocument(_Doc_).getObject(Rev).Reversed = 0
            #App.getDocument(_Doc_).recompute()
            print('[App] recompute')
            #Gui.getDocument(_Doc_).resetEdit()
            App.getDocument(_Doc_).getObject(sketch_name).Visibility = False
            Gui.getDocument(_Doc_).getObject(new_val).ShapeColor=(0.7803999781608582, 0.5685999989509583, 0.1137000024318695, 0.0)            # Gold color        
            FreeCAD.ActiveDocument.recompute()    
            Gui.runCommand('Std_DrawStyle',5)  
            print('[FreeCAD] recompute')
        except:
            self.error_msg.setText('Error while creating 3D object, control the sketch!')
            self.error_msg.show()
            

# Chiamare la funzione per creare l'oggetto
if __name__ == '__main__':
    window = AmmoMaker()
