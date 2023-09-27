from textblob import TextBlob 
import pyttsx3
import speech_recognition as sr 
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import wikipedia
import datetime
import random

# escuchar micro y devolver audio como texto
def voice_to_text():
    # almacenar recognizer en variable
    r = sr.Recognizer()
    
    # config micro
    with sr.Microphone() as origen:
        
        # tiempo de espera
        r.pause_threshold = 0.8
        
        # limpiar ruido
        r.adjust_for_ambient_noise(origen, duration=1)
        print("Escuchando...")
        try:
            # escuchar audio
            audio = r.listen(origen)
            
            # convertir audio a texto
            text = r.recognize_google(audio, language="es-ES")
            print(text)
            return text
        except sr.UnknownValueError as e:
            print(e)
            print("No entendí, intenta de nuevo")
            return "No entendí, intenta de nuevo"
        except sr.RequestError as e:
            print(e)
            print("No hay servicio")
            return "No hay servicio"
        except:
            print(e)
            print("Algo ha salido mal")
            return "Algo ha salido mal"
        # traducción del texto al inglés
        # text = r.recognize_google(audio, language="en-US")
        # print(text)
        # return text
        # hablar con el robot
        
def censure(text):
    palabrotas = ["hijo de puta", "hijoputa", "cabron", "tonto", "tonta", "tontas", "tontos", "gilipollas", "hijos de puta", "hijas de puta", "putas", "puta", 
                  "putos", "puto", "hijaputa", "imbecil", "subnormal", "retrasado", "retrasada", "capullo", "come mierda", "mierda", "cabrona", "polla", "soplapollas", 
                  "pollas", "coño", "coños", "cabrón", "mamón", "tomar por culo", "joder"]
    for p in palabrotas:
        if p in text:
            text = text.replace(p, "¡No se dicen palabrotas!")
    return text
            
            
def speak_spa(text):
    # almacenar engine en variable
    engine = pyttsx3.init()
    
    # configurar voz
    voices = engine.getProperty("voices")
    engine.setProperty("voice", id4)
    
    # hablar
    engine.say(text)
    engine.runAndWait()

def speak_eng(text):
    # almacenar engine en variable
    engine = pyttsx3.init()
    
    # configurar voz
    voices = engine.getProperty("voices")
    engine.setProperty("voice", id3)
    
    # hablar
    engine.say(text)
    engine.runAndWait()
    
# buscar información sobre un término o frase
def search_wikipedia(text):
    # buscar en wikipedia
    wikipedia.set_lang("es")
    result = wikipedia.summary(text, sentences=1)
    print(result)
    speak_spa("En wikipedia he encontrado esto...")
    speak_spa(result)


# translate
def translate(text):
    palabraTraducir = TextBlob(text)
    palabra_traducida = str(palabraTraducir.translate(from_lang='es', to='en'))
    print(palabra_traducida)
    return palabra_traducida

def day_of_week():
    day = datetime.date.today()
    print(day)
    day_week = day.weekday()
    day_week_dic = {
        0: "lunes",
        1: "martes",
        2: "miercoles",
        3: "jueves",
        4: "viernes",
        5: "sabado",
        6: "domingo"
    }
    speak_spa(f'Ayer fue {day_week_dic[day_week - 1]}. Hoy es {day_week_dic[day_week]}. Mañana será {day_week_dic[day_week + 1]}') 
    
def what_time_is_it():
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        moment = "de la noche"
    elif hour.hour >= 6 and hour.hour < 13:
        moment = "de la mañana"
    else:  
        moment = "de la tarde"
    speak_spa(f'Ahora mismo son las {hour.hour} y {hour.minute} minutos {moment}')
    
def voice_assistant():
    start = True
    while start:
        text = voice_to_text().lower()
        if "hora" in text:
            what_time_is_it()
        elif "día" in text:
            day_of_week()
        elif "youtube" in text:
            speak_spa("Ahora mismo abro youtube")
            webbrowser.open(f"youtube.com")
        elif "wikipedia" in text:
            text = text.replace("busca en wikipedia", "")
            search_wikipedia(text)
        elif "traduce" in text:
            text = text.replace("traduce", "")
            speak_spa(f'{text} en inglés se dice: ')
            speak_eng(translate(text))
        elif "chiste" in text:
            list_of_jokes = pyjokes.get_jokes(language="es", category="all")
            speak_spa(list_of_jokes[random.randint(0, len(list_of_jokes)-1)])
        elif "reproduce" in text:
            text = text.replace("reproduce", "")
            pywhatkit.playonyt(text)
        elif "abre" in text:
            text = text.replace("abre", "")
            webbrowser.open(f"{text}.com")
        elif "el precio de las acciones" in text:
            action = text.split("de")[-1].strip()
            cartera = {"apple":"APPL",
                       "amazon":"AMZN",
                       "google":"GOOGL"}
            try:
                accion_search = cartera[action]
                accion_search = yfinance.Ticker(accion_search)
                price = accion_search.info["regularMarketPrice"]
                speak_spa(f'El precio de las acciones de {action} es de {price} dólares')
            except:
                speak_spa("No he encontrado la información")
        elif "cierra" in text:
            start = False
            speak_spa("Hasta luego")
        else:
            speak_spa("No te he entendido")

id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id4 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"


voice_assistant()

# what_time_is_it()
# day_of_week()
# text = voice_to_text()
# text_censure = censure(text)
# speak_spa(text_censure)
# speak_eng(translate(text))
# day_of_week()



# engine = pyttsx3.init()
# for voz in engine.getProperty("voices"):
#     print(voz)