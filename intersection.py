import random
import time
from collections import deque

# --- Settings ---
LANES = ["North", "South", "East", "West"]
SIM_TIME = 60 # seconds
GREEN_TIME = 15
ARRIVAL_RATE = 0.35

class Lane:
    def __init__(self, name):
        self.name = name
        self.queue = 0
        self.total_passed = 0
        self.total_wait = 0

lanes = {name: Lane(name) for name in LANES}

def simulate():
    print("=== TRAFFIC INTERSECTION SIMULATION ===")
    print(f"Duration: {SIM_TIME}s | Green: {GREEN_TIME}s")
    print("-" * 50)

    current_green = 0 # index of lane with green

    for sec in range(SIM_TIME):
        # 1. Vehicle arrival
        for l in lanes.values():
            if random.random() < ARRIVAL_RATE:
                l.queue += 1
                l.total_wait += 1

        # 2. Traffic light change
        if sec % GREEN_TIME == 0 and sec!= 0:
            current_green = (current_green + 1) % len(LANES)

        green_lane_name = LANES[current_green]
        green_lane = lanes[green_lane_name]

        # 3. Vehicles passing on green (2 per second)
        if green_lane.queue > 0:
            passed = min(2, green_lane.queue)
            green_lane.queue -= passed
            green_lane.total_passed += passed

        # 4. Display every 5 seconds
        if sec % 5 == 0:
            queues = " | ".join([f"{n}:{lanes[n].queue}" for n in LANES])
            print(f"[{sec:02d}s] GREEN->{green_lane_name} | {queues}")

    # --- Final Report ---
    print("\n" + "="*50)
    print("FINAL REPORT")
    print("="*50)
    total_system = 0
    for name in LANES:
        l = lanes[name]
        total_system += l.queue
        print(f"{name:6s} | In Queue: {l.queue:2d} | Passed: {l.total_passed:2d} | Avg Wait: {l.total_wait/max(1,l.total_passed):.1f}s")

    print("-" * 50)
    print(f"Total vehicles still in system: {total_system}")
    print(f"Total vehicles passed: {sum(l.total_passed for l in lanes.values())}")
    print("Simulation Complete.")

if __name__ == "__main__":
    simulate()