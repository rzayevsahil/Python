# -*- coding: utf-8 -*-


lights = ["red", "yellow", "green"]

currentLight = lights[2]

print(currentLight)


if currentLight == "red":
    print("STOP!")
elif currentLight == "yellow":
    print("READY!")
else:
    print("GO!")
