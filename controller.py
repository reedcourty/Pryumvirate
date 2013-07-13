#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json

from PySide import QtGui, QtCore

from plurk_oauth.PlurkAPI import PlurkAPI
import tweepy

class Controller:
    twitter = None
    plurk = None
    gui = None
    
    def __init__(self):
        self.gui = None
        
    def init_services(self):
        self.twitter = self.init_twitter()
        self.plurk = self.init_plurk()
    
    def init_plurk(self):
        try:
            keys = open('plurk_api.keys', 'r+')
            data = json.load(keys)
            plurk = PlurkAPI(data["CONSUMER_KEY"], data["CONSUMER_SECRET"])
            plurk.authorize(data["ACCESS_TOKEN"],data["ACCESS_TOKEN_SECRET"])
            return plurk
        except Exception as e:
            print("Valami error van a plurk loginnál :S")
            print(e)
            self.gui.plainTextEdit_output.appendPlainText(u"Valami error van a plurk loginnál :S")
    
    def init_twitter(self):
        try:
            keys = open('twitter_api.keys', 'r+')
            data = json.load(keys)

            auth = tweepy.OAuthHandler(data["CONSUMER_KEY"], data["CONSUMER_SECRET"])
            auth.set_access_token(data["ACCESS_KEY"], data["ACCESS_SECRET"])

            twitter = tweepy.API(auth)
            return twitter
        except Exception as e:
            print("Valami error van a twitter loginnál :S")
            print(e)
            self.gui.plainTextEdit_output.appendPlainText(u"Valami error van a twitter loginnál :S")
            
    def send(self, post):
        if (self.gui.checkBox_twitter.isChecked()):
            try:
                status_twitter = self.twitter.update_status(str(post))
                print(status_twitter)
                self.gui.plainTextEdit_output.appendPlainText(u"Twitter: {}\n".format(status_twitter.text))
                last_twit = self.twitter.user_timeline(id="reedcourty",count=1)
                last_twit_str = u"Utolsó tweet: {} ({}, forrás: {})".format(last_twit[0].text, str(last_twit[0].created_at), last_twit[0].source)
                self.gui.plainTextEdit_output.appendPlainText(last_twit_str)
            except Exception as e:
                print(e)
                self.gui.plainTextEdit_output.appendPlainText(u"Twitter: {}".format(e.message[0]['message']))
                
        if (self.gui.checkBox_plurk.isChecked()):
            try:
                status_plurk = self.plurk.callAPI('/APP/Timeline/plurkAdd', {'content': str(post), 'qualifier': ':' })
                print(status_plurk['content'])
                self.gui.plainTextEdit_output.appendPlainText(u"Plurk: {}\n".format(status_plurk['content']))
            except Exception as e:
                print(e)
                self.gui.plainTextEdit_output.appendPlainText(u"Plurk: {}\n".format(e.message[0]['message']))
            