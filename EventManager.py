import time

class EventManager():
	"""
		docstring for EventManager
	"""
	def __init__(self):
		self.event_list = []

	def add(self, event: str):
		# Добавляет новый эвент
		self.event_list.append(event)

	def delete(self, event: str):
		# Удаляет эвент из списка
		for event_item in self.event_list:
			if event_item == event:
				self.event_list.remove(event)

	def get(self):
		# Возвращает список эвентов
		return self.event_list

	def clear(self):
		# Для отчистки листа
		self.event_list = []

	def contrast(self, other_list: list):
		# Для выявлений отличий
		result = []
		for other_event in other_list:
			if other_event not in self.event_list:
				result.append(other_event)

		return result
