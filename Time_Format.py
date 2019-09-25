Time = input()
if Time[-2:] == "AM" and Time[:2] == "12":
    print("00"+Time[2:-2])
elif Time[-2:] == "AM":
    print(Time[:-2])
elif Time[-2:] == "PM" and Time[:2] == "12":
    print(Time[:-2])
else:
    print(str(int(str(Time[:2]))+12) + str(Time[2:8]))
