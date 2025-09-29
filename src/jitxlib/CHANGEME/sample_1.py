from jitx.circuit import Circuit
from jitx.sample import SampleDesign

from jitxlib.parts.query_api import ResistorQuery, Resistor


def get_random_number():
    # https://xkcd.com/221/
    return 4  # chosen by fair dice roll, guaranteed to be random


class MainCircuit(Circuit):
    def __init__(self):
        self.r1 = Resistor(resistance=100)
        self.r2 = Resistor(resistance=get_random_number() * 100)

        self.nets = [
            self.r1.p1 + self.r2.p1,
            self.r1.p2 + self.r2.p2,
        ]


class ResistorDesign(SampleDesign):
    resistor_defaults = ResistorQuery(case="0402")

    circuit = MainCircuit()
