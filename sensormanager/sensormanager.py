import json

from bierprototype_support import bierprototype_support


class Sensormanager(object):

    def __init__(self):
        self.current_state = self.load_current_state()

        print("Sensorinit done")

    def count_pulse(self):
        self.current_state["impulse_seit_reset"] += 1
        self.current_state["gesamtimpulse"] += 1
        self.current_state["inhalt"] -= 1 / 12500
        self.current_state["gesamtverbrauch"] += 1 / 12500

        #print("Gesamtverbrauch   : " + str(self.current_state["gesamtverbrauch"]))
        #print("Gesamtimpulse     : " + str(self.current_state["gesamtimpulse"]))
        #print("Inhalt            : " + str(self.current_state["inhalt"]))
        #print("Impulse seit reset: " + str(self.current_state["impulse_seit_reset"]))
        self.save_current_state()
        bierprototype_support.refresh()

    @staticmethod
    def load_current_state():
        with open("/home/resi/PycharmProjects/Bierzaehler/save.json", "r") as read_file:
            current_state = json.load(read_file)
        return current_state

    def save_current_state(self):
        with open("/home/resi/PycharmProjects/Bierzaehler/save.json", "w") as write_file:
            json.dump(self.current_state, write_file)

    def reset(self):
        self.current_state["impulse_seit_reset"] = 0
        self.current_state["gesamtimpulse"] = 0
        self.current_state["inhalt"] = 30
        self.current_state["gesamtverbrauch"] = 0
        self.save_current_state()
        bierprototype_support.refresh()
