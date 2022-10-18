def is_anagram(first_string, second_string):
    def sorter(list):
        n = len(list)  

        for ordered_elements in range(
            n - 1
        ):  
            for item in range(
                0, n - 1 - ordered_elements
            ):  
                if (
                    list[item] > list[item + 1]
                ):  
                    current_element = list[item]
                    list[item] = list[item + 1]
                    list[item + 1] = current_element

        return list

    first_string_formatted = list(first_string.lower())
    second_string_formatted = list(second_string.lower())


    first_string_ordered = sorter(first_string_formatted)
    second_string_ordered = sorter(second_string_formatted)


    if first_string_ordered == second_string_ordered:
        return True
    else:
        return False
