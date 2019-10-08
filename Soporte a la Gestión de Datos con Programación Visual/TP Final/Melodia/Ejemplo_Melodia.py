import vamp
import librosa
import numpy as np
import matplotlib.pyplot as plt
import math as m
from librosa import display as d
import melosynth as mel
from pydub import AudioSegment


audioAr = 'C:/Users/ornec/Google Drive/Facu/4to/Soporte a la GDD/TPS/TP Final/Pruebas/Escala_Melodica_Sostenidos.wav'

audio, sr = librosa.load(audioAr, sr=44100, mono = True)
print(type(audio[0]))

params = {"minfqr": 25.0, "maxfqr": 2000.0, "voicing": 0.2, "minpeaksalience": 0.0}

data = vamp.collect(audio, sr, "mtg-melodia:melodia", parameters=params)
hop, melody = data['vector']

timestamps = 8 * 128/44100.0 + np.arange(len(melody)) * (128/44100.0)

melody_pos = melody[:]
melody_pos[melody <= 0] = None
plt.figure(figsize=(18,6))
plt.plot(timestamps, melody_pos)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()

NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()

def freq_to_number(f): return 69 + 12*np.log2(f/440.0)
def number_to_freq(n): return 440 * 2.0**((n-69)/12.0)
def note_name(n): return NOTE_NAMES[n % 12] + str(n/12 - 1)

nota = []

for i in range(len(melody_pos)):
    if i > 0:
        num = (freq_to_number(melody_pos[i]))
        if not m.isnan(melody_pos[i]):
            nota.append(note_name(int(num)))

archivo = open("jaja.txt", "w")

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

mel.melosynth("jaja.txt", outputfile=None ,fs= 44100, nHarmonics= 1, square= False, useneg=False)

audio, sr = librosa.load('C:/Users/ornec/PycharmProjects/Melodia/jaja_melosynth.wav' , sr = 44100 , mono = True)

chroma = librosa.feature.chroma_cqt(y = audio, sr = sr)
nombre="aksdas"

plt.figure(figsize=(10, 4))

d.specshow(chroma, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()
plt.savefig("./"+nombre+"chroma")
plt.show()
