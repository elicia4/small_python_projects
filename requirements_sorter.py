# This program reads strings of job requirements and adds them to a dictionary.
# After the user is finished, it sorts them and the list is printed to a
# "sorted_requirements.txt" file.

requirements = {
}

print(f"""
######################################################################
The purpose of this program is to help you find what things you should
prioritize studying while applying for a job.
######################################################################
""")

technology = ""
while (technology != "done"):

    i = 0;
    for requirement in requirements.keys():
        print(f"{i}: {requirement} {requirements[requirement]}")
        i += 1

    technology = input(f"\nPlease enter a needed technology: ").lower()
    print("Enter \"done\" when you're done with your entries.")
    if technology == "done":
        break

    if technology not in requirements.keys():
        requirements[technology] = 1
        print("Adding new technology...") 
    else:
        requirements[technology] += 1

sorted_requirements = dict(sorted(requirements.items(), key=lambda x:x[1], reverse=True))

print(f"""
#############################################
Here's the final sorted list of requirements:
#############################################""")

for key in sorted_requirements.keys():
    with open("sorted_requirements.txt", "a") as f:
        print(f"{key} {sorted_requirements[key]}", file=f)
    print(f"\t{key} {sorted_requirements[key]}")

print("""#############################################\n
Printed the sorted list to the \"sorted_requirements.txt\" file.""")
