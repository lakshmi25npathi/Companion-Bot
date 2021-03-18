

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
####################################################################################################

# List of parks
class ActionParksList(Action):

    def name(self):
        return "action_ParksList"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_fitness_goal")

         return []

# List of Golf Ranges
class ActionGolfRanges(Action):

    def name(self):
        return "action_GolfRanges"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_golf_ranges_list")

         return []

# List of Golf Swings Videos
class ActionGolfSwingsV(Action):

    def name(self):
        return "action_GolfSwingsV"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_deny_golf_range")

         return []

# list of daily goals
class ActionDailyGoals(Action):

    def name(self):
        return "action_DailyGoals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_daily_goals")

         return []

# list of saved goals recommend videos
class ActionSavedGoals(Action):

    def name(self):
        return "action_SavedGoals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        
         dispatcher.utter_message(template="utter_select_saved_goals")

         return []
