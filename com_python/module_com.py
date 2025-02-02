from flask import Flask, request, jsonify
import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
import datetime
import os
import logging

app = Flask(__name__)

# Configuration du logging
logging.basicConfig(level=logging.INFO)  # Tu peux définir le niveau selon tes besoins
logger = logging.getLogger(__name__)

#setup engine 

engine = pyttsx3.init()
engine.setProperty('engine', 'espeak') #defini espeak comme lecteur
engine.setProperty('voice', 'fr') #defini la langue de lecture
engine.setProperty('rate', 150) #vitesse de lecture
engine.setProperty('volume', 1.0) #volume de lecture
 
    
def speak_text(texte):
    """
    Convertit un texte en parole et le lit à voix haute.
    :param texte: Le texte à lire.
    """
   
    engine.say(texte)
    engine.runAndWait()



@app.route("/read-text", methods=["POST"])
def read_text():
    """
    Endpoint pour lire un texte fourni dans le body de la requête.
    :return: JSON avec un message de confirmation.
    """
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Le champ 'text' est requis"}), 400
    speak_text(data["text"])
    return jsonify({"message": "Texte lu avec succès"})



@app.route("/read-file", methods=["POST"])
def read_file():
    """
    Endpoint pour lire le contenu d'un fichier dont le nom est fourni dans le body de la requête.
    :return: JSON avec un message de confirmation.
    """
    data = request.get_json()
    if not data or "filename" not in data:
        return jsonify({"error": "Le champ 'filename' est requis"}), 400
    filename = data["filename"]
    if not os.path.exists(filename):
        return jsonify({"error": "Fichier introuvable"}), 404
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    speak_text(text)
    return jsonify({"message": "Fichier lu avec succès"})



@app.route("/record-audio", methods=["POST"])
def record_audio():
    """
    Enregistre un audio pendant une durée spécifiée et le sauvegarde dans un fichier.
    :return: JSON avec un message de confirmation.
    """
    data = request.get_json()
    rate = 44100
    if not data or "filename" not in data or "duration" not in data:
        return jsonify({"error": "Les champs 'filename' et 'duration' sont requis"}), 400
    filename = data["filename"]
    duration = int(data["duration"])
    
    #Initialisation de PyAudio
    audio = pyaudio.PyAudio()
    
    #Ouverture du flux audio
    stream = audio.open(format=pyaudio.paInt16, 
                        channels=1, 
                        rate=rate, 
                        input=True, 
                        frames_per_buffer=1024)
    
    print("Enregistrement en cours...")
    speak_text("Enregistrement en cours...")
    frames = []
    
    for i in range(0, int(rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
        
    print("Enregistrement terminé.")
    speak_text("Enregistrement terminé.")
    
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    return jsonify({"message": "Enregistrement terminé"})



@app.route("/recognize-speech", methods=["POST"])
def recognize_speech():
    """
    Reconnaît la parole dans un fichier audio et retourne le texte détecté.
    :return: JSON avec le texte reconnu.
    """
    data = request.get_json()
    if not data or "filename" not in data:
        return jsonify({"error": "Le champ 'filename' est requis"}), 400
    filename = data["filename"]
    if not os.path.exists(filename):
        return jsonify({"error": "Fichier introuvable"}), 404
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        speak_text("Vous avez dit : " + text)
        return jsonify({"message": "Texte reconnu", "text": text}), 200
    except sr.UnknownValueError as e:
        logger.error(f"Erreur de reconnaissance vocale: {e}")
        return jsonify({"error": f"Impossible de reconnaître l'audio: {e}"}), 400
    except sr.RequestError as e:
        return jsonify({"error": f"Erreur du service de reconnaissance vocale : {e}"}), 500






if __name__ == "__main__":
    app.run(debug=True)
