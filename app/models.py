# -*- coding: utf-8 -*-
import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Song(db.Model):
    __tablename__ = 'Song'

    ID = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(100))
    Duration = db.Column(db.Integer())
    Uploaded = db.Column(db.DateTime)
    
    def __init__(self, audio_info):
        self.ID = audio_info["id"]
        self.Name = audio_info["name"]
        self.Duration = audio_info["duration"]
        self.Uploaded = datetime.datetime.fromisoformat(audio_info["uploaded"])
        assert datetime.datetime.now() < self.Uploaded, "datetime shouldn't be past"


class Podcast(db.Model):
    __tablename__ = "Podcast"
    
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Duration = db.Column(db.Integer)
    Uploaded = db.Column(db.DateTime)
    Host = db.Column(db.String(100))
    Participants = db.Column(db.ARRAY(db.String()))
    
    def __init__(self, audio_info):
        self.ID = audio_info["id"]
        self.Name = audio_info["name"]
        self.Duration = audio_info["duration"]
        self.Uploaded = datetime.datetime.fromisoformat(audio_info["uploaded"])
        self.Host = audio_info["host"]
        self.Participants = audio_info["participants"]
        assert datetime.datetime.now() < self.Uploaded, "datetime shouldn't be past"


class Audiobook(db.Model):
    __tablename__ = "Audiobooks"

    ID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Author = db.Column(db.String(100))
    Narrator = db.Column(db.String(100))
    Duration =  db.Column(db.Integer)
    Uploaded = db.Column(db.DateTime)

    def __init__(self, audio_info):
        self.ID = audio_info["id"]
        self.Title = audio_info["title"]
        self.Author = audio_info["author"]
        self.Narrator = audio_info["narrator"]
        self.Duration = audio_info["duration"]
        self.Uploaded = datetime.datetime.fromisoformat(audio_info["uploaded"])
        assert datetime.datetime.now() < self.Uploaded, "datetime shouldn't be past"