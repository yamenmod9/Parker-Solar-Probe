#from cProfile import label
from tkinter import *
# from tkinter import ttk
#from PIL import ImageTk, Image


# root window
root = Tk()
root.geometry('1365x800')
root.resizable(False, False)
root.title('Parker Solar Probe')
#img = ImageTk.PhotoImage(Image.open("forest.jpg"))
#bg = photoimage(file="C:\image100.png")
#label0 = Label(root, image='images/image100.png')
pic = PhotoImage(file='ns2.2.png')
label0 = Label(root, image = pic)
label0.place(x=0, y=-25, relwidth=1, relheight=1)

#imageFile = "image100.png"
#label1 = Label(image= imagefile)
#label1.place(x=10, y=20)
# exit button\
def exit_button():
    exit_button= Tk()
open_exit_button = Button(root, text='Exit', command=lambda: root.quit())
open_exit_button.place(x= 0, y=700)

#exit_button.pack(
   # ipadx=5,
   # ipady=5,
    #expand=True
#)
def cooling_system():
    root.destroy()
    cooling_system= Tk()
    cooling_system.geometry('1365x800')
    cooling_system.configure(bg='#18D591')
    label2 = Label (cooling_system, text ='''
    A heated tank that keeps the coolant from freezing 
    during launch, two radiators that will keep
    the coolant from freezing, aluminum fins to maximize
    cooling surface, and pumps to circulate the coolant.'''
    , fg = 'black',font=('tajawal', 36, 'bold'), justify=LEFT, bg="#18D591")
    label2.place(x=0, y=10)
    #root.config(background="blue")
    
    

#open_cooling_system.geometry('500x500+300+300')

open_cooling_system = Button(root, text = 'cooling system',font=('tajawal', 18, 'bold'), command= cooling_system ,width=17,height=1 )
open_cooling_system.place(x= 445, y=41)

def solar_panels():
    root.destroy()
    solar_panels = Tk()
    solar_panels.configure(bg='#FF7B00')

    solar_panels.geometry('1365x800')
    label3 = Label(solar_panels, text = '''
    devices which are used to absorb the sun's rays and
    convert them into electricity or heat. A solar panel is
    actually a collection of solar (or photovoltaic) cells, which
    can be used to generate electricity through photovoltaic effect.
''', fg = 'black',font=('tajawal', 33, 'bold'), justify=LEFT, bg="#FF7B00")
    label3.place(x=0, y=0)
    

open_solar_panels= Button(root, text = 'solar panels', command= solar_panels,font=('tajawal', 18, 'bold'), width=14,height=1)
open_solar_panels.place(x=155, y=183)

def ion_sensor():
    root.destroy()
    ion_sensor = Tk()
    ion_sensor.configure(bg='#C5C8C7')
    ion_sensor.geometry('1365x800')
    label4 = Label(ion_sensor, text='''
        devices which are used to absorb the sun's rays and
        convert them into electricity or heat. A solar panel is
        actually a collection of solar (or photovoltaic) cells, which
        can be used to generate electricity through photovoltaic effect.
    ''', fg='black', font=('tajawal', 31, 'bold'), justify=LEFT, bg="#C5C8C7")
    label4.place(x=0, y=0)


open_ion_sensor= Button(root, text = 'ion sensor', command= ion_sensor,font=('tajawal', 18, 'bold'),width=12,height=1)
open_ion_sensor.place(x=580, y=467)


def Antenna():
    root.destroy()
    Antenna = Tk()
    Antenna.configure(bg='#909292')
    Antenna.geometry('1365x800')
    label5 = Label(Antenna, text = '''
A conductor by which electromagnetic waves are sent
out or received, consisting commonly of a wire or 
set of wires. Many electronic devices like radio,
television, radar, wireless LAN, cell phone, and
GPS need antennas to do their job. Antennas work
 both in air and outer space.
''', fg = 'black' ,font=('tajawal', 36, 'bold'), justify=LEFT, bg="#909292" )
    label5.place(x=0, y=10)

open_Antenna= Button(root, text = 'Antenna', command= Antenna,font=('tajawal', 18, 'bold'),width=11,height=1)
open_Antenna.place(x= 50, y=431)

def mangetometer():
    root.destroy()
    mangetometer= Tk()
    mangetometer.configure(bg='#D9CFCF')
    mangetometer.geometry('1365x800')
    label4 = Label(mangetometer, text = '''
    is a device that measures magnetic field or
    magnetic dipole moment. Spacecraft magnetometers 
    are magnetometers used aboard spacecraft and
    satellites, mostly for scientific investigations,
    plus attitude sensing. Magnetometers are among
    the most widely used scientific instruments
    in exploratory and observation satellites.
''', fg = 'black',font=('tajawal', 36, 'bold'), justify=LEFT, bg="#D9CFCF")
    label4.place(x=0, y=0)

open_mangetometer= Button(root, text = 'mangetometer', command= mangetometer,font=('tajawal', 18, 'bold'),width=16,height=1)
open_mangetometer.place(x=230, y=591)


def thermal_shield_made_of_carbon_composite():
    root.destroy()
    thermal_shield_made_of_carbon_composite = Tk()
    thermal_shield_made_of_carbon_composite.configure(bg='#F87709')
    thermal_shield_made_of_carbon_composite.geometry('1365x800')
    label5 = Label(thermal_shield_made_of_carbon_composite, text = '''
    Layers, of high-density material located within 
    a reactor pressure vessel or between the vessel
    and the biological shield to reduce radiation
    heating in the vessel and the biological shield.''', fg = 'black' ,font=('tajawal', 38, 'bold') , justify=LEFT, bg="#F87709")
    label5.place(x=0, y=10)

open_thermal_shield_made_of_carbon_composite= Button(root, text = 'Thermal Shield', command= thermal_shield_made_of_carbon_composite,font=('tajawal', 20, 'bold'),width=20,height=2 )
open_thermal_shield_made_of_carbon_composite.place(x= 840, y=359)
#open_newwindow = ttk.Button(
#    root,
#    text='open',
#    command=lambda: openNewWindow()

#    open_button.pack(
#    ipadx=5,
#    ipady=5,
#    expand=True
#)
    

    

root.mainloop()