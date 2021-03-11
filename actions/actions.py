

 from typing import Any, Text, Dict, List

 from rasa_sdk import Action, Tracker
 from rasa_sdk.executor import CollectingDispatcher

# Outdoor activities list
 class ActionOutdoorActivities(Action):

     def name(self):
         return "action_OutdoorActivities"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_outdoor_activities")

         return []


# Indoor activities list
 class ActionIndoorActivities(Action):

     def name(self):
         return "action_IndoorActivities"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_indoor_activities")

         return []


# Local hikes list
 class ActionLocalHikes(Action):

     def name(self):
         return "action_LocalHikes"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_local_hikes")

         return []