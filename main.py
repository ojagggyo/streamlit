#import streamlit as st
# #st.write("Good morning")
# #st.write("Hello!")

# import urllib.request
# #with urllib.request.urlopen('https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv') as u:
# with urllib.request.urlopen('https://api.upbit.com/v1/ticker?markets=KRW-STEEM') as u:
#     st.write(u.info())
#     s = u.read()
#     st.write(s)
 #st.write("<br>".join(s.decode('utf-8').split('\r\n')))


#st.write(os.getcwd())

#f = open('data.csv', 'r', encoding='UTF-8')
#data = f.read()
#st.write(data)
#f.close()

#st.write("callback( { \"name\" : \"Fukumori\" } )");


 
#出力
#print ("Content-Type:text/javascript")
#print ("Content-type: application/x-javascript")
#print ()
#print ("callback({'name':'abc'});")

# import requests
# import json

# #print ("Content-Type:text/javascript")
# print ("Content-Type:application/javascript")
# print ("")
# print ("callback({\"name\":\"This is JSONP\"});")

# data = {
#             'name': 'shobon',
#             'url': 'shobon.com'
#         }

# #print ('Content-Type: application/json')
# print ('Content-Type: application/javascript')
# #print ('%s(%s)' % ('callback', json.dumps(data, ensure_ascii=False)) )
# print ("callback({\"name\":\"This is JSONP\"});")

from flask import Flask, jsonify, make_response, request
import json

api = Flask(__name__)

@api.route('/user', methods=['POST'])
def post_user_():
  data = json.loads(request.data)
  result = {
    'name' : data.get('name'),
    'age'  : data.get('age'),
    'sex'  : data.get('sex')
    }
  return make_response(jsonify(result)) 


if __name__ == '__main__': 
  api.run(host = '0.0.0.0', port = 80) 
