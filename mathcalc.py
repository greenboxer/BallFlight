# Setup a bunch of global variables
DragCoefficient = 0.275 # default Cd
AirDensity = 1.225      # kg/m^3
AirDynDens = 1.805e-5   # kg/m-s
SurfaceArea = 0.001330  # m^2 effective surface area (dimpled) 0.00133
Radius = 0.042672       # meters
Vx0 = 40                # m/s
Vy0 = 25                # m/s
Vz0 = 0                 # m/s
BackSpin = 104.719755   # rad/s Z axis spin
SideSpin = 14.719755    # rad/s Y axis spin this needs to be *-1 in the equations for convention
BarrelSp = 0            # rad/s X axis spin
g = 9.8                 # m/s^2
m = 0.04592623          # kg weight of golf ball
balldiam = 0.042672     # meters
spindecay = 0.04        # 4% per second

import math

def calcX(dt,vx,vy,vz):
    xresist = calcAirResist(vx)
    xmagnus = calcMagnus(BackSpin,-vy)
    zmagnus = calcMagnus(-SideSpin,vz)
    dx = vx*dt # need to solve for dx
    vx = vx - xresist*dt/m + xmagnus*dt/m + zmagnus*dt/m
    return dx,vx

def calcY(dt,vy,vx,vz):
    yresist = calcAirResist(vy)
    ymagnus = calcMagnus(BackSpin,vx)
    zmagnus = calcMagnus(BarrelSp,-vz)
    
    dy = vy*dt  # need to solve for dy
    vy = vy - g*dt - yresist*dt/m + ymagnus*dt/m + zmagnus*dt/m
    return dy,vy

def calcZ(dt,vz,vx,vy):
    zresist = calcAirResist(vz)
    ymagnus = calcMagnus(BarrelSp,vy)
    xmagnus = calcMagnus(-SideSpin,-vx)
    dz = vz*dt
    vz = vz - zresist*dt/m - xmagnus*dt/m + ymagnus*dt/m
    return dz,vz

def calcAirResist(Velocity):
    calcDragCoef(Velocity)
    airResistance = 0.5 * DragCoefficient * AirDensity * SurfaceArea * Velocity**2
    return airResistance

def calcDragCoef(Velocity):
    global DragCoefficient
    reynolds = AirDensity * Velocity * balldiam / AirDynDens
    # At High velocities there will be less drag
    DragCoefficient = max(min(1.35 - 1.0e-5 * reynolds,1),0.15) # Rough estimate based on available prov1 and chromesoft data

def calcMagnus(s1,v1):
    g = 2 * math.pi * Radius**2 * s1        # MagnusCoefficient
    Mforce = AirDensity * v1 * g * 0.001    # linear G i forget why i needed 0.001
    return Mforce

def calcSpinDecay(dt):
    global BackSpin
    global SideSpin

    BackSpin = BackSpin - BackSpin*spindecay*dt
    SideSpin = SideSpin - SideSpin*spindecay*dt

def updateGlobals(ballspeed,launchangle,sprate,sangle,sspinr):
    global Vy0
    global Vx0
    global Vz0
    global BackSpin
    global SideSpin

    Vx0 = ballspeed * 0.44704 * math.cos(math.radians(launchangle)) # Convert mph to m/s
    Vy0 = ballspeed * 0.44704 * math.sin(math.radians(launchangle)) # Convert mph to m/s
    Vz0 = ballspeed * 0.44704 * math.sin(math.radians(sangle))
    BackSpin = sprate * 2 * math.pi / 60 # Convert RPM to rad/sec
    SideSpin = sspinr * 2 * math.pi / 60 # Convert RPM to rad/sec

def getInitialV():
    global Vy0
    global Vx0
    global Vz0
    return Vx0,Vy0,Vz0

def meterstoyards(meter_array):
    yard_array = [element * 1.09361 for element in meter_array] # Convert meters to yards
    return yard_array

def yardstofeet(yard_array):
    ft_array = [element * 3 for element in yard_array] # Convert yards to meters
    return ft_array


if __name__ == '__main__':
    print("Test")