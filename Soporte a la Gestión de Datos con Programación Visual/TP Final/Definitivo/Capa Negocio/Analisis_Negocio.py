import vamp
import librosa
import numpy as np
import matplotlib.pyplot as plt
import math as m
from librosa import display as d
import melosynth as mel
import wave
import pyaudio
import os

def Generar_Melodia(nombre):
    """Abre el archivo WAV (de la carpeta del proyecto) y genera el archivo WAV de la melodía"""
    path = "./" + nombre + ".wav"
    audio, sr = librosa.load(path, sr=44100, mono = True)

    params = {"minfqr": 25.0, "maxfqr": 2000.0, "voicing": 0.2, "minpeaksalience": 0.0}
    data = vamp.collect(audio, sr, "mtg-melodia:melodia", parameters = params)
    hop, melody = data['vector']
    timestamps = 8 * 128/44100.0 + np.arange(len(melody)) * (128/44100.0)

    nombreMel = nombre + ".txt"
    archivo = open(nombreMel, "w")
    for i in range(len(timestamps)):
        time = str(timestamps[i])
        if not m.isnan(melody[i]):
            archivo.write(time)
            archivo.write('\t')
            archivo.write(str(melody[i]))
            archivo.write('\n')

        else:
            archivo.write(str(timestamps[i]))
            archivo.write('\t')
            archivo.write(str(-220))
            archivo.write('\n')
    archivo.close()
    mel.melosynth(nombreMel, outputfile=None ,fs= 44100, nHarmonics= 1, square= False, useneg=False)


def Guardar_Analisis(nombre):
    """Guarda los datos del analisis en la base de datos"""
    wfOrig = wave.open(nombre+".wav", 'rb')
    dataOrig = wfOrig.readframes(1024)
    wfMel = wave.open(nombre+"_melosynth.wav")
    dataMel = wfMel.readframes(1024)
    #Guardar Archivo en BD

def Crea_Chromagrama(nombre):
    """Crea la png del Chromagrama"""
    path = "./" + nombre + "_melosynth.wav"
    audio, sr = librosa.load(path , sr = 44100 , mono = True)

    chroma = librosa.feature.chroma_cqt(y = audio, sr = sr)

    plt.figure(figsize=(10, 4))
    d.specshow(chroma, y_axis='chroma', x_axis='time')
    plt.colorbar()
    plt.title('Chromagram')
    plt.tight_layout()
    plt.savefig("./"+nombre+"_chroma")

def Abre_Wav_Original(framesOr, nombre):
    """Abre solo el WAV para cuando viene de grabar"""
    p = pyaudio.PyAudio()

    wfOrig = wave.open(nombre+".wav",'wb')
    wfOrig.setnchannels(1)
    wfOrig.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wfOrig.setframerate(44100)
    wfOrig.writeframes(b''.join(framesOr))
    wfOrig.close()

def Abre_Wavs_Foto(nombre):
    """Abre los wav y png de la base en la carpeta del proyecto para cuando viene de abrir"""

    """Abrir los wav de la BD"""

    p = pyaudio.PyAudio()

    wfOrig = wave.open(nombre+".wav", 'wb')
    wfOrig.setnchannels(1)
    wfOrig.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wfOrig.setframerate(44100)
    wfOrig.writeframes(b''.join(framesOr))
    wfOrig.close()

    wfMel = wave.open(nombre+"_melosynth.wav", 'wb')
    wfMel.setnchannels(1)
    wfMel.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wfMel.setframerate(44100)
    wfMel.writeframes(framesMel)
    wfMel.close()

    """Falta formato de Imagen"""


def Cierra(nombre):
    """Elimina los archivos abiertos en la carpeta del proyecto"""
    pathOr = "./"+nombre+".wav"
    pathMel = "./"+nombre+"_melosynth.wav"
    pathImg = "./"+nombre+".img"
    os.remove(pathOr)
    os.remove(pathMel)
    os.remove(pathImg)

def Reproduce_Analisis(nombre):
    """Reproduce Audios en la Seccion de Analisis"""
    p = pyaudio.PyAudio()

    wf = wave.open(nombre, 'rb')
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

    data = wf.readframes(1024)

    while str(data)!="b''":
        stream.write(data)
        data = wf.readframes(1024)

    stream.close()
    p.terminate()

