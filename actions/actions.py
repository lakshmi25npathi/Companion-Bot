
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from datetime import datetime
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted, ReminderScheduled, ReminderScheduled, SlotSet

# Case 1 – Activity Recommendation
################################################################################################################################################

# Outdoor activities list
class ActionOutdoorActivities(Action):

    def name(self):
        return "action_OutdoorActivities"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_outdoor_activities")

         return []

# Local hikes list
class ActionLocalHikes(Action):

    def name(self):
        return "action_LocalHikes"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_local_hikes_list")

         return []

# Easy hikes list
class ActionEasyHikes(Action):

    def name(self):
        return "action_EasyHikes"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_recommend_hike_type_easy")

         return []

# tough hikes list
class ActionToughHikes(Action):

    def name(self):
        return "action_ToughHikes"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_recommend_hike_type_tough")

         return []

# Rock climbing places list
class ActionRockClimbing(Action):

    def name(self):
        return "action_RockClimbing"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_recommend_outdoor_activities_rock_climbing")

         return []


# Camping places list
class ActionCamping(Action):

    def name(self):
        return "action_Camping"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_recommend_outdoor_activities_camping")

         return []

# Fishing places list
class ActionFishing(Action):

    def name(self):
        return "action_Fishing"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_recommend_outdoor_activities_fishing")

         return []

# Rafting places list
class ActionRafting(Action):

    def name(self):
        return "action_Rafting"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_recommend_outdoor_activities_rafting")

         return []

# Indoor activities list
class ActionIndoorActivities(Action):

    def name(self):
        return "action_IndoorActivities"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_recommend_indoor_activities")

         return []

# Watch movie
class ActionWatchMovie(Action):

    def name(self):
        return "action_WatchMovie"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_indoor_activities_watch_movie")

         return []

# Do Cooking 
class ActionCooking(Action):

    def name(self):
        return "action_Cooking"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_indoor_activities_cooking")

         return []

# Do Yoga 
class ActionYoga(Action):

    def name(self):
        return "action_Yoga"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_indoor_activities_yoga")

         return []

# Start a Garden
class ActionStartGarden(Action):

    def name(self):
        return "action_StartGarden"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_indoor_activities_start_garden")

         return []

# Read a book
class ActionReadBook(Action):

    def name(self):
        return "action_ReadBook"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_indoor_activities_read_book")

         return []

# Other Indoor activities list
class ActionOtherIndoorActivities(Action):

    def name(self):
        return "action_OtherIndoorActivities"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_recommend_other_indoor_activities")

         return []


# Case 2 – Self-Improvement Journey (Goal setting)
####################################################################################################

# List of parks
class ActionParksList(Action):

    def name(self):
        return "action_ParksList"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_fitness_goal")

         return []

# List of Golf Ranges
class ActionGolfRanges(Action):

    def name(self):
        return "action_GolfRanges"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_golf_ranges_list")

         return []

# List of Golf Swings Videos
class ActionGolfSwingsV(Action):

    def name(self):
        return "action_GolfSwingsV"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_deny_golf_range")

         return []

# list of daily goals
class ActionDailyGoals(Action):

    def name(self):
        return "action_DailyGoals"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_daily_goals")

         return []

# list of saved goals recommend videos
class ActionSavedGoals(Action):

    def name(self):
        return "action_SavedGoals"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_select_saved_goals")

         return []

# list of videos for eating habits
class ActionEatingHabits(Action):

    def name(self):
        return "action_EatingHabits"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_goal_setting_improve_goal_eating_habits")

         return []

# list of videos for Mindfulness
class ActionMindfulness(Action):

    def name(self):
        return "action_Mindfulness"

    def run(self, dispatcher, tracker, domain):
        
         dispatcher.utter_message(template="utter_goal_setting_improve_goal_mindfulness")

         return []


class ActionRestarted(Action):

    def name(self):
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]


