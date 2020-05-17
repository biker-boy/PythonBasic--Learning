#!/usr/bin/env python
# coding: utf-8

# In[2]:


def hello():
   print("hello world")


# In[3]:


hello()


# In[5]:


def add_10(x):
    return x+10


# In[6]:


add_10(3)


# In[7]:


add_10(7)


# In[13]:


def odd_even(x):
    if x%2==0:
        print (x," is even ")
    else:
        print (x, " is odd ")


# In[15]:


odd_even(7)


# In[18]:


g=lambda x:x*x*x


# 

# In[ ]:





# In[19]:


g(10)


# In[20]:


g(13)


# In[21]:


#lambda with fliter 


# In[26]:


l1 = [12,34,5,65,66,78,44,22,46]
final_list=list(filter(lambda x:(x%2==0),l1))


# In[27]:


final_list


# 

# In[28]:


#lambda with maps


# In[ ]:





# In[30]:


l1 = [1,2,3,4,5,6,7,8,9]
Final_list_new=list(map( lambda x:x*2 , l1))


# In[31]:


Final_list_new


# In[32]:


from functools import reduce


# In[34]:


sum = reduce( lambda x,y: x+y, l1)


# In[36]:


sum


# In[51]:


class phone:
    def make_call(self):
        print ("Making phone call")
                  
    def Play_game(self):
        print ("Playing Game")


# In[52]:


p1 = phone()


# In[53]:


p1.make_call()


# In[54]:


p1.Play_game()


# In[149]:


class Phone:
    def set_colour(self,colour):
        self.colour=colour
    def set_cost(self,cost):
        self.cost=cost
    def show_colour(self):
        return self.colour
    def show_cost(self):
        return self.cost


# In[150]:


p2 = Phone()


# In[152]:


p2.set_colour("blue")


# In[153]:


p2.set_cost(5000)


# In[154]:


p2.show_cost()


# In[156]:


p2.show_colour()


# In[125]:


class Tele1:
    def set_color(self , color):
        self.color=color
    def set_cost(self , cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
 


# In[111]:


p3 = Tele1()


# In[113]:


p3.set_color("red")


# In[114]:


p3.set_cost(6000)


# In[131]:


p3.show_color()


# In[132]:


p3.show_cost()


# In[ ]:


#Somewhat trick it is that (phone)
#Define new variable(colour/Cost) define multiple value (self , colour ) 
#then from multple value define (set_colour) & (self.colour)


# In[157]:


class Employee:
    def __init__ (self,name , age,salary,gender):
        
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        
    def show_employee_details(self):
        print ("Name of employee is" ,self.name)
        print ("Age of employee is", self.age)
        print ("salary of employee is" , self.salary)
        print ("Gender of employee is" , self.gender)
        


# In[159]:


e1 = Employee ("ram",45,56785,"Male")


# In[163]:


e1.show_employee_details()


# In[164]:


#inheritance of python


# In[170]:


class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost= cost
    
    def show_vehicles_details(self):
        print ("mileage of my vehicle is", self.mileage)
        print ("cost of my vehicle is" , self.cost)
        print ("i am vehicle")


# In[172]:


v1 = Vehicle(23,500)


# In[173]:


v1.show_vehicles_details()


# In[174]:


class Car(Vehicle):
    def show_car_details(self):
        print ("i am car")


# In[175]:


c1 = Car(40,6000)


# In[176]:


c1.show_vehicles_details()


# In[177]:


c1.show_car_details()


# In[178]:


#over-riding init method 


# In[201]:


class Cars(Vehicle):
    def __init__ (self, mileage,cost,typre,hp):
        super().__init__(mileage,cost)
        self.typre =typre
        self.hp = hp
        
    def show_Cars_details(self):
            print ("typre of my car is",self.typre)
            print ("hp of my car is", self.hp)
            print ("i am car")


# In[206]:


c2 = Cars(23,4566,"Apolo",85)


# In[207]:


c2.show_vehicles_details()


# In[208]:


c2.show_Cars_details()


# In[209]:


#multiple inheritance 


# In[216]:


class Parent1:
    def assign_string_one(self,str1):
        self.str1= str1
    def show_string_one(self):
            return self.str1 


# In[219]:


class Parent2:
    def assign_string_two(self, str2):
        self.str2 = str2
    def show_string_two(self):
        return self.str2


# In[221]:


class Child (Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3 = str3
    def show_string_three(self):
        return self.str3


# In[225]:


my_chid = Child()


# In[226]:


my_chid.assign_string_one("i am string of Parent1")


# In[227]:


my_chid.assign_string_two("i am string of Parent 2")


# In[228]:


my_chid.assign_string_three("i am string of child")


# In[229]:


my_chid.show_string_three()


# In[231]:


my_chid.show_string_one()


# In[232]:


my_chid.show_string_two()


# In[233]:


#Multiple inheritance  (parent - child - grand child)


# In[254]:


class Porent:
    def get_name(self,name):
        self.name = name
    def show_name(self):
        return self.name 


# In[ ]:





# In[255]:


class Mulga(Porent):
    def get_age (self , age):
        self.age = age
    def show_age (self):
        return self.age


# In[263]:


class Baap(Mulga):
    def get_gender (self, gender):
        self.gender =gender
    def show_gender(self):
        return self.gender


# In[264]:


g1 = Baap()


# In[267]:


g1.get_name("Jignesh")


# In[269]:


g1.get_age(67)


# In[270]:


g1.get_gender("Male")


# In[272]:


g1.show_name()


# In[274]:


g1.show_age()


# In[275]:


g1.show_gender()


# In[277]:


#libraries in Pythonv - tools 
#(numpy ( numberial Computing  ), panda ( Data Manuplation ), matplotlib ( VIsualization - graphical representation ) )


# In[278]:


#numpy (numberical Python)


# In[279]:


import numpy as np


# In[282]:


j1 = [1,2,3,4]


# In[283]:


n1=np.array(j1)


# In[284]:


type(n1)


# In[287]:


n2=np.array([[1,2,3,4],[4,3,2,1]])


# In[288]:


type(n2)


# In[289]:


n2


# In[290]:


n1


# In[291]:


#intializing of Numpy


# In[292]:


n3 = np.zeros((2,3)) #intialzing with zero


# In[293]:


n3


# In[294]:


type(n3)


# In[296]:


n4= np.zeros((10,10))


# In[297]:


n4


# In[298]:


n5=np.full((3,3),5) #Full used for Intiailize with specfic number 


# In[299]:


n5


# In[304]:


n6=np.arange(50,101) #arange is used for ranging from number to last number 


# In[305]:


n6


# In[306]:


n7=np.arange(50,1011,5) #arrange can also be used for array seperated from particular number 


# In[307]:


n7


# In[308]:


n8 = np.random.randint(100,200,10) 
#random.randint is used for random numbr from provide limits ; everytime it keep changing 


# In[309]:


n8


# In[311]:


n9 = np.random.randint(100,200,10)


# In[312]:


n9


# In[313]:


#numpy Shape #using syntax shape ; you are able change shape of matrix or numpay matrix 


# In[314]:


n10= np.array([[1,2,3,4],[4,3,2,1]])


# In[315]:


n10


# In[316]:


n10.shape = (4,2)


# In[317]:


n10


# In[319]:


n10.shape = (8,1)


# In[320]:


n10


# In[321]:


#joining numpy arrays 

#Vertical Stack using Syntax vstack()
#horizontal stack using hstack()
#column stack using column_stack()


# In[324]:


n11=np.array([10,20,30])


# In[325]:


n12=np.array([20,40,60])


# In[326]:


np.vstack([n11,n12]) #vstack 


# In[328]:


np.hstack([n11,n12])


# In[329]:


np.hstack([n12,n11]) #hstack


# In[332]:


np.column_stack((n11,n12)) #np.column_stack


# In[333]:


#numpy Intersection and difference 

#intersect1d is used for finding common number in between matrix 
#setdiff1d is used for finding different number in matrix comparing 1st to 2nd or Vice versa.


# In[334]:


n13=np.array ((10,20,30 ,40,50,60,75,85,90))


# In[336]:


n14=np.array((50,70,80,90,100))


# In[337]:


np.intersect1d(n13,n14) #used Syntax for intersect1d


# In[339]:


np.setdiff1d(n13,n14) #used syntax for setdiff1d


# In[340]:


np.setdiff1d(n14,n13)


# In[341]:


#numpy Array mathematics 


# In[ ]:


#addition of array syntax : np.sum([n10,n20]) ; np.sum([n10,n30] , axis =0) ; np.sum([n10,n30] , axis =1)


# In[342]:


n15 = np.array ([10,20])


# In[343]:


n16 = np.array ([30,60])


# In[344]:


np.sum([n15,n16])


# In[345]:


np.sum([n15,n16], axis =0) #addition vertical column


# In[347]:


np.sum([n15,n16], axis =1) #addtion of horizontal column


# In[348]:


n17= np.array([10,20,30])


# In[349]:


n17


# In[350]:


n17=n17+6 #addition of specific number to Array 


# In[351]:


n17


# In[352]:


n17=n17-8 #subtraction of specfic number from array 


# In[353]:


n17


# In[354]:


n17=n17*100 #multplying array from specfic number 


# In[355]:


n17


# In[356]:


n17=n17/120 #divinding  array from specfic number 


# In[357]:


n17


# In[358]:


#Mean ,Median ,Standard Deviation 


# In[359]:


n18= np.array([13,56,78])


# In[360]:


np.median(n18) #median 


# In[362]:


np.std(n18) #Standard Deviation 


# In[363]:


np.mean(n18) #mean


# In[367]:


n19=np.random.randint(10,88 ,7)  #random Integer from 10 to 88


# In[368]:


n19


# In[369]:


np.mean(n19)


# In[370]:


np.median(n19)


# In[371]:


np.std(n19)


# In[ ]:


#numpy Saving and loading .


# In[372]:


n20=np.random.randint(233,788,19)


# In[373]:


n20


# In[374]:


np.save('myarray', n20)


# In[375]:


n21=np.load("myarray.npy")


# In[376]:


n21


# In[1]:


import pandas as pd   #pandas being 


# In[3]:


s1=pd.Series([1,2,3,4,5])


# In[8]:


s1


# In[4]:


type(s1)


# In[6]:


s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])


# In[9]:


s2


# In[14]:


s3=pd.Series({"k1":10, 'k2':20,'k3':30})  #dictonary


# In[15]:


s3


# In[19]:


import pandas as pd


# In[33]:


s4=pd.Series({'k1':10,'k2':20,'k3':30},index=['k3','k1','k4','k2'])


# In[34]:


s4


# In[35]:


l16=[1,2,3,4,5,6,7,8,9]


# In[37]:


s5=pd.Series(l16)


# In[38]:


s5


# In[39]:


s5[4]


# In[40]:


s5[:4]


# In[41]:


s5[-4:]


# In[42]:


s5


# In[43]:


s5+10


# In[44]:


s5-16 #subtraction 


# In[45]:


s5*12 #multiplication 


# In[47]:


s5/2 #division


# In[49]:


s6= pd.Series([10,20,30,40,50,60,70,80,90])


# In[50]:


s5+s6


# In[51]:


#multiple dimensional row - coloumn 


# In[53]:


pd.DataFrame({'Name':['Annee' , 'Jay' , 'Harry'], 'Mark': [ 34 ,56,78]})


# In[54]:


#dataframe in-built function


# In[56]:


iris = pd.read_csv ('iris.csv')


# In[57]:


iris.head()


# In[58]:


iris.tail()


# In[60]:


iris.shape


# In[61]:


iris.describe()


# In[62]:


iris.head()


# In[63]:


iris.iloc[5:11,2:]


# In[70]:


iris.loc[1:10,("PetalLengthCm","Species")]


# In[71]:


#dropping column 


# In[72]:


iris.head()


# In[74]:


iris.drop('Species' , axis=1)


# In[75]:


iris.head()


# In[76]:


i1=iris.drop([5,6,7],0)


# In[78]:


i1.head(11)


# In[79]:


iris.mean()


# In[80]:


iris.median()


# In[81]:


iris.min()


# In[83]:


iris.max()


# In[85]:


#apply method 


# In[86]:


iris.head()


# In[99]:


def double_max(s):
    return s*2


# In[100]:


iris[["SepalWidthCm","PetalWidthCm"]].apply(double_max)


# In[101]:


iris['Species'].value_counts()


# In[102]:


iris.sort_values(by='SepalWidthCm')


# In[103]:


iris.sort_values(by='PetalLengthCm')


# In[104]:


#data visualisation Matplotlib 


# In[105]:


import numpy as np


# In[106]:


from matplotlib import pyplot as plt


# In[107]:


x = np.arange(1,11)


# In[108]:


x


# In[111]:


y =3*x


# In[112]:


y


# In[117]:


plt.plot(x,y)
plt.show()


# In[126]:


plt.plot(x,y,color='g',linestyle=':' , linewidth = 4)
plt.title("X vs Y")
plt.xlabel('This is X axis')
plt.ylabel('This is Y axis')
plt.show()


# In[127]:


import numpy as np


# In[146]:


from matplotlib import pyplot as plt


# In[147]:


x=np.arange(11,27)


# In[148]:


y2= 3*x


# In[149]:


y1= 4*x


# In[150]:


x


# In[151]:


y1


# In[152]:


y2


# In[153]:


plt.plot(x,y1)
plt.plot(x,y2)
plt.show()


# In[165]:


plt.plot(x,y1,color='g' ,linestyle=':', linewidth=2)
plt.plot(x,y2,color='r', linewidth=3)
plt.title('Neil Nitin Mukesh')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.show()


# In[174]:


plt.subplot(2,1,1)
plt.plot(x,y1,color='g' ,linestyle=':', linewidth=2)

plt.subplot(2,1,2)
plt.plot(x,y2,color='r', linewidth=3)
plt.title('Neil Nitin Mukesh')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.show()


# In[175]:


plt.plot(x,y2,color='r', linewidth=3)
plt.title('Neil Nitin Mukesh')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.show()


# In[176]:


#barplot 


# In[183]:


import numpy as np


# In[185]:


Cricketer = {"sachin":99 , "Ganguly":63 , "Sehwag":46}


# In[186]:


names = list(Cricketer.keys())
values = list(Cricketer.values())


# In[187]:


names 


# In[188]:


values


# In[194]:


plt.bar(names,values)
plt.title("Score")
plt.xlabel('names of cricketer')
plt.ylabel('run')
plt.show()


# In[ ]:


#horizontal graph barh


# In[197]:


plt.barh(names,values, color='r')
plt.title("Score")
plt.xlabel('names of cricketer')
plt.ylabel('run')
plt.show()


# In[198]:


#scatter plot 


# In[199]:


import numpy as np


# In[4]:


from matplotlib import pyplot as plt


# In[5]:


x = [45,67,32,56,11,55,56,23,88,11]
y = [79,23,72,93,77,45,49,11,33,00]


# In[6]:


plt.scatter(x,y,marker="*",c='g', s=100)
plt.show()


# In[7]:


x = [45,67,32,56,11,55,56,23,88,11]
y = [79,23,72,93,77,45,49,11,33,00]
z = [34,44,55,66,88,77,99,22,20,99]


# In[8]:


plt.scatter(x,y, marker='*', c='g', s=50)
plt.scatter(x,z, marker ='.', c='r', s=60)
plt.show()


# In[9]:


import numpy as np


# In[14]:


from matplotlib import pyplot as plt


# In[18]:


plt.subplot(1,2,1)
plt.scatter(x,y, marker='*', c='g', s=50)

plt.subplot(1,2,2)
plt.scatter(x,z, marker ='.', c='r', s=60)
plt.show()


# In[28]:





# In[19]:


data = [ 3,4,5,6,2,3,4,8,3,1,8,3,2,3]


# In[31]:


plt.hist(data , color = 'r' , bins = 10)
plt.show()


# In[34]:


import pandas as pd


# In[35]:


iris = pd.read_csv("iris.csv")


# In[36]:


iris.head()


# In[38]:


plt.hist(iris['PetalLengthCm'], color = 'r')
plt.show()


# In[39]:


one = [ 22,33,44,55,66,77,88,99,11]


# In[41]:


two = [ 22,51,30,93,81,29,19,19,86]


# In[42]:


three = [37,95,33,59,22,62,78,19,22]


# In[44]:


data = list([one,two,three])


# In[45]:


plt.boxplot(data)
plt.show()


# In[46]:


four = [ 1,4,5,7,8,2,4]
five = [ 3,7,8,9,3,2,1]
six = [ 2,4,5,7,2,3,4]


# In[47]:


ficker = list ([four,five , six])


# In[50]:


plt.boxplot(ficker)
plt.show()


# In[51]:


plt.violinplot(ficker)
plt.show()


# In[52]:


plt.violinplot(data)
plt.show()


# In[53]:


#piechart


# In[55]:


fruit = [ 'apple' , 'manago' , 'pineapple' , 'orange' , 'strawberry']
quantity = [ 12,18,6,24,36]


# In[56]:


plt.pie(quantity, labels = fruit)
plt.show()


# In[57]:


plt.pie(quantity, labels = fruit , autopct='%0.1f%%')  #percentage
plt.show()


# In[58]:


plt.pie(quantity, labels = fruit , autopct='%0.1f%%' , colors = ('blue','orange' , 'yellow' , 'pink' , 'green' ) )  #colour
plt.show()


# In[65]:


plt.pie(quantity, labels=fruit ,radius=2)
plt.pie([100],colors = 'w',radius=1)
plt.show()


# In[2]:


import pandas as pd


# In[3]:


iris = pd.read_csv ('iris.csv')


# In[4]:


iris.iloc[3:0,2:0]


# In[5]:


iris.iloc[0:3,0:2]


# In[6]:


iris.iloc[0:6,0:4]


# In[7]:


s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])


# In[8]:


s1


# In[11]:


import numpy as np


# In[13]:


n1=[45,60]
n2=[55,40]


# In[18]:


np.sum([n1,n2],axis=1)


# In[16]:


np.vstack((n1,n2))


# In[17]:


np.sum([n1,n2],axis=0)


# In[19]:


import numpy as np


# In[25]:


np.array([1,2,3,4],[6,7,8,9])
n1.shape


# In[24]:





# In[ ]:




