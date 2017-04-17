#This program computes vector operations in R^3. Need to work on rounding. May be helpful for STEM first year undergrads.
import math

dot=lambda u,v: (u[0]*v[0]+u[1]*v[1]+u[2]*v[2])

sub=lambda u,v: ((u[0]-v[0],u[1]-v[1],u[2]-v[2]))

def proj(u,v):
    k=(dot(v,u))/(dot(u,u))
    return(k*u[0],k*u[1],k*u[2])
        
def norm(u):
    k=1/(math.sqrt(u[0]**2+u[1]**2+u[2]**2))
    return (k*u[0],k*u[1],k*u[2])

while True:
    print("Options")
    print("Enter 'add' to add two vectors")
    print("Enter 'subtract' to subtract two vectors")
    print("Enter 'dot' to compute dot product of two vectors")
    print("Enter 'cross' to compute cross product of two vectors")
    print("Enter 'normalize' to normalize a vector (compute unit vector in its direction)")
    print("Enter 'Gram-Schmidt' to orthonormalize three linearly independent vectors")
    print("Enter 'quit' to leave")
    
    user_input=input(": ")

    if user_input=="quit":
        break
    elif user_input=="Gram-Schmidt":
        print("Enter the components of the three linearly-independent vectors you want to orthonormalize")
        v1=(float(input("First component of first vector ")), float(input("Second component of first vector ")), float(input("Third component of first vector ")))
        v2=(float(input("First component of second vector ")), float(input("Second component of second vector ")), float(input("Third component of second vector ")))
        v3=(float(input("First component of third vector ")), float(input("Second component of third vector ")), float(input("Third component of third vector ")))
        print("Here is the orthonormal basis: "+str(norm(v1))+str(norm(sub(v2,proj(v1,v2))))+str(norm(sub(sub(v3,proj(v1,v3)),proj(sub(v2,proj(v1,v2)),v3)))))
        
                                    
    elif user_input=="normalize":
        x = float(input("Enter the x component of the vector: "))
        y = float(input("Enter the y component of the vector: "))
        z = float(input("Enter the z component of the vector: "))
        u=1/(math.sqrt(x**2+y**2+z**2))
        print("The normalized vector is "+str([x/u, y/u, z/u])+".")
    else:
        num1 = float(input("Enter the x component of first vector: "))
        num2 = float(input("Enter the y component of first vector: "))
        num3 = float(input("Enter the z component of first vector: "))
     
        num4 = float(input("Enter the x component of second vector: "))
        num5 = float(input("Enter the y component of second vector: "))
        num6 = float(input("Enter the z component of second vector: "))
        
    if user_input=="add":
        print("The vector sum is "+str(([num1+num4, num2+num5, num3+num6]))+".")
    elif user_input=="subtract":
        print("The difference is "+str(([num1-num4, num2-num5, num3-num6]))+".")
    elif user_input=="dot":
        print("The scalar product is "+(str(num1*num4+num2*num5+num3*num6))+".")
    elif user_input=="cross":
        print("The vector product is "+(str([(num2*num6)-(num3*num5), (num3*num4)-(num1*num6), (num1*num5)-(num2*num4)]))+".")
    
        
        
