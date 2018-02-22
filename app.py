# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os
import boto3

from pathlib import Path
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def makeWebhookResult(req):
    if req.get("result").get("action") != "shipping.cost":
        return {}
    result = req.get("result")
    sessionID = req.get("sessionId")
    
      
  
        
    
    contexts = result.get("contexts")
    contextName = contexts[0].get("name");
    #parameters = result.get("parameters")
    #useranswer = parameters.get("answer")
    
    contextName = "chapter1"
    correctIncorrectMessage =""
    QuestionText = "Sample Question"
    Option1 ="Option1"
    Option2 ="Option2"
    Option3 ="Option3"
    Option4 ="OPtion3"
    
    folderpath =""
    corpuspath = ""
    #key = 'description_' + str(fid) + '.json'
    #response = s3.put_object(Bucket='d2c-api2-bucket',      Body=json_data,           Key=key                         )
    usersessionQuestion_file = Path(folderpath + sessionID +".txt")
    if usersessionQuestion_file.exists():
        line = readLine(usersessionQuestion_file,contextName)
        
        words3 = line.split("#")
        if useranswer != getAnswer(usersessionQuestion_file,contextName):
        if useranswer != 1:
            correctIncorrectMessage = "Incorrect Answer"
        else:
            correctIncorrectMessage = "Great! Correct Answer"
            
            
        QuestionText = words3[1]
        Option1 = words3[2]
        Option2 = words3[3]
        Option3 = words3[4]
        Option4 = words3[5]
    
  
    else:    
        myfile = open( usersessionQuestion_file, 'w+')
        for x in range(30):
            #myfile.write(random_line(corpuspath + contextName + ".txt"))
            myfile.write("1#Question1#Option1#Option2#Option3#Option4#1")
        myfile.close()
        #line = readLine(usersessionQuestion_file +'.txt',1)
        line = "1#Question1#Option1#Option2#Option3#Option4#1"
        words3 = line.split("#")
        QuestionText = words3[1]
        Option1 = words3[2]
        Option2 = words3[3]
        Option3 = words3[4]
        Option4 = words3[5]

    cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':400, 'Africa':500}
    var5	="          \"type\": 0,	"
    var6	="          \"platform\": \"facebook\",	"
    var7	="          \"speech\": \"Question Text1\"	"
    speech = "HELLO"
    speech1 = var5 + var6  + var7

    print("Response:")
    print(speech)
     #"contextOut": [],
    emptyspace = ""
    return {
   
   "speech":"",
   "messages":[
      {
         "type":3,
         "platform":"facebook",
         "imageUrl":"http://charityrefresh.org/ella/asset.hello-ella.gif"
      },
      {
         "type":0,
         "platform":"facebook",
         "speech": correctIncorrectMessage
      },
      {
         "type":0,
         "platform":"facebook",
         "speech":QuestionText 
      },
      {
         "type":0,
         "platform":"facebook",
         "speech":Option1
      },
      {
         "type":0,
         "platform":"facebook",
         "speech":Option2
      },
      {
         "type":0,
         "platform":"facebook",
         "speech":Option3
      },
      {
         "type":0,
         "platform":"facebook",
         "speech":Option4
      },
      {
         "type":0,
         "platform":"facebook",
         "speech":"My Second Responsedd " 
      },
      {
         "type":0,
         "platform":"facebook",
         "speech":sessionID
      },
        {
         "type":0,
         "platform":"facebook",
         "speech":contextName
      },
       {
          "type": 2,
          "platform": "facebook",
          "title": "What can I help you with",
          "replies": [
            "1",
            "2",
            "3",
            "4"
          ]
     },
      {
         "type":4,
         "platform":"facebook",
         "payload":{
            "facebook":{
               "attachment":{
                  "type":"template",
                  "payload":{
                     "template_type":"button",
                     "text":"What can I help you with?",
                     "buttons":[
                        {
                           "type":"postback",
                           "title":"Answer A",
                           "payload":"A"
                        },
                        {
                           "type":"postback",
                           "title":"Answer B",
                           "payload":"B"
                        },
                        {
                           "type":"postback",
                           "title":"Answer C",
                           "payload":"C"
                        }
                     ]
                  }
               }
            }
         }
      }
   ]
}

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def readLine(file_name,contextName):
    fp = open(file_name)
    for i, line in enumerate(fp):
        if i == string.replace(string.replace(contextName,"q",""),"Q",""):
            # 26th line
            return line
            #questiontext
            #answer = words2[3]
            break
    fp.close()

def getAnswer(file_name,contextName):
    QuestionText = "Sample Question"
    Option1 ="Option1"
    Option2 ="Option2"
    Option3 ="Option3"
    Option4 ="OPtion3"
    Answer ="1"
    fp = open(file_name)
    for i, line in enumerate(fp):
        if i == string.replace(string.replace(contextName,"q",""),"Q",""):
            # 26th line
            words3 = line.split("#")
            QuestionText = words3[1]
            Option1 = words3[2]
            Option2 = words3[3]
            Option3 = words3[4]
            Option4 = words3[5]
            Answer = words3[6]
            return Answer
            #questiontext
            #answer = words2[3]
            break
    fp.close()
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
