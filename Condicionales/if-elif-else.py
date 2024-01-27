room = "bed"
area = 14.0

if room == "kit" : 
    print("looking around in the kitchen")
elif room == "bed":
    print ("looking around in the bedroom")
else:
    print("looking around elsewhere")
    if area > 15:
        print("big place!")
    else:
        print("pretty small")
