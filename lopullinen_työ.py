# -*- coding: cp1252 -*-
import turtle

#taustan v�ri
#aliohjelm muuntaa suomenkieliset v�rit englnanniksi
def taustan_vari(vari):
    if vari == "musta":
        vari = "black"
    elif vari == "punainen":
        vari = "red"
    elif vari == "sininen":
        vari = "blue"
    elif vari == "vihre�":
        vari = "green"
    elif vari == "valkoinen":
        vari = "white"
    else:
        print ("Virheellinen v�ri!")
    return vari

#tekstin v�ri
#aliohjelm muuntaa suomenkieliset v�rit englnanniksi
def tekstin_vari(tekstivari):
    if tekstivari == "musta":
        tekstivari = "black"
    elif tekstivari == "punainen":
        tekstivari = "red"
    elif tekstivari == "sininen":
        tekstivari = "blue"
    elif tekstivari == "vihre�":
        tekstivari = "green"
    elif tekstivari == "valkoinen":
        tekstivari = "white"
    else:
        print ("Virheellinen v�ri!")
    return tekstivari

#Ikkunan piirt�minen
def ikkuna_ja_teksti(vari, kyna_vari, teksti, koko):

    #m��ritet��n ikkunan komennot muutujaan
    #ja m��ritet��n ikkunan arvot
    ikkuna = turtle.Screen()
    ikkuna.title("Ikkuna")
    ikkuna.bgcolor(vari)
    ikkuna.setup(width=800, height=600)
    ikkuna.tracer(0)

    #m��ritet��n kilpikonnan komennot muutujaan
    #ja m��ritet��n kyn�n arvot
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color(kyna_vari)
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write(teksti, align="center", font=("Comic Sans MS", koko, "normal"))

#aliojelma joka tallentaa annetut tiedot tiedostoon
#omille riveilleen
def tallennus(tausta_vari, kyna_vari, teksti, koko):
    tiedosto = open("jutut.txt", "w")
    tiedosto.write(tausta_vari + "\n")
    tiedosto.write(kyna_vari + "\n")
    tiedosto.write(teksti + "\n")
    tiedosto.write(koko + "\n")

    tiedosto.close

#avaus ja luku
#aliojelma joka lukke tiedoston ja paluttaa sen listan
def aku():
    tiedosto = open("jutut.txt", "r")
    data = tiedosto.read()
    tiedosto.close
    lista = data.split("\n")
    return lista

#palauttaa listasta taustan v�rin
def tausta(lista):
    tausta = lista[0]
    return tausta

#palauttaa listasta kyn�n v�rin
def kyna(lista):
    kyna = lista[1]
    return kyna

#palauttaa listasta tulostettavan tekstin
def teksti(lista):
    teksti = lista[2]
    return teksti

#palauttaa listasta tekstiin koon
def koko(lista):
    koko = lista[3]
    return koko


###########
#p��ohjelma
###########

#m��ritet���n jatkuuko erisuureksi kuin E
jatkuuko = "e"

#jatkuu kunnes ohjelma lopetetaan
while jatkuuko != "E":

    #kokeilee onnsituuko t�m�n suoritus
    try:
        #kysyy mit� halutaan tehd�
        mita = input("Haluatko avata viimeisen tekstin vai kirjoittaa uuden? (v/u): ")

        #jos vastaus v, haetaan tiedot tiedostosta
        #ja tulostetaan se ikkunaan
        if mita == "v":
            ikkuna_ja_teksti(tausta(aku()), kyna(aku()), teksti(aku()), koko(aku()))

        #jos vastaus u, tallannetaan tiedot tiedostoon
        #ja tulostetaan tiedot ikkunaan
        elif mita == "u":

            #kysyt��n mit� kitjoitetaan ja mill� koolla
            teksti = input("Mit� haluat kirjoittaa?: ")
            tekstikoko = input("Kuinka suuren tekstin haluat? (luku 0-100): ")
            tekstikoko = int(tekstikoko)

            #jos tekstin koko ei ole 1-100 palataan alkuun
            if tekstikoko < 0 or tekstikoko > 100:
                print ("Virheellinen luku")
                continue

            #jos tekstin koko on on 1-100
            elif tekstikoko > 0 or tekstikoko < 100:
                tekstikoko = str(tekstikoko)

                #kysyt��n tekstin ja taustan v�ri
                taustavari = input("Anna taustan v�ri (musta/punainen/sininen/vihre�/valkoinen): ")
                tekstivari = input("Valitse tekstin v�ri (musta/punainen/sininen/vihre�/valkoinen): ")

            #tallennetan tiedot tiedostoon
            ikkuna_ja_teksti(taustan_vari(taustavari), tekstin_vari(tekstivari), teksti, tekstikoko)

            #tulostetaan tiedot ikkunaan
            tallennus(taustan_vari(taustavari), tekstin_vari(tekstivari), teksti, tekstikoko)

        #jos vastaus ei ole u tai v palataan alkuun
        else:
            print ("Virheellinen sy�te!")
            continue

    #jos try lohkossa tapahtuu virhe suoritetaan t�m�
    except:
        print ("Jokin meni vikaan kokeile k�ynist�� ohjelma uudestaan!!")

    #kysyt��n halutaanko ohjelma lopettaa
    jatkuuko = input("Paina E + Enter lopettaaksesi ohjelma: ")
