import os
import unidecode
from pydub import AudioSegment
from playsound import playsound
from pydub.playback import play

#Registro de silabas existentes en el registro de grabaciones
silabs_2 = []
silabs_3 = []
silabs_4 = []
words = []
letters_f = "./sound/letters/"
letters_sound_f = "./sound/single_letter/"
silabs_2_f = "./sound/silaba_2l/"
silabs_3_f = "./sound/silaba_3l/"
silabs_4_f = "./sound/silaba_4l/"
words_f = "./sound/words/"
chars_f = "./sound/chars/"
special_terms = ["con"]

#Información para el proceso de separacion en silabas
g_consonanticos = ["bl","br","cl","cr","dr","fl","fr","gl","gr","pl","pr","tl","tr","ch","rr"]
diptongos = ["iu", "ui", "ia", "ie", "io", "ua", "ue", "uo", "ai", "au", "ei", "eu", "oi", "ou"]
vocals = ["a","e","i","o","u"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]
perm_chars = [",", ".", ":"]
#Funcion para dividir palabras en sus respectivas silabas
def parse_word(word):
    silabas = [""]
    count = 0
    postv = ""
    vf = False
    for ch in word:
        if(ch in vocals):
            if vf:
                if len(postv) > 1 and len(postv) < 4:
                    if postv[-2]+postv[-1] in g_consonanticos:
                        silabas[count] += postv[:-2]
                        count+=1
                        silabas.append("")
                        silabas[count] +=  postv[-2:] + ch
                    else:
                        silabas[count] += postv[:len(postv)-int(len(postv)/2)]
                        count += 1
                        silabas.append("")
                        silabas[count] += postv[int(len(postv)/2):] + ch
                elif len(postv) == 1:
                    count += 1
                    silabas.append("")
                    silabas[count] += postv + ch
                elif len(postv) == 0:
                    if(silabas[count][-1]+ch in diptongos):
                        silabas[count] += ch
                    else:
                        silabas.append("")
                        count+=1
                        silabas[count] += ch
                else:
                    silabas[count] += postv[:len(postv)-len(postv)/2]
                    count += 1
                    silabas.append("")
                    silabas[count] += postv[len(postv)/2:] + ch
                postv = ""
            else:
                vf = True
                silabas[count] += ch
        elif ch in letters:
            if vf:
                postv+=ch
            else:
                silabas[count] += ch
    silabas[count] += postv
    return silabas

def fix_paragraph(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.replace("?","")
    paragraph = paragraph.replace("ñ","?")
    paragraph = unidecode.unidecode(paragraph)
    paragraph = paragraph.replace("?","ñ")
    paragraph = paragraph.replace(","," , ")
    paragraph = paragraph.replace("."," . ")
    paragraph =  paragraph.replace(" :)"," cara sonriente")
    paragraph =  paragraph.replace(":"," : ")
    paragraph = paragraph.replace("?","")
    paragraph = paragraph.replace("¿","")
    paragraph = paragraph.replace("¡","")
    paragraph = paragraph.replace("!","")
    return paragraph

def list_files():
    listOfFile = os.listdir(silabs_2_f)
    for file in listOfFile:
        silabs_2.append(file[:-4])
    listOfFile = os.listdir(silabs_3_f)
    for file in listOfFile:
        silabs_3.append(file[:-4])
    listOfFile = os.listdir(silabs_4_f)
    for file in listOfFile:
        silabs_4.append(file[:-4])
    listOfFile = os.listdir(words_f)
    for file in listOfFile:
        words.append(file[:-4])

def tts(text):
    last_w_char = True
    text = fix_paragraph(text)
    parts = text.split(" ")
    sound = AudioSegment.empty()
    espacio = AudioSegment.from_file(chars_f+"espacio.wav", format="wav")
    for part in parts:
        print(part)
        if len(part) == 0:
            stri = "do nothing"
        elif part[0] in perm_chars and not last_w_char:
            if part[0] == '.':
                sound+=AudioSegment.from_file(chars_f+"punto.wav", format="wav")
            elif part[0] == ',':
                sound+=AudioSegment.from_file(chars_f+"coma.wav", format="wav")
            elif part[0] == ':':
                sound+=AudioSegment.from_file(chars_f+"coma.wav", format="wav")
            last_w_char = True
        else:
            if(not last_w_char):
                sound+=espacio
            if(part in words):
                print("The words is in the storage")
                if(part in special_terms):
                    part += "_"
                sound+=AudioSegment.from_file(words_f+part+".wav", format="wav")
            else:
                silabas = parse_word(part)
                for silaba in silabas:
                    while len(silaba)>0:
                        done = False
                        if len(silaba) >= 4:
                            for sl in silabs_4:
                                if sl == silaba[:4] or sl == silaba[:4]+"_":
                                    sound+=AudioSegment.from_file(silabs_4_f+sl+".wav", format="wav")
                                    silaba = silaba[4:]
                                    done = True
                        if not done and len(silaba) >= 3:
                            for sl in silabs_3:
                                if sl == silaba[:3] or sl == silaba[:3]+"_":
                                    sound+=AudioSegment.from_file(silabs_3_f+sl+".wav", format="wav")
                                    silaba = silaba[3:]
                                    done = True
                        if not done and len(silaba) >= 2:
                            for sl in silabs_2:
                                if sl == silaba[:2] or sl == silaba[:2]+"_":
                                    sound+=AudioSegment.from_file(silabs_2_f+sl+".wav", format="wav")
                                    silaba = silaba[2:]
                                    done = True
                        if not done:
                            sound+=AudioSegment.from_file(letters_sound_f+silaba[0]+".wav", format="wav")
                            silaba = silaba[1:]
                        print(silaba)
    file_handle = sound.export("./sound/out/output.wav", format="wav")
    play(sound)

list_files()
tts(input())
