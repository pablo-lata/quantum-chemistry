# This code is written in Python 2.7. It generates ternary plot for range of stoichiometries for three-element compounds.
# It automatically removes repeating stoichiometries (i.e. (2,2,2) is the same as (1,1,1))
# Please enter range of coefficients (for >100 it can work a bit slow, I use it in my research up to 5).
# I turned off 3D plot, sorry for the mess

import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#from matplotlib import cm
#from matplotlib.ticker import LinearLocator, FormatStrFormatter
#import numpy as np
def st_gen(n1min,n1max,n2min,n2max,n3min,n3max):
#generates the combinations of stoichiometric coordinates
    set_tabl=set()
    for i in range(n1min,n1max+1):
        for j in range(n2min,n2max+1):
            for k in range(n3min,n3max+1):
                x=(i,j,k)

                f=float(i)
                g=float(j)
                h=float(k)

                for l in range(2,max(i,j,k)+1):
                    if f % l == 0 and g % l == 0 and h % l == 0:
                        break
                else:
                    if x not in set_tabl:
                        set_tabl.add(x)
    if (0,0,0) in set_tabl:
        set_tabl.remove((0,0,0))
    tabl = []
    for j in set_tabl:
        tabl.append(list(j))
    tabl_sort = sorted(tabl)

    return tabl_sort
#-----------------------------------------------
#
#
#-----------------------------------------------

#x1 = input("Amin: ")
x2 = input("Amax: ")
#y1 = input("Bmin: ")
y2 = input("Bmax: ")
#z1 = input("Cmin: ")
z2 = input("Cmax: ")

ddd = st_gen(0,x2,0,y2,0,z2)

coordx=[]
coordy=[]
coordz=[]
 
for elem in ddd:
    
    a=float(elem[0])
    b=float(elem[1])
    c=float(elem[2])

    if (a+b+c) == 0:
        print "dzielenie przez 0"
    else:

        y=float(c/(a+b+c)*(3**(0.5))/2)
        x=float(b/(a+b+c)+y/(3**0.5))
        z=float(a+b+c)**2
#        print "For stoichiometry %s%d%s%d%s%d coordinates: x = %f y = %f" % (at1,a,at2,b,at3,c,x,y)
        coordx.append(x)
        coordy.append(y)
        coordz.append(z)
#print coordx
#print coordy
#print coordz
coordx_len=0
coordy_len=0
coordz_len=0
for i in range(0,len(ddd)):
    if len(str(coordx[i])) > coordx_len:
        coordx_len=len(str(coordx[i]))
#    else:
#        print "n",
    if len(str(coordy[i])) > coordy_len:
        coordy_len=len(str(coordy[i]))
#    else:
#        print "n",
    if len(str(coordz[i])) > coordz_len:
        coordz_len=len(str(coordz[i]))
#    else:
#        print "n",



plt.plot([0,0.5],[0,3**0.5/2],'k-',[0,1],[0,0],'k-',[0.5,1],[3**0.5/2,0],'k-',linewidth=1.5)
plt.plot(coordx,coordy,'mo',ms=5.0)
plt.plot([0.1,0.55],[0,0.9*3**0.5/2],'k--',[0.2,0.60],[0,0.8*3**0.5/2],'k--',[0.3,0.65],[0,0.7*3**0.5/2],'k--',[0.4,0.7],[0,0.6*3**0.5/2],'k--',[0.5,0.75],[0,0.5*3**0.5/2],'k--',[0.6,0.8],[0,0.4*3**0.5/2],'k--',[0.7,0.85],[0,0.3*3**0.5/2],'k--',[0.8,0.90],[0,0.2*3**0.5/2],'k--',[0.9,0.95],[0,0.1*3**0.5/2],'k--',linewidth=0.5)
plt.plot([0.1,0.05],[0,0.1*3**0.5/2],'k--',[0.2,0.10],[0,0.2*3**0.5/2],'k--',[0.3,0.15],[0,0.3*3**0.5/2],'k--',[0.4,0.2],[0,0.4*3**0.5/2],'k--',[0.5,0.25],[0,0.5*3**0.5/2],'k--',[0.6,0.3],[0,0.6*3**0.5/2],'k--',[0.7,0.35],[0,0.7*3**0.5/2],'k--',[0.8,0.40],[0,0.8*3**0.5/2],'k--',[0.9,0.45],[0,0.9*3**0.5/2],'k--',linewidth=0.5)
plt.plot([0.05,0.95],[0.1*3**0.5/2,0.1*3**0.5/2],'k--',[0.1,0.9],[0.2*3**0.5/2,0.2*3**0.5/2],'k--',[0.15,0.85],[0.3*3**0.5/2,0.3*3**0.5/2],'k--',[0.2,0.8],[0.4*3**0.5/2,0.4*3**0.5/2],'k--',[0.25,0.75],[0.5*3**0.5/2,0.5*3**0.5/2],'k--',[0.3,0.7],[0.6*3**0.5/2,0.6*3**0.5/2],'k--',[0.35,0.65],[0.7*3**0.5/2,0.7*3**0.5/2],'k--',[0.4,0.6],[0.8*3**0.5/2,0.8*3**0.5/2],'k--',[0.45,0.55],[0.9*3**0.5/2,0.9*3**0.5/2],'k--',linewidth=0.5)
#plt.ylabel('some numbers')
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()
#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#coordx,coordy=np.meshgrid(coordx,coordy)
#ax.scatter(coordx,coordy,coordz)
#ax.set_zlim(-1.01,250)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#fig.colorbar(surf,shrink=0.5,aspect=5)
#plt.show()
#target = open('danespisane', 'w')
#target.write("Na   C    O      x                   y                  (a + b + c)^2\n")
#for i in range(0,len(ddd)):
#    c = ddd[i]
#    target.write("%s    %s    %s     " % (c[0],c[1],c[2]))
#    target.write("%s" % (coordx[i]) + "0" * (coordx_len - len(str(coordx[i]))) + "    ")
#    target.write("%s" % (coordy[i]) + "0" * (coordy_len - len(str(coordy[i]))) + "    ")
#    target.write("   %s" % (coordz[i]) + "0" * (coordz_len - len(str(coordz[i]))) )
#    target.write('\n')
#    
#target.close()
#plt.show()
#
#for i in range(0,len(ddd)):
#    c = ddd[i]
#    print repr(c[0]).rjust(1), repr(c[1]).rjust(3), repr(c[2]).rjust(3),
#    print repr(coordx[i]).rjust(20), repr(coordy[i]).rjust(20), repr(coordz[i]).rjust(20)
#
#pr1=[2,2,1]
#pr2=[3,4,5]
#
#y1=float(float(pr1[2])/float((pr1[0]+pr1[1]+pr1[2]))*(3**(0.5))/2)
#x1=float(float(pr1[1])/float((pr1[0]+pr1[1]+pr1[2]))+y1/(3**0.5))
#y2=float(float(pr2[2])/float((pr2[0]+pr2[1]+pr2[2]))*(3**(0.5))/2)
#x2=float(float(pr2[1])/(pr2[0]+pr2[1]+pr2[2])+y2/(3**0.5))
#ax=float((y2-y1)/(x2-x1))
#bx=float((y2*x1-y1*x2)/(x1-x2))
#
#for elem in ddd:
#
#
#    a=float(elem[0])
#    b=float(elem[1])
#    c=float(elem[2])
#
#    if (a+b+c) == 0:
#        print "dzielenie przez 0"
#    else:
#
#        y=float(c/(a+b+c)*(3**(0.5))/2)
#        x=float(b/(a+b+c)+y/(3**0.5))
#        z=float(a+b+c)**2
#        print "For stoichiometry %s%d%s%d%s%d coordinates: x = %f y = %f" % (at1,a,at2,b,at3,c,x,y)
#        coordx.append(x)
#        coordy.append(y)
#        coordz.append(z)
#        if (float(y) - (float(ax) * float(x) + float(bx))) < 0.0001 and (float(y) - ((float(ax) * float(x) + float(bx)))) > -0.0001:
#            print "%s, %s, %s" % (elem[0],elem[1],elem[2])
#
#    if (a - pr2[0]) / (pr2[0] - pr1[0]) == (b - pr2[1]) / (pr2[1] - pr1[1]) == ((c - pr2[2]) / (pr2[2] - pr1[2])):
#        print elem
#    else:
#        print "",
#
#x1,y1,z1 = 1,2,3
#x2,y2,z2 = 1,1,1
#for x in range(0,n+1):
#        for y in range(0,n+1):
#            for z in range(0,n+1):
#
#                if (x2 - x1) == 0:
#                    if x == x2:
#                        dx = 'zero'
#                    else:
#                        dx = 'error'
#                else:
#                    dx = (x - x1) / (x2 - x1)
#
#                if (y2 - y1) == 0:
#                    if y == y2:
#                        dy = 'zero'
#                    else:
#                        dy = 'error'
#                else:
#                    dy = (y - y1) / (y2 - y1)
#                if (z2 - z1) == 0:
#                    if z == z2:
#                        dz = 'zero'
#                    else:
#                        dz = 'error'
#                else:
#                    dz = (z - z1) / (z2 - z1)
#
#                if dx == dy == dz:
#                    print "%d %d %d" % (x,y,z)
