# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType
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
      return {"module": None}
    dispatcher.utter_message(text=f"OK! You want to approve in {slot_value} module.")
    return {"module": slot_value}
  
class ActionSubmitApprovalForm(Action):
  def name(self) -> Text:
    return "action-submit-approval-form"
  
  def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: DomainDict,) -> List[Dict[Text, Any]]:
    module = next(tracker.get_latest_entity_values("module"), None)
    ref_number = next(tracker.get_latest_entity_values("ref_number"), None)

    # if module is None:
    #   dispatcher.utter_message(text="Module is Invalid, Retry")
    # if module == ""

    msg = f"Approval Request Sent of module {module} with reference number {ref_number}."
    dispatcher.utter_message(text=msg)

    return []

