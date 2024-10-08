# This program reads strings of job requirements and adds them to a dictionary.
# After the user is finished, it sorts them and the list is printed to a
# "sorted_requirements.txt" file.

# printed sorted requirements
def print_requirements(dictionary):
    for i, tech in enumerate(dictionary):
        print(f"{i + 1}: {tech} {dictionary[tech]}")

def get_sorted_techs():
    # define an empty dictionary of job requirements
    requirements = { }
    # the current technology variable
    technology = input(f"\n> Please enter a needed technology ('q' to quit): ").lower()
    # enter new technologies until the user inputs q
    while (technology != "q"):
        # if technology not in requirements, initialize it with 1
        if technology not in requirements.keys():
            requirements[technology] = 1
            print("Adding new technology...") 
        # else increment the number of mentions
        else:
            requirements[technology] += 1
        # after each prompt, print
        requirements = dict(sorted(requirements.items(), key=lambda item: item[1], reverse=True))
        print_requirements(requirements)
        technology = input(f"\n> Please enter a needed technology ('q' to quit): ").lower()
    if requirements:
        return requirements
    else:
        print("The list is empty. Quitting...")
        quit()

print(f"""######################################################################
The purpose of this program is to help you find what things you should
prioritize studying while applying for a job.
######################################################################""")

requirements = get_sorted_techs()

print(f"""
Here's the final sorted list of requirements: """)

print_requirements(requirements)

# write the final result to the sorted_requirements.txt file
with open("sorted_requirements.txt", "w") as file:
    for i, tech in enumerate(requirements):
        print(f"{i + 1}: {tech} {requirements[tech]}", file=file)

print(f"""
Printed the sorted list to the \"sorted_requirements.txt\" file.""")
