import pyaudio
import wave
import os

def Lista_Audios():
    """Pide audios de la BD y los devuelve a la Interfaz"""
    pass

def Abrir_Reproducir(nombre):
    """Pide Item de la BD y consigue los Frames, Hace el WAV y lo reproduce"""

    """Sacar Frames"""

    p = pyaudio.PyAudio()

    wf = wave.open(nombre+".wav")
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))

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

    os.remove("./"+nombre+".wav")
