Web VPython 3.2

scene = canvas(width=600, height=600)

scene.container = "left"
scene.append_to_caption('<h3 style="margin-top:20px;">Balloon Parameters</h3>')

scene.userzoom = False
scene.userspin = False
scene.userpan = False


fluidDens = 1.225
airTemperature = 37
velocity = 0
dragCoeff = 0.5
crossSectArea = 2800 #A=pi*r^2 through center of sphere
airPressure = 101325
mass = 3000
gravity = 9.80665
fluidVol = 2800
altitude = 0
heightAboveSeaLvl = 0
material = 'Nylon'
air = 'Air'
wind = 0
homePlanet = "Earth"



# variables: fluid density, velocity, drag coefficient, cross sectional area, mass, gravity, fluid volume, altitude



def setMass(event):
    if event.id is 'x':
        mass = event.value

def setfluidDens():
    fluidDens = 45

def setPlanet(p):
    if p.checked:
        homePlanet = p.plan
        setDefaults(planet)
    else:
        setDefaults(Earth)
    for i in range(len(buttons)):
        if i != p.i:
            buttons[i].checked = False

def setDefaults(x):
    if x == "Earth":
        backgroundPic = 45
    elif x == "Saturn":
        backgroundPic = 45
        fluidDens = 00
        airTemperature = 00
        dragCoeff = 0.515 #based on Atlas rocket https://web.archive.org/web/20170313142729/http://www.braeunig.us/apollo/saturnV.htm
        planetMass = 5.684*10^26
        fluidVol = 00
        air = 'air'
    elif x == "Venus":
        backgroundPic = 45
        fluidDens = 00
        airTemperature = 00
        dragCoeff = 0.515
        planetMass = 5.684*10^26
        fluidVol = 00
        air = 'air'
    elif x == "Mars":
        backgroundPic = 45
        fluidDens = 00
        airTemperature = 00
        dragCoeff = 0.515
        planetMass = 5.684*10^26
        fluidVol = 00
        air = 'air'
    elif x == "Jupiter":
        backgroundPic = 45
        fluidDens = 00
        airTemperature = 00
        dragCoeff = 0.515
        planetMass = 5.684*10^26
        fluidVol = 00
        air = 'air'
    elif x == "Neptune":
        backgroundPic = 45
        fluidDens = 00
        airTemperature = 00
        dragCoeff = 0.515
        planetMass = 5.684*10^26
        fluidVol = 00
        air = 'air'
    elif x == "Uranus":
        backgroundPic = 45
        fluidDens = 00
        airTemperature = 00
        dragCoeff = 0.515
        planetMass = 5.684*10^26
        fluidVol = 00
        air = 'air'
        



def changeAir(evt):
    air = evt.id

    
speedVsTime = graph(title = 'Speed vs Time', xtitle = 'Time (s)', ytitle = 'Speed (m/s)', xmin = 0, ymin = 0, align="right", width="250", height="2")
positionVsTime = graph(title = 'Position vs Time', xtitle = 'Time (s)', ytitle = 'Position', xmin = 0, ymin = 0, align="right", width="250", height="2")
forceVsTime = graph(title = 'Force vs Time', xtitle = 'Time (s)', ytitle = 'Force', xmin = 0, ymin = 0, align="right", width="250", height="2")

speedCurve = gcurve(graph=speedVsTime, color=color.red)
positionCurve = gcurve(graph=positionVsTime, color=color.green)
forceCurve = gcurve(graph=forceVsTime, color=color.blue)

time_points = [0, 1, 2, 3, 4, 5]
speed_values = [0, 5, 10, 15, 20, 25]
position_values = [0, 10, 25, 45, 70, 100]
force_values = [300, 500, 400, 450, 430, 420]

for i in range(len(time_points)):
    rate(5)
    speedCurve.plot(time_points[i], speed_values[i])
    positionCurve.plot(time_points[i], position_values[i])
    forceCurve.plot(time_points[i], force_values[i])

venusRadio = radio(bind=setPlanet, text = "Venus", i = 0, plan = "Venus")
marsRadio = radio(bind=setPlanet, text = "Mars", i = 1, plan = "Mars")
earthRadio = radio(bind=setPlanet, text = "Earth", i = 2, plan = "Earth")
saturnRadio = radio(bind=setPlanet, text = "Saturn", i = 3, plan = "Saturn")
jupiterRadio = radio(bind=setPlanet, text = "Jupiter", i = 4, plan = "Jupiter")
neptuneRadio = radio(bind=setPlanet, text = "Neptune", i = 5, plan = "Neptune")
uranusRadio = radio(bind=setPlanet, text = "Uranus", i = 5, plan = "Uranus")

buttons = [saturnRadio, earthRadio, venusRadio, jupiterRadio, neptuneRadio, uranusRadio, marsRadio] 

scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')


passengerSlider = slider(min = 0, max = 10, value = 0, bind = numPassengers, step = 1)
scene.append_to_caption('</div>')

def numPassengers(s):
    mass = s.value
    numPassengersValueDisplay.text = str(passengerSlider.value)
numPassengersTextDisplay = wtext(text = 'Number of Passengers = ')
numPassengersValueDisplay = wtext(text = str(passengerSlider.value))

scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')
sizeOfBalloonSlider = slider(bind = balloonSize, min = 150, max = 1000, value = 222)
scene.append_to_caption('</div>')

def balloonSize(s):
    crossSectArea = s.value
    balloonSizeValueDisplay.text = str(sizeOfBalloonSlider.value)
balloonSizeTextDisplay = wtext(text = 'Cross Sectional Area of Balloon (m^2) = ')
balloonSizeValueDisplay = wtext(text = str(sizeOfBalloonSlider.value))
    
scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')
tempOfFlameSlider = slider(bind = changeTemp, min = 0, max = 700, value = 350)
scene.append_to_caption('</div>')

def changeTemp(s):
    airTemperature = s.value
    tempOfFlameValueDisplay.text = str(tempOfFlameSlider.value)
tempOfFlameTextDisplay = wtext(text = 'Temperature of Flame (°C) = ')
tempOfFlameValueDisplay = wtext(text = str(tempOfFlameSlider.value))

scene.append_to_caption('<div id="right">')
scene.append_to_caption('<div style="margin-bottom: 15px;">')

windSlider = slider(bind = changeWind, min = 0, max = 1000, value = 0)
scene.append_to_caption('</div>')

def changeWind(s):
    wind = s.value
    windValueDisplay.text = str(windSlider.value)
windTextDisplay = wtext(text = 'Wind Speed (km/h) = ')
windValueDisplay = wtext(text = str(windSlider.value))
scene.append_to_caption('<div></div>')

materialList = ['Nylon', 'Polyester',
             'Wicker', 'Stainless steel', 'Copper', 'Aluminum', 
             'Plastic', 'Leather', 'Suede']
balloon = sphere(pos = vec(0, altitude, 0), opacity=1, radius = sqrt(crossSectArea/pi), color = color.blue, texture="https://i.imgur.com/YwqXpCA.jpeg")

def changeMaterial(evt):
    if evt.index < 1:
        balloon.texture = "https://i.imgur.com/YwqXpCA.jpeg"
    elif evt.index is 1:
        balloon.color = color.yellow
        balloon.texture = "https://i.imgur.com/aHf7shx.png"
    elif evt.index is 2:
        balloon.color = color.red
        balloon.texture = "https://i.imgur.com/z1NDKU1.png"
    elif evt.index is 3: 
        balloon.color = color.green
        balloon.texture = "https://i.imgur.com/z1NDKU1.png"
    elif evt.index is 4: 
        #balloon.color = color.black
        balloon.texture="https://i.imgur.com/FkrZo0R.png"
    elif evt.index is 5:
        balloon.texture="https://i.imgur.com/zEuDPcK.jpeg"
    elif evt.index is 6:
        balloon.texture="https://i.imgur.com/puph7Hw.jpeg"
    elif evt.index is 7:
        balloon.texture="https://i.imgur.com/NqIjoHj.jpeg"
    elif evt.index is 8:
        balloon.texture="https://i.imgur.com/3N4NFBM.jpeg"


menu(choices = materialList, bind = changeMaterial)
materialCaption = wtext(text = ' Material: ' + material + ' ')
scene.append_to_caption('<div></div>')


    


airList = ['Air', 'Hydrogen', 'Nitrogen', 'Helium', 'Oxygen', 'Tungsten hexafluoride']

menu(choices=airList, bind=changeAir)
airCaption = wtext(text = ' Air: ' + air + " ")

totalMass = mass + passengerSlider.value
dragForce = 0.5 * (fluidDens) * velocity * velocity * dragCoeff * crossSectArea * (velocity/abs(velocity))
gravForce = totalMass * gravity
buoForce = (fluidDens) * gravity * fluidVol    
totalForce = buoForce - gravForce + dragForce

acceleration = totalForce/totalMass

running = False

def start(b):
    if b.text == "Run":
        b.text = "Pause"
        global running = True
    else: 
        b.text == "Run"
        global running = False

startButton = button(text = "Run", pos = scene.title_anchor, bind = start)

time = 0; dt=3600

while(running):
    rate(1000)
    velocity = velocity + (acceleration * time)
    
