Web VPython 3.2

scene = canvas(width=600, height=600)

scene.container = "left"
scene.append_to_caption('<h3 style="margin-top:20px;">Balloon Parameters</h3>')

scene.userzoom = False
scene.userspin = True
scene.userpan = True
scene.resizable = False
scene.autoscale = False

fluidDens = 1.225 #kg/m^3
airTemperature = 273.15 #Kelvin at 1 bar
vx = 0
vy = 0
velocity = 0
dragCoeff = 0.5
crossSectArea = 467 #pi*r^2
airPressure = 101325 # Pa
balloonMass = 350
payloadMass = 124 #kg (one person = 62kg)
gravity = 9.80665
fluidVol = 4/3 * pi * (sqrt(crossSectArea / pi))**3
sizeOfBalloonMass = fluidVol * fluidDens # massOfAir but in kg
mass = balloonMass + payloadMass + sizeOfBalloonMass # total mass calculated w/ massOfAir in sizeOfBalloonMass
altitude = 0
heightAboveSeaLvl = 0
material = 'Nylon'
air = 'Air'
wind = 0
homePlanet = "Earth"
pressureAtSeaLevel = 101325
molarMass = 0.028965
flameTemperature = 225 + 273.15 #Kelvin
numberOfMoles = (fluidVol * fluidDens / 1000) / 28.965
massOfAir = fluidVol * fluidDens / 1000 # in g
planetMass = 5.97219 * (10 ** 24)
crossSectAreaDueToTemp = 0
totalCrossSectionalArea = crossSectArea + crossSectAreaDueToTemp
newFluidVol = fluidVol * ((273.15) / airTemperature)   

# variables: fluid density, velocity, drag coefficient, cross sectional area, mass, gravity, fluid volume, altitude

# def setMass(event):
#     global mass
#     if event.id == 'x':
#         mass = event.value

#def setfluidDens():
 #   global fluidDens
  #  fluidDens = 45

def setPlanet(p):
    global homePlanet
    if p.checked:
        homePlanet = p.plan
        setDefaults(homePlanet)
    else:
        setDefaults("Earth")
    for i in range(len(buttons)):
        if i != p.i:
            buttons[i].checked = False

def setDefaults(x):
    global fluidDens, airTemperature, dragCoeff, planetMass, air
    if x == "Earth":
        backgroundPic = "https://i.imgur.com/wHGxacb.png"
        fluidDens = 1.225 #at 1 bar
        airTemperature = 273.15 #Kelvin at 1 bar
        dragCoeff = 0.5 #based on Atlas rocket https://web.archive.org/web/20170313142729/http://www.braeunig.us/apollo/saturnV.htm
        planetMass = 5.97219 * (10 ** 24)
        air = 'Air'
    elif x == "Saturn": #done
        backgroundPic = "mars.png"
        fluidDens = 0.19 #at 1 bar
        airTemperature = 134 #Kelvin at 1 bar
        dragCoeff = 0.515 #based on Atlas rocket https://web.archive.org/web/20170313142729/http://www.braeunig.us/apollo/saturnV.htm
        planetMass = 5.684*10**26
        air = 'Helium'
    elif x == "Venus": #done
        backgroundPic = "mars.png"
        fluidDens = 65 #kg/m^3 at surface - would be much lower at 1 bar
        airTemperature = 301.5 #Kelvin at 1 bar
        dragCoeff = 2 #between 1.7-2.3
        planetMass = 4.8673*10**24
        air = 'Carbon Dioxide'
    elif x == "Mars":
        backgroundPic = "mars.png"
        fluidDens = 0.020      # kg/m³ @ surface (~0.006 bar)
        airTemperature = 210.0      # K  (–63 °C), no 1 bar level exists
        dragCoeff = 0.3
        planetMass = 6.4171e23  # kg
        air = "Carbon Dioxide"
    elif x == "Jupiter":
        backgroundPic = "jupiter.png"
        fluidDens = 0.16       # kg/m³ @ 1 bar
        airTemperature = 165.0      # K  (–108 °C)
        dragCoeff = 0.47
        planetMass = 1.8982e27  # kg
        air = "Helium"
    elif x == "Neptune":
        backgroundPic = "neptune.png"
        fluidDens = 0.45       # kg/m³ @ 1 bar
        airTemperature = 72.0       # K  (–201 °C)
        dragCoeff = 0.47
        planetMass = 1.02413e26 # kg
        air = "Helium"
    elif x == "Uranus":
        backgroundPic = "uranus.png"
        fluidDens = 0.22       # kg/m³ @ 1 bar
        airTemperature = 76.0       # K  (–197 °C)
        dragCoeff = 0.47
        planetMass = 8.6810e25  # kg
        air = "Helium"
    backgroundBox.texture = backgroundPic
        
def changeAir(evt): # stp
    global air, molarMass, fluidDens, numberOfMoles, massOfAir
    air = evt.selected
    if air == 'Air':
        molarMass = 28.965 #g/mol
        fluidDens = 1.225 #kg/m^3
    elif air == 'Hydrogen':
        molarMass = 2
        fluidDens = 0.09 
    elif air == 'Nitrogen':
        molarMass = 28.02 
        fluidDens = 1.2506 
    elif air == 'Helium':
        molarMass = 4 
        fluidDens = 0.1784
    elif air == 'Oxygen':
        molarMass = 32
        fluidDens = 1.43
    elif air == 'Tungsten hexafluoride':
        molarMass = 297.83
        fluidDens = 13
    elif air == 'Carbon Dioxide':
        molarMass = 44.003
        fluidDens = 1.98
    
    massOfAir = fluidVol * fluidDens / 1000
    numberOfMoles = massOfAir / molarMass

venusRadio = radio(bind=setPlanet, text = "Venus", i = 0, plan = "Venus")
marsRadio = radio(bind=setPlanet, text = "Mars", i = 1, plan = "Mars")
earthRadio = radio(bind=setPlanet, text = "Earth", i = 2, plan = "Earth", checked = True)
saturnRadio = radio(bind=setPlanet, text = "Saturn", i = 3, plan = "Saturn")
jupiterRadio = radio(bind=setPlanet, text = "Jupiter", i = 4, plan = "Jupiter")
neptuneRadio = radio(bind=setPlanet, text = "Neptune", i = 5, plan = "Neptune")
uranusRadio = radio(bind=setPlanet, text = "Uranus", i = 6, plan = "Uranus")

buttons = [saturnRadio, earthRadio, venusRadio, jupiterRadio, neptuneRadio, uranusRadio, marsRadio] 

scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')

passengerSlider = slider(min = 0, max = 10, value = 2, bind = numPassengers, step = 1)
scene.append_to_caption('</div>')

def numPassengers(s):
    global mass, sizeOfBalloonMass, payloadMass, balloonMass
    payloadMass = s.value * 62
    mass = sizeOfBalloonMass + payloadMass + balloonMass
    numPassengersValueDisplay.text = str(passengerSlider.value)
    
numPassengersTextDisplay = wtext(text = 'Number of Passengers = ')
numPassengersValueDisplay = wtext(text = str(passengerSlider.value))

scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')
sizeOfBalloonSlider = slider(bind = balloonSize, min = 150, max = 1000, value = 222)
scene.append_to_caption('</div>')

def balloonSize(s):
    global crossSectArea, mass, fluidVol, sizeOfBalloonMass, payloadMass, balloonMass
    crossSectArea = sizeOfBalloonSlider.value
    balloonSizeValueDisplay.text = str(sizeOfBalloonSlider.value)
    radius = sqrt(crossSectArea / pi)
    fluidVol = (4/3)*pi*radius**3
    sizeOfBalloonMass = fluidDens * fluidVol
    mass = sizeOfBalloonMass + payloadMass + balloonMass

balloonSizeTextDisplay = wtext(text = 'Cross Sectional Area of Balloon (m^2) = ')
balloonSizeValueDisplay = wtext(text = str(sizeOfBalloonSlider.value))
    
scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')
tempOfFlameSlider = slider(bind = changeTemp, min = 0, max = 350, value = 0)
scene.append_to_caption('</div>')

def changeTemp(s):
    global flameTemperature, fluidVol, crossSectAreaDueToTemp, totalCrossSectionalArea, crossSectArea, newFluidVol
    flameTemperature = tempOfFlameSlider.value
    tempOfFlameValueDisplay.text = str(tempOfFlameSlider.value)
    newFluidVol = fluidVol * ((tempOfFlameSlider.value + 273.15) / airTemperature)    
    newRadius = pow(((3/4) * newFluidVol / pi),(1/3))
    totalCrossSectionalArea = pi * newRadius ** 2
    crossSectAreaDueToTemp = totalCrossSectionalArea - crossSectArea

tempOfFlameTextDisplay = wtext(text = 'Temperature of Flame (°C) = ')
tempOfFlameValueDisplay = wtext(text = str(tempOfFlameSlider.value))

scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')
windSlider = slider(bind = changeWind, min = -100, max = 100, value = 0)
scene.append_to_caption('</div>')

def changeWind(s):
    global wind, vx
    wind = windSlider.value
    vx = wind * 1000/3600
    windValueDisplay.text = str(windSlider.value)

windTextDisplay = wtext(text = 'Wind Speed (km/h) = ')
windValueDisplay = wtext(text = str(windSlider.value))
scene.append_to_caption('<div></div>')

choicelist = ['Nylon', 'Polyester',
             'Wicker', 'Stainless steel', 'Copper', 'Aluminum', 
             'Plastic', 'Leather', 'Suede']

menu(choices=choicelist, bind=changeMaterial)
windCaption = wtext(text = ' Material: ' + material + ' ')
scene.append_to_caption('<div></div>')

airList = ['Air', 'Hydrogen', 'Nitrogen', 'Helium', 'Oxygen', 'Carbon Dioxide', 'Tungsten hexafluoride']

menu(choices=airList, bind=changeAir)
airCaption = wtext(text = ' Air: ' + air + " ")

running = False

def start(b):
    global running
    running = True
    if running: 
        startButton.text = "Running"
    else: 
        startButton.text = "Run"

def reset(b):
    global running, time, posx, posy, vx, vy, altitude, heightAboveSeaLvl, balloon, speedCurve, altitudeCurve, forceCurve
    running = False
    startButton.text = "Run"
    
    time = 0
    altitude = 0
    heightAboveSeaLvl = 0
    posx = 0
    posy = 0
    
    vx = 0
    vy = 0
    
    balloon.pos = vec(0, altitude - 9, 0)
    
    speedCurve.delete()
    altitudeCurve.delete() 
    forceCurve.delete()
    
    speedCurve = gcurve(graph=speedVsTime, color=color.red)
    altitudeCurve = gcurve(graph=altitudeVsTime, color=color.green)
    forceCurve = gcurve(graph=forceVsTime, color=color.blue)
    
    scene.center = balloon.pos
    
startButton = button(text = "Run", pos = scene.title_anchor, bind = start)
resetButton = button(text = "Reset", pos = scene.title_anchor, bind = reset)

balloon = sphere(pos = vec(0, altitude - 9, 0), radius = sqrt(totalCrossSectionalArea/pi) / 50, color = color.blue)
#attach_arrow(balloon, "velocity", color=color.green, scale=10, shaftwidth=balloon.radius/3)

def changeMaterial(evt):
    global balloonMass, fluidVol
    materialDens = 0
    if evt.index < 1:
        balloon.texture = "https://i.imgur.com/YwqXpCA.jpeg"
        materialDens = 1150  # Nylon, kg/m^3
    elif evt.index == 1:
        balloon.texture = "https://i.imgur.com/aHf7shx.png"
        materialDens = 1380  # Polyester, kg/m^3
    elif evt.index == 2:
        balloon.texture = "https://i.imgur.com/z1NDKU1.png"
        materialDens = 500   # Wicker (approx), kg/m^3
    elif evt.index == 3: 
        balloon.texture = "https://i.imgur.com/z1NDKU1.png"
        materialDens = 8000  # Stainless steel, kg/m^3
    elif evt.index == 4: 
        balloon.texture = "https://i.imgur.com/FkrZo0R.png"
        materialDens = 8960  # Copper, kg/m^3
    elif evt.index == 5:
        balloon.texture = "https://i.imgur.com/zEuDPcK.jpeg"
        materialDens = 2700  # Aluminum, kg/m^3
    elif evt.index == 6:
        balloon.texture = "https://i.imgur.com/puph7Hw.jpeg"
        materialDens = 1200  # Plastic (average), kg/m^3
    elif evt.index == 7:
        balloon.texture = "https://i.imgur.com/NqIjoHj.jpeg"
        materialDens = 950   # Leather, kg/m^3
    elif evt.index == 8:
        balloon.texture = "https://i.imgur.com/3N4NFBM.jpeg"
        materialDens = 700   # Suede (approx), kg/m^3
    balloonMass = materialDens * pow(fluidVol * (3/4) / pi, (2/3)) * 4 * pi
        
backgroundBox = box(pos = vector(0, 0, -1), size = vector(40, 40, 0.1), texture = "https://i.imgur.com/wHGxacb.png")

time = 0; dt=0.01

posx = balloon.pos.x
posy = balloon.pos.y

vx = 0
ay = 0
ax = 0

balloon.velocity = 0
    
speedVsTime = graph(title = 'Speed vs Time', xtitle = 'Time (s)', ytitle = 'Speed (m/s)', xmin = 0, ymin = 0, width=380, height=180)
altitudeVsTime = graph(title = 'Altitude vs Time', xtitle = 'Time (s)', ytitle = 'Altitude (m)', xmin = 0, ymin = 0, width=380, height=180)
forceVsTime = graph(title='Net Force vs Time', xtitle='Time (s)', ytitle='Force (N)', xmin=0, width=380, height=180)    

speedCurve = gcurve(graph=speedVsTime, color=color.red)
altitudeCurve = gcurve(graph=altitudeVsTime, color=color.green)
forceCurve = gcurve(graph=forceVsTime, color=color.blue)

while True:
    global velocity, airPressure, newFluidVol, fluidVol, heightAboveSeaLvl, flameTemperature, fluidDens, dragForce, dragXForce, dragYForce, gravForce, buoForce, totalXForce, totalYForce, ax, ay, viy, vix, vfy, vfx, posxIncr, posyIncr, finalPosX, finalPosY, altitude, vy, vx, posx, posy, time, mass, balloonMass, payloadMass, sizeOfBalloonMass, crossSectArea, crossSectAreaDueToTemp, totalCrossSectionalArea, wind
    
    rate(100)
    if running:        
        if heightAboveSeaLvl < 0:
            print("height" + heightAboveSeaLvl)
            running = False
        else:
            hotAirDensity = fluidDens * (airTemperature / (tempOfFlameSlider.value + 273.15))

            newFluidVol = fluidVol * ((tempOfFlameSlider.value + 273.15) / airTemperature)    
            sizeOfBalloonMass = newFluidVol * hotAirDensity
            mass = balloonMass + payloadMass + sizeOfBalloonMass

            newRadius = pow(((3/4) * newFluidVol / pi),(1/3))
            totalCrossSectionalArea = pi * newRadius ** 2
            
            balloon.radius = (sqrt(totalCrossSectionalArea/pi) / 50)

            velocity = sqrt(vx**2 + vy**2)
            airPressureOut = (pressureAtSeaLevel)*(exp((-(molarMass)*gravity*heightAboveSeaLvl)/(8.314 * (airTemperature)))) #Pascals
            fluidDensOut = (airPressureOut)/((287.058)*(airTemperature)) #kg/m^3

            airPressureIn = (pressureAtSeaLevel)*(exp(-(molarMass)*gravity*heightAboveSeaLvl)/(8.314 * (tempOfFlameSlider.value + 273.15))) #Pascals
            fluidDensIn = (airPressureIn)/((287.058)*(tempOfFlameSlider.value + 273.15)) #kg/m^3

            fluidDensDiff = fluidDensOut - fluidDensIn
                
            if velocity > 0:
                drag_magnitude = 0.5 * fluidDensOut * velocity**2 * dragCoeff * totalCrossSectionalArea
                dragXForce = -drag_magnitude * (vx / velocity)
                dragYForce = -drag_magnitude * (vy / velocity)
            else:
                dragXForce = 0
                dragYForce = 0
            
            gravForce = mass * gravity
            buoForce = (fluidDensDiff) * gravity * newFluidVol  # archimedes principle
        
            totalXForce = dragXForce
            totalYForce = buoForce - gravForce + dragYForce
            
            totalForceFinal = sqrt(totalXForce*totalXForce + totalYForce*totalYForce)
        
            print("buo" + buoForce)
            print("grav" + gravForce)
            print("drag" + dragYForce)
        
            print(totalYForce)
            print(posy)
                
            ay = totalYForce / mass
            ax = totalXForce / mass
            
            viy = vy
            vix = vx
            vfy = vy + ay * dt 
            vfx = vx + ax * dt
            
            if abs(ax) > 0:
                posxIncr = (vfx**2 - vix**2) / (2*ax)
            else:
                posxIncr = vfx * dt
            if abs(ay) > 0:
                posyIncr = (vfy**2 - viy**2) / (2*ay)
            else:
                posyIncr = vfy * dt
        
            finalPosX = posx + posxIncr
            finalPosY = posy + posyIncr
        
            balloon.pos = vec(finalPosX, finalPosY, 0)
            
            altitude = finalPosY
            posx = finalPosX
            posy = finalPosY
            
            vy = vfy
            vx = vfx
            
            speedCurve.plot(time, abs(vfy))
            altitudeCurve.plot(time, posy+9)
            forceCurve.plot(time, totalForceFinal)
            
            scene.center = balloon.pos

            heightAboveSeaLvl = altitude + 9
            
            time += dt
            
