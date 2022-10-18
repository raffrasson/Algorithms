def study_schedule(permanence_period, target_time):
    students = 0
    try:
        for entry, leave in permanence_period:
            if entry == None:
                return None
            if leave == None:
                return None
            if target_time == None:
                return None
            if entry <= leave and entry <= target_time and leave >= target_time:
                students += 1
        return students
    except TypeError:
        return None
