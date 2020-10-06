Family={ "Favas":33,"Aydin":3,"Shifna":22 }

print(Family["Favas"])
Family["Favas"] =32
print("My family :",Family)
del Family["Favas"]
print("My family :",Family)
for name in Family:
    print("name",name," ",Family[name])
"Faheem" in Family
Family["Faheem"]=30
print("My family :",Family)
point=(3,4)
print("x axis",point[0])
print("y axis",point[1])