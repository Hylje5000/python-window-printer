# -*- coding: cp1252 -*-
import turtle

#taustan väri
#aliohjelm muuntaa suomenkieliset värit englnanniksi
def taustan_vari(vari):
    if vari == "musta":
        vari = "black"
    elif vari == "punainen":
        vari = "red"
    elif vari == "sininen":
        vari = "blue"
    elif vari == "vihreä":
        vari = "green"
    elif vari == "valkoinen":
        vari = "white"
    else:
        print ("Virheellinen väri!")
    return vari

#tekstin väri
#aliohjelm muuntaa suomenkieliset värit englnanniksi
def tekstin_vari(tekstivari):
    if tekstivari == "musta":
        tekstivari = "black"
    elif tekstivari == "punainen":
        tekstivari = "red"
    elif tekstivari == "sininen":
        tekstivari = "blue"
    elif tekstivari == "vihreä":
        tekstivari = "green"
    elif tekstivari == "valkoinen":
        tekstivari = "white"
    else:
        print ("Virheellinen väri!")
    return tekstivari

#Ikkunan piirtäminen
def ikkuna_ja_teksti(vari, kyna_vari, teksti, koko):

    #määritetään ikkunan komennot muutujaan
    #ja määritetään ikkunan arvot
    ikkuna = turtle.Screen()
    ikkuna.title("Ikkuna")
    ikkuna.bgcolor(vari)
    ikkuna.setup(width=800, height=600)
    ikkuna.tracer(0)

    #määritetään kilpikonnan komennot muutujaan
    #ja määritetään kynän arvot
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

#palauttaa listasta taustan värin
def tausta(lista):
    tausta = lista[0]
    return tausta

#palauttaa listasta kynän värin
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
#pääohjelma
###########

#määritetäään jatkuuko erisuureksi kuin E
jatkuuko = "e"

#jatkuu kunnes ohjelma lopetetaan
while jatkuuko != "E":

    #kokeilee onnsituuko tämän suoritus
    try:
        #kysyy mitä halutaan tehdä
        mita = input("Haluatko avata viimeisen tekstin vai kirjoittaa uuden? (v/u): ")

        #jos vastaus v, haetaan tiedot tiedostosta
        #ja tulostetaan se ikkunaan
        if mita == "v":
            ikkuna_ja_teksti(tausta(aku()), kyna(aku()), teksti(aku()), koko(aku()))

        #jos vastaus u, tallannetaan tiedot tiedostoon
        #ja tulostetaan tiedot ikkunaan
        elif mita == "u":

            #kysytään mitä kitjoitetaan ja millä koolla
            teksti = input("Mitä haluat kirjoittaa?: ")
            tekstikoko = input("Kuinka suuren tekstin haluat? (luku 0-100): ")
            tekstikoko = int(tekstikoko)

            #jos tekstin koko ei ole 1-100 palataan alkuun
            if tekstikoko < 0 or tekstikoko > 100:
                print ("Virheellinen luku")
                continue

            #jos tekstin koko on on 1-100
            elif tekstikoko > 0 or tekstikoko < 100:
                tekstikoko = str(tekstikoko)

                #kysytään tekstin ja taustan väri
                taustavari = input("Anna taustan väri (musta/punainen/sininen/vihreä/valkoinen): ")
                tekstivari = input("Valitse tekstin väri (musta/punainen/sininen/vihreä/valkoinen): ")

            #tallennetan tiedot tiedostoon
            ikkuna_ja_teksti(taustan_vari(taustavari), tekstin_vari(tekstivari), teksti, tekstikoko)

            #tulostetaan tiedot ikkunaan
            tallennus(taustan_vari(taustavari), tekstin_vari(tekstivari), teksti, tekstikoko)

        #jos vastaus ei ole u tai v palataan alkuun
        else:
            print ("Virheellinen syöte!")
            continue

    #jos try lohkossa tapahtuu virhe suoritetaan tämä
    except:
        print ("Jokin meni vikaan kokeile käynistää ohjelma uudestaan!!")

    #kysytään halutaanko ohjelma lopettaa
    jatkuuko = input("Paina E + Enter lopettaaksesi ohjelma: ")
