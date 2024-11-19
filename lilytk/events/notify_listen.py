'''
Copyright (C) 2024-2024 Lilith Cybi - All Rights Reserved.
You may use, distribute and modify this code under the
terms of the MIT license.

You should have received a copy of the MIT license with
this file. If not, please write to: lilith.cybi@syrency.com, 
or visit: https://github.com/jmeaster30/lilytk/LICENSE
'''

from typing import Any, Callable
from lilytk.utils.singleton import Singleton


def Notifies(event_name):
  def NotifyDecorator(func):
    def wrapper(*args, **kwargs):
      NotifyListenerManager().notify(event_name, func(*args, **kwargs))
    return wrapper
  return NotifyDecorator

def Listens(event_name):
  def ListensDecorator(func):
    NotifyListenerManager().register(event_name, func)
    def wrapper(*args, **kwargs):
      return func(*args, **kwargs)
    return wrapper
  return ListensDecorator

@Singleton
class NotifyListenerManager:
  def __init__(self):
    self.events_to_listeners: dict[str, list[Callable[[Any], None]]] = {}
  
  def notify(self, event_name: str, data: Any):
    if event_name in self.events_to_listeners:
      for listener in self.events_to_listeners[event_name]:
        listener(data)

  def register(self, event_name: str, listener: Callable[[Any], None]):
    if event_name not in self.events_to_listeners:
      self.events_to_listeners[event_name] = [listener]
    elif event_name in self.events_to_listeners and listener not in self.events_to_listeners[event_name]:
      self.events_to_listeners[event_name].append(listener)
