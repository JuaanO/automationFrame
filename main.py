import requests
import json
import subprocess


process = subprocess.Popen('./geckodriver')

host = 'http://127.0.0.1:9515/'

capabilities = {
    "desiredCapabilities": {
        "chromeoptions": {
            "binary": "/opt/google/chrome/google-chrome/chrome"
        },
        "platform": "ANY"
    }
}

reponse = requests.request('POST', host + 'session', data=json.dumps(capabilities).encode('utf8'))
session_id = json.loads(reponse.text)['sessionId']
requests.request('POST', host + 'session/' + session_id + '/url', data=json.dumps({"url": "http://www.duckduckgo.com"}).encode('utf8'))
requests.request('DELETE', host + 'session/' + session_id + 'window')
requests.request('DELETE', host + 'session/' + session_id)
process.terminate()
