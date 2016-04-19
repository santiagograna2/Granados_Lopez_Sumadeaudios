

class sumas:

    def __init__(self,Audio,Audio2,Audio3):
        self.Audio=Audio
        self.Audio2=Audio2
        self.Audio3=Audio3

    def sumaclass(self):

        a=self.Audio

        print "audio", a
        suma=[]

        for i in range (len(self.Audio)):
            suma.append(self.Audio[i])
        for i in range(len (self.Audio2)):
            suma.append(self.Audio2[i])
        for i in range(len (self.Audio3)):
            suma.append(self.Audio3[i])



        print "suma",suma

        return suma

    def sumarealclass(self):
        sumarealarray=[]
        #AUDIO 1 ES EL MAYOOOOOR MMGVO
        if len(self.Audio2)<len(self.Audio) and len(self.Audio3)<len(self.Audio):

            if len(self.Audio2)<len(self.Audio3):
                for i in range(0,len (self.Audio2)):
                    datation=(self.Audio[i]+self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio2),len(self.Audio3)):
                    datation=(self.Audio[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio3),len(self.Audio)):
                    sumarealarray.append(self.Audio[i])

            if len(self.Audio3)<len(self.Audio2):
                for i in range(0,len (self.Audio3)):
                    datation=(self.Audio[i]+self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio3),len(self.Audio2)):
                    datation=(self.Audio[i]+self.Audio2[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio2),len(self.Audio)):
                    sumarealarray.append(self.Audio[i])

            if len(self.Audio2)==len(self.Audio3):
                for i in range (0,len(self.Audio2)):
                    datation=(self.Audio[i]+self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio2),len(self.Audio)):
                    sumarealarray.append(self.Audio[i])

    #AUDIO 2 ES EL MAYOOOOOR MMGVO

        if len(self.Audio)<len(self.Audio2) and len(self.Audio3)<len(self.Audio2):

            if len(self.Audio)<len(self.Audio3):
                for i in range(0,len (self.Audio)):
                    datation=(self.Audio[i]+self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio),len(self.Audio3)):
                    datation=(self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio3),len(self.Audio2)):
                    sumarealarray.append(self.Audio2[i])

            if len(self.Audio3)<len(self.Audio):
                for i in range(0,len (self.Audio3)):
                    datation=(self.Audio[i]+self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio3),len(self.Audio)):
                    datation=(self.Audio[i]+self.Audio2[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio),len(self.Audio2)):
                    sumarealarray.append(self.Audio2[i])

            if len(self.Audio)==len(self.Audio3):
                for i in range (0,len(self.Audio)):
                    datation=(self.Audio[i]+self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio),len(self.Audio2)):
                    sumarealarray.append(self.Audio2[i])

    #AUDIO 3 ES EL MAYOOOOOR MMGVO

        if len(self.Audio)<len(self.Audio3) and len(self.Audio2)<len(self.Audio3):

            if len(self.Audio)<len(self.Audio2):
                for i in range(0,len (self.Audio)):
                    datation=(self.Audio[i]+self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio),len(self.Audio2)):
                    datation=(self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio2),len(self.Audio3)):
                    sumarealarray.append(self.Audio3[i])

            if len(self.Audio2)<len(self.Audio):
                for i in range(0,len (self.Audio2)):
                    datation=(self.Audio[i]+self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio2),len(self.Audio)):
                    datation=(self.Audio[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio),len(self.Audio3)):
                    sumarealarray.append(self.Audio3[i])

            if len(self.Audio)==len(self.Audio2):
                for i in range (0,len(self.Audio)):
                    datation=(self.Audio[i]+self.Audio2[i]+self.Audio3[i])
                    sumarealarray.append(datation)
                for i in range(len(self.Audio),len(self.Audio3)):
                    sumarealarray.append(self.Audio3[i])

        print "suma real",sumarealarray
        return sumarealarray

    def sumaestereoR(self):
        sumaR=[]
        sumaL=[]


    #AUDIO 1 ES EL MAYOOOOOR MMGVO
        if len(self.Audio3)<len(self.Audio):
            for i in range(0,len(self.Audio3)):
                datation=(self.Audio[i]+self.Audio3[i])
                sumaR.append(datation)
            for i in range(len(self.Audio3),len(self.Audio)):
                sumaR.append(self.Audio[i])

        if len(self.Audio)<len(self.Audio3):
            for i in range(0,len(self.Audio)):
                datation=(self.Audio[i]+self.Audio3[i])
                sumaR.append(datation)
            for i in range(len(self.Audio),len(self.Audio3)):
                sumaR.append(self.Audio3[i])

        if len(self.Audio3)==len(self.Audio):
            for i in range(0,len(self.Audio)):
                datation=(self.Audio[i]+self.Audio3[i])
                sumaR.append(datation)


        return sumaR

    def sumaestereoL(self):
        sumaL=[]
    #SUMA ESTEREO IZQUIERDO
        if len(self.Audio3)<len(self.Audio2):
            for i in range(0,len(self.Audio3)):
                datation=(self.Audio2[i]+self.Audio3[i])
                sumaL.append(datation)
            for i in range(len(self.Audio3),len(self.Audio2)):
                sumaL.append(self.Audio2[i])

        if len(self.Audio2)<len(self.Audio3):
            for i in range(0,len(self.Audio2)):
                datation=(self.Audio2[i]+self.Audio3[i])
                sumaL.append(datation)
            for i in range(len(self.Audio2),len(self.Audio3)):
                sumaL.append(self.Audio3[i])

        if len(self.Audio2)==len(self.Audio3):
            for i in range(0,len(self.Audio2)):
                datation=(self.Audio2[i]+self.Audio3[i])
                sumaL.append(datation)

        return sumaL