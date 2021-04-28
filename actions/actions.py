# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#import custom_actions as ca

import os
import webbrowser
from pynput.keyboard import Key,Controller
import time
import wikipedia

### RECORD OF SITES AND THEIR LINKS ###
site_links = {
    "google" : "https://www.google.com",
    "wikipedia" : "www.wikipedia.org",
    "youtube" : "www.youtube.com",
}

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


### ACTION TO OPEN BROWSER ###
class ActionOpenSites(Action):

    def name(self) -> Text:
        return "action_open_sites"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            entity = tracker.latest_message['entities'] #gets entities

            print(entity)

            for e in entity:
                print(f"Entity: {e['entity']} Value: {e['value']}")

                site = e['value']

            if site in site_links:
                dispatcher.utter_message(text="Opening Site...")
                webbrowser.open(site_links[site])
            else:
                dispatcher.utter_message(text="I'm sorry I couldn't find the exact site, here's what I found in the internet")
                webbrowser.open(f"https://www.google.com/search?q={site}")
        
        except:
            dispatcher.utter_message(text=f"There was an error while extracting entity")

        return []

### ACTION TO CHANGE VOLUME ###
class ActionChangeVolume(Action):

    def name(self) -> Text:
        return "action_increase_volume"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity = tracker.latest_message['entities']

        print(entity)

        try:
            for e in entity:
                print(f"Entity: {e['entity']} Value: {e['value']}")

                mode = e['value']
            
            keyboard = Controller()

            if mode in ['increase','up']:
                for i in range(10):
                    keyboard.press(Key.media_volume_up)
                    keyboard.release(Key.media_volume_up)
                    time.sleep(0.1)
            else:
                for i in range(10):
                    keyboard.press(Key.media_volume_down)
                    keyboard.release(Key.media_volume_down)
                    time.sleep(0.1)

            dispatcher.utter_message(text="Changing Volume...")

        except:
            dispatcher.utter_message(text=f"There was an error while extracting entity")

        return []

### ACTION TO ASK WIKI ###
class ActionQueryInfo(Action):

    def name(self) -> Text:
        return "action_query_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity = tracker.latest_message['entities']

        print(entity)

        
        for e in entity:
            print(f"Entity: {e['entity']} Value: {e['value']}")

            topic = e['value']
            
        topic = "_".join(topic.split())
        print(topic)
        
        try:
            result = wikipedia.summary(topic,2)
            dispatcher.utter_message(text=f"According to Wikipedia, {result}")
            
        except:
            dispatcher.utter_message(text=f"I'm sorry, I couldn't get any info")

        return []