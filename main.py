import random
import os, time 
from tkinter import*
"""array_hiraganas=["あ","い","う","え","お" ## aiueo
                "か","き","く","け","こ"  ## Ka
                "さ","し","す","せ","そ", ## Sa
                "た","ち","つ","て","と", ## Ta
                "な","に","ぬ","ね","の", ## Na
                "は","ひ","ふ","へ","ほ", ## Ha
                "ま","み","む","め","も", ## Ma
                "や","ゆ","よ", ## Ya
                "ら","り","る","れ","ろ", ## Ra
                "わ","を","ん", ## wa o n
                "が","ぎ","ぐ","げ","ご", ## Ga
                "ざ","じ","ず","ぜ","ぞ", ## Za
                "だ","ぢ","づ","で","ど", ## Da
                "ば","び","ぶ","べ","ぼ", ## Ba
                "ぱ","ぴ","ぷ","ぺ","ぽ", ## Pa
                "きや","きゅ","きよ", ## kya
                "しや","しゅ","しよ", ## Sha
                "ちや","ちゅ","ちよ", ## Cha
                "にや","にゅ","によ", ## Nya
                "ひや","ひゅ","ひよ", ## Hya
                "みや","みゅ","みよ", ## Mya
                "りや","りゅ","りよ", ## Rya
                "ぎや","ぎゅ","ぎよ", ## Gya
                "じや","じゅ","じよ", ## Ja
                "びや","びゅ","びよ", ## Bya
                "ぴや","ぴゅ","ぴよ", ## Pya
                ]"""
def cambio_de_hiragana(diccionario,label_a_cambiar,texto_caja,caja_texto):
    eliminar(caja_texto)
    label_a_cambiar.config(text=diccionario.hiragana)
    
    print("Antes: "+ diccionario.sonido +"Caja: "+texto_caja)
    if (caracterMostrado.sonido==texto_caja):
        print("Muy Bien")

def eliminar(textobox):
    textobox.delete(0,END)

class Interfaz:
    def __init__(self,diccionario_de_hiraganas):
        self.diccionario_de_hiraganas = diccionario_de_hiraganas
        self.hiragana_a_responder = ""
    
    def setDiccionario(self,diccionario):
        self.diccionario_de_hiraganas = diccionario

    def getDiccionario(self):
        return self.diccionario_de_hiraganas
    
    def randomizarHiragana(self):
        caracter = self.getDiccionario().get(random.randint(0,70))
        return caracter
    
    def get_hiragana_a_responder(self):
        return self.hiragana_a_responder 

    def set_hiragana_a_responder(self,hiragana):
        self.hiragana_a_responder = hiragana

    def verificar(self,label_hiragana):
        #print("verifico")
        nuevo_caracter = self.randomizarHiragana()
        self.set_hiragana_a_responder(nuevo_caracter) 
        label_hiragana.config(text=self.get_hiragana_a_responder().hiragana)

    def interfaz(self):
        self.set_hiragana_a_responder(self.randomizarHiragana())
        ## Caja Principal
        principal = Tk()
        principal.title("Practica de Hiraganas")
        principal.resizable(0,0)
        principal.geometry("320x320")

        ## Interfaz

        frame_Juego=Frame(principal,height=320,width=320)
        frame_Juego.config(bg="white",relief="sunken",bd=20)
        frame_Juego.pack(side="left")

        ## Pantalla del Hiragana
        

        label_hiragana = Label(frame_Juego,text=self.get_hiragana_a_responder().hiragana)
        label_hiragana.config(fg="Blue",justify="center",font=("calibri",50))
        label_hiragana.grid(row=0,column=0,padx=5)


        #Pantalla del TextBox
        texto = Entry(frame_Juego) 
        texto.grid(row=0,column=1)
        
        button = Button(frame_Juego, text="Finalizar", command=lambda: self.verificar(label_hiragana) )
        button.grid(row=1, column=1)



        principal.mainloop()




    


def crear_diccionario():

    x0 =Hiragana("あ",'a')
    x1 =Hiragana("い",'i')
    x2 =Hiragana("う",'u')
    x3 =Hiragana("え",'e')
    x4 =Hiragana("お",'o')

    x5 =Hiragana("か",'ka')
    x6 =Hiragana("き",'ki')
    x7 =Hiragana("く",'ku')
    x8 =Hiragana("け",'ke')
    x9 =Hiragana("こ",'ko')

    x10 =Hiragana("さ",'sa')
    x11 =Hiragana("し",'shi')
    x12 =Hiragana("す",'su')
    x13 =Hiragana("せ",'se')
    x14 =Hiragana("そ",'so')

    x15 =Hiragana("た",'ta')
    x16 =Hiragana("ち",'chi')
    x17 =Hiragana("つ",'tsu')
    x18 =Hiragana("て",'te')
    x19 =Hiragana("と",'to')

    x20 =Hiragana("な",'na')
    x21 =Hiragana("に",'ni')
    x22 =Hiragana("ぬ",'nu')
    x23 =Hiragana("ね",'ne')
    x24	=Hiragana("の",'no')

    x25 =Hiragana("は",'ha')
    x26 =Hiragana("ひ",'hi')
    x27 =Hiragana("ふ",'fu')
    x28 =Hiragana("へ",'he')
    x29 =Hiragana("ほ",'ho')

    x30 =Hiragana("ま",'ma')
    x31 =Hiragana("み",'mi')
    x32 =Hiragana("む",'mu')
    x33 =Hiragana("め",'me')
    x34 =Hiragana("も",'mo')

    x35	=Hiragana("や",'ya')
    x36 =Hiragana("ゆ",'yu')
    x37 =Hiragana("よ",'yo')

    x38 =Hiragana("ら",'ra')
    x39 =Hiragana("り",'ri')
    x40 =Hiragana("り",'ru')
    x41 =Hiragana("れ",'re')
    x42 =Hiragana("ろ",'ro')

    x43 =Hiragana("わ",'wa')
    x44 =Hiragana("を",'o')
    x45	=Hiragana("ん",'n')

    x46 =Hiragana("が",'ga')
    x47 =Hiragana("ぎ",'gi')
    x48 =Hiragana("ぐ",'gu')
    x49 =Hiragana("げ",'ge')
    x50 =Hiragana("ご",'go')

    x51	=Hiragana("ざ",'za')
    x52 =Hiragana("じ",'ji')
    x53 =Hiragana("ず",'zu')
    x54	=Hiragana("ぜ",'ze')
    x55	=Hiragana("ぞ",'zo')

    x56	=Hiragana("だ",'da')
    x57 =Hiragana("ぢ",'ji')
    x58	=Hiragana("づ",'zu')
    x59	=Hiragana("で",'de')
    x60	=Hiragana("ど",'do')

    x61	=Hiragana("ば",'ba')
    x62	=Hiragana("び",'bi')
    x63	=Hiragana("ぶ",'bu')
    x64	=Hiragana("べ",'be')
    x65	=Hiragana("ぼ",'bo')

    x66	=Hiragana("ぱ",'pa')
    x67	=Hiragana("ぴ",'pi')
    x68	=Hiragana("ぷ",'pu')
    x69	=Hiragana("ぺ",'pe')
    x70	=Hiragana("ぽ",'po')

    diccionario = {0:x0,1:x1,2:x2,3:x3,4:x4,5:x5,6:x6,7:x7,8:x8,9:x9,10:x10,11:x11,12:x12,13:x13,14:x14,15:x15,16:x16
                    ,17:x17,18:x18,19:x19,20:x20,21:x21,22:x22,23:x23,24:x24,25:x25,26:x26,27:x27,28:x28,29:x29,30:x30,31:x31,32:x32,33:x33,34:x34
                    ,35:x35,36:x36,37:x37,38:x38,39:x39,40:x40,41:x41,42:x42,43:x43,44:x44,45:x45,46:x46,47:x47,48:x48,49:x49,50:x50,51:x51,52:x52
                    ,53:x53,54:x54,55:x55,56:x56,57:x57,58:x58,59:x59,6:x60,61:x61,62:x62,63:x63,64:x64,65:x65,66:x66,67:x67,68:x68,69:x69,70:x70}
    #print(diccionario.get(random.randint(0,4)).hiragana)
    return diccionario

class Hiragana:
    def __init__(self,hiragana,sonido):
        self.hiragana = hiragana
        self.sonido = sonido

def elegir_hiragana():
    enPartida = True
    while(enPartida):
        diccionario = crear_diccionario()
        seleccionado = diccionario.get(random.randint(0,70))
        hiragana = seleccionado.hiragana
        fonetica = seleccionado.sonido


        print(hiragana)    
        
        respuesta = str(ingreso()).lower()
        enPartida = fonetica == respuesta
        if (enPartida):
            print("correcto")
        else:  
            print("Incorrecto, es:"+ fonetica)
        time.sleep(2)    
        os.system("cls")
        



def ingreso():
    respuesta = input("")
    return respuesta

if __name__ == "__main__":
    #elegir_hiragana()
    main = Interfaz(crear_diccionario())
    #print(main.diccionario_de_hiraganas)
    main.interfaz()
