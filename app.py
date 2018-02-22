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


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
