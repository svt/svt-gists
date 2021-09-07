# SPDX-FileCopyrightText: 2021 Sveriges Television AB
#
# SPDX-License-Identifier: MIT

import csv
import sys
file=sys.argv[1]
types=["Task", "Reflection"]
reflections=[]
tasks=[]
with open(file, mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, quotechar='"')
    for row in reader:
        if row['type'] == "Task":
            tasks.append(row)
        elif row['type'] == "Reflection":
            reflections.append(row)


prompts = set()
for reflection in reflections:        
    prompts.add(reflection['prompt'])

print("## Action points")
for task in tasks:
    print("* " + task['content'])

currentGroup=""
for prompt in prompts:
    print("")
    print("## " + prompt)
    for reflection in reflections:
        if reflection['prompt'] == prompt:
            if currentGroup != reflection['reflectionGroup']:
                currentGroup = reflection['reflectionGroup']
#                print('\n')
            print("* " + reflection['content'])
