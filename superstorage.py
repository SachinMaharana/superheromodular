import os.path
import json
# DejaVu Sans Mono

def set_superheros(superheros):
	global _superheros
	_superheros = superheros

def superheros():
	global _superheros
	return _superheros

def set_locations(locations):
	global _locations
	_locations = locations

def locations():
	global _locations
	return _locations

def items():
	global _items
	return _items

def add_superhero(name, location):
	global _items
	# print(type(_items))
	_items.append((name, location))
	_save_items()

def remove_superhero(name, location):
	global _items
	for i in range(len(_items)):
		nam, loc = _items[i]
		if nam == name and loc == location:
			del _items[i]
			_save_items()
			return True
	return False

def init():
	_load_items()

def _load_items():
	global _items
	if os.path.exists("superhero.json"):
		f = open("superhero.json","r")
		_items = json.loads(f.read())
		# print(_items)
		f.close()
	else:
		_items = []


def _save_items():
	global _items
	f = open("superhero.json","w")
	f.write(json.dumps(_items))
	f.close()

init()
# # remove_superhero("Joker","Circus")
add_superhero("Joker","Circus")