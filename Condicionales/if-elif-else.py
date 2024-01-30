room = "bed"
area = 20.0

if room == "kit" : 
    print("looking around in the kitchen")
elif room == "bed":
    print ("looking around in the bedroom")
else:
    print("looking around elsewhere")
    if area > 15:
        print("big place!")
    elif area <20:
        print("no es primo")
    else:
        print("pretty small")

