# chmod 666 main.py
# export FLASK_ENV=development
# export FLASK_APP=main.py
# python3 main.py -p 5000
# docker container run --rm -p 8080:5000 --mount type=bind,source=/Users/akhan2/Python/flask-app/source-code,target=/opt/flask-app --name flask-app khan2a/flask-app
# pip install simple-websocket

import os, logging, random
from argparse import ArgumentParser
from flask import Flask, request, jsonify, Response
from multiprocessing import Value
from nccos import *

counter = Value('i', 0)
app = Flask(__name__)
logging.basicConfig(format="%(message)s", level=logging.INFO)
# SERVER_URL = "http://khan2a.com:8080"
SERVER_URL = "https://9b2af9f4-0c77-4c58-88f2-211c03ef2bd0-00-1b5tuzgaiqczj.janeway.replit.dev"
API_KEY = "xxxxx"
# # API_KEY = "hxxxxx"
API_SECRET = "xxxxx"
# API_KEY = "xxxxxxx"
# API_SECRET = "xxxxx"


@app.route("/amd_event_url", methods=["GET", "POST"])
def amd_event_url():
  try:
    ncco, action = "", ""
    event_json = request.get_json() if request.is_json else {}
    for arg in request.args.keys():
      event_json[arg] = request.args.get(arg)
    action = event_json["action"] if event_json["action"] != "" else "talk"
    event_json["SERVER_URL"] = SERVER_URL
    print("amd_event_url:\n" + str(event_json))
    try:
      if "status" in event_json:
        if "sub_state" in event_json and event_json["sub_state"] != "":
          print("\n*****\namd_event_url: AMD event detected --> {0}\n*****\n".
                format(event_json["sub_state"]))
          ncco = ncco_set[action][event_json["sub_state"]](event_json)
          print(
              "amd_event_url: AMD event detected --> sending NCCO: {0}".format(
                  str(ncco)))
        elif event_json["status"] in ncco_set[action]:
          print("\n*****\namd_event_url: AMD event detected --> {0}\n*****\n".
                format(event_json["status"]))
          ncco = ncco_set[action][event_json["status"]](event_json)
          print(
              "amd_event_url: AMD event detected --> sending NCCO: {0}".format(
                  str(ncco)))
        else:
          print("amd_event_url: Call event detected --> {0}".format(
              event_json["status"]))
      else:
        print("amd_event_url: An event detected --> {0}".format(
            event_json["status"]))
    except Exception as e:
      print(e)
    return (jsonify(ncco) if ncco != "" else "", 200)
  except Exception:
    if request.is_json:
      print("voice_event_url --> " + str(request.get_json()))
    else:
      print("voice_event_url --> " + str(request))
    return ("", 200)


@app.route("/answer_url", methods=["GET", "POST"])
def answer_url():
  ncco = ""
  event_json = {}
  for arg in request.args.keys():
    event_json[arg] = request.args.get(arg)
  ncco = [        {
            "action": "connect",
            "eventType": "synchronous",
            "eventUrl": [
                event_json["eventUrl"]
            ],
            "from": event_json["from"],
            "endpoint": [
                {
                    "type": "websocket",
                    "uri": event_json["uri"],
                    "content-type": "audio/l16;rate=16000",
                    "headers": {
                        "app": "audiosocket"
                    }
                }
            ]
        }]
  print("\n*****\nanswer_url --> Sending NCCO: {0}\n*****\n".format(ncco))
  return (jsonify(ncco) if ncco != "" else "", 200)


@app.route("/uui", methods=["GET", "POST"])
def uui():
  ncco = ""
  event_json = {}
  for arg in request.args.keys():
    event_json[arg] = request.args.get(arg)
  ncco = [{
      "action":
      "connect",
      "eventUrl": [event_json["eventUrl"]],
      "from":
      event_json["from"],
      "endpoint": [{
          "type": "sip",
          "uri": event_json["uri"],
          "standard_headers": {
              "User-to-User": "342342ef34;encoding=hex;purpose=foo;content=bar"
          },
          "headers": {
              "story": "gruffalo",
              "occupation": "developer"
          }
      }]
  }]
  print("\n*****\nanswer_url --> Sending NCCO: {0}\n*****\n".format(ncco))
  return (jsonify(ncco) if ncco != "" else "", 200)


@app.route("/asr", methods=["GET", "POST"])
def asr():
  # time.sleep(7)
  event_json = request.get_json() if request.is_json else {}
  for arg in request.args.keys():
    event_json[arg] = request.args.get(arg)
  ncco = [{
      "action": "talk",
      "text": "Hello and welcome to the ASR demo app. Please say a number."
  }, {
      "speech": {
          "context": ["one", "two", "three", "four"],
          "language": "en-GB",
          "maxDuration": 10
      },
      "action":
      "input",
      "eventUrl": ["http://qaservices1.flint.npe:8555/callback?qa_type=asr"]
  }]
  print("\n*****\nanswer_url --> Sending NCCO: {0}\n*****\n".format(ncco))
  return (jsonify(ncco) if ncco != "" else "", 200)


@app.route("/dtmf", methods=["GET", "POST"])
def dtmf():
  ncco, action = "", ""
  if request.is_json:
    event_json = request.get_json()
    for arg in request.args.keys():
      event_json[arg] = request.args.get(arg)
    print("dtmf:\n" + str(event_json))
    try:
      if "dtmf" in event_json and event_json["dtmf"]["digits"] != "":
        if event_json["dtmf"]["digits"] == "1":
          ncco = [
              {
                  "action":
                  "talk",
                  "voiceName":
                  "Amy",
                  "level":
                  "1",
                  "text":
                  "Thank you for your input {0}. Please wait for stream action."
                  .format(event_json["dtmf"]["digits"]),
              },
              {
                  "action":
                  "stream",
                  "streamUrl": [
                      "https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_1OMB_MP3.mp3"
                  ],
              },
          ]
        elif event_json["dtmf"]["digits"] == "2":
          ncco = [
              {
                  "action":
                  "talk",
                  "voiceName":
                  "Amy",
                  "level":
                  "1",
                  "text":
                  "Thank you for your input {0}. Please wait for record and connect action."
                  .format(event_json["dtmf"]["digits"]),
              },
              # {
              #   "action": "record",
              #   "eventUrl": [event_json["notify_event_url"]]
              # },
              {
                  "action": "connect",
                  "endpoint": [{
                      "type": "phone",
                      "number": "441174960064"
                  }],
                  "limit": "180",
              },
          ]
        elif event_json["dtmf"]["digits"] == "3":
          conv_name = "second-conv-{0}".format(random.randint(100, 100000))
          conv_url = "{0}?qa_unique_id={1}".format(
              event_json["notify_event_url"], conv_name)
          print("conversation: conversation url --> {0}".format(conv_url))
          ncco = [
              {
                  "action":
                  "talk",
                  "voiceName":
                  "Amy",
                  "level":
                  "1",
                  "text":
                  "Thank you for your input {0}. Please wait for conversation action."
                  .format(event_json["dtmf"]["digits"]),
              },
              {
                  "action": "conversation",
                  "name": conv_name,
                  "muted": False,
                  "record": True,
                  "earmuff": False,
                  "playExitSound": True,
                  "playEnterSound": True,
                  "endOnExit": True,
                  "startOnEnter": True,
                  "eventCallbackUrl": [conv_url],
              },
          ]
        elif event_json["dtmf"]["digits"] == "0":
          ncco = [
              {
                  "action":
                  "talk",
                  "voiceName":
                  "Amy",
                  "level":
                  "1",
                  "text":
                  "Thank you for your input {0}. We will now hangup the call.".
                  format(event_json["dtmf"]["digits"]),
              },
              {
                  "action": "hangup"
              },
          ]
      else:
        ncco = [
            {
                "action": "talk",
                "voiceName": "Amy",
                "level": "1",
                "text": "No input detected. Please try again",
            },
            {
                "action": "input",
                "type": ["dtmf"],
                "timeOut": "10",
                "eventUrl": ["{0}/dtmf".format(SERVER_URL)],
                "eventMethod": "POST",
            },
        ]
    except Exception as e:
      print("Exception: {0}".format(e))
  print("dtmf: dtmf event detected --> sending NCCO: {0}".format(str(ncco)))
  return (jsonify(ncco) if ncco != "" else "", 200)


@app.route("/voice_event_url", methods=["GET", "POST"])
def voice_event_url():
  # if request.is_json:
  #   print("voice_event_url --> " + str(request.get_json()))
  # else:
  #   print("voice_event_url --> " + str(request))
  return ("", 204)


@app.route("/rtc_event_url", methods=["GET", "POST"])
def rtc_event_url():
  # if request.is_json:
  #   print("rtc_event_url --> " + str(request.get_json()))
  # else:
  #   print("rtc_event_url --> " + str(request))
  return ("", 204)


@app.route("/ncco_event_url", methods=["GET", "POST"])
def ncco_event_url():
  if request.is_json:
    print("ncco_event_url --> " + str(request.get_json()))
    if "recording_url" in request.get_json():
      print("\n>>>>>\nrecording_url: {0}?api_key={1}&api_secret={2}\n<<<<<\n".
            format(request.get_json()["recording_url"], API_KEY, API_SECRET))
    elif "speech" in request.get_json():
      speech = request.get_json()["speech"]
      print("\n>>>>>\speech: {0}\n<<<<<\n".format(
          request.get_json()["speech"]))
      if "results" in speech:
        results = speech["results"]
        for result in results:
          print("result: {0}".format(result))
  else:
    print("ncco_event_url --> " + str(request))
  return ("", 204)


@app.route("/tts_ng6", methods=["GET", "POST"])
def tts_ng6():
  # resp = Response("")
  # resp.headers['Content-Type'] = 'application/json'
  # return (resp, 200)
  return (jsonify([{"tts_ng6": "400"}]), 200)


@app.route("/ncco_eventUrl", methods=["GET", "POST"])
def ncco_eventUrl():
  if request.is_json:
    print("ncco_event_url --> " + str(request.get_json()))
    if "recording_url" in request.get_json():
      print("\n>>>>>\nrecording_url: {0}?api_key={1}&api_secret={2}\n<<<<<\n".
            format(request.get_json()["recording_url"], API_KEY, API_SECRET))
  else:
    print("ncco_eventUrl --> " + str(request))
  return ("", 204)


@app.route("/omar", methods=["GET", "POST"])
def omar():
  if request.is_json:
    print("ncco_event_url --> " + str(request.get_json()))
    if "recording_url" in request.get_json():
      print("\n>>>>>\nrecording_url: {0}?api_key={1}&api_secret={2}\n<<<<<\n".
            format(request.get_json()["recording_url"], API_KEY, API_SECRET))
  else:
    print("ncco_eventUrl --> " + str(request))
  resp = Response("")
  with counter.get_lock():
    counter.value += 1
    out = counter.value
  # resp.headers['Content-Type'] = 'application/json'
  if out % 2 == 0:
    return (resp, 400)
  else:
    return (resp, 200)
  # return (jsonify([{"tts_ng6": "400"}]), 200)


@app.route("/", methods=["GET", "POST"])
def base():
  if request.is_json:
    print("ncco_event_url --> " + str(request.get_json()))
    if "recording_url" in request.get_json():
      print("\n>>>>>\nrecording_url: {0}?api_key={1}&api_secret={2}\n<<<<<\n".
            format(request.get_json()["recording_url"], API_KEY, API_SECRET))
  else:
    print("ncco_eventUrl --> " + str(request))
  return ("hello world", 200)


@app.route('/audio/<filename>')
def stream_audio(filename):
  print(f"audio file requested: {filename}")
  def generate():
    with open(f"audio/{filename}", "rb") as faudio:
        data = faudio.read(1024)
        while data:
            yield data
            data = faudio.read(1024)
  return Response(generate(), mimetype=f"audio/x-{filename.split('.')[1]}")


if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("-p")
  args = parser.parse_args()
  p = args.p
  port = int(os.environ.get("PORT", p))
  app.run(host="0.0.0.0", port=port, debug=True)
