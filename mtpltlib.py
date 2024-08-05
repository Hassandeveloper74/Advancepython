
# matplotlib tutorial guidance from udemy course

import matplotlib.pyplot as plt
import numpy as np
# basic plot

# x=[1,2,3,5]
# y=[3,4,5,6]

# plt.plot(x,y)
# plt.show()


# Customize Plot

# plt.plot(x,y,linestyle='--',color='green',label='My Line')
# plt.xlabel('X-axis label')
# plt.ylabel('Y-axis  label')
# plt.title("Customize Line Pilot")
# plt.legend()
# plt.show()


# ploting with marker

# xpoint=np.array([1,3])
# ypoint=np.array([4,8])

# plt.plot(xpoint,ypoint,"o") o is here marker
# plt.show()


# xpoint=np.array([1,7,9,3])
# ypoint=np.array([4,7,5,8])

# plt.plot(ypoint,marker='o')
# plt.show()

# plt.plot(xpoint,ypoint, marker='o',label='Circle')
# plt.plot(xpoint,ypoint, marker='s',label='Square')
# plt.plot(xpoint,ypoint, marker='^',label='Triangle')
# plt.plot(xpoint,ypoint, marker='*',label='Star')
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('Basic types marker')
# plt.legend()
# plt.show()

# Multipel lines in single plot

# x=[1,2,3,5]
# y=[3,4,5,6]
# y2=[39,40,53,73]

# plt.plot(x,y, label='Line 1')
# plt.plot(x,y2,linestyle='--',color='green',label='Line 2')

# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title("Multiple line in one graph")
# plt.legend()
# plt.show()

# Labels

# x=[1,2,3,5]
# y=[3,4,5,6]
# y2=[39,40,53,73]
# plt.plot(x,y,label='LINE 1')
# plt.plot(x,y2,label="line 2")

# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title("label plot with posiion")
# plt.legend(loc='upper left',fontsize=2,frameon=False)
# plt.show()


# Grid


# x=[1,2,3,5]
# y=[3,4,5,6]


# plt.subplot(1,2,1)
# plt.plot(x,y)
# plt.grid(True)


# plt.subplot(1,2,2)
# plt.plot(x,[i**2 for i in y])
# plt.grid(True)

# plt.plot(x,y)
# plt.grid(color='green',linestyle='--',linewidth=0.5)
# plt.show()

# Scatter

# x=[1,2,3,5]
# y=[3,4,5,6]
# plt.scatter(x,y)
# plt.show()

# Bars      

# Categories=['categories A','categories b','categories c','categories d']
# values=[3,4,5,7]
# plt.bar(Categories,values)
# plt.show()


# Histograms

# data=[3,4,6,8,9,5,7]
# plt.hist(data,bins=5)
# plt.show()

# x=np.random.normal(170,19,250)
# plt.hist(x)
# plt.show()

# pie chart
x=np.array([170,190,250])
mylabel=['aple','bannana','mango']
plt.pie(x,labels=mylabel, startangle=90)
plt.legend()
plt.show()


