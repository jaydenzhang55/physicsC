Web VPython 3.2

scene = canvas(width=600, height=600)
scene.userzoom = False
scene.userspin = False
scene.userpan = False

fluidDens = 1.225
airTemperature = 37
velocity = 0
dragCoeff = 0.5
crossSectArea = 2800
mass = 3000
gravity = 9.80665
fluidVol = 2800
altitude = 0
heightAboveSeaLvl = 0
material = 'nylon'
air = 'air'
wind = 0

homePlanet = "Earth"

# variables: fluid density, velocity, drag coefficient, cross sectional area, mass, gravity, fluid volume, altitude

dragForce = 0.5 * (fluidDens) * velocity * velocity * dragCoeff * crossSectArea
gravForce = mass * gravity
buoForce = - (fluidDens) * gravity * fluidVol

def setMass(event):
    if event.id is 'x':
        mass = event.value

def setfluidDens():
    fluidDens = 45

def numPassengers(s):
    mass = s.value
    passengerSlider.text = 'Number of Passengers =' + '{:1.0f}'.format(passengerSlider.value) + "\n\n"

def setPlanet(p):
    if p.checked:
        homePlanet = p.plan
        setDefaults(planet)
    else:
        setDefaults(Earth)
    for i in range(len(buttons)):
        if i != p.i:
            buttons[i].checked = False

def setDafaults(x):
    if x == "Earth":
        backgroundPic = 45
    elif x == "Saturn":
        backgroundPic = 45

def changeMaterial(evt):
    material = evt.id

def changeAir(evt):
    air = evt.id

venusRadio = radio(bind=setPlanet, text = "Venus", i = 0, plan = "Venus")
marsRadio = radio(bind=setPlanet, text = "Mars", i = 1, plan = "Mars")
earthRadio = radio(bind=setPlanet, text = "Earth", i = 2, plan = "Earth")
saturnRadio = radio(bind=setPlanet, text = "Saturn", i = 3, plan = "Saturn")
jupiterRadio = radio(bind=setPlanet, text = "Jupiter", i = 4, plan = "Jupiter")
neptuneRadio = radio(bind=setPlanet, text = "Neptune", i = 5, plan = "Neptune")
uranusRadio = radio(bind=setPlanet, text = "Uranus", i = 5, plan = "Uranus")

buttons = [saturnRadio, earthRadio, venusRadio, jupiterRadio, neptuneRadio, uranusRadio, marsRadio] 

passengerSlider = slider(bind = numPassengers, min = 0, max = 10, value = 0)
passengerSliderCaption = wtext(text = 'Number of Passengers =' + ' {:1.0f}'.format(passengerSlider.value)+"\n\n")

def balloonSize(s):
    crossSectArea = s.value
    sizeOfBalloonSlider.text = 'Cross Sectional Area of Balloon (m^2) =' + ' {:1.0f}'.format(sizeOfBalloonSlider.value) + "\n\n"

sizeOfBalloonSlider = slider(bind = balloonSize, min = 150, max = 1000, value = 222)
sizeOfBalloonSliderCaption = wtext(text = 'Cross Sectional Area of Balloon (m^2) =' + ' {:1.0f}'.format(sizeOfBalloonSlider.value)+"\n\n")

def changeTemp(s):
    airTemperature += s.value
    tempOfFlameSlider.text = 'Temperature of Flame (°C) =' + '{:1.2f}'.format(tempOfFlameSlider.value)+"\n\n"
    
tempOfFlameSlider = slider(bind = changeTemp, min = 0, max = 700, value = 350)
tempOfFlameSliderCaption = wtext(text = 'Temperature of Flame (°C) =' + ' {:1.2f}'.format(tempOfFlameSlider.value)+"\n\n")

def changeWind(s):
    wind = s.value
    windSlider.text = 'Wind Speed (km/h) =' + '{:1.2f}'.format(windSlider.value)+"\n\n"

windSlider = slider(bind = changeWind, min = 0, max = 1000, value = 0)
windSliderCaption = wtext(text = 'Wind Speed (km/h) =' + ' {:1.2f}'.format(windSlider.value)+"\n\n")

choicelist = ['nylon', 'polyester',
             'wicker', 'stainless steel', 'copper', 'aluminum', 
             'plastic', 'leather', 'suede']

menu(choices=choicelist, bind=changeMaterial)

airList = ['air', 'hydrogen', 'nitrogen', 'helium', 'oxygen', 'tungsten hexafluoride']

menu(choices=airList, bind=changeAir)

speedVsTime = graph(title = 'Speed vs Time', xtitle = 'Time (s)', ytitle = 'Speed (m/s)', xmin = 0, ymin = 0 )
positionVsTime = graph(title = 'Position vs Time', xtitle = 'Time (s)', ytitle = 'Position', xmin = 0, ymin = 0)
forceVsTime = graph(title = 'Force vs Time', xtitle = 'Time (s)', ytitle = 'Force', xmin = 0, ymin = 0)


