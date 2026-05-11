a=int(input("Enter upto how many cubes you want:"))
cubes={x:x*x*x for x in range(a+1)}
print("Cubes upto ", a, ":", cubes)