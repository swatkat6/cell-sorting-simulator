
# Basic features of this code are outlined in FileUpdate.txt.

import random
import math

import Tkinter as tk
from Tkinter import *
import tkMessageBox
import PIL
from PIL import Image,ImageTk


class Animation(object):
  
    def mousePressed(self, event):
        x,y=event.x,event.y
        r,c,count=0,0,0
        sw,sh=self.canvas.data["singleWidth"],self.canvas.data["singleHeight"]
        sm=self.canvas.data["margin"]
        rows,cols=self.canvas.data["rows"],self.canvas.data["cols"]
        cellBoard=self.canvas.data["cellBoard"]
        if x<=sm+(sw*cols) and x>=sm and y>=sm and y<=sm+(sh*rows) and self.canvas.data["simulation"]:
            for row in xrange(rows):
                if(sm+row*sh)<=y and (sm+(row+1)*sh)>y:r,count=row,1    
            for col in xrange(cols):
                if(sm+col*sw)<=x and (sm+(col+1)*sw)>x:c,count=col,1
            if(self.canvas.data["cell1Pressed"]) and (count==1):
                if(cellBoard[r][c]==0):cellBoard[r][c]=1
                elif(cellBoard[r][c]==1):cellBoard[r][c]=0
                
            elif(self.canvas.data["cell2Pressed"]) and (count==1):
                if(cellBoard[r][c]==0):cellBoard[r][c]=2
                elif(cellBoard[r][c]==2):cellBoard[r][c]=0
                
            
            elif(self.canvas.data["cell3Pressed"]) and (count==1):
                if(cellBoard[r][c]==0):cellBoard[r][c]=3
                elif(cellBoard[r][c]==3):cellBoard[r][c]=0
                
            
            elif(self.canvas.data["cell4Pressed"]) and (count==1):
                if(cellBoard[r][c]==0):cellBoard[r][c]=4
                elif(cellBoard[r][c]==4):cellBoard[r][c]=0
        
            self.canvas.data["cellBoard"]=cellBoard            
            simul.deltaDraw([1,0,0,r,c],sm,sw,sh,cellBoard,self.canvas.data["counter"],self.canvas)                
                
            
    def keyPressed(self, event): pass
    def timerFired(self): pass
    def init(self): pass
    def redrawAll(self,canvas): pass
    def repeat(self):pass
    def button1Pressed(self,root):
        self.canvas.data["start"]=True
    
    def button2Pressed(self,root):
        self.canvas.data["start"]=False
    
    def button3Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunch2(self.canvas)
    
    def cell1(self,root):
        if(self.canvas.data["choose"]):
            self.canvas.data["cell1Pressed"]=True
            self.canvas.data["cell2Pressed"]=False
            self.canvas.data["cell3Pressed"]=False
            self.canvas.data["cell4Pressed"]=False
        
    def cell2(self,root):
        if(self.canvas.data["choose"]):
            self.canvas.data["cell1Pressed"]=False
            self.canvas.data["cell2Pressed"]=True
            self.canvas.data["cell3Pressed"]=False
            self.canvas.data["cell4Pressed"]=False
        
    def cell3(self,root):
        if(self.canvas.data["choose"]):
            self.canvas.data["cell1Pressed"]=False
            self.canvas.data["cell2Pressed"]=False
            self.canvas.data["cell3Pressed"]=True
            self.canvas.data["cell4Pressed"]=False
    
    def cell4(self,root):
        if(self.canvas.data["choose"]):
            self.canvas.data["cell1Pressed"]=False
            self.canvas.data["cell2Pressed"]=False
            self.canvas.data["cell3Pressed"]=False
            self.canvas.data["cell4Pressed"]=True
    
    
    def r1chosen(self,root):
        self.canvas.data["r1"]=True
        self.canvas.data["r2"]=False
        self.canvas.data["counter"]=0
        self.canvas.data["donechoosing"]=True
        self.canvas.data["end"]=False
        self.canvas.data["start"]=False
        #if self.canvas.data["r1"] and self.canvas.data["simulation"]:
        cellBoard=[([0]*self.cols) for row in xrange(self.rows)]
        self.canvas.data["cellBoard"]=cellBoard
        self.cellBoard=simul.setCells(self.rows,self.cols,self.types,self.canvas)
        self.scoreBoard=simul.setScore(self.cellBoard,self.canvas)
        self.scoreBoard=simul.setScore(self.cellBoard,self.canvas)
        
        simul.drawCellboard(self.canvas.data["singleWidth"],self.canvas.data["singleHeight"],\
                self.canvas.data["margin"],self.canvas.data["cellBoard"],self.canvas.data["counter"],self.canvas)
                
            
    def r2chosen(self,root):
        tkMessageBox.showinfo("Info", "Please choose a cell type and place in the black box")
        self.canvas.data["r2"]=True
        self.canvas.data["r1"]=False
        self.canvas.data["counter"]=0
        self.canvas.data["start"]=False
        self.canvas.data["end"]=False
        cellBoard=[([0]*self.cols) for row in xrange(self.rows)]
        self.canvas.data["cellBoard"]=cellBoard
        simul.drawCellboard(self.canvas.data["singleWidth"],self.canvas.data["singleHeight"],\
                self.canvas.data["margin"],self.canvas.data["cellBoard"],self.canvas.data["counter"],self.canvas)
        simul.chooseCells(self.rows,self.cols,self.types,self.canvas)
        self.cellBoard=self.canvas.data["cellBoard"]
        self.scoreBoard=simul.setScore(self.cellBoard,self.canvas)
        self.scoreBoard=simul.setScore(self.cellBoard,self.canvas)
        
        
        simul.drawCellboard(self.canvas.data["singleWidth"],self.canvas.data["singleHeight"],\
                self.canvas.data["margin"],self.canvas.data["cellBoard"],self.canvas.data["counter"],self.canvas)
        
    def end(self,root):
        self.canvas.data["end"]=True
        count=self.canvas.data["counter"]
        if(not self.canvas.data["start"]):
            for x in xrange(count, 40000):
                self.canvas.data["info"]=simul.simulation(self.canvas.data["cellBoard"],self.canvas)
                self.canvas.data["counter"]+=1
                runSim.drawProgressBar(self.canvas)
            runSim.redrawAll(self.canvas)
                                  
            
        #simul.drawCellboard(self.canvas.data["singleWidth"],self.canvas.data["singleHeight"],\
        #    self.canvas.data["margin"],self.canvas.data["cellBoard"],self.canvas.data["counter"],self.canvas)
    
    
    
    def donechoosing(self,root):
        self.canvas.data["donechoosing"]=True
        return self.canvas.data["cellBoard"]
    
    def button4Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunchDes1(self.canvas)
        
    def button5Pressed(self,root):
        self.canvas.delete(ALL)
        self.canvas.data["simulation"]=True
        self.redrawAll(self.canvas)
        #runSim.drawLauchSim()
        
    def button6Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunch2(self.canvas)
        
    def button7Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunchDes2(self.canvas)
    
    def button8Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunchDes3(self.canvas)
        
    def button9Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunchDes1(self.canvas)
        
    def button10Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunch2(self.canvas)
        
    def button11Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunch2(self.canvas)   
    
    def button12Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunchDes2(self.canvas)
    ###########  
    def button13Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunchDes5(self.canvas)
        
    
    def button14Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunch2(self.canvas)
        
    
    def button15Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.drawLaunchDes4(self.canvas)
        
    ###############
    
    def button16Pressed(self,root):
        self.canvas.delete(ALL)
        runSim.redrawAll(self.canvas)
        
    def button17Pressed(self,root):
        self.canvas.delete(ALL)
        root.destroy()
    
    def initUI(self,root,canvas):
        
        def b1Pressed(): self.button1Pressed(root)
        b1 = Button(canvas, text="START!", command=b1Pressed, font="Algerian", highlightbackground="yellow")
        self.canvas.data["button1"]=b1
        
        def b2Pressed(): self.button2Pressed(root)
        b2 = Button(canvas, text="PAUSE", command=b2Pressed, font="Algerian")
        self.canvas.data["button2"]=b2
        
        def endPressed():self.end(root)
        end= Button(canvas, text="JUMP TO END RESULT!!", command=endPressed, font="Algerian")
        self.canvas.data["endResult"]=end
       
        T = Scale(root, from_=1, to=20,background="red",\
                  troughcolor="light blue",sliderlength=10,length=100,label="T",resolution=0.5)
        canvas.data["T"]=T
        ####################
        Cell11 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell1-Cell1",resolution=0.5)
        Cell11.set(-15)
        canvas.data["Cell11"]=Cell11
        
        Cell12 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell1-Cell2",resolution=0.5)
        Cell12.set(15)
        canvas.data["Cell12"]=Cell12
        
        Cell13 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell1-Cell3",resolution=0.5)
        Cell13.set(15)
        canvas.data["Cell13"]=Cell13
        
        Cell14 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell1-Cell4",resolution=0.5)
        Cell14.set(15)
        canvas.data["Cell14"]=Cell14
        
        Cell10 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell1-ECM",resolution=0.5)
        Cell10.set(0)
        canvas.data["Cell10"]=Cell10
        
        Cell1W = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell1-Boundary",resolution=0.5)
        Cell1W.set(5)
        canvas.data["Cell1W"]=Cell1W
        ##########################
        
        
        Cell22 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell2-Cell2",resolution=0.5)
        Cell22.set(-15)
        canvas.data["Cell22"]=Cell22
        
        Cell23 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell2-Cell3",resolution=0.5)
        Cell23.set(15)
        canvas.data["Cell23"]=Cell23
        
        Cell24 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell2-Cell4",resolution=0.5)
        Cell24.set(15)
        canvas.data["Cell24"]=Cell24
        
        Cell20 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell2-ECM",resolution=0.5)
        canvas.data["Cell20"]=Cell20
                
        Cell2W = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell2-Boundary",resolution=0.5)
        canvas.data["Cell2W"]=Cell2W
        Cell2W.set(5)
        ##################
        
        Cell33 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell3-Cell3",resolution=0.5)
        canvas.data["Cell33"]=Cell33
        Cell33.set(-15)
        
        Cell34 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell3-Cell4",resolution=0.5)
        canvas.data["Cell34"]=Cell34
        Cell34.set(15)
        
        Cell30 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell3-ECM",resolution=0.5)
        canvas.data["Cell30"]=Cell30
        
        Cell3W = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell3-Boundary",resolution=0.5)
        canvas.data["Cell3W"]=Cell3W
        Cell3W.set(-5)
        ##################
        
        Cell44 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell4-Cell4",resolution=0.5)
        canvas.data["Cell44"]=Cell44
        Cell44.set(-15)
        
        Cell40 = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell4-ECM",resolution=0.5)
        canvas.data["Cell40"]=Cell40
        
        
        Cell4W = Scale(root, from_=-50, to=50,background="red",orient=HORIZONTAL,\
                  troughcolor="light blue",sliderlength=10,length=100,label="Cell4-Boundary",resolution=0.5)
        canvas.data["Cell4W"]=Cell4W
        Cell4W.set(-5)
        ###################
        
        
        v = IntVar()
        def r1(): self.r1chosen(root)
        r1=Radiobutton(root, text="Load default", variable=v, value=1,command=r1)
        self.canvas.data["r1chosen"]=r1
        def r2(): self.r2chosen(root)
        r2=Radiobutton(root, text="Make my own simulation", variable=v, value=2,command=r2)
        self.canvas.data["r2chosen"]=r2
       
        def cell1Pressed(): self.cell1(root)
        cell1 = Button(canvas, text="CELL1", command=cell1Pressed, font="Algerian", highlightbackground="yellow")
        self.canvas.data["cell1"]=cell1
       
        def cell2Pressed(): self.cell2(root)       
        cell2 = Button(canvas, text="CELL2", command=cell2Pressed, font="Algerian", highlightbackground="yellow")
        self.canvas.data["cell2"]=cell2
        
        def cell3Pressed(): self.cell3(root)       
        cell3 = Button(canvas, text="CELL3", command=cell3Pressed, font="Algerian", highlightbackground="yellow")
        self.canvas.data["cell3"]=cell3
        
        def cell4Pressed(): self.cell4(root)       
        cell4 = Button(canvas, text="CELL4", command=cell4Pressed, font="Algerian", highlightbackground="yellow")
        self.canvas.data["cell4"]=cell4
        
        def chosen(): self.donechoosing(root)
        chosen= Button(canvas,text="Done Choosing Cells!", command=chosen,font="Algerian")
        self.canvas.data["chosen"]=chosen
        
        
        ######
        def b3Pressed():self.button3Pressed(root)
        img= Image.open("Pics Folder/bluearrow.jpg")
        img = img.resize((30,30), Image.ANTIALIAS)
        img.save('Pics Folder/resized_arrow.jpg')
        image=Image.open("resized_arrow.jpg")
        
        photo = ImageTk.PhotoImage(image)
        
        b3=Button(canvas,image=photo, command=b3Pressed,bg="black")
        b3.image=photo
        self.canvas.data["button3"]=b3
        
       
       
        #######
        def b4Pressed():self.button4Pressed(root)
        b4= Button(canvas,image=photo, command=b4Pressed,bg="light blue")
        b4.image=photo
        self.canvas.data["button4"]=b4
        
        def b5Pressed():self.button5Pressed(root)
        b5= Button(canvas,image=photo, command=b5Pressed,bg="light blue")
        b5.image=photo
        self.canvas.data["button5"]=b5
        
        ############
        
        img= Image.open("Pics Folder/arrowblueleft.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        img.save('Pics Folder/resized_arrowblueleft.png')
        image=Image.open("Pics Folder/resized_arrowblueleft.png")
        photo3 = ImageTk.PhotoImage(image)
        
        def b6Pressed():self.button6Pressed(root)
        b6= Button(canvas,image=photo3, command=b6Pressed,bg="light blue")
        b6.image=photo3
        self.canvas.data["button6"]=b6
        
        img= Image.open("Pics Folder/arrowblue.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        img.save('Pics Folder/resized_arrowblue.png')
        image=Image.open("Pics Folder/resized_arrowblue.png")
        photo2 = ImageTk.PhotoImage(image)
        
        def b7Pressed():self.button7Pressed(root)
        b7= Button(canvas,image=photo2, command=b7Pressed,bg="light blue")
        b7.image=photo2
        self.canvas.data["button7"]=b7
        
        ###########
        
        def b8Pressed():self.button8Pressed(root)
        b8= Button(canvas,image=photo2, command=b8Pressed,bg="light blue")
        b8.image=photo2
        self.canvas.data["button8"]=b8
        
        def b9Pressed():self.button9Pressed(root)
        b9= Button(canvas,image=photo3, command=b9Pressed,bg="light blue")
        b9.image=photo3
        self.canvas.data["button9"]=b9
                
        img= Image.open("Pics Folder/Down-Arrow-Icon.jpg")
        img = img.resize((30,30), Image.ANTIALIAS)
        img.save('Pics Folder/resized_Down-Arrow-Icon.jpg')
        image=Image.open("Pics Folder/resized_Down-Arrow-Icon.jpg")
        photo4 = ImageTk.PhotoImage(image)
                
        
        def b10Pressed():self.button10Pressed(root)
        b10= Button(canvas,image=photo4, command=b10Pressed,bg="light blue")
        b10.image=photo4
        self.canvas.data["button10"]=b10
        
        
        
    
    ########### 
        
        def b11Pressed():self.button11Pressed(root)
        b11= Button(canvas,image=photo2, command=b11Pressed,bg="light blue")
        b11.image=photo2
        self.canvas.data["button11"]=b11
        
        def b12Pressed():self.button12Pressed(root)
        b12= Button(canvas,image=photo3, command=b12Pressed,bg="light blue")
        b12.image=photo3
        self.canvas.data["button12"]=b12
       
    ################ Simulator Page only##########    
        
        def b13Pressed():self.button13Pressed(root)
        b13= Button(canvas,image=photo2, command=b13Pressed,bg="light blue")
        b13.image=photo2
        self.canvas.data["button13"]=b13
        
        def b14Pressed():self.button14Pressed(root)
        b14= Button(canvas,image=photo3, command=b14Pressed,bg="light blue")
        b14.image=photo3
        self.canvas.data["button14"]=b14
       
        def b15Pressed():self.button15Pressed(root)
        b15= Button(canvas,image=photo4, command=b15Pressed,bg="light blue")
        b15.image=photo4
        self.canvas.data["button15"]=b15
           
        ###############   
        def b16Pressed():self.button16Pressed(root)
        b16= Button(canvas,image=photo4, command=b16Pressed,bg="light blue")
        b16.image=photo4
        self.canvas.data["button16"]=b16
        
        #############
        img= Image.open("Pics Folder/byesmiley.jpg")
        img = img.resize((50,50), Image.ANTIALIAS)
        img.save('Pics Folder/resized_byesmiley.png')
        image=Image.open("Pics Folder/resized_byesmiley.png")
        photo6 = ImageTk.PhotoImage(image)
        
        
        
        def b17Pressed():self.button17Pressed(root)
        b17= Button(canvas,image=photo6, command=b17Pressed,bg="light blue")
        b17.image=photo6
        self.canvas.data["button17"]=b17
        
       
       
        canvas.pack()
        
    def run(self, width=700, height=600):
        # create the root and the canvas
    
        root = Tk()
        self.width = width
        self.height = height
        
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack()
        root.canvas=self.canvas.canvas=self.canvas
        self.canvas.data={}
        self.canvas.data["width"]=width
        self.canvas.data["height"]=height
        
        self.canvas.data["simulation"]=False
        
        #self.canvas.data["mainMenu"]=False
        self.initUI(root,self.canvas)
        
        # set up events
        def redrawAllWrapper():
            self.canvas.delete(ALL)
            self.redrawAll(self.canvas)
        def mousePressedWrapper(event):
            self.mousePressed(event)
            #redrawAllWrapper()
        def keyPressedWrapper(event):
            self.keyPressed(event)
            #redrawAllWrapper()
        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<Key>", keyPressedWrapper)
               
        
        # set up timerFired events
        self.timerFiredDelay = 1 # milliseconds
        def timerFiredWrapper():
            count=self.timerFired()
            if(count<=5000):
                # pause, then call timerFired again
                self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
        
        self.init()
        timerFiredWrapper()
        
        
        
        root.mainloop()

#######################################################################


class epidermalCell(object):
    def __init__(self,x0,y0,x1,y1):
        self.x0=x0
        self.x1=x1
        self.y0=y0
        self.y1=y1
    @classmethod
    def energyRecord(cls,canvas):
        return {0:canvas.data["Cell10"].get(),1:canvas.data["Cell11"].get(),2:canvas.data["Cell12"].get(),3:canvas.data["Cell13"].get(),\
                4:canvas.data["Cell14"].get(), 6:canvas.data["Cell1W"].get()}
    #0: ECM, #1: Same type #2: Other type #6. Wall
    
    def drawCell(self,canvas):
        canvas.create_rectangle(self.x0,self.y0,self.x1,self.y1,fill="black")
        canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill="red", outline="black")
        canvas.create_oval(self.x0+(self.x1-self.x0)/4,self.y0+(self.y1-self.y0)/4,\
                           self.x1-(self.x1-self.x0)/4,self.y1-(self.y1-self.y0)/4,fill="brown", outline="black")
        #canvas.create_oval(0.2*self.x0,0.2*self.y0,0.2*self.x1,0.2*self.y1,fill="black")
        
class mesenchymalCell(object):
    def __init__(self,x0,y0,x1,y1):
        self.x0=x0
        self.x1=x1
        self.y0=y0
        self.y1=y1
    @classmethod
    def energyRecord(cls,canvas):
        return {0:canvas.data["Cell30"].get(),1:canvas.data["Cell13"].get(),2:canvas.data["Cell23"].get(),3:canvas.data["Cell33"].get(),\
                4:canvas.data["Cell34"].get(), 6:canvas.data["Cell3W"].get()}
    #0: ECM, #1: Same type #2: Other type #6. Wall
    
    def drawCell(self,canvas):
        canvas.create_rectangle(self.x0,self.y0,self.x1,self.y1,fill="black")
        canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill="light blue", outline="black")
        canvas.create_oval(self.x0+(self.x1-self.x0)/4,self.y0+(self.y1-self.y0)/4,\
                           self.x1-(self.x1-self.x0)/4,self.y1-(self.y1-self.y0)/4,fill="brown", outline="black")
        #canvas.create_oval(0.2*self.x0,0.2*self.y0,0.2*self.x1,0.2*self.y1,fill="black")

class boneCell(object):
    def __init__(self,x0,y0,x1,y1):
        self.x0=x0
        self.x1=x1
        self.y0=y0
        self.y1=y1
    @classmethod
    def energyRecord(cls,canvas):
        return {0:canvas.data["Cell40"].get(),1:canvas.data["Cell14"].get(),2:canvas.data["Cell24"].get(),3:canvas.data["Cell34"].get(),\
                4:canvas.data["Cell44"].get(), 6:canvas.data["Cell4W"].get()}
    #0: ECM, #1: Same type #2: Other type #6. Wall
    
    def drawCell(self,canvas):
        canvas.create_rectangle(self.x0,self.y0,self.x1,self.y1,fill="black")
        canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill="yellow", outline="black")
        canvas.create_oval(self.x0+(self.x1-self.x0)/4,self.y0+(self.y1-self.y0)/4,\
                           self.x1-(self.x1-self.x0)/4,self.y1-(self.y1-self.y0)/4,fill="brown", outline="black")
        #canvas.create_oval(0.2*self.x0,0.2*self.y0,0.2*self.x1,0.2*self.y1,fill="black")

        

class strangeCell(object):
    def __init__(self,x0,y0,x1,y1):
        self.x0=x0
        self.x1=x1
        self.y0=y0
        self.y1=y1
    
    @classmethod    
    def energyRecord(cls,canvas):
        return {0:canvas.data["Cell20"].get(),1:canvas.data["Cell12"].get(),2:canvas.data["Cell22"].get(),3:canvas.data["Cell23"].get(),\
                4:canvas.data["Cell24"].get(), 6:canvas.data["Cell2W"].get()}
    
    def drawCell(self,canvas):
        x0=self.x0
        x1=self.x1
        y0=self.y0
        y1=self.y1
        width,height=x1-x0,y1-y0

        canvas.create_arc(x0+(width/2)-width/15,y0,x0+(width/2)+(width/15),y0+height/5, start=0,extent=180,style=ARC)#up
        canvas.create_arc(x1-width/15,y0+height/15,x1-(width/5),y0+height/5, start=290,extent=210,style=ARC) #right angle
        canvas.create_arc(x0+width/15,y0+height/15,x0+(width/5),y0+height/5, start=0,extent=270,style=ARC)  #left angle
        
        canvas.create_arc(x0+(width/2)-width/15,y1,x0+(width/2)+(width/15),y1-height/5, start=180,extent=180,style=ARC) #down
        canvas.create_arc(x1-width/15,y1-height/15,x1-(width/5),y1-height/5, start=200,extent=210,style=ARC) #right angle
        canvas.create_arc(x0+width/15,y1-height/15,x0+(width/5),y1-height/5, start=100,extent=240,style=ARC)  #left angle
        
        canvas.create_arc(x0,y0+height/2-height/15,x0+(width/5),y0+height/2+height/15, start=90,extent=180,style=ARC) # left
        canvas.create_arc(x1,y0+height/2-height/15,x1-(width/5),y0+height/2+height/15, start=270,extent=180,style=ARC) #right
        
        canvas.create_line(x0+(width/2)+(width/15),y0+height/10,x1-width/6,y0+height/12)
        
        #canvas.create_arc(x0+(width/2))
        canvas.create_line(x1-width/9,y0+height/5,x1-width/10,y0+height/2-height/15)
        
        
        canvas.create_line(x1-(width/10),y0+height/2+height/15,x1-width/11,y1-height/5.5)
        
        canvas.create_line(x1-(width/5),y1-height/9,x0+(width/2)+width/15,y1-height/10)
        
        
        canvas.create_line(x0+(width/2)+(width/15),y0+height/10,x1-width/6,y0+height/12)
        
        
        
        canvas.create_line(x0+(width/2)-(width/15),y1-height/10,x0+width/5.0,y1-height/9)
        
        
        canvas.create_line(x0+(width/8.5),y1-height/5,x0+(width/10),y0+height/2+height/15)
        
        
        canvas.create_line(x0+(width/10),y0+height/2-height/15,x0+(width/8),y0+height/5)
        
        canvas.create_line(x0+(width/5),y0+height/8,x0+(width/2)-width/15,y0+height/10)
        

######################################################################
class simul(object):
    
    @classmethod
    def setCells(cls,rows,cols,types,canvas): # assigns initial random board
        
        cellBoard=canvas.data["cellBoard"]
        for row in xrange(rows):
            for col in xrange(cols):
                cellBoard[row][col]=random.choice((range(0,types+1)))
        canvas.data["cellBoard"]=cellBoard
        return cellBoard

    @classmethod   # calculates the energy of a cell, via the neighbours shared
    def setScore(cls,cellBoard,canvas):
        rows=len(cellBoard)
        cols=len(cellBoard[0])
        scoreBoard=[([0]*cols) for row in xrange(rows)]     
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        for row in xrange(rows):
            for col in xrange(cols):
                if(cellBoard[row][col]==0): scoreBoard[row][col]==0
                else:
                    if(cellBoard[row][col]==1):
                        energy=epidermalCell.energyRecord(canvas)
                    elif(cellBoard[row][col]==2):
                        energy=strangeCell.energyRecord(canvas)
                    elif (cellBoard[row][col]==3):
                        energy=mesenchymalCell.energyRecord(canvas)
                    elif (cellBoard[row][col]==4):
                        energy=boneCell.energyRecord(canvas)
                    for direction in dirs:
                        if (row+direction[0]<rows and row+direction[0]>=0\
                        and col+direction[1]<cols and col+direction[1]>=0):
                            scoreBoard[row][col]+=energy[cellBoard[row+direction[0]]\
                                                         [col+direction[1]]]        
                        else:scoreBoard[row][col]+=energy[6]
        return scoreBoard
    
    @classmethod
    def chooseCells(cls,row,col,types,canvas):
        canvas.data["choose"]=True
        canvas.data["donechoosing"]=False
        m=canvas.data["margin"]
   
    
    @classmethod  # entire score (hamiltonian of configuration)                      
    def totalScore(cls,scoreBoard):
        totalScore=0
        rows,cols=len(scoreBoard),len(scoreBoard[0])
        for row in xrange(rows):
            for col in xrange(cols):
                totalScore+=scoreBoard[row][col]
        return totalScore        

    @classmethod
    def simulation(cls,cellBoard,canvas): # simulates sorting
        change,ROW,COL,ROW1,COL1=0,0,0,0,0
        T=canvas.data["T"].get()
        print T
        rows,cols=len(cellBoard),len(cellBoard[0])
        row=random.randint(0,len(cellBoard)-1)  #pick random cell
        col=random.randint(0,len(cellBoard[0])-1)
        print "searching..."
        while True:
            dirs= [(0,1),(1,0),(0,-1),(-1,0)] # pick any adjacent cell
            direction=random.choice(dirs)
            if (row+direction[0]<rows and row+direction[0]>=0 and\
                col+direction[1]<cols and col+direction[1]>=0):
                break
        if(cellBoard[row][col]!=cellBoard[row+direction[0]][col+direction[1]]) and cellBoard[row][col]==0 or\
            cellBoard[row+direction[0]][col+direction[1]]==0:
            scoreBoard=cls.setScore(cellBoard,canvas)  
            totalScoreprior=cls.totalScore(scoreBoard)
            change,ROW,COL,ROW1,COL1=1,row,col,row+direction[0],col+direction[1]
            (cellBoard[row][col],cellBoard[row+direction[0]]\
            [col+direction[1]])=(cellBoard[row+direction[0]]\
                            [col+direction[1]],cellBoard[row][col]) #swap cells
            scoreBoard=cls.setScore(cellBoard,canvas) # get new energy
            totalScorepost=cls.totalScore(scoreBoard)
            diff=(totalScorepost-totalScoreprior)
            if(totalScorepost>totalScoreprior): # Metropolis criteria
                factor=math.exp(-1.0*float(totalScorepost-totalScoreprior)/T)
                number=random.uniform(0,1)
                if(number>factor):
                    change=0 # reverse change
                    (cellBoard[row+direction[0]][col+direction[1]],\
                     cellBoard[row][col])=(cellBoard[row][col],\
                    cellBoard[row+direction[0]][col+direction[1]])
        
        return (change,ROW,COL,ROW1,COL1) # return information on change
                
    # way to visualize
    
    @classmethod
    def drawCellboard(cls,singleWidth,singleHeight,margin,cellBoard,counter,canvas):
        rows,cols=len(cellBoard),len(cellBoard[0])
        colorDict={0:"black",1:"blue",2:"green",3:"yellow",4: "pink",5:"brown"}
        canvas.create_rectangle(margin,margin/2,margin+\
                singleWidth*cols,margin,fill="white") #removed grey
        canvas.create_text((2.0*margin+singleWidth*cols)/2,3*margin/4.0,\
            text="Simulations: %d"%(counter))
        for row in xrange(rows):
            for col in xrange(cols):
                x0=margin+singleWidth*col
                y0=margin+singleHeight*row
                x1=x0+singleWidth
                y1=y0+singleHeight
                
                color=colorDict[cellBoard[row][col]]
                if cellBoard[row][col]==0:
                    canvas.create_rectangle(x0,y0,x1,y1,fill=color,outline=color)
                elif cellBoard[row][col]==1:
                    epidermalCell(x0,y0,x1,y1).drawCell(canvas)
                elif cellBoard[row][col]==2:
                    canvas.create_rectangle(x0,y0,x1,y1,fill=color,outline=color)
                    strangeCell(x0,y0,x1,y1).drawCell(canvas)
                elif cellBoard[row][col]==3:
                    mesenchymalCell(x0,y0,x1,y1).drawCell(canvas)
                elif cellBoard[row][col]==4:
                    boneCell(x0,y0,x1,y1).drawCell(canvas)    
                
                #canvas.create_text((x0+x1)/2,(y0+y1)/2,text=cellBoard[row][col])
            
                    
    @classmethod                
    def deltaDraw(cls,info,margin,singleWidth,singleHeight,cellBoard,counter,canvas): # redraw only the change
        (rows,cols)=(len(cellBoard),len(cellBoard[0]))
        [change,row,col,newRow,newCol]=info
        colorDict={0:"black",1:"blue",2:"green",3:"yellow",4:"pink",5:"brown"}
        x0,x0new=margin+singleWidth*col, margin+singleWidth*newCol
        y0,y0new=margin+singleHeight*row, margin+singleHeight*newRow
        x1,x1new=x0+singleWidth, x0new+singleWidth
        y1,y1new=y0+singleHeight, y0new+singleHeight
        
        canvas.create_rectangle(margin,margin/2,margin+singleWidth*cols,\
                                        margin,fill="white") # removed grey
        canvas.create_text((2.0*margin+singleWidth*cols)/2,3*margin/4.0,\
                text="Simulations: %d"%(counter))    
        if change==1:
            color=colorDict[cellBoard[row][col]]
            if cellBoard[row][col]==0:
                canvas.create_rectangle(x0,y0,x1,y1,fill=color,outline=color)
            elif cellBoard[row][col]==1:
                epidermalCell(x0,y0,x1,y1).drawCell(canvas)
            elif cellBoard[row][col]==2:
                canvas.create_rectangle(x0,y0,x1,y1,fill=color,outline=color)
                strangeCell(x0,y0,x1,y1).drawCell(canvas)
            elif cellBoard[row][col]==3:
                mesenchymalCell(x0,y0,x1,y1).drawCell(canvas)
            elif cellBoard[row][col]==4:
                boneCell(x0,y0,x1,y1).drawCell(canvas)    
                
            
            
            #canvas.create_text((x0+x1)/2,(y0+y1)/2, text=cellBoard[row][col])
                       
            #Change
           
            color=colorDict[cellBoard[newRow][newCol]]
            if cellBoard[newRow][newCol]==0:
                canvas.create_rectangle(x0new,y0new,x1new,y1new,fill=color,outline=color)
            elif cellBoard[newRow][newCol]==1:
                epidermalCell(x0new,y0new,x1new,y1new).drawCell(canvas)
            elif cellBoard[newRow][newCol]==2:
                canvas.create_rectangle(x0new,y0new,x1new,y1new,fill=color,outline=color)
                strangeCell(x0new,y0new,x1new,y1new).drawCell(canvas)
            elif cellBoard[newRow][newCol]==3:
                mesenchymalCell(x0new,y0new,x1new,y1new).drawCell(canvas)
            elif cellBoard[newRow][newCol]==4:
                boneCell(x0new,y0new,x1new,y1new).drawCell(canvas)    
                           
            #canvas.create_text((x0new+x1new)/2,(y0new+y1new)/2,text=cellBoard[newRow][newCol])
        
  
##############################################################

class runSim(Animation):
    
    def __init__(self,rows,cols,types):
        self.rows=rows
        self.cols=cols
        self.types=types
        
        
    def init(self):
        self.drawLaunch()
        self.margin=100
        self.canvas.data["rows"]=self.rows
        self.canvas.data["cols"]=self.cols
        self.canvas.data["margin"]=self.margin
        self.singleWidth,self.singleHeight=30,30
        self.canvas.data["singleWidth"]=self.singleWidth
        self.canvas.data["singleHeight"]=self.singleHeight
        self.canvas.data["cell1Pressed"]=False
        self.canvas.data["cell2Pressed"]=False
        self.canvas.data["cell3Pressed"]=False
        self.canvas.data["cell4Pressed"]=False
        self.canvas.data["start"]=False
        self.canvas.data["choose"]=False
        
        self.canvas.data["r1"]=True
        self.canvas.data["r2"]=False
        cellBoard=[([0]*self.cols) for row in xrange(self.rows)]
        self.canvas.data["cellBoard"]=cellBoard
        self.canvas.data["counter"]=0
        
        
        
            
        
           
    def drawLaunch(self):
        img = Image.open('Pics Folder/image1.jpg')
        #wpercent = (basewidth / float(img.size[0]))
        #hsize = int((float(img.size[1]) * float(wpercent)))
        w,h=self.canvas.data["width"],self.canvas.data["height"]
        
        img = img.resize((w,h), Image.ANTIALIAS)
        img.save('Pics Folder/resized_image.jpg')
        image=Image.open("Pics Folder/resized_image.jpg")
                
        #photo = PhotoImage(file="image1.gif")
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        self.canvas.create_text(w/2,h/2,text="WELCOME TO\n CELL SORTING SIMULATOR!!", font=("Algerian",30,"bold"),fill="light slate blue")
        b3=self.canvas.data["button3"]
        self.canvas.create_window(w-50,h-50,window=b3)
        #label.pack()
    
    @classmethod
    def drawLaunch2(cls,canvas):
        w,h=canvas.data["width"],canvas.data["height"]
        img1 = Image.open('Pics Folder/image9.jpg')
        
        img1= img1.resize((700,600), Image.ANTIALIAS)
        img1.save('Pics Folder/resized_imageSlide.jpg')
        image=Image.open("Pics Folder/resized_imageSlide.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        text="""    WHAT IS CELL SORTING AND REALLY...\n    WHY SHOULD I CARE??\n\n\n       TAKE ME TO THE SIMULATOR!! """
        canvas.create_text(w/2,h/2,text=text,font=("Comic Sans MS",25,"bold"),fill="black")
        b4=canvas.data["button4"]
        canvas.create_window(w-50,h/2,window=b4)
        b5=canvas.data["button5"]
        canvas.create_window(w-50,3*h/4.0,window=b5)
        
    @classmethod
    def drawLaunchSim(cls):
        pass
    
    @classmethod
    def drawLaunchDes1(cls,canvas):
        w,h=canvas.data["width"],canvas.data["height"]
        img = Image.open('Pics Folder/SlideBackground.jpg')
        
        img = img.resize((w,h), Image.ANTIALIAS)
        img.save('Pics Folder/resized_imageSlide1.jpg')
        image=Image.open("Pics Folder/resized_imageSlide1.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        img = Image.open('Pics Folder/ThinkingSmiley.jpg')
        
        img = img.resize((w/8,h/8), Image.ANTIALIAS)
        img.save('Pics Folder/resized_imageThinkingSmiley.jpg')
        image=Image.open("Pics Folder/resized_imageThinkingSmiley.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(2*w/5.0,3*h/5.5, anchor=NW, image=photo)
        label1 = Label(image=photo)
        label1.image = photo
        
        img = Image.open('Pics Folder/CellsPic.jpg')
        
        img = img.resize((w/4,w/4), Image.ANTIALIAS)
        img.save('Pics Folder/resized_image.jpg')
        image=Image.open("Pics Folder/resized_image.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(30,30, anchor=NW, image=photo)
        label2 = Label(image=photo)
        label2.image = photo
        
        canvas.create_text(w/2.5,h/5, text=\
                """\t\t\t\tYOUR BODY HAS ALMOST 100 TRILLION CELLS.....\n
                    \t\t\tAND THERE IS SO MUCH TO IT THAN JUST BEING \n
                    \t\t\tA RANDOM COLLECTION OF DIFFERENT CELLS!!\n""",\
                            font=("Times New Roman", 13, "bold"))
        
        canvas.create_text(w/2.5,3*h/5.0,text="""
                            EVER WONDERED WHY YOUR RETINA FORMS AT A\n 
                            PRECISE DISTANCE BEHIND YOUR EYE LENS AND NOT\n
                            IN YOUR BONE??\n\n ...
                            HOW DO RANDOM CELLS IN YOUR BODY DEVELOP INTO\n
                            SUCH INTRICATE STRUCTURES??""",
                                    font=("Times New Roman", 15, "bold"))
        
        b6=canvas.data["button6"]
        canvas.create_window(w/3,h-50,window=b6)
        b7=canvas.data["button7"]
        canvas.create_window(2*w/3.0,h-50,window=b7)        
        
    @classmethod        
    def drawLaunchDes2(cls,canvas):
        w,h=canvas.data["width"],canvas.data["height"]
        image=Image.open("Pics Folder/resized_imageSlide1.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        img=Image.open("Pics Folder/BirdsOffeather.jpg")
        img = img.resize((3*w/7,h/2), Image.ANTIALIAS)
        img.save('Pics Folder/resized_image.jpg')
        
        image=Image.open("Pics Folder/resized_image.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(3*w/5, 10, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        img=Image.open("Pics Folder/different celltypes.jpg")
        img = img.resize((2*w/5,2*h/5), Image.ANTIALIAS)
        img.save('Pics Folder/resized_image.jpg')
        
        image=Image.open("Pics Folder/resized_image.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(50, 10, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
                
        img=Image.open("Pics Folder/Smileyidea.jpg")
        img = img.resize((w/9,h/7), Image.ANTIALIAS)
        img.save('Pics Folder/resized_image.jpg')
        
        image=Image.open("Pics Folder/resized_image.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(w/3+50,2*h/5+20, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        
        canvas.create_text(w/4,h*3/5.0, text= """
                           \t\t\t\tONE WAY TO THINK OF IT...\n\n
                           \t\t\t\tWHEN A BABY DEVELOPS FROM A SINGLE CELL TO CONTAIN DIFFERENT TYPES \n
                           \t\t\t\tOF CELLS, WHAT IF EACH OF THESE CELLS WANTED TO ONLY\n
                           \t\t\t\tBE WITH ITS OWN CELL TYPE??""", font=("Times New Roman", 13, "bold"))
        b8=canvas.data["button8"]
        canvas.create_window(w-50,h-50,window=b8)
        b9=canvas.data["button9"]
        canvas.create_window(w/3,h-50,window=b9)
        b10=canvas.data["button10"]
        canvas.create_window(3*w/5,h-50,window=b10)
        canvas.create_text(3*w/5-20,h-100,text="Main Menu!", font=("Comic Sans MS", 9,"bold"))
        
        
        
              
    @classmethod
    def drawLaunchDes3(cls,canvas):
        image=Image.open("Pics Folder/resized_imageSlide1.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        img=Image.open("Pics Folder/Sorting.jpg")
        img = img.resize((100,380), Image.ANTIALIAS)
        img.save('Pics Folder/resized_image.jpg')
        
        image=Image.open("Pics Folder/resized_image.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(400,30, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        b11=canvas.data["button11"]
        canvas.create_window(450,450,window=b11)
        b12=canvas.data["button12"]
        canvas.create_window(150,450,window=b12)
        b10=canvas.data["button10"]
        canvas.create_window(280,480,window=b10)
        canvas.create_text(280,450,text="Main Menu!", font=("Comic Sans MS", 9,"bold"))
        
        
        
    @classmethod
    def drawLaunchDes4(cls,canvas):
        width,height=canvas.data["width"],canvas.data["height"]
        img=Image.open("Pics Folder/wallpaper.jpg")
        img = img.resize((width,height), Image.ANTIALIAS)
        img.save('Pics Folder/resized_image.jpg')
        
        image=Image.open("Pics Folder/resized_image.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0,0, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        
        w,h=canvas.data["width"],canvas.data["height"]
        canvas.create_text(w/2,20, text="ENERGY CONTROLS FOR EACH CELL TYPE", font=("Algerian", 12, "bold"))
        canvas.create_window(w/8.0,h/7.0,window=canvas.data["Cell10"])
        canvas.create_window(w/8.0,2*h/7.0,window=canvas.data["Cell11"])
        canvas.create_window(w/8.0,3*h/7.0,window=canvas.data["Cell12"])
        canvas.create_window(w/8.0,4*h/7.0,window=canvas.data["Cell13"])
        canvas.create_window(w/8.0,5*h/7.0,window=canvas.data["Cell14"])    
        canvas.create_window(w/8.0,6*h/7.0,window=canvas.data["Cell1W"])
        canvas.create_window(3.5*w/8.0,h/7.0,window=canvas.data["Cell20"])
        canvas.create_window(3.5*w/8.0,2*h/7.0,window=canvas.data["Cell22"])
        canvas.create_window(3.5*w/8.0,3*h/7.0,window=canvas.data["Cell23"])
        canvas.create_window(3.5*w/8.0,4*h/7.0,window=canvas.data["Cell24"])
        canvas.create_window(3.5*w/8.0,5*h/7.0,window=canvas.data["Cell2W"])
        canvas.create_window(3.5*w/8.0,6*h/7.0,window=canvas.data["Cell30"])
        canvas.create_window(6*w/8.0,h/7.0,window=canvas.data["Cell33"])
        canvas.create_window(6*w/8.0,2*h/7.0,window=canvas.data["Cell34"])
        canvas.create_window(6*w/8.0,3*h/7.0,window=canvas.data["Cell3W"])
        canvas.create_window(6*w/8.0,4*h/7.0,window=canvas.data["Cell40"])
        canvas.create_window(6*w/8.0,5*h/7.0,window=canvas.data["Cell44"])
        canvas.create_window(6*w/8.0,6*h/7.0,window=canvas.data["Cell4W"])
        
        b16=canvas.data["button16"]
        canvas.create_window(280,h-20,window=b16)
        canvas.create_text(360,h-30,text="Back to Simulator!", font=("Comic Sans MS", 9,"bold"))
        
    @classmethod    
    def drawLaunchDes5(cls,canvas):
        w,h=canvas.data["width"],canvas.data["height"]
        img=Image.open("Pics Folder/Background3.jpg")
        img = img.resize((w,h), Image.ANTIALIAS)
        img.save('Pics Folder/resized_image.jpg')
        
        image=Image.open("Pics Folder/resized_image.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0,0, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        canvas.create_text(w/2,h/2, text="Hope you had a nice time!", font=("Lucida Calligraphy",15,"bold"))
        
        b10=canvas.data["button10"]
        canvas.create_window(w/2,h-60,window=b10)
        canvas.create_text(w/2,h-100,text="Main Menu!", font=("Comic Sans MS", 12,"bold"))
        
        b17=canvas.data["button17"]
        canvas.create_window(w-70,h-50,window=b17)
        canvas.create_text(w-70,h-100,text="Close Application!", font=("Comic Sans MS", 12,"bold"))
        
        
        
    @classmethod
    def drawProgressBar(cls,canvas):
        w,h=canvas.data["width"],canvas.data["height"]
        canvas.create_rectangle(50,50,500,500,fill="black")
        print "Print this!?!"
        
    @classmethod        
    def redrawAll(cls,canvas): #draw board
        width,height=canvas.data["width"],canvas.data["height"]
        img=Image.open("Pics Folder/free-wallpaper-3.jpg")
        img = img.resize((width,height), Image.ANTIALIAS)
        img.save('Pics Folder/resized_image.jpg')
        
        image=Image.open("Pics Folder/resized_image.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0,0, anchor=NW, image=photo)
        label = Label(image=photo)
        label.image = photo
        
        b1 = canvas.data["button1"]
        canvas.create_window(4.0/5*width, 4.0/5*height, window=b1)
        b2 = canvas.data["button2"]
        canvas.create_window(4.0/5*width,4.0/5*height+50, window=b2)
        simul.drawCellboard(canvas.data["singleWidth"],canvas.data["singleHeight"],\
                canvas.data["margin"],canvas.data["cellBoard"],canvas.data["counter"],canvas)
        
                
        T=canvas.data["T"]
        canvas.create_window(9.0/10*width,4.0/5*height+25, window=T)
       
       
       
        r1=canvas.data["r1chosen"]
        r2=canvas.data["r2chosen"]
        #r1.config[bg:"orange",activebackground:"light blue"]
        canvas.create_window(4.0/5*width,1.0/5*height, window=r1)
        #r2.config[bg:"orange",activebackground:"light blue"]
        canvas.create_window(4.0/5*width+35,1.0/5*height+25, window=r2)
        
        c1 = canvas.data["cell1"]
        canvas.create_window(4.0/5*width, 2.0/5*height, window=c1)
        
        c2 = canvas.data["cell2"]
        canvas.create_window(4.0/5*width, 2.0/5*height+25, window=c2)
        
        c3 = canvas.data["cell3"]
        canvas.create_window(4.0/5*width, 2.0/5*height+50, window=c3)
        
        c4 = canvas.data["cell4"]
        canvas.create_window(4.0/5*width, 2.0/5*height+75, window=c4)
        
        c5= canvas.data["chosen"]
        canvas.create_window(4.0/5*width, 2.0/5*height+150, window=c5)
        
        end=canvas.data["endResult"]
        canvas.create_window(4.0/5*width, 2.0/5*height+180, window=end)
        
        b13=canvas.data["button13"]
        canvas.create_window(450,450,window=b13)
        b14=canvas.data["button14"]
        canvas.create_window(150,450,window=b14)
        b15=canvas.data["button15"]
        canvas.create_window(280,480,window=b15)
        canvas.create_text(280,450,text="Energy Controls!", font=("Comic Sans MS", 9,"bold"))
    def drawLaunchSim():pass
    
              
    def repeat(self): # iterations
        
        self.canvas.data["info"]=simul.simulation(self.cellBoard,self.canvas)
        self.canvas.data["counter"]+=1
        print "done"
        simul.deltaDraw(self.canvas.data["info"],self.margin,self.singleWidth,self.singleHeight,\
                        self.cellBoard,self.canvas.data["counter"],self.canvas)
        return self.canvas.data["counter"]
        
    def timerFired(self):
        if(self.canvas.data["start"]) and (self.canvas.data["donechoosing"]):
            count=self.repeat()
            return count
####################################################################




runSim(10,10,4).run()


