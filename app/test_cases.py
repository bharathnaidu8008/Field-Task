# -*- coding: utf-8 -*-

import requests
import json
"""
This script test create, update, delete operation on Song, Podcast, Audiobook
"""
class AppTest:
    
    def __init__(self):
        self.__base_URL = "http://127.0.0.1:5000/"
        self.__headers = { 'Content-Type': 'application/json' }
    
    def create(self, payload):
        __create_URL = self.__base_URL + "create"
        response = requests.request("POST", __create_URL, headers=self.__headers, data=json.dumps(payload))
        return response.text

    def get(self, audio_type, id_=None):
        if id_:
            __get_url = self.__base_URL + audio_type + "/" + str(id_) + "/"
        else:
            __get_url = self.__base_URL + audio_type 
        response = requests.request("GET", __get_url, headers=self.__headers)
        return response.text
    
    def update(self, audio_type, id_, payload):
        if id_:
            __get_url = self.__base_URL + audio_type + "/" + str(id_) + "/"
        else:
            __get_url = self.__base_URL + audio_type 
        response = requests.request("PUT", __get_url, headers=self.__headers, data=json.dumps(payload))
        return response.text
    
    def delete(self, audio_type, id_):
        if id_:
            __get_url = self.__base_URL + audio_type + "/" + str(id_) + "/"
        else:
            __get_url = self.__base_URL + audio_type 
        response = requests.request("DELETE", __get_url, headers=self.__headers)
        return response.text


app_test = AppTest();
#----------------------------------------------Song creation----------------------------------------
payload = {
            "audioFileType" : "Song",
            "audioFileInfo" : {"id": 5132422,
                               "name": "Party rocks",
                               "duration": 450,
                               "uploaded": "2021-03-11 13:55:26"}}
# Testcase1 
print(app_test.create(payload))
# Output: {"message":"datetime shouldn't be past"}

payload = {
            "audioFileType" : "Song",
            "audioFileInfo" : {"id": 5132422,
                               "name": "Party rocks",
                               "duration": 450,
                               "uploaded": "2021-03-11 13:55:26"}}
# Testcase2
print(app_test.create(payload))
# Output:{"message":"successfully inserted data"}

payload = {
            "audioFileType" : "Song",
            "audioFileInfo" : {"id": 513222,
                               "name": "rocky rocks",
                               "duration": 450,
                               "uploaded": "2021-03-21 13:55:26"}}
# Testcase3
print(app_test.create(payload))
# Output:{"message":"successfully inserted data"}


#.............................................Song get-----------------------------------------------
# Testcase1
print(app_test.get("Song"))
# output: """Result: [{'ID': 50001, 'Name': 'rocks the party', 'Duration': 456, 'Uploaded': '03-14-2021, 13:55:26'}, {'ID': 50002, 'Name': 'rocks the party', 'Duration': 456, 'Uploaded': '03-14-2021, 13:55:26'}, {'ID': 50003, 'Name': 'rocks the party That\u2019s great, it starts with an earthquake, birds and snakes\u2026', 'Duration': 456, 'Uploaded': '03-14-2021, 13:55:26'}, {'ID': 5132422, 'Name': 'Party rocks', 'Duration': 450, 'Uploaded': '03-21-2021, 13:55:26'}, {'ID': 513222, 'Name': 'rocky rocks', 'Duration': 450, 'Uploaded': '03-21-2021, 13:55:26'}]"""

# Testcase2
print(app_test.get("Song", 50001))
# "Result: [{'ID': 50001, 'Name': 'rocks the party', 'Duration': 456, 'Uploaded': '03-14-2021, 13:55:26'}]"

#.............................................Song delete-----------------------------------------------
# Testcase1
print(app_test.delete("Song", 50001))
# output: {"message":"deleted sucessfully"}


#.............................................Song update.................................................
payload = {
    "audioFileInfo" : {"id": 50001,
    "name": "Uppena Songs",
    "duration": 300,
    "uploaded": "2021-03-11 13:55:26"}
}
# Testcase1
print(app_test.update("Song", 50001, payload))
# output: {"message":"updated sucessfully"}

#--------------------------------------------Audiobook create-------------------------------------------
payload = {
    "audioFileType" : "Audiobook",
    "audioFileInfo" : {"id": 600,
    "title": "bharath ani nenu",
    "author": "bharath naidu dabbra",
    "narrator": "bharath",
    "duration": 11,
    "uploaded": "2021-03-15 13:55:26"}
}
print(app_test.create(payload))
# Output:{"message":"successfully inserted data"}

#...........................................Audiobook update----------------------------------------------
payload = {
    "audioFileInfo" : {"id": 600,
    "title": "bharath ani nenu",
    "author": "bharath naidu dabbra",
    "narrator": "bharath",
    "duration": 11,
    "uploaded": "2021-03-15 13:55:26"}
}
print(app_test.update("Audiobook", 600, payload))
# Output:{"message":"successfully inserted data"}

#...........................................Audiobook delete........................................
# Testcase1
print(app_test.delete("Audiobook", 600))
# output: {"message":"deleted sucessfully"}

#.............................................Audiobook get-----------------------------------------------
# Testcase1
print(app_test.get("Audiobook"))
# Result: [{'ID': 510, 'Title': 'bharath naidu dabbra', 'Author': 'bharath naidu dabbra', 'Narrator': 'bharath naidu dabbra', 'Duration': 300, 'Uploaded': '03-15-2021, 13:55:26'}, {'ID': 511, 'Title': 'bharath naidu dabbra', 'Author': 'bharath naidu dabbra', 'Narrator': 'bharath naidu dabbra', 'Duration': 11, 'Uploaded': '03-15-2021, 13:55:26'}]"

# Testcase2
print(app_test.get("Audiobook", 510))
# "Result: [{'ID': 510, 'Title': 'bharath naidu dabbra', 'Author': 'bharath naidu dabbra', 'Narrator': 'bharath naidu dabbra', 'Duration': 300, 'Uploaded': '03-15-2021, 13:55:26'}]"