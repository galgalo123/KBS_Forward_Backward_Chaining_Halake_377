# Course Eligibility Expert System
# Forward Chaining and Backward Chaining Implementation
# APT 3020B – Knowledge Based Systems
# Student: Galgalo Molu Halake
# Admission Number: 669377
# RULE DEFINITIONS

rules = [
    {
        "conditions": ["Programming I", "Mathematics I"],
        "conclusion": "Eligible for Data Structures"
    },
    {
        "conditions": ["Data Structures", "Computer Organization"],
        "conclusion": "Eligible for Algorithms"
    },
    {
        "conditions": ["Programming I", "Statistics"],
        "conclusion": "Eligible for Machine Learning Basics"
    },
    {
        "conditions": ["Algorithms", "GPA>=3.0"],
        "conclusion": "Eligible for Advanced AI"
    },
    {
        "conditions": ["GPA<2.5"],
        "conclusion": "Not eligible for advanced courses"
    }
]

# FORWARD CHAINING

def forward_chaining(student):
    facts = set(student["courses"])
    gpa = student["gpa"]

    inferred = set()
    fired_rules = []

    # GPA conditions added as facts
    if gpa >= 3.0:
        facts.add("GPA>=3.0")
    if gpa < 2.5:
        facts.add("GPA<2.5")

    print("\nInitial Facts:", facts)

    changed = True

    while changed:
        changed = False

        for rule in rules:
            conditions = set(rule["conditions"])
            conclusion = rule["conclusion"]

            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                inferred.add(conclusion)
                fired_rules.append(rule)

                print("Rule Fired:", conditions, "→", conclusion)

                changed = True

    print("\nFinal Eligible Courses:")
    for fact in inferred:
        print("-", fact)

    return facts


# BACKWARD CHAINING

def backward_chaining(goal, facts, visited=None):

    if visited is None:
        visited = set()

    if goal in facts:
        print("Goal", goal, "already known.")
        return True

    if goal in visited:
        return False

    visited.add(goal)

    for rule in rules:
        if rule["conclusion"] == goal:

            print("\nChecking rule:", rule["conditions"], "→", goal)

            all_true = True

            for condition in rule["conditions"]:
                if not backward_chaining(condition, facts, visited):
                    all_true = False
                    break

            if all_true:
                print("Rule satisfied →", goal, "PROVED")
                facts.add(goal)
                return True

    print("Could not prove:", goal)
    return False

# STUDENT TEST CASES

students = [
    {
        "name": "Alice",
        "courses": ["Programming I", "Statistics"],
        "gpa": 3.2,
        "query": "Eligible for Machine Learning Basics"
    },
    {
        "name": "Brian",
        "courses": ["Programming I", "Mathematics I", "Computer Organization"],
        "gpa": 3.4,
        "query": "Eligible for Algorithms"
    },
    {
        "name": "Carol",
        "courses": ["Programming I"],
        "gpa": 2.2,
        "query": "Eligible for Advanced AI"
    }
]

# RUN TEST CASES

for student in students:

    print("\n=================================")
    print("Student:", student["name"])
    print("Completed Courses:", student["courses"])
    print("GPA:", student["gpa"])

    # Forward Chaining
    print("\n--- Forward Chaining ---")
    derived_facts = forward_chaining(student)

    # Backward Chaining
    print("\n--- Backward Chaining ---")
    goal = student["query"]

    print("\nQuery:", goal)

    if backward_chaining(goal, derived_facts):
        print("\nResult: PROVED")
    else:
        print("\nResult: NOT PROVED")

    print("=================================\n")