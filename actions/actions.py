# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import requests
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

ALLOWED_MODULE = ['purchase requisition', 'purchase order', 'non po invoice']

class ValidateApprovalForm(FormValidationAction):
  def name(self) -> Text:
    return "validate_approval_form"

  def validate_module(
      self,
      slot_value: Any,
      dispatcher: CollectingDispatcher,
      tracker: Tracker,
      domain: DomainDict,
  ) -> Dict[Text, Any]:
    if slot_value.lower() not in ALLOWED_MODULE:
      dispatcher.utter_message(text=f"We only accept purchase requisition, purchase order and non po invoice module.")
      return {"module_name": None}
    dispatcher.utter_message(text=f"OK! You want to approve in {slot_value} module.")
    return {"module_name": slot_value}
  
class ActionSubmitApprovalForm(Action):
  def name(self) -> Text:
    return "action-submit-approval-form"
  
  def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: DomainDict,) -> List[Dict[Text, Any]]:
    currentValues = tracker.current_slot_values()

    module = currentValues["module_name"] if currentValues["module_name"] else None
    ref_number = currentValues["ref_number"] if currentValues["ref_number"] else None

    url = 'http://localhost:5000/api/v1/rasa/test'
    data = {
      "module_name" : module,
      "ref_number" : ref_number,
    }

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(url, json=data, headers=headers)
    dispatcher.utter_message(text=response.json()["message"])


    return [AllSlotsReset()]
  
class ActionSubmitDisapprovalForm(Action):
  def name(self) -> Text:
    return "action-submit-disapproval-form"
  
  def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: DomainDict,) -> List[Dict[Text, Any]]:
    currentValues = tracker.current_slot_values()

    module = currentValues["module_name"] if currentValues["module_name"] else None
    ref_number = currentValues["ref_number"] if currentValues["ref_number"] else None
    comments = currentValues["comments"] if currentValues["comments"] else None

    url = 'http://localhost:5000/api/v1/rasa/test'
    data = {
      "module_name" : module,
      "ref_number" : ref_number,
      "comments": comments,
    }

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(url, json=data, headers=headers)
    dispatcher.utter_message(text=response.json()["message"])


    return [AllSlotsReset()]

class ActionSubmitRejectForm(Action):
  def name(self) -> Text:
    return "action-submit-reject-form"
  
  def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: DomainDict,) -> List[Dict[Text, Any]]:
    currentValues = tracker.current_slot_values()

    module = currentValues["module_name"] if currentValues["module_name"] else None
    ref_number = currentValues["ref_number"] if currentValues["ref_number"] else None
    comments = currentValues["comments"] if currentValues["comments"] else None

    url = 'http://localhost:5000/api/v1/rasa/test'
    data = {
      "module_name" : module,
      "ref_number" : ref_number,
      "comments": comments,
    }

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(url, json=data, headers=headers)
    dispatcher.utter_message(text=response.json()["message"])


    return [AllSlotsReset()]


