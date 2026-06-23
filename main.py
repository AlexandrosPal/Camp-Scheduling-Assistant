import random


activities = [
    {"name": "Swimming", "teacher": "John", "room": "Pool"},
    {"name": "Crafts", "teacher": "Anna", "room": "Hall A"},
    {"name": "Archery", "teacher": "John", "room": "Field"},
    {"name": "Music", "teacher": "Jack", "room": "Hall B"},
    {"name": "Football", "teacher": "Marie", "room": "Field"},
    {"name": "Climbing", "teacher": "Jack", "room": "Field"},
    {"name": "Chess", "teacher": "Jack", "room": "Hall A"},
    {"name": "Tenis", "teacher": "Alex", "room": "Field"},
    {"name": "Volley", "teacher": "Alex", "room": "Pool"}
]

timeslots = [
    "07:30",
    "09:00",
    "10:30",
    "12:00"
]

def generate_conflicts(activities):
    return {
        first_activity["name"]: [
            second_activity["name"]
            for second_activity in activities
            if activities_are_conflicting(
                first_activity,
                second_activity
            )
        ]
        for first_activity in activities
    }

def activities_are_conflicting(first_activity, second_activity):
    if first_activity["name"] == second_activity["name"]:
        return False
    
    return any([
        first_activity["room"] == second_activity["room"],
        first_activity["teacher"] == second_activity["teacher"]
    ])

def can_assign(activity, timeslot, schedule, conflicts):
    for neighbor in conflicts[activity]:
        if schedule.get(neighbor) == timeslot:
            return False
        
    return True

def generate_schedule(conflicts, timeslots):
    schedule = {}
    timeslot_counts = {timeslot: 0 for timeslot in timeslots}

    activities = sorted(
        conflicts,
        key=lambda activity: (
            len(conflicts[activity]),
            random.random()
        ),
        reverse=True
    )

    for activity in activities:

        valid_timeslots = [timeslot for timeslot in timeslots if can_assign(activity, timeslot, schedule, conflicts)]
        random.shuffle(valid_timeslots)
        if not valid_timeslots:
            return None
        
        min_count = min(timeslot_counts[timeslot] for timeslot in valid_timeslots)

        best_slots = [
            timeslot
            for timeslot in valid_timeslots
            if timeslot_counts[timeslot] == min_count
        ]

        best_slot = random.choice(best_slots)

        schedule[activity] = best_slot
        timeslot_counts[best_slot] += 1

    return schedule

def print_schedule(time_schedule):
    table = {slot: [] for slot in timeslots}
    for activity, slot in time_schedule.items(): 
        table[slot].append(activity) 

    print("+-----------+--------------------------------+") 
    print("| Timeslot | Activities                      |") 
    print("+-----------+--------------------------------+") 

    for slot, activities in table.items(): 
        activities_str = ", ".join(activities) 
        print(f"| {slot:<9} | {activities_str:<30} |") 

    print("+-----------+--------------------------------+")


random.shuffle(activities)
conflicts = generate_conflicts(activities)
time_schedule = generate_schedule(conflicts, timeslots)

print_schedule(time_schedule)
