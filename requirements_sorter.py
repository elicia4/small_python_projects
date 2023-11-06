# This program reads strings of job requirements and adds them to a dictionary.
# After the user is finished, it sorts them and the list is printed to a
# "sorted_requirements.txt" file.

def print_requirements(dictionary):
    for i, tech in enumerate(dictionary):
        print(f"{i}: {tech} {dictionary[tech]}")

def get_sorted_techs():
    # define an empty dictionary of job requirements
    requirements = {
    }
    # the current technology variable
    technology = input(f"\nPlease enter a needed technology: ").lower()
    print("Enter \"done\" when you're done with your entries.")
    # enter new technologies until the user inputs done
    while (technology != "done"):
        if technology not in requirements.keys():
            requirements[technology] = 1
            print("Adding new technology...") 
        else:
            requirements[technology] += 1
        print_requirements(requirements)
        technology = input(f"\nPlease enter a needed technology: ").lower()
        print("Enter \"done\" when you're done with your entries.")
    return dict(sorted(requirements.items(), key=lambda x:x[1], reverse=True))

print(f"""
######################################################################
The purpose of this program is to help you find what things you should
prioritize studying while applying for a job.
######################################################################
""")

sorted_requirements = get_sorted_techs()

print(f"""
#############################################
Here's the final sorted list of requirements:
#############################################""")

print_requirements(sorted_requirements)

# write the final result to the sorted_requirements.txt file
with open("sorted_requirements.txt", "w") as file:
    for key in sorted_requirements.keys():
        print(f"{key} {sorted_requirements[key]}", file=file)
print("""#############################################\n
Printed the sorted list to the \"sorted_requirements.txt\" file.""")
