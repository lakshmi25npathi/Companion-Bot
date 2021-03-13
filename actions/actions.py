

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Case 1 – Activity Recommendation
################################################################################################################################################

# Outdoor activities list
class ActionOutdoorActivities(Action):

    def name(self):
        return "action_OutdoorActivities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_outdoor_activities")

         return []

# Local hikes list
class ActionLocalHikes(Action):

    def name(self):
        return "action_LocalHikes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_local_hikes_list")

         return []

# Easy hikes list
class ActionEasyHikes(Action):

    def name(self):
        return "action_EasyHikes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_recommend_easy_hike")

         return []

# Indoor activities list
class ActionIndoorActivities(Action):

    def name(self):
        return "action_IndoorActivities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_recommend_indoor_activities")

         return []

# Other activities other than hike list
class ActionOtherActivities(Action):

    def name(self):
        return "action_OtherActivities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_recommend_other_activities")

         return []


# Case 2 – Self-Improvement Journey (Goal setting)
#################################################################################################################################################