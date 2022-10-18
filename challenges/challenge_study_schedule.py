def study_schedule(permanence_period, target_time):
    students = 0
    try:
        for entry, leave in permanence_period:
            if entry <= leave and entry <= target_time <= leave:
                students += 1
        return students
    except TypeError:
        return None
