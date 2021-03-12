# -*- coding: utf-8 -*-

import pickle
import jsonschema
from datetime import datetime
from jsonschema import validate
from flask_migrate import Migrate
from flask import Flask, request, jsonify

from models import db, Song, Podcast, Audiobook
from utils import song_schema, podcast_schema, audiobook_schema
from utils import podcast_result_to_json, audiobook_result_to_json, song_result_to_json

# load pickle file to get database info
with open("database_info", "rb") as f:
    database_info = pickle.load(f)

username = database_info["username"]
password = database_info["password"]
host = database_info["host"]
port = database_info["port"]
db_name = database_info["db_name"]
Audio_File_Types = ["Song", "Podcast", "Audiobook"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


"""
query: It will get the audioTypeFile information based on given Type(localhost/Song) or Type and Id(/Song/5001)
"""
@app.route('/<audiotype>/<ID>/', methods = ["GET"])
@app.route('/<audiotype>', methods = ["GET"])
def query(audiotype, ID=None):
    output = []
    try:
        if audiotype == "Song":
            if ID is not None:
                user = Song.query.filter_by(ID=ID).first_or_404()
                output.append(song_result_to_json(user))
            else:
                users = Song.query.all()
                for user in users:
                    output.append(song_result_to_json(user))
            return jsonify(f"Result: {output}")
        elif audiotype == "Audiobook":
            if ID is not None:
                user = Audiobook.query.filter_by(ID=ID).first_or_404()
                output.append(audiobook_result_to_json(user))
            else:
                users = Audiobook.query.all()
                for user in users:
                    output.append(audiobook_result_to_json(user))
            return jsonify(f"Result: {output}")
        elif audiotype == "Podcast":
            if ID is not None:
                user = Podcast.query.filter_by(ID=ID).first_or_404()
                output.append(podcast_result_to_json(user))
            else:
                users = Podcast.query.all()
                for user in users:
                    output.append(podcast_result_to_json(user))
            return jsonify(f"Result: {output}")
        else:
            return "Not found....."
    except Exception as e:
        return jsonify({"message": f"{e}"}), 400


"""
Create: insert records to specified audio type: Song(/create)
"""
@app.route('/create', methods = ["POST"])
def create():
    db.create_all()
    json_data = request.get_json()
    audio_file_type = json_data.get("audioFileType", None)
    audio_file_info = json_data.get("audioFileInfo", None)
    
    assert audio_file_type != None, "audioFileType is a required field"
    assert audio_file_type in Audio_File_Types, "audioFileType value is not supported"

    try:
        if audio_file_type == "Song":
            validate(instance=audio_file_info, schema=song_schema)
            db.session.add(Song(audio_file_info))
            db.session.commit()
        elif audio_file_type == "Podcast":
            validate(instance=audio_file_info, schema=podcast_schema)
            db.session.add(Podcast(audio_file_info))
            db.session.commit()
        else:
            validate(instance=audio_file_info, schema=audiobook_schema)
            db.session.add(Audiobook(audio_file_info))
            db.session.commit()
        return jsonify({"message": "successfully inserted data"}), 200
    except jsonschema.exceptions.ValidationError as e:
        return jsonify({"message": f"Invalid json: {e}"}), 400
    except Exception as e:
        return jsonify({"message": f"{e}"}), 400


"""
delete: delete record of specified audio file and with respect to id
"""
@app.route('/<audio_type>/<ID>/', methods=["DELETE"])
def delete(audio_type, ID):
    try:
        if audio_type == "Song":
            info = Song.query.filter_by(ID=ID).first_or_404()
            db.session.delete(info)
            db.session.commit()
        elif audio_type == "Podcast":
            info = Podcast.query.filter_by(ID=ID).first_or_404()
            db.session.delete(info)
            db.session.commit()
        elif audio_type == "Audiobook":
            info = Audiobook.query.filter_by(ID=ID).first_or_404()
            db.session.delete(info)
            db.session.commit()
        else:
            raise "Invalid operation"
        return jsonify({"message": "deleted sucessfully"}), 200
    except Exception as e:
        return jsonify({"message": f"{e}"}), 400


"""
update: update specified audio type file with respect to id and with provided info
"""
@app.route('/<audio_type>/<ID>/', methods=["PUT"])
def update(audio_type, ID):
    try:
        json_data = request.get_json()
        audio_file_info = json_data.get("audioFileInfo", None)
        if audio_type == "Song":
            validate(instance=audio_file_info, schema=song_schema)
            info = db.session.query(Song).filter_by(ID=ID)
            info.update(dict(ID = audio_file_info["id"], Name = audio_file_info["name"], 
                             Duration = audio_file_info["duration"], Uploaded = datetime.fromisoformat(audio_file_info["uploaded"])))
            db.session.commit()
        elif audio_type == "Podcast":
            info = Podcast.query.filter_by(ID=ID)
            info.update(dict(ID = audio_file_info["id"], Name = audio_file_info["name"], 
                             Duration = audio_file_info["duration"], Uploaded = datetime.fromisoformat(audio_file_info["uploaded"]),
                             Host = audio_file_info["host"], Participants = audio_file_info["participants"]))
            db.session.commit()
        elif audio_type == "Audiobook":
            info = Audiobook.query.filter_by(ID=ID)
            info.update(dict(ID = audio_file_info["id"], Title = audio_file_info["title"], 
                             Duration = audio_file_info["duration"], Uploaded = datetime.fromisoformat(audio_file_info["uploaded"]),
                             Author = audio_file_info["author"], Narrator = audio_file_info["narrator"]))
            db.session.commit()
        else:
            raise "Invalid operation"
        return jsonify({"message": "updated sucessfully"}), 200
    except Exception as e:
        return jsonify({"message": f"{e}"}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)