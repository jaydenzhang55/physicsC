Web VPython 3.2

scene = canvas(width=1450, height=600)
scene.append_to_title('<h1 style="margin-top:20px; text-align:center"><i>Hot</i> AIR BALLOON SIMULATOR!</h1>')
scene.background = vector(0.3, 0.6, 1)

startButton = button(text = "Run", pos = scene.caption_anchor, bind = start)
resetButton = button(text = "Reset", pos = scene.caption_anchor, bind = reset)

scene.container = "left"
scene.append_to_caption('<h3 style="margin-top:5px; text-align:center">Balloon Parameters</h3>')

scene.userzoom = False
scene.userspin = False
scene.userpan = False
scene.resizable = False
scene.autoscale = False

fluidDens = 1.225 #kg/m^3
airTemperature = 273.15 #Kelvin at 1 bar
vx = 0
vix = 0
vfx = 0
vfy = 0
vfx = 0
vy = 0
ax = 0
ay = 0
velocity = 0
dragCoeff = 0.5
crossSectArea = 225.25 #pi*r^2
airPressure = 101325 # Pa
payloadMass = 124 #kg (one person = 62kg)
fluidVol = 4/3 * pi * (sqrt(crossSectArea / pi))**3
sizeOfBalloonMass = fluidVol * fluidDens # massOfAir but in kg
altitude = -16.25
heightAboveSeaLvl = 0
material = 'Nylon'
air = 'Air'
wind = 0
homePlanet = "Earth"
pressureAtSeaLevel = 101325
molarMass = 28.965 #g/mol
flameTemperature = 100 + 273.15 #Kelvin
numberOfMoles = (fluidVol * fluidDens / 1000) / 28.965
massOfAir = fluidVol * fluidDens / 1000 # in g
planetMass = 5.97219 * (10 ** 24)
newFluidVol = fluidVol * ((100 + 273.15) / airTemperature)   
totalCrossSectionalArea = pi * pow(((3/4) * newFluidVol / pi),(1/3)) ** 2
crossSectAreaDueToTemp = totalCrossSectionalArea - crossSectArea
gravitationalC = 6.6743 * 10 ** -11
planetRadius = 6378 * 10 ** 3
speccAirConst = 287.058    
materialDens = 1150
result = False
thickness = 2 * 10 ** -5 #m
balloonMass = balloonMass = materialDens * 4 * crossSectArea * thickness # should NOT change unless crossSectArea is changing
mass = balloonMass + payloadMass + sizeOfBalloonMass # total mass calculated w/ massOfAir in sizeOfBalloonMass
dragResult = False
maxAltitude = 0.02 * planetRadius
t = 0
windAngle = 0
relWindVy = 0
relWindVx = 0
airOfPlanet = "Air"
molarMassPlanet = 28.965
speccAirConstPlanet = 287.058
fluidDensPlanet = 1.225
landscapeObjects = []

# variables: fluid density, velocity, drag coefficient, cross sectional area, mass, gravity, fluid volume, altitude

# def setMass(event):
#     global mass
#     if event.id == 'x':
#         mass = event.value

#def setfluidDens():
 #   global fluidDens
  #  fluidDens = 45

def check():
    global vx, vy
    if not running:
        vx = 0
        vy = 0

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

def setDefaults(evt):
    global fluidDens, airTemperature, dragCoeff, planetMass, airOfPlanet, planetRadius, molarMassPlanet, speccAirConstPlanet, fluidDensPlanet    
    x = evt.text.strip()
    if x == "Earth":
        backgroundPic = "https://i.imgur.com/v1IQIPy.png"
        fluidDens = 1.225 #at 1 bar
        airTemperature = 273.15 #Kelvin at 1 bar
        dragCoeff = 0.5 #based on Atlas rocket https://web.archive.org/web/20170313142729/http://www.braeunig.us/apollo/saturnV.htm
        planetMass = 5.97219 * (10 ** 24)
        planetRadius = 6378 * 10 ** 3
        airOfPlanet = 'Air'
        molarMassPlanet = 28.965
        fluidDensPlanet = 1.225
        speccAirConstPlanet = 287.058
    elif x == "Saturn": #done
        backgroundPic = "https://i.imgur.com/ONgh9aA.png"
        fluidDens = 0.19 #at 1 bar
        airTemperature = 134 #Kelvin at 1 bar
        dragCoeff = 0.515 #based on Atlas rocket https://web.archive.org/web/20170313142729/http://www.braeunig.us/apollo/saturnV.htm
        planetMass = 5.684*10**26
        planetRadius = 60268*10**3
        airOfPlanet = 'Helium'
        molarMassPlanet = 4 
        fluidDensPlanet = 0.1784
        speccAirConstPlanet = 2077
    elif x == "Venus": #done
        backgroundPic = "https://i.imgur.com/ao1TDhl.png"
        fluidDens = 65 #kg/m^3 at surface - would be much lower at 1 bar
        airTemperature = 301.5 #Kelvin at 1 bar
        dragCoeff = 2 #between 1.7-2.3
        planetMass = 4.8673*10**24
        planetRadius = 6052*10**3
        airOfPlanet = 'Carbon Dioxide'
        molarMassPlanet = 44.003
        fluidDensPlanet = 1.98
        speccAirConstPlanet = 188.9
    elif x == "Mars":
        backgroundPic = "https://i.imgur.com/aFW1iTl.png"
        fluidDens = 0.020      # kg/m³ @ surface (~0.006 bar)
        airTemperature = 210.0      # K  (–63 °C), no 1 bar level exists
        dragCoeff = 0.3
        planetMass = 6.4171* 10 ** 23  # kg
        planetRadius = 3396 * 10**3
        airOfPlanet = "Carbon Dioxide"
        molarMassPlanet = 44.003
        fluidDensPlanet = 1.98
        speccAirConstPlanet = 188.9
    elif x == "Jupiter":
        backgroundPic = "https://i.imgur.com/kVOR7oH.png"
        fluidDens = 0.16       # kg/m³ @ 1 bar
        airTemperature = 165.0      # K  (–108 °C)
        dragCoeff = 0.47
        planetMass = 1.8982 * 10 ** 27  # kg
        planetRadius = 71492*10**3
        airOfPlanet = "Helium"
        molarMassPlanet = 4  
        fluidDensPlanet = 0.1784
        speccAirConstPlanet = 2077
    elif x == "Neptune":
        backgroundPic = "https://i.imgur.com/PRQPcN6.png"
        fluidDens = 0.45       # kg/m³ @ 1 bar
        airTemperature = 72.0       # K  (–201 °C)
        dragCoeff = 0.47
        planetMass = 1.02413* 10 ** 26 # kg
        planetRadius = 24764 * 10**3
        airOfPlanet = "Helium"
        molarMassPlanet = 4 
        fluidDensPlanet = 0.1784
        speccAirConstPlanet = 2077
    elif x == "Uranus":
        backgroundPic = "https://i.imgur.com/xvepFcP.png"
        fluidDens = 0.22       # kg/m³ @ 1 bar
        airTemperature = 76.0       # K  (–197 °C)
        dragCoeff = 0.47
        planetMass = 8.6810 * 10 ** 25  # kg
        planetRadius = 25559 * 10 ** 3
        airOfPlanet = "Helium"
        molarMassPlanet = 4  
        fluidDensPlanet = 0.1784
        speccAirConstPlanet = 2077
    # backgroundBox.texture = backgroundPic
        
def changeAir(evt): # stp
    global air, molarMass, fluidDens, numberOfMoles, massOfAir, speccAirConst, sizeOfBalloonMass, mass
    air = evt.selected
    if air == 'Air':
        molarMass = 28.965 #g/mol
        fluidDens = 1.225 #kg/m^3
        speccAirConst = 287.058
    elif air == 'Hydrogen':
        molarMass = 2
        fluidDens = 0.09
        speccAirConst = 4.1242
    elif air == 'Nitrogen':
        molarMass = 28.02 
        fluidDens = 1.2506 
        speccAirConst = 296.8
    elif air == 'Helium':
        molarMass = 4 
        fluidDens = 0.1784
        speccAirConst = 2077
    elif air == 'Oxygen':
        molarMass = 32
        fluidDens = 1.43
        speccAirConst = 218
    elif air == 'Tungsten hexafluoride':
        molarMass = 297.83
        fluidDens = 13
        speccAirConst = 27.91
    elif air == 'Carbon Dioxide':
        molarMass = 44.003
        fluidDens = 1.98
        speccAirConst = 188.9
    
    massOfAir = fluidVol * fluidDens / 1000
    numberOfMoles = massOfAir / molarMass

    sizeOfBalloonMass = fluidVol * fluidDens
    mass = balloonMass + payloadMass + sizeOfBalloonMass

    check()

venusRadio = radio(bind=setPlanet, text = "Venus                              ", i = 0, plan = "Venus", checked = False)
marsRadio = radio(bind=setPlanet, text = "Mars                                 ", i = 1, plan = "Mars", checked = False)
earthRadio = radio(bind=setPlanet, text = "Earth                              ", i = 2, plan = "Earth", checked = True)
saturnRadio = radio(bind=setPlanet, text = "Saturn                              ", i = 3, plan = "Saturn", checked = False)
jupiterRadio = radio(bind=setPlanet, text = "Jupiter                              ", i = 4, plan = "Jupiter", checked = False)
neptuneRadio = radio(bind=setPlanet, text = "Neptune                              ", i = 5, plan = "Neptune", checked = False)
uranusRadio = radio(bind=setPlanet, text = "Uranus", i = 6, plan = "Uranus", checked = False)

buttons = [saturnRadio, earthRadio, venusRadio, jupiterRadio, neptuneRadio, uranusRadio, marsRadio] 

scene.append_to_caption('<div style="margin-top: 10px;">')

choicelist = ['Nylon', 'Polyester',
             'Wicker', 'Stainless steel', 'Copper', 'Aluminum', 
             'Plastic', 'Leather', 'Suede']

materialCaption = wtext(text = ' Material: ')
materialMenu = menu(choices=choicelist, bind=changeMaterial)

airList = ['Air', 'Hydrogen', 'Nitrogen', 'Helium', 'Oxygen', 'Carbon Dioxide', 'Tungsten hexafluoride']
airCaption = wtext(text = '                                                                                                                                                                                                                 Air: ')
airMenu = menu(choices=airList, bind=changeAir)

scene.append_to_caption('</div>')



def numPassengers(s):
    global mass, sizeOfBalloonMass, payloadMass, balloonMass
    payloadMass = s.value * 62
    mass = sizeOfBalloonMass + payloadMass + balloonMass
    numPassengersValueDisplay.text = str(passengerSlider.value)

    check()

def balloonSize():
    global crossSectArea, mass, fluidVol, sizeOfBalloonMass, payloadMass, balloonMass, totalCrossSectionalArea, balloon
    crossSectArea = sizeOfBalloonSlider.value
    balloonSizeValueDisplay.text = str(sizeOfBalloonSlider.value)
    radius = sqrt(crossSectArea / pi)
    fluidVol = (4/3)*pi*radius**3
    sizeOfBalloonMass = fluidDens * fluidVol
    mass = sizeOfBalloonMass + payloadMass + balloonMass
    changeTemp()
    balloon = createBalloon(sqrt(totalCrossSectionalArea/pi) / 4)

    check()



scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')
sizeOfBalloonSlider = slider(bind = balloonSize, min = 150, max = 1000, value = 222.25, step = 0.25)
balloonSizeTextDisplay = wtext(text = 'Cross Sectional Area of Balloon (m^2) = ')
balloonSizeValueDisplay = wtext(text = str(sizeOfBalloonSlider.value))
balloonSizeCaptionSpace = wtext(text = "                             ")
scene.append_to_caption('</div>')

passengerSlider = slider(min = 0, max = 10, value = 2, bind = numPassengers, step = 1)
numPassengersTextDisplay = wtext(text = 'Number of Passengers = ')
numPassengersValueDisplay = wtext(text = str(passengerSlider.value))


def changeTemp():
    global flameTemperature, fluidVol, crossSectAreaDueToTemp, totalCrossSectionalArea, crossSectArea, newFluidVol, balloon
    flameTemperature = tempOfFlameSlider.value
    tempOfFlameValueDisplay.text = str(tempOfFlameSlider.value)
    newFluidVol = fluidVol * ((tempOfFlameSlider.value + 273.15) / airTemperature)    
    newRadius = pow(((3/4) * newFluidVol / pi),(1/3))
    totalCrossSectionalArea = pi * newRadius ** 2
    crossSectAreaDueToTemp = totalCrossSectionalArea - crossSectArea

    balloon = createBalloon(sqrt(totalCrossSectionalArea/pi) / 4)

    check()

scene.append_to_caption('<div id="a">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')
tempOfFlameSlider = slider(bind = changeTemp, min = 0, max = 350, value = 100, step = 0.01)
tempOfFlameTextDisplay = wtext(text = 'Temperature of Flame (°C) = ')
tempOfFlameValueDisplay = wtext(text = str(tempOfFlameSlider.value))
tempOfFlameSliderText = wtext(text = "                                                  ")
scene.append_to_caption('</div>')


def changeWind(s):
    global wind
    wind = windSlider.value
    windValueDisplay.text = str(windSlider.value)
    check()

windSlider = slider(bind = changeWind, min = 0, max = 100, value = 0)
windTextDisplay = wtext(text = 'Wind (km/h) = ')
windValueDisplay = wtext(text = str(windSlider.value))
scene.append_to_caption('<div></div>')

running = False

def createBalloon(radius):
    global balloonTop, balloonBottom, ropeOne, ropeTwo, ropeThree, ropeFour, balloon
    
    if balloon:
        balloon.visible = False
        del balloon
    
    balloonTop = sphere(pos = vector(0, 5, 0), radius = radius, color = color.red)
    balloonBottom = box(pos = vector(0, 0, 0), length = 1.25, height = 0.75, width = 1.25, color = color.gray(0.5))
    ropeOne = cylinder(pos=vector(0.5,0,0.5), axis = vector(0,3.5,0), radius = 0.02, color = vector (0.367, 0.295, 0))
    ropeTwo = cylinder(pos=vector(-0.5,0,0.5), axis = vector(0,3.5,0), radius = 0.02, color = vector (0.367, 0.295, 0))
    ropeThree = cylinder(pos=vector(0.5,0,-0.5), axis = vector(0,3.5,0), radius = 0.02, color = vector (0.367, 0.295, 0))
    ropeFour = cylinder(pos=vector(-0.5,0,-0.5), axis = vector(0,3.5,0), radius = 0.02, color = vector (0.367, 0.295, 0))
    
    balloon = compound([balloonTop, balloonBottom, ropeOne, ropeTwo, ropeThree, ropeFour], pos = vector(0, altitude + 3, 0))
    return balloon

def createTree(pos, scale):
    trunk = cylinder(pos=vector(0, 0, 0), axis=vector(0, 4.5 * scale, 0), radius=0.5 * scale, color=vector(0.580, 0.362, 0))
    l1 = cone(pos=vector(0, 4.5 * scale, 0), axis=vector(0, 2.5 * scale, 0), radius=2 * scale, color=color.green)
    l2 = cone(pos=vector(0, 6 * scale, 0), axis=vector(0, 2.5 * scale, 0), radius=1.5 * scale, color=color.green)
    l3 = cone(pos=vector(0, 7.5 * scale, 0), axis=vector(0, 2 * scale, 0), radius=1 * scale, color=color.green)
    return compound([trunk, l1, l2, l3], pos=pos)

def createTallTree(pos, scale):
    trunk = cylinder(pos=vector(0, 0, 0), axis=vector(0, 8 * scale, 0), radius=0.75 * scale, color=vector(0.580, 0.362, 0))
    l1 = cone(pos=vector(0, 8 * scale, 0), axis=vector(0, 4 * scale, 0), radius=3 * scale, color=color.green)
    l2 = cone(pos=vector(0, 10 * scale, 0), axis=vector(0, 3.75 * scale, 0), radius=2.5 * scale, color=color.green)
    l3 = cone(pos=vector(0, 11.75 * scale, 0), axis=vector(0, 3.5 * scale, 0), radius=2 * scale, color=color.green)
    l4 = cone(pos=vector(0, 13.25 * scale, 0), axis=vector(0, 3.25 * scale, 0), radius=1.5 * scale, color=color.green)
    return compound([trunk, l1, l2, l3, l4], pos=pos)

def createMountain(pos, size):
    return pyramid(pos=pos, size=size, color=color.gray(0.5), axis=vector(0, 1, 0))

def createLandscape():
    global landscapeObjects
    landscapeObjects = []

    ground_main = box(pos=vector(0, -22, -10), size=vector(200, 4, 600), color=color.green*0.6)
    landscapeObjects.append(ground_main)

    for i in range(100):  
        x = -80 + random() * 160  
        z = -40 + random() * 25   
        y = -16.25 
        scale = 0.8 + random() * 0.7
        
        tree = createTree(vector(x, y, z), scale)
        landscapeObjects.append(tree)
    
    for i in range(40):  
        x = -70 + random() * 140
        z = -35 + random() * 23
        y = -16.25  
        scale = 0.6 + random() * 0.6 
        
        tall_tree = createTallTree(vector(x, y, z), scale)
        landscapeObjects.append(tall_tree)
    
    mountainPositions = [
        vector(-60, -26, -80),   
        vector(-30, -26, -90),
        vector(0, -26, -100),    
        vector(35, -26, -85),
        vector(70, -26, -95),
        vector(-90, -26, -70),
        vector(90, -26, -75),
        vector(-45, -26, -120),  
        vector(45, -26, -110),
        vector(0, -26, -130)
    ]
    
    mountainSizes = [
        vector(40, 80, 30),   
        vector(35, 70, 25),
        vector(50, 100, 40), 
        vector(38, 75, 28),
        vector(45, 90, 35),
        vector(42, 85, 32),
        vector(36, 72, 27),
        vector(55, 110, 45),  
        vector(48, 95, 38),
        vector(60, 120, 50)   
    ]

    for i in range(len(mountainPositions)):
        mountain = createMountain(mountainPositions[i], mountainSizes[i])
        landscapeObjects.append(mountain)
    
createLandscape()

def createGraphs():
    global speedVsTime, altitudeVsTime, forceVsTime, speedCurve, altitudeCurve, forceCurve
    
    speedVsTime = graph(title = 'Speed vs Time', xtitle = 'Time (s)', ytitle = 'Speed (m/s)', xmin = 0, ymin = 0, width=1450/3, height=180, align='left')
    altitudeVsTime = graph(title = 'Altitude vs Time', xtitle = 'Time (s)', ytitle = 'Altitude (m)', xmin = 0, ymin = 0, width=1450/3, height=180, align='left')
    forceVsTime = graph(title='Net Force vs Time', xtitle='Time (s)', ytitle='Force (N)', xmin=0, width=1450/3, height=180, align='left')    

    speedCurve = gcurve(graph=speedVsTime, color=color.red)
    altitudeCurve = gcurve(graph=altitudeVsTime, color=color.green)
    forceCurve = gcurve(graph=forceVsTime, color=color.blue)

def deleteGraphs():
    global speedVsTime, altitudeVsTime, forceVsTime, speedCurve, altitudeCurve, forceCurve
    
    if speedCurve:
        speedCurve.delete()
        speedCurve = None

    if altitudeCurve:
        altitudeCurve.delete()
        altitudeCurve = None

    if forceCurve:
        forceCurve.delete()
        forceCurve = None
    
    if speedVsTime:
        speedVsTime.delete()
        speedVsTime = None

    if altitudeVsTime:
        altitudeVsTime.delete()
        altitudeVsTime = None

    if forceVsTime:
        forceVsTime.delete()
        forceVsTime = None

def enableControls():
    startButton.disabled = False
    dtSlider.disabled = False
    passengerSlider.disabled = False
    sizeOfBalloonSlider.disabled = False
    materialMenu.disabled = False
    airMenu.disabled = False
    for button in buttons:
        button.disabled = False

def disableControls():
    startButton.disabled = True
    dtSlider.disabled = True
    passengerSlider.disabled = True
    sizeOfBalloonSlider.disabled = True
    materialMenu.disabled = True
    airMenu.disabled = True
    for button in buttons:
        button.disabled = True

def start(b):
    global running
    running = True
    if running: 
        #print(sqrt(totalCrossSectionalArea/pi) / 8)
        #print(flameTemperature)
        #print(crossSectArea)
        #print(crossSectAreaDueToTemp)
        startButton.text = "Running"
        disableControls()
        createGraphs()
    else: 
        startButton.text = "Run"
        enableControls()

def reset():
    #print("\n" * 100)
    global fluidDensPlanet, molarMassPlanet, speccAirConstPlanet, airOfPlanet, relWindVy, relWindVx, windAngle, t, maxAltitude, vix, vfx, vfy, viy, dragResult, dt, buttons, airTemperature, planetRadius, planetMass, flameTemperature, pressureAtSeaLevel, homePlanet, airPressure, dragCoeff, velocity, numberOfMoles, fluidDens, speccAirConst, molarMass, ax, ay, result, materialDens, material, air, running, time, posx, posy, vx, vy, altitude, heightAboveSeaLvl, balloon, speedCurve, altitudeCurve, forceCurve, crossSectArea, fluidVol, sizeOfBalloonMass, payloadMass, balloonMass, mass, wind, vx    
    running = False
    result = False
    dragResult = False
    startButton.text = "Run"
    enableControls()

    deleteGraphs()
    
    time = 0
    altitude = -16.25
    heightAboveSeaLvl = 0
    posx = 0
    posy = altitude

    dragCoeff = 0.5
    t = 0
    windAngle = 0

    airOfPlanet = "Air"
    molarMassPlanet = 28.965
    speccAirConstPlanet = 287.058
    fluidDensPlanet = 1.225

    airTemperature = 273.15 #Kelvin at 1 bar
    airPressure = 101325 # Pa
    payloadMass = 124 #kg (one person = 62kg)

    homePlanet = "Earth"
    pressureAtSeaLevel = 101325
    flameTemperature = 100 + 273.15 #Kelvin
    planetMass = 5.97219 * (10 ** 24)
    planetRadius = 6378 * 10 ** 3
    maxAltitude = 0.02 * planetRadius
    
    vx = 0
    vy = 0
    ax = 0
    ay = 0
    velocity = 0

    relWindVx = 0
    relWindVy = 0

    vix = 0
    vfx = 0
    vfy = 0
    vfx = 0

    material = "Nylon"
    materialCaption.text = " Material: "
    air = "Air"
    airCaption.text = " Air: "

    for button in buttons:
        if button.i == 2:
            button.checked = True
        else:
            button.checked = False

    molarMass = 28.965 #g/mol
    fluidDens = 1.225 #kg/m^3
    speccAirConst = 287.058

    passengerSlider.value = 2
    sizeOfBalloonSlider.value = 225.25
    tempOfFlameSlider.value = 100
    windSlider.value = 0
    
    numPassengersValueDisplay.text = str(passengerSlider.value)
    balloonSizeValueDisplay.text = str(sizeOfBalloonSlider.value) + "                             "
    tempOfFlameValueDisplay.text = str(tempOfFlameSlider.value)
    windValueDisplay.text = str(windSlider.value)
    
    payloadMass = 2 * 62  
    crossSectArea = 225.25
    wind = 0

    dt = 0.0100000001
    dtSlider.value = 0.0100000001 
    dtCaption.text = "Time Interval (s) = " + str(dt) + " "
    windAngleCaption.text = "Wind Angle (°) = " + str(windAngle) + " "

    materialMenu.selected = "Nylon"
    airMenu.selected = "Air"
    
    radius = sqrt(crossSectArea / pi)
    fluidVol = (4/3)*pi*radius**3
    materialDens = 1150
    balloonMass = materialDens * 4 * crossSectArea * thickness # should NOT change unless crossSectArea is changing

    massOfAir = fluidVol * fluidDens / 1000
    numberOfMoles = massOfAir / molarMass

    sizeOfBalloonMass = fluidVol * fluidDens
    mass = balloonMass + payloadMass + sizeOfBalloonMass

    changeTemp()
    balloonSize()
    
    balloon = createBalloon(sqrt(totalCrossSectionalArea/pi) / 4)

    balloon.pos = vector(0, altitude, 0)
    scene.center = vector(balloon.pos.x, balloon.pos.y + 5.2, 0)
    
    speedCurve.delete()
    altitudeCurve.delete() 
    forceCurve.delete()
    
    speedCurve = gcurve(graph=speedVsTime, color=color.red)
    altitudeCurve = gcurve(graph=altitudeVsTime, color=color.green)
    forceCurve = gcurve(graph=forceVsTime, color=color.blue)

changeTemp()  
balloon = createBalloon(sqrt(totalCrossSectionalArea/pi) / 4)

#attach_arrow(balloon, "velocity", color=color.green, scale=10, shaftwidth=balloon.radius/3)

def changeMaterial(evt):
    global balloonMass, fluidVol, materialDens, mass, thickness, crossSectArea
    if evt.selected == "Nylon":
        balloon.texture = "https://i.imgur.com/YwqXpCA.jpeg"
        materialDens = 1150  # Nylon, kg/m^3
    elif evt.selected == "Polyester":
        balloon.texture = "https://i.imgur.com/aHf7shx.png"
        materialDens = 1380  # Polyester, kg/m^3
    elif evt.selected == "Wicker":
        balloon.texture = "https://i.imgur.com/z1NDKU1.png"
        materialDens = 500   # Wicker (approx), kg/m^3
    elif evt.selected == "Stainless steel": 
        balloon.texture = "https://i.imgur.com/z1NDKU1.png"
        materialDens = 8000  # Stainless steel, kg/m^3
    elif evt.selected == "Copper": 
        balloon.texture = "https://i.imgur.com/FkrZo0R.png"
        materialDens = 8960  # Copper, kg/m^3
    elif evt.selected == "Aluminum":
        balloon.texture = "https://i.imgur.com/zEuDPcK.jpeg"
        materialDens = 2700  # Aluminum, kg/m^3
    elif evt.selected == "Plastic":
        balloon.texture = "https://i.imgur.com/puph7Hw.jpeg"
        materialDens = 1200  # Plastic (average), kg/m^3
    elif evt.selected == "Leather":
        balloon.texture = "https://i.imgur.com/NqIjoHj.jpeg"
        materialDens = 950   # Leather, kg/m^3
    elif evt.selected == "Suede":
        balloon.texture = "https://i.imgur.com/3N4NFBM.jpeg"
        materialDens = 700   # Suede (approx), kg/m^3
    balloonMass = materialDens * 4 * crossSectArea * thickness # should NOT change unless crossSectArea is changing
    mass = balloonMass + payloadMass + sizeOfBalloonMass
        
# backgroundBox = box(pos = vector(0, 0, -1), size = vector(52, 43, 0.1), texture = "https://i.imgur.com/v1IQIPy.png")

time = 0; dt=0.0100000001

scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')

dtSlider = slider(bind = changeDT, min = 0.000000001, max = 0.100000000, value = 0.0100000001, step = 0.000001000)
dtCaption = wtext(text = 'Time Interval (s) = ' + dt + " ")
dtCaptionText = wtext(text = "                                                ")

windAngleSlider = slider(bind = changeWindAngle, min = 0, max = 360, value = 0, step = 1)
windAngleCaption = wtext(text = "Wind Angle (°) = " + windAngle + " ")
scene.append_to_caption('</div>')
scene.append_to_caption('<div style="margin-top:5px;">\n</div>')

scene.append_to_caption('<h3 style="margin-top:5px; text-align:center; ">Graphs Below (Click Run To See Them!)</h3>')

def changeWindAngle():
    global windAngle
    windAngle = windAngleSlider.value
    windAngleCaption.text = "Wind Angle (°) = " + windAngle + " "

def changeDT():
    global dt
    dt = dtSlider.value
    dtCaption.text = "Time Interval (s) = " + dt + " "

posx = balloon.pos.x
posy = balloon.pos.y

vx = 0
vy = 0
ay = 0
ax = 0

balloon.velocity = 0
scene.center = vector(balloon.pos.x, balloon.pos.y + 5.2, 0)

while True:
    global airOfPlanet, molarMassPlanet, speccAirConstPlanet, relWindVx, relWindVy, windAngle, t, maxAltitude, vix, viy, vfy, vfi, dt, ay, ax, result, lanetRadius, planetMass, velocity, airPressure, newFluidVol, fluidVol, heightAboveSeaLvl, flameTemperature, fluidDens, dragForce, dragXForce, dragYForce, gravForce, buoForce, totalXForce, totalYForce, ax, ay, viy, vix, vfy, vfx, posxIncr, posyIncr, finalPosX, finalPosY, altitude, vy, vx, posx, posy, time, mass, balloonMass, payloadMass, sizeOfBalloonMass, crossSectArea, crossSectAreaDueToTemp, totalCrossSectionalArea, wind
    
    rate(1/(dt))
    if running:      
        maxAltitude = 0.02 * planetRadius
        #fun sky changing color
        t = heightAboveSeaLvl / maxAltitude
        scene.background = vector((1 - t) * 0.3, (1 - t) * 0.6, (1 - t) * 1.0)

        hotAirDensity = fluidDens * (airTemperature / (tempOfFlameSlider.value + 273.15))

        newFluidVol = fluidVol * ((tempOfFlameSlider.value + 273.15) / airTemperature)    
        sizeOfBalloonMass = newFluidVol * hotAirDensity
        mass = balloonMass + payloadMass + sizeOfBalloonMass

        #print("BM: " + balloonMass)
        #print("payload: " + payloadMass)
        #print("sizeOFB: " + sizeOfBalloonMass)

        newRadius = pow(((3/4) * newFluidVol / pi),(1/3))
        totalCrossSectionalArea = pi * newRadius ** 2
            
        distanceToCenter = planetRadius + posy
        velocity = sqrt(vx**2 + vy**2)

        newGravity = (gravitationalC * planetMass) / (distanceToCenter ** 2)

        #print("newGrav: " + newGravity)

        airPressureOut = (pressureAtSeaLevel)*(exp((-(molarMassPlanet/1000)*newGravity*heightAboveSeaLvl)/(8.314 * (airTemperature)))) #Pascals
        fluidDensOut = (airPressureOut)/((speccAirConstPlanet)*(airTemperature)) #kg/m^3

        airPressureIn = (pressureAtSeaLevel)*(exp(-(molarMass/1000)*newGravity*heightAboveSeaLvl)/(8.314 * (tempOfFlameSlider.value + 273.15))) #Pascals
        fluidDensIn = (airPressureIn)/((speccAirConst)*(tempOfFlameSlider.value + 273.15)) #kg/m^3

        fluidDensDiff = fluidDensOut - fluidDensIn

        relWindVx = vx - wind * 1000/3600 * cos(radians(windAngle))
        relWindVy = vy - wind * 1000/3600 * sin(radians(windAngle))
            
        if sqrt(relWindVx**2 + relWindVy**2) > 0:
            drag_magnitude = 0.5 * fluidDensOut * sqrt(relWindVx**2 + relWindVy**2)**2 * dragCoeff * totalCrossSectionalArea
            dragXForce = -drag_magnitude * (relWindVx / sqrt(relWindVx**2 + relWindVy**2))
            dragYForce = -drag_magnitude * (relWindVy / sqrt(relWindVx**2 + relWindVy**2))
        else:
            drag_magnitude = 0
            dragXForce = 0
            dragYForce = 0

        if drag_magnitude > 10000000:
            dragResult = confirm(f"WARNING: Drag too high: {drag_magnitude:.2f} N. Set the time interval lower!")
            
        if dragResult:
            reset()
        
        #print("mass: " + mass)

        gravForce = mass * gravitationalC * planetMass / (distanceToCenter ** 2)
        buoForce = (fluidDensDiff) * newGravity * newFluidVol  # archimedes principle
    
        totalXForce = dragXForce
        totalYForce = buoForce - gravForce + dragYForce
        
        totalForceFinal = sqrt(totalXForce*totalXForce + totalYForce*totalYForce)
    
        #print("buo" + buoForce)
        #print("grav" + gravForce)
        #print("drag" + dragYForce)
        #print("densdiff" + fluidDensDiff)
        #print(totalYForce)
        #print(posy)
            
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

        #print("vix: " + vix)
        #print("vfx: " + vfx)
        #print("viy: " + viy)
        #print("vfy: " + vfy)
    
        finalPosX = posx + posxIncr
        finalPosY = posy + posyIncr
    
        balloon.pos = vector(finalPosX, finalPosY, 0)
        
        altitude = finalPosY
        posx = finalPosX
        posy = finalPosY
        
        vy = vfy
        vx = vfx
        
        speedCurve.plot(time, abs(vfy))
        altitudeCurve.plot(time, posy + 16.25)
        forceCurve.plot(time, totalForceFinal)
        
        if posy >= -8:
            scene.center = balloon.pos
        elif posy <= 12 and (posx < -5 or posx > 5):
            scene.center =  vector(balloon.pos.x, balloon.pos.y + 5.2, 0)

        heightAboveSeaLvl = altitude

        if posy < -18:
            #print("HEHEHEHEHEH" + posy)
            result = confirm("Balloon has crashed! Would you like to restart?")
        elif posy > (maxAltitude):
            result = confirm("Balloon has lifted out of this world! Would you like to restart?")

        if result:
            reset()
        
        time += dt
    else:
        hotAirDensity = fluidDens * (airTemperature / (tempOfFlameSlider.value + 273.15))

        newFluidVol = fluidVol * ((tempOfFlameSlider.value + 273.15) / airTemperature)    
        sizeOfBalloonMass = newFluidVol * hotAirDensity
        mass = balloonMass + payloadMass + sizeOfBalloonMass

        newRadius = pow(((3/4) * newFluidVol / pi),(1/3))
        totalCrossSectionalArea = pi * newRadius ** 2
        balloonTop.radius = (sqrt(totalCrossSectionalArea/pi) / 8)

