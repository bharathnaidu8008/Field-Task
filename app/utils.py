# -*- coding: utf-8 -*-
# song metadata validation
song_schema = {
   'type': 'object',
   'properties': {
       'id': {
           'type': 'integer',
       },
       'name': {
           'type': 'string',
           'maxLength' : 100,
       },
      'duration': {
           'type': 'integer',
           'minimum': 1,
       },
      'uploaded': {
           'type': 'string',
           "format": "date-time",
       },
   },
   'required': ['id', 'name', 'duration', 'uploaded']
}


# podcast metadata validation
podcast_schema = {
   'type': 'object',
   'properties': {
       'id': {
           'type': 'integer',
       },
       'name': {
           'type': 'string',
           'maxLength' : 100,
       },
      'duration': {
           'type': 'integer',
           'minimum': 1,
       },
      'uploaded': {
           'type': 'string',
           "format": "date-time",
       },
      'host': {
           'type': 'string',
           'maxLength' : 100,
       },
      'Participants': {
           'type': 'array',
           'maxLength' : 10,
           'contains': { 
               "type": "number",
               'maxLength': 100,
               }
       },
   },
   'required': ['id', 'name', 'duration', 'uploaded', 'host']
}

# audiobook schema
audiobook_schema = {
   'type': 'object',
   'properties': {
       'id': {
           'type': 'integer',
       },
       'title': {
           'type': 'string',
           'maxLength' : 100,
       },
      'author': {
           'type': 'string',
           'maxLength' : 100,
       },
      'narrator': {
           'type': 'string',
           'maxLength' : 100,
       },
      'duration': {
           'type': 'integer',
           'minimum': 1,
       },
      'uploaded': {
           'type': 'string',
           "format": "date-time",
       },
   },
   'required': ['id', 'title', 'author', 'narrator', 'duration', 'uploaded']
}

def song_result_to_json(result):
    json_result = {}
    json_result["ID"] = result.ID
    json_result["Name"] = result.Name
    json_result["Duration"] = result.Duration
    json_result["Uploaded"] = result.Uploaded.strftime("%m-%d-%Y, %H:%M:%S")
    return json_result

def podcast_result_to_json(result):
    json_result = {}
    json_result["ID"] = result.ID
    json_result["Name"] = result.Name
    json_result["Duration"] = result.Duration
    json_result["Host"] = result.Host
    json_result["Participants"] = result.Participants
    json_result["Uploaded"] = result.Uploaded.strftime("%m-%d-%Y, %H:%M:%S")
    return json_result

def audiobook_result_to_json(result):
    json_result = {}
    json_result["ID"] = result.ID 
    json_result["Title"] = result.Author
    json_result["Author"] = result.Author
    json_result["Narrator"] = result.Author
    json_result["Duration"] = result.Duration
    json_result["Uploaded"] = result.Uploaded.strftime("%m-%d-%Y, %H:%M:%S")
    return json_result