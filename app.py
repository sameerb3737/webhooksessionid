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
    #parameters = result.get("parameters")
    #zone = parameters.get("shipping-zone")

    cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':400, 'Africa':500}

    var1	="'fulfillment': {	"
var2	="      'speech': '',	"
var3	="      'messages': [	"
var4	="        {	"
var5	="          'type': 0,	"
var6	="          'platform': 'slack',	"
var7	="          'speech': 'Question Text1'	"
var8	="        },	"
var9	="        {	"
var10	="          'type': 0,	"
var11	="          'platform': 'slack',	"
var12	="          'speech': '1. Option1'	"
var13	="        },	"
var14	="        {	"
var15	="          'type': 0,	"
var16	="          'platform': 'slack',	"
var17	="          'speech': '2. Option2'	"
var18	="        },	"
var19	="        {	"
var20	="          'type': 0,	"
var21	="          'platform': 'slack',	"
var22	="          'speech': '3. Option3'	"
var23	="        },	"
var24	="        {	"
var25	="          'type': 0,	"
var26	="          'platform': 'slack',	"
var27	="          'speech': '4. Option4'	"
var28	="        },	"
var29	="        {	"
var30	="          'type': 2,	"
var31	="          'platform': 'slack',	"
var32	="          'title': 'Answer Choice',	"
var33	="          'replies': [	"
var34	="            '1',	"
var35	="            '2',	"
var36	="            '3',	"
var37	="            '4'	"
var38	="          ]	"
var39	="        },	"
var40	="        {	"
var41	="          'type': 0,	"
var42	="          'platform': 'facebook',	"
var43	="          'speech': 'Question Text1'	"
var44	="        },	"
var45	="        {	"
var46	="          'type': 0,	"
var47	="          'platform': 'facebook',	"
var48	="          'speech': '1. Option1'	"
var49	="        },	"
var50	="        {	"
var51	="          'type': 0,	"
var52	="          'platform': 'facebook',	"
var53	="          'speech': '2. OPtion2'	"
var54	="        },	"
var55	="        {	"
var56	="          'type': 0,	"
var57	="          'platform': 'facebook',	"
var58	="          'speech': '3. Option3'	"
var59	="        },	"
var60	="        {	"
var61	="          'type': 0,	"
var62	="          'platform': 'facebook',	"
var63	="          'speech': '4. Option4'	"
var64	="        },	"
var65	="        {	"
var66	="          'type': 2,	"
var67	="          'platform': 'facebook',	"
var68	="          'title': 'Answer Choices',	"
var69	="          'replies': [	"
var70	="            '1',	"
var71	="            '2',	"
var72	="            '3',	"
var73	="            '4'	"
var74	="          ]	"
var75	="        },	"
var76	="        {	"
var77	="          'type': 0,	"
var78	="          'platform': 'telegram',	"
var79	="          'speech': 'Question Text1'	"
var80	="        },	"
var81	="        {	"
var82	="          'type': 0,	"
var83	="          'platform': 'telegram',	"
var84	="          'speech': '1. Option1'	"
var85	="        },	"
var86	="        {	"
var87	="          'type': 0,	"
var88	="          'platform': 'telegram',	"
var89	="          'speech': '2. Option2'	"
var90	="        },	"
var91	="        {	"
var92	="          'type': 0,	"
var93	="          'platform': 'telegram',	"
var94	="          'speech': '3. Option3'	"
var95	="        },	"
var96	="        {	"
var97	="          'type': 0,	"
var98	="          'platform': 'telegram',	"
var99	="          'speech': '4. Option4'	"
var100	="        },	"
var101	="        {	"
var102	="          'type': 2,	"
var103	="          'platform': 'telegram',	"
var104	="          'title': 'Answer Choice',	"
var105	="          'replies': [	"
var106	="            '1',	"
var107	="            '2',	"
var108	="            '3',	"
var109	="            '4'	"
var110	="          ]	"
var111	="        },	"
var112	="        {	"
var113	="          'type': 0,	"
var114	="          'platform': 'kik',	"
var115	="          'speech': 'Question Text1'	"
var116	="        },	"
var117	="        {	"
var118	="          'type': 0,	"
var119	="          'platform': 'kik',	"
var120	="          'speech': '1. Option1'	"
var121	="        },	"
var122	="        {	"
var123	="          'type': 0,	"
var124	="          'platform': 'kik',	"
var125	="          'speech': '2. Option2'	"
var126	="        },	"
var127	="        {	"
var128	="          'type': 0,	"
var129	="          'platform': 'kik',	"
var130	="          'speech': '3. Option3'	"
var131	="        },	"
var132	="        {	"
var133	="          'type': 0,	"
var134	="          'platform': 'kik',	"
var135	="          'speech': '4. Option4'	"
var136	="        },	"
var137	="        {	"
var138	="          'type': 2,	"
var139	="          'platform': 'kik',	"
var140	="          'title': 'Answer Choice',	"
var141	="          'replies': [	"
var142	="            '1',	"
var143	="            '2',	"
var144	="            '3',	"
var145	="            '4'	"
var146	="          ]	"
var147	="        },	"
var148	="        {	"
var149	="          'type': 0,	"
var150	="          'platform': 'viber',	"
var151	="          'speech': 'Question Text1'	"
var152	="        },	"
var153	="        {	"
var154	="          'type': 0,	"
var155	="          'platform': 'viber',	"
var156	="          'speech': '1. Option1'	"
var157	="        },	"
var158	="        {	"
var159	="          'type': 0,	"
var160	="          'platform': 'viber',	"
var161	="          'speech': '2. Option2'	"
var162	="        },	"
var163	="        {	"
var164	="          'type': 0,	"
var165	="          'platform': 'viber',	"
var166	="          'speech': '3. Option3'	"
var167	="        },	"
var168	="        {	"
var169	="          'type': 0,	"
var170	="          'platform': 'viber',	"
var171	="          'speech': '4. Option4'	"
var172	="        },	"
var173	="        {	"
var174	="          'type': 2,	"
var175	="          'platform': 'viber',	"
var176	="          'title': 'Answer Choice',	"
var177	="          'replies': [	"
var178	="            '1',	"
var179	="            '2',	"
var180	="            '3',	"
var181	="            '4'	"
var182	="          ]	"
var183	="        },	"
var184	="        {	"
var185	="          'type': 0,	"
var186	="          'platform': 'skype',	"
var187	="          'speech': 'Question Text1'	"
var188	="        },	"
var189	="        {	"
var190	="          'type': 0,	"
var191	="          'platform': 'skype',	"
var192	="          'speech': '1. Option1'	"
var193	="        },	"
var194	="        {	"
var195	="          'type': 0,	"
var196	="          'platform': 'skype',	"
var197	="          'speech': '2. Option2'	"
var198	="        },	"
var199	="        {	"
var200	="          'type': 0,	"
var201	="          'platform': 'skype',	"
var202	="          'speech': '3. Option3'	"
var203	="        },	"
var204	="        {	"
var205	="          'type': 0,	"
var206	="          'platform': 'skype',	"
var207	="          'speech': '4. Option4'	"
var208	="        },	"
var209	="        {	"
var210	="          'type': 2,	"
var211	="          'platform': 'skype',	"
var212	="          'title': 'Answer Choice',	"
var213	="          'replies': [	"
var214	="            '1',	"
var215	="            '2',	"
var216	="            '3',	"
var217	="            '4'	"
var218	="          ]	"
var219	="        }	"
var220	="      ]	"
var221	="    }	"
speech = var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44 + var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100 + var101 + var102 + var103 + var104 + var105 + var106 + var107 + var108 + var109 + var110 + var111 + var112 + var113 + var114 + var115 + var116 + var117 + var118 + var119 + var120 + var121 + var122 + var123 + var124 + var125 + var126 + var127 + var128 + var129 + var130 + var131 + var132 + var133 + var134 + var135 + var136 + var137 + var138 + var139 + var140 + var141 + var142 + var143 + var144 + var145 + var146 + var147 + var148 + var149 + var150 + var151 + var152 + var153 + var154 + var155 + var156 + var157 + var158 + var159 + var160 + var161 + var162 + var163 + var164 + var165 + var166 + var167 + var168 + var169 + var170 + var171 + var172 + var173 + var174 + var175 + var176 + var177 + var178 + var179 + var180 + var181 + var182 + var183 + var184 + var185 + var186 + var187 + var188 + var189 + var190 + var191 + var192 + var193 + var194 + var195 + var196 + var197 + var198 + var199 + var200 + var201 + var202 + var203 + var204 + var205 + var206 + var207 + var208 + var209 + var210 + var211 + var212 + var213 + var214 + var215 + var216 + var217 + var218 + var219 + var220 + var221

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
