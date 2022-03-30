from tkinter import *
from matplotlib import projections
from matplotlib.pyplot import autoscale
from matplotlib.pyplot import gca
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from mpl_toolkits import mplot3d

from mathcalc import *

class uiWindow():
    def __init__(self):

        bgcolor = "#FFFFFF"
        fgcolor = "#000000"
        self.grcolor = "#929591"
        self.resetPlColor()

        self.root = Tk() #Makes the window
        self.root.wm_title("Ball Flight") #Makes the title that will appear in the top left
        self.root.config(background = bgcolor)
        
        # Setup some drawing variables
        labelwidth = 15
        entrywidth = 10
        xpadding = 5
        ypadding = 2
        
        # Instantiate all Frame Elements
        self.leftFrame = Frame(self.root, width=100, height = 600, bg = bgcolor)
        self.leftFrame.grid(row=0, column=0, padx=xpadding, pady=ypadding)

        self.rightFrame = Frame(self.root, width=400, height = 600, bg = bgcolor)
        self.rightFrame.grid(row=0, column=1, padx=xpadding, pady=ypadding)
        
        self.root.update()

        # Draws all the left frame elements
        Label(self.leftFrame, text="Ball Speed (mph):", bg=bgcolor, anchor="e", width=labelwidth).grid(row=0, column=0, padx=xpadding, pady=ypadding)
        self.ballspeed = Entry(self.leftFrame,width=10)
        self.ballspeed.grid(row=0, column=1, padx=xpadding, pady=ypadding)
        self.ballspeed.insert(0,"100.0")

        Label(self.leftFrame, text="Launch Angle (deg):", bg=bgcolor, anchor="e", width=labelwidth).grid(row=1, column=0, padx=xpadding, pady=ypadding)
        self.launchangle = Entry(self.leftFrame,width=10)
        self.launchangle.grid(row=1, column=1, padx=xpadding, pady=ypadding)
<<<<<<< HEAD
        self.launchangle.insert(0,"17.0")
=======
        self.launchangle.insert(0,"17.3")
>>>>>>> 67646f2fca4fba12a3b9d0fe0ab6b005f36f323a
        
        Label(self.leftFrame, text="Back Spin (rpm):", bg=bgcolor, anchor="e", width=labelwidth).grid(row=2, column=0, padx=xpadding, pady=ypadding)
        self.spinrate = Entry(self.leftFrame,width=10)
        self.spinrate.grid(row=2, column=1, padx=xpadding, pady=ypadding)
<<<<<<< HEAD
        self.spinrate.insert(0,"7000")

=======
        self.spinrate.insert(0,"6000")
>>>>>>> 67646f2fca4fba12a3b9d0fe0ab6b005f36f323a

        Label(self.leftFrame, text="Shape Angle (deg):", bg=bgcolor, anchor="e", width=labelwidth).grid(row=3, column=0, padx=xpadding, pady=ypadding)
        self.sideangle = Entry(self.leftFrame,width=10)
        self.sideangle.grid(row=3, column=1, padx=xpadding, pady=ypadding)
<<<<<<< HEAD
        self.sideangle.insert(0,"1")
=======
        self.sideangle.insert(0,"-4")
>>>>>>> 67646f2fca4fba12a3b9d0fe0ab6b005f36f323a

        Label(self.leftFrame, text="Side Spin (rpm):", bg=bgcolor, anchor="e", width=labelwidth).grid(row=4, column=0, padx=xpadding, pady=ypadding)
        self.sidespin = Entry(self.leftFrame,width=10)
        self.sidespin.grid(row=4, column=1, padx=xpadding, pady=ypadding)
<<<<<<< HEAD
        self.sidespin.insert(0,"-100")
=======
        self.sidespin.insert(0,"-200")
>>>>>>> 67646f2fca4fba12a3b9d0fe0ab6b005f36f323a

        self.clrplt = IntVar()
        self.clrcheck = Checkbutton(self.leftFrame,text="Clear Plots?",bg=bgcolor,variable=self.clrplt)
        self.clrcheck.grid(row=5,column=0,columnspan=2,padx=xpadding, pady=ypadding)

        # Drawing UI Elements - Update Buttom
        self.updateButton = Button(self.leftFrame,text="Update",command=lambda:self.update())
        self.updateButton.grid(row=10, column=0, columnspan=2, padx=xpadding, pady=ypadding)

        # UI Element Final Carry and apex
        Label(self.leftFrame, text="Total Carry (yds):", bg=bgcolor, anchor="e", width=labelwidth).grid(row=11, column=0, padx=xpadding, pady=ypadding)
        self.totalcarry = StringVar()
        self.totalcarry.set("0")
        Label(self.leftFrame, textvariable=self.totalcarry, bg=bgcolor, anchor="w", width=labelwidth, font="bold").grid(row=11, column=1, padx=xpadding, pady=ypadding)
        
        Label(self.leftFrame, text="Apex (ft):", bg=bgcolor, anchor="e", width=labelwidth).grid(row=12, column=0, padx=xpadding, pady=ypadding)
        self.apex = StringVar()
        self.apex.set("0")
        Label(self.leftFrame, textvariable=self.apex, bg=bgcolor, anchor="w", width=labelwidth, font="bold").grid(row=12, column=1, padx=xpadding, pady=ypadding)

        # Draws all the plot area elements
        # Create Figure and Subplot Axes Objects
        self.fig = Figure(figsize = (5, 6),dpi = 100)
        self.threedf = Figure(figsize=(6,6),dpi = 100)

        # Plots the plot object to canvas position
        
        self.plotcanvas = FigureCanvasTkAgg(self.fig,self.rightFrame)
        self.plotcanvas.get_tk_widget().grid(row=0, column=0, padx=xpadding, pady=ypadding)
        self.plotthreed = FigureCanvasTkAgg(self.threedf,self.rightFrame)
        self.plotthreed.get_tk_widget().grid(row=0, column=1, padx=xpadding, pady=ypadding)
        
        self.makesubplots()

    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI
    
    def update(self):
        bspeed = float(self.ballspeed.get())
        langle = float(self.launchangle.get())
        sprate = float(self.spinrate.get())
        sangle = float(self.sideangle.get())
        sspinr = float(self.sidespin.get())
        updateGlobals(bspeed,langle,sprate,sangle,sspinr)

        # Initialize Data
        xpos = 0
        ypos = 0
        zpos = 0
<<<<<<< HEAD

=======
>>>>>>> 67646f2fca4fba12a3b9d0fe0ab6b005f36f323a
        xdata = []
        ydata = []
        zdata = []
        

        InitVx,InitVy,InitVz = getInitialV()

        # Build Data Array
<<<<<<< HEAD
        for t in range(10000000):
            dt = 0.1       # 10ms increments
=======
        for t in range(100000):
            dt = 0.1
>>>>>>> 67646f2fca4fba12a3b9d0fe0ab6b005f36f323a
            dx,InitVx = calcX(dt,InitVx,InitVy,InitVz)
            dy,InitVy = calcY(dt,InitVy,InitVx,InitVz)
            dz,InitVz = calcZ(dt,InitVz,InitVx,InitVy)
            xpos = xpos + dx
            ypos = ypos + dy
            zpos = zpos + dz
            if ypos < 0:
                break
            xdata.append(xpos)
            ydata.append(ypos)
            zdata.append(zpos)
            calcSpinDecay(dt)
        
        # Convert data to yards
        xdata = meterstoyards(xdata)
        ydata = meterstoyards(ydata)
        zdata = meterstoyards(zdata)
        
        # Plot Data
        self.plotdata(xdata,ydata,zdata)
    
    def makesubplots(self):
        self.sideplot = self.fig.add_subplot(211,autoscale_on=TRUE)
        self.sideplot.axis("equal")
        self.sideplot.tick_params(bottom=TRUE,top=FALSE,left=TRUE,right=FALSE)
        self.sideplot.grid(axis="y", color=self.grcolor, alpha=0.5, linewidth = 0.5, linestyle=":")
        self.sideplot.set_ylabel("Height (ft)")
        self.sideplot.set_xlabel("Distance (yds)")

        self.topplot = self.fig.add_subplot(212,autoscale_on=TRUE)
        self.topplot.axis("equal")
        self.topplot.tick_params(bottom=TRUE,top=FALSE,left=TRUE,right=FALSE)
        self.topplot.grid(axis="y", color=self.grcolor, alpha=0.5, linewidth = 0.5, linestyle=":")
        self.topplot.set_ylabel("Distance (yds)")
        self.topplot.set_xlabel("Deflection (yds)")

        self.threedp = self.threedf.add_subplot(111,projection="3d")
        self.threedp.set_xlabel("Distance (yds)")
        self.threedp.set_ylabel("Deflection (yds)")
        self.threedp.set_zlabel("Height (yds)")
        self.threedp.invert_xaxis()
        self.threedp.view_init(30,0)

        self.fig.tight_layout()

    def drawEraseCube(self,min,max):
        alignmentline = self.threedp.plot([min,max],[min,max],[min,max],linestyle='-',color="#ffffff")

        line = alignmentline.pop(0)
        line.remove()
        self.plotthreed.draw()
    
    def incrementPlColor(self):
        rcolorval = int(self.plcolor[1:3],16)
        gcolorval = int(self.plcolor[3:5],16)
        bcolorval = int(self.plcolor[5:7],16)
        increment = 20
        if rcolorval == min(rcolorval,gcolorval,bcolorval) and gcolorval != max(rcolorval,gcolorval,bcolorval):
            gcolorval = gcolorval + increment #if red is lowest and green is not is highest, increase green
        elif gcolorval == max(rcolorval,gcolorval,bcolorval) and bcolorval != min(rcolorval,gcolorval,bcolorval):
            bcolorval = bcolorval - increment #if green is highest, decrease blue
        elif bcolorval == min(rcolorval,gcolorval,bcolorval) and rcolorval != max(rcolorval,gcolorval,bcolorval):
            rcolorval = rcolorval + increment #if blue is lowest, increase red
        elif rcolorval == max(rcolorval,gcolorval,bcolorval) and gcolorval != min(rcolorval,gcolorval,bcolorval):
            gcolorval = gcolorval - increment #if red is highest, decrease green
        elif gcolorval == min(rcolorval,gcolorval,bcolorval) and bcolorval != max(rcolorval,gcolorval,bcolorval):
            bcolorval = bcolorval + increment #if green is lowest, increase blue
        elif bcolorval == max(rcolorval,gcolorval,bcolorval):
            rcolorval = rcolorval - increment #if blue is highest, decrease red blue

        # print(rcolorval)
        # print(gcolorval)
        # print(bcolorval)
        self.plcolor = "#" + str(format(rcolorval,"x")) + str(format(gcolorval,"x")) + str(format(bcolorval,"x"))
    
    def resetPlColor(self):
        self.plcolor = "#8080e4"

    def plotdata(self,xdata,ydata,zdata):
        self.incrementPlColor()

        if self.clrplt.get():
            # Clear figures
            self.fig.clf()
            self.threedf.clf()
            self.makesubplots()
            self.resetPlColor()
        
        self.totalcarry.set(str(round(xdata[-1],1)))
        self.apex.set(str(round(max(ydata)*3,1)))

        tdplotmin = min(min(xdata),min(ydata),min(zdata))
        tdplotmax = max(max(xdata),max(ydata),max(zdata))

        yheight = yardstofeet(ydata)
        

        self.sideplot.plot(xdata,yheight,linestyle='-',color=self.plcolor)
        self.topplot.plot(zdata,xdata,linestyle='-',color=self.plcolor)
        self.plotcanvas.draw()

        self.threedp.plot(xdata,zdata,ydata,linestyle='-',color=self.plcolor)
        self.plotthreed.draw()
        self.drawEraseCube(tdplotmin,tdplotmax)
        
        
        
        

if __name__ == '__main__':
    wifiUI = uiWindow()
    wifiUI.start()