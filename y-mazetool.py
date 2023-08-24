# Definition of Types of Behaviours
arms = ["A", "B", "C"]
SAP = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
AAR = ["ABA", "ACA", "BAB", "BCB", "CAC", "CBC"]
SAR = ["AA", "BB", "CC"]


def string_count_overlapping(path, pattern):
    count = 0
    start = 0
    while True:
        i = path.find(pattern, start)
        if i >= 0:
            count += 1
            start = i + 1
        else:
            break
    return count


# Storage
list_ids = []
list_paths = []
list_entries = []
list_possible_triads = []
list_SAP = []
list_SAP_percent = []
list_AAR = []
list_AAR_percent = []
list_SAR = []
list_SAR_percent = []

# Import data
while True:
    i_number_ids = input("Insert the number of animals to analyze: ")
    try:
        number_ids = int(i_number_ids)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for animal in range(number_ids):
    start = 0
    entries = 0
    SAP_counter = 0
    AAR_counter = 0
    SAR_counter = 0
    animal_id = input("Enter the ID for animal {}: ".format(animal + 1))
    list_ids.append(animal_id)
    while True:
        animal_path = input(f"Enter the path for {animal_id}: ")
        animal_path = animal_path.upper()
        if "," in animal_path:
            animal_path = animal_path.replace(",", "")
        elif "." in animal_path:
            animal_path = animal_path.replace(".", "")
        elif " " in animal_path:
            animal_path = animal_path.replace(" ", "")
        if all(arm in arms for arm in animal_path):
            break
        else:
            print("Invalid input. Please enter a path containing only the letters A, B, and C.")

    list_paths.append(animal_path)
    for arm in arms:
        entries += animal_path.count(arm)
    list_entries.append(entries)
    possible_triads = (entries - 2)
    list_possible_triads.append(possible_triads)
    if possible_triads < 1:
        list_SAP.append("N/A")
        list_SAP_percent.append("N/A")
        list_AAR.append("N/A")
        list_AAR_percent.append("N/A")
        list_SAR.append("N/A")
        list_SAR_percent.append("N/A")
    else:
        for spontaneous_alt in SAP:
            SAP_counter += string_count_overlapping(animal_path, spontaneous_alt)
        list_SAP.append(SAP_counter)
        list_SAP_percent.append((SAP_counter / possible_triads) * 100)

        for alternate_arm_returns in AAR:
            AAR_counter += string_count_overlapping(animal_path, alternate_arm_returns)
        list_AAR.append(AAR_counter)
        list_AAR_percent.append((AAR_counter / possible_triads) * 100)

        for same_arm_returns in SAR:
            SAR_counter += string_count_overlapping(animal_path, same_arm_returns)
        list_SAR.append(SAR_counter)
        list_SAR_percent.append((SAR_counter / possible_triads) * 100)

# Export results CSV
print("ID, path, number of entries, number of possible triads, "
      "percentage of spontaneous alternations, number spontaneous alternations, "
      "percentage of alternate arms returns, number of alternate arms returns, "
      "percentage of same arm returns, number of same arm returns")
for animal in range(len(list_ids)):
    print(f"{list_ids[animal]}, {list_paths[animal]}, {list_entries[animal]}, {list_possible_triads[animal]},"
          f"{list_SAP_percent[animal]}, {list_SAP[animal]}, "
          f"{list_AAR_percent[animal]}, {list_AAR[animal]}, "
          f"{list_SAR_percent[animal]}, {list_SAR[animal]}")
print("All done!")
