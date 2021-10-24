from flask import Flask, session, render_template, redirect
import Aria
import os
import pyttsx3
app = Flask(__name__)
app.secret_key='AriaTechkeyId8888297h8b6rcr4gf5ctu@@@kdkdfkd--jjfkd'
user=None
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/Aria/api/ask/<devId>/<query>')
def AriaAPI(query,devId):
    devicesIdFile = open('device.id','r')
    for x in devicesIdFile.read().split(','):
        x=x.split(':')
        if x[1] == devId:
            user=x
            break
    devicesIdFile.close()
    if user != None:
        return Aria.check(query)
    else:
        return '_Invalid Device Id'
@app.route('/Aria/api/speak/<instance>/<text>')
def speak(instance,text):
    try:
        os.makedirs('static/'+instance)
        engine = pyttsx3.init() 
        engine.save_to_file(text, 'static/'+instance+'/tts.mp3')
        engine.runAndWait()
    except:
        engine = pyttsx3.init() 
        engine.save_to_file(text, 'static/'+instance+'/tts.mp3')
        engine.runAndWait()
    return ''
@app.route('/Aria/manage/api/<nUser>/<key>')
def editKeys(nUser,key):
    return 'Service not availiable' 
@app.route('/download')
def download():
    return redirect('/static/windows.exe')

if __name__=='__main__':
    app.run()