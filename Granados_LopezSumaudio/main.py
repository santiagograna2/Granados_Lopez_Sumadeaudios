#programa que suma archivos de audio
#disenado por santiago granados e ismael lopez
#programacion de audio aplicada
#universidad de san buenaventura

from Tkinter import *
from openfile import open
from sumas import sumas
import pyaudio
import  wave
import numpy as np
import struct
ventana = Tk()
ventana.title('Suma de audios')
ventana.geometry("408x318")
ventana.configure(bg="black")
imageL=PhotoImage(file="sumaudioimg.gif")
lblImagen=Label(ventana,image=imageL).place(x=1,y=160)

audio_file_name = ''
audio_file_name2 = ''
Audio1=[]
global primero, segundo


def archivo():
    global Audio
    onda= open()
    Audio=onda.open_masker()
    for i in range (len (Audio)):
        primero=np.asarray(Audio[i])
    print "nuevo",Audio
    return Audio
def archivo2():
    global Audio2
    print Audio
    onda= open()
    Audio2=onda.open_masker()
    for i in range (len (Audio2)):
        segundo=np.asarray(Audio2[i])
    print "nuevo 2",Audio2
def archivo3():
    global Audio3
    onda= open()
    Audio3=onda.open_masker()
    for i in range (len (Audio3)):
        tercero=np.asarray(Audio3[i])
    print "nuevo",Audio
    print "nuevo 2",Audio2
    print "nuevo 3",Audio3

def suma():

    sumaresult=sumas(Audio,Audio2,Audio3)
    suma= sumaresult.sumaclass()

    output = wave.open("Nombre.wav", 'w')
    Set_Bits = 16/8
    output.setparams((1, Set_Bits, 44100, 0, 'NONE', 'not compressed'))
    values = []
    for i in range(0, len(suma)):
            packed_value = struct.pack('<h', suma[i])
            values.append(packed_value)
    value_str = ''.join(values)
    output.writeframes(value_str)
    output.close()
    rf = wave.open("Nombre.wav", 'rb')
    prof = rf.getsampwidth()
    channels = rf.getnchannels()
    rate = rf.getframerate()
    audioN = pyaudio.PyAudio()
    streamN = audioN.open(format=audioN.get_format_from_width(prof), channels=channels, rate=rate, output=True)
    datos = rf.readframes(1024)
    while datos != '':
        streamN.write(datos)
        datos = rf.readframes(1024)
    rf.close()
    streamN.stop_stream()
    streamN.close()
    audioN.terminate()




def sumareal():

    print len(Audio)
    print len(Audio2)
    print len(Audio3)
    sumaresult=sumas(Audio,Audio2,Audio3)
    sumarealarray= sumaresult.sumarealclass()
    output = wave.open("Nombresumareal.wav", 'w')
    Set_Bits = 16/8
    output.setparams((1, Set_Bits, 44100, 0, 'NONE', 'not compressed'))

    values = []
    for i in range(0, len(sumarealarray)):

            packed_value = struct.pack('<h', sumarealarray[i])

            values.append(packed_value)
    value_str = ''.join(values)
    output.writeframes(value_str)
    output.close()
    rf = wave.open("Nombresumareal.wav", 'rb')
    prof = rf.getsampwidth()
    channels = rf.getnchannels()
    rate = rf.getframerate()
    audioN = pyaudio.PyAudio()
    streamN = audioN.open(format=audioN.get_format_from_width(prof), channels=channels, rate=rate, output=True)
    datos = rf.readframes(1024)
    while datos != '':
        streamN.write(datos)
        datos = rf.readframes(1024)
    rf.close()
    streamN.stop_stream()
    streamN.close()
    audioN.terminate()




def sumaestereo():

    sumaresult=sumas(Audio,Audio2,Audio3)
    sumaR= sumaresult.sumaestereoR()
    sumaL= sumaresult.sumaestereoL()


#AUDIO 1 ES EL MAYOOOOOR MMGVO
    if len(Audio3)<len(Audio):
        for i in range(0,len(Audio3)):
            datation=(Audio[i]+Audio3[i])
            sumaR.append(datation)
        for i in range(len(Audio3),len(Audio)):
            sumaR.append(Audio[i])

    if len(Audio)<len(Audio3):
        for i in range(0,len(Audio)):
            datation=(Audio[i]+Audio3[i])
            sumaR.append(datation)
        for i in range(len(Audio),len(Audio3)):
            sumaR.append(Audio3[i])

    if len(Audio3)==len(Audio):
        for i in range(0,len(Audio)):
            datation=(Audio[i]+Audio3[i])
            sumaR.append(datation)


#SUMA ESTEREO IZQUIERDO
    if len(Audio3)<len(Audio2):
        for i in range(0,len(Audio3)):
            datation=(Audio2[i]+Audio3[i])
            sumaL.append(datation)
        for i in range(len(Audio3),len(Audio2)):
            sumaL.append(Audio2[i])

    if len(Audio2)<len(Audio3):
        for i in range(0,len(Audio2)):
            datation=(Audio2[i]+Audio3[i])
            sumaL.append(datation)
        for i in range(len(Audio2),len(Audio3)):
            sumaL.append(Audio3[i])

    if len(Audio2)==len(Audio3):
        for i in range(0,len(Audio2)):
            datation=(Audio2[i]+Audio3[i])
            sumaL.append(datation)

    output = wave.open("Sumaestereo.wav", 'w')
    output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

    values = []

    if len(sumaL)<len(sumaR):

        for i in range(0, len(sumaL)):

            L=struct.pack('<h', sumaL[i])
            R=struct.pack('<h', sumaR[i])
            values.append(L)
            values.append(R)

        for i in range(len(sumaL), len(sumaR)):

            L=struct.pack('<h', 0)
            R=struct.pack('<h', sumaR[i])
            values.append(L)
            values.append(R)

    if len(sumaR)<len(sumaL):

        for i in range(0, len(sumaR)):

            L=struct.pack('<h', sumaL[i])
            R=struct.pack('<h', sumaR[i])
            values.append(L)
            values.append(R)

        for i in range(len(sumaR), len(sumaL)):

            L=struct.pack('<h', sumaL[i])
            R=struct.pack('<h', 0)
            values.append(L)
            values.append(R)


    value_str = ''.join(values)
    output.writeframes(value_str)
    output.close()
    rf = wave.open("Sumaestereo.wav", 'rb')
    prof = rf.getsampwidth()
    channels = rf.getnchannels()
    rate = rf.getframerate()
    audioN = pyaudio.PyAudio()
    streamN = audioN.open(format=audioN.get_format_from_width(prof), channels=channels, rate=rate, output=True)
    datos = rf.readframes(1024)

    while datos != '':
        streamN.write(datos)
        datos = rf.readframes(1024)

    rf.close()
    streamN.stop_stream()
    streamN.close()
    audioN.terminate()




b1 = Button(ventana,text="ARCHIVO 1",command = archivo ,font=("Agency FB", 14),width=10).place(x=20,y=20)
b2 = Button(ventana,text="ARCHIVO 2",command = archivo2,font=("Agency FB", 14),width=10).place(x=150,y=20)

b3 = Button(ventana,text="ARCHIVO 3",command = archivo3,font=("Agency FB", 14),width=10).place(x=290,y=20)

b4 = Button(ventana,text="SUMA CONSECUTIVA",command = suma, font=("Agency FB", 14),width=20).place(x=20,y=50)
b5 = Button(ventana,text="SUMA REAL",command =sumareal,font=("Agency FB", 14),width=10).place(x=150,y=80)
b6 = Button(ventana,text="SUMA ESTEREO",command = sumaestereo,font=("Agency FB", 14),width=20).place(x=210,y=50)





ventana.mainloop()


