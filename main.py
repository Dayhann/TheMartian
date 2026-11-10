from Astronaut import Astronaut
from Greenhouse import Greenhouse
from MarsOutpost import MarsOutpost
from OxygenGenerator import OxygenGenerator
from Rover import Rover
from WaterExtractor import WaterExtractor


astronaut = Astronaut("Alex")
outpost = MarsOutpost(astronaut)
rover = Rover()

outpost.add_supplies("food", 3)
outpost.add_supplies("water", 1)
outpost.add_supplies("oxygen", 1)

outpost.add_equipment(WaterExtractor())
outpost.add_equipment(OxygenGenerator())
outpost.add_equipment(Greenhouse())
outpost.add_equipment(rover)

print("Starting outpost:")
print(outpost.status_report())
print()

while not outpost.is_finished():
    next_sol = outpost.sols_completed + 1
    if next_sol == 2:
        rover.break_down()
        print("Rover breakdown. Broken equipment:")
        for item in outpost.get_broken_equipment():
            print(item)
    elif next_sol == 3:
        rover.repair()
        print("Rover repaired.")
    elif next_sol == 6:
        rover.recharge()
        print("Rover recharged.")

    outpost.advance_sol()
    print(outpost.status_report())
    print()

print("Recorded equipment failures:")
for entry in outpost.get_log_entries("failed"):
    print(entry)

print("\nSeparate shortage example:")
shortage_outpost = MarsOutpost(Astronaut("Sam"), target_sols=2)
shortage_outpost.add_supplies("food", 2)
shortage_outpost.add_supplies("oxygen", 2)
shortage_outpost.advance_sol()
print(shortage_outpost.status_report())
for entry in shortage_outpost.get_log_entries("failed"):
    print(entry)
