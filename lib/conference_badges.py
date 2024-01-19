def badge_maker(name):
   return f"Hello, my name is {name}."
name = "Ariel"


def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    assignments = []
    for room in range(1, len(names) + 1):
        assignments.append(f'Hello, {names[room - 1]}! You\'ll be assigned to room {room}!')
    
    return assignments


def printer(names):
    for badges in batch_badge_creator(names):
        print(badges)

    for assignments in assign_rooms(names):
        print(assignments)

        
