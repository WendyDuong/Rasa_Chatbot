# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# import mysql.connector as mysql
import requests
# from database_connectivity import dataupdate
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
# from rasa_sdk.events import EventType
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, FormValidationAction


def dataupdate(student_group, input_activity, input_outside, input_workingtime, input_environment, input_company,
               input_skills,
               input_personally, input_problems_dealing, input_public, min_salary, wish_salary
               ):
    # mydb = mysql.connect(host="localhost",
    #                      user="root",
    #                      passwd="chatbot2020",
    #                      database="chatbot",
    #                      )
    activity = ""
    outside = ""
    workingtime = ""
    environment = ""
    company = ""
    skills = ""
    personally = ""
    problems_dealing = ""
    public = ""

    if int(input_activity) > 2:
        activity += "Abwechslungsreiche Tätigkeit, Herausfordernde Tätigkeit, Aufstiegsmöglichkeiten, " \
                    "Weiterbildungsmöglichkeiten "
    else:
        activity += "NA"
    if int(input_outside) > 2:
        outside += "Kundenkontakt,Dienstreisen, Gute Beziehung zu Vorgesetzten"
    else:
        outside += "NA"
    if int(input_workingtime) > 2:
        workingtime += "Flexible Arbeitszeit, Überstundenkonto, Arbeitszeiterfassung"
    else:
        workingtime += "NA"

    if int(input_environment) > 2:
        environment += "Lockere Arbeitsatmosphäre, Anbindung an öffentliche Verkehrsmittel, Kantine, moderne Büro"
    else:
        environment += "NA"

    if int(input_company) > 2:
        company += "Innovatives Unternehmen, Etabliertes Unternehmen, Start-up"
    else:
        company += "NA"

    if int(input_skills) > 2:
        skills += "Kommunikationsfähigkeit, Organisationsfähigkeit und Teamfähigkeit"
    else:
        skills += "NA"

    if int(input_personally) > 2:
        personally += "Lernbereitschaft, Neugier, Selbstdisziplin und analytisches Denkenvermögen"
    else:
        personally += "NA"

    if int(input_problems_dealing) > 2:
        problems_dealing += "Problemlösungskompetenz, Kritikfähigkeit, Stressresistenz"
    else:
        problems_dealing += "NA"

    if int(input_public) > 2:
        public += "Integrationsbereitschaft, Präsentationsskills und Empathie"
    else:
        public += "NA"

    # mycursor = mydb.cursor()
    # # sql = "CREATE TABLE userinput2 (activity LONGTEXT,outside LONGTEXT,workingtime LONGTEXT,environment " \
    # #       "LONGTEXT,company LONGTEXT,skills LONGTEXT,personally LONGTEXT,problems_dealing VARCHAR(" \
    # #       "255),public LONGTEXT,min_salary VARCHAR(255),wish_salary VARCHAR(255)); "
    #
    # # sql = "CREATE TABLE userinput(student_group VARCHAR(255), activity LONGTEXT, outside LONGTEXT, workingtime
    # # LONGTEXT, environment LONGTEXT, company LONGTEXT, skills LONGTEXT, personally LONGTEXT, problems_dealing
    # # VARCHAR(255), public LONGTEXT, min_salary VARCHAR(255), wish_salary VARCHAR(255)); "
    #
    # sql = 'INSERT INTO userinput (student_group, activity, outside, workingtime, environment, company, skills, ' \
    #       'personally,problems_dealing, public, min_salary, wish_salary) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}",' \
    #       '"{6}","{7}","{8}","{9}","{10}","{11}");'.format(
    #     student_group, activity, outside, workingtime, environment, company, skills, personally, problems_dealing,
    #     public, min_salary, wish_salary)
    # mycursor.execute(sql)
    # mydb.commit()
    # print(mycursor.rowcount, "user input inserted!")


class FormInfo(Action):

    def name(self) -> Text:
        return "validate_form_info"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: "DomainDict") -> List[
        Dict[Text, Any]]:
        required_slot = ["1_activity", "2_outside", "3_workingtime", "4_environment", "5_company", "6_skills",
                         "7_personally",
                         "8_problems_dealing", "9_public",
                         "10_min_salary", "11_wish_salary"]

        for slot_name in required_slot:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill the slot next
                return [SlotSet("required_slot", slot_name)]

        # All slots are filled
        return [SlotSet("required_slot", None)]


class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dataupdate(tracker.get_slot("student_group"), tracker.get_slot("1_activity"), tracker.get_slot("2_outside"),
                   tracker.get_slot("3_workingtime"),
                   tracker.get_slot("4_environment"), tracker.get_slot("5_company"), tracker.get_slot("6_skills"),
                   tracker.get_slot("7_personally"), tracker.get_slot("8_problems_dealing"),
                   tracker.get_slot("9_public"),
                   tracker.get_slot("10_min_salary"),
                   tracker.get_slot("11_wish_salary"))
        dispatcher.utter_message(template="utter_slots_values", activity=tracker.get_slot("1_activity"),
                                 outside=tracker.get_slot("2_outside"), workingtime=tracker.get_slot("3_workingtime"),
                                 environment=tracker.get_slot("4_environment"), company=tracker.get_slot("5_company"),
                                 skills=tracker.get_slot("6_skills"),
                                 personally=tracker.get_slot("7_personally"),
                                 problems_dealing=tracker.get_slot("8_problems_dealing"),
                                 public=tracker.get_slot("9_public"),
                                 min_salary=tracker.get_slot("10_min_salary"),
                                 wish_salary=tracker.get_slot("11_wish_salary"))
        return []

