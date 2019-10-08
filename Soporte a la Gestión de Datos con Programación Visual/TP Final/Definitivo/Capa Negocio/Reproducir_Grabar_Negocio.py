import pyaudio
import wave
import os

chunk = 1024 #Graba en 24 trozos de 1024 samples
sample_format = pyaudio.paInt16 #16 bits por sample
channels = 1
fs = 44100 #Graba 44100 samples por segundo
p = pyaudio.PyAudio()


def Grabar(stream):
    """inicia la Grabacion"""
    frames = []
    if stream is None:
        stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
        stream.start_stream()
    while stream.is_active():
        data = stream.read(chunk)
        frames.append(data)
    return stream, frames

def Parar(stream, frames):
    """Detiene la Grabacion y crea su archivo WAV"""
    stream.stop_stream()
    stream.close()
    return frames


def Reproducir(frames, nombre):
    """Reproduce un Audio"""
    p = pyaudio.PyAudio()

        #Crea Archivo Wav de la Grabacion
    wf = wave.open(nombre, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    p.terminate()

    stream = p.open(format = sample_format,
                    channels = channels,
                    rate = fs,
                    output = True)

    for f in frames:
        stream.write(f)

    stream.close()
    p.terminate()
    os.remove("./"+nombre+".wav")
    return frames

def Guardar_Audio(frames, nombre, autor, descripcion):
    """Invoca Metodo de guardar en capa de datos"""
    pass

