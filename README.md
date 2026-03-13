# Course Eligibility Expert System

**APT 3020B – Knowledge-Based Systems Practical Assignment**

## Student Information

**Name:** Galgalo Molu Halake
**Admission Number:** 669377

---

# 1. Problem Description

This project implements a small **rule-based Knowledge-Based System (KBS)** in Python that determines whether a student is eligible for specific university courses.

The system demonstrates two important reasoning techniques used in expert systems:

* **Forward Chaining (Data-Driven Reasoning)**
* **Backward Chaining (Goal-Driven Reasoning)**

The system evaluates student eligibility based on:

* Completed prerequisite courses
* GPA (Grade Point Average)
* Predefined inference rules

The implementation simulates a **course advisory system similar to what universities may use to guide students on course progression**.

---

# 2. Knowledge Base Design

## Facts

Facts represent the known information about a student. These include:

* Student name
* Completed courses
* GPA

Facts are stored using Python structures such as:

* Sets
* Lists
* Dictionaries

Example fact:

Student: Galgalo Halake
Completed Courses: IST 2010, IST 1025, STA 2020
GPA: 3.4

---

## Rules

The system contains logical rules that determine course eligibility.

Example rules used in the system include:

* If a student completed **IST 2010 and IST 1025** → Eligible for **IST 3020**
* If a student completed **IST 3020 and IST 2040** → Eligible for **IST 3030**
* If a student completed **IST 2010 and STA 2020** → Eligible for **IST 4035**
* If a student completed **IST 3030 and GPA ≥ 3.2** → Eligible for **IST 4060**
* If **GPA < 2.5** → Student is **restricted from advanced IST courses**

These rules form the **knowledge base** used by the inference engine.

---

# 3. Forward Chaining

Forward chaining is a **data-driven reasoning method**.

Steps followed in this implementation:

1. The system begins with known facts about the student.
2. The inference engine checks which rules can be applied.
3. If rule conditions are satisfied, the rule fires.
4. New conclusions (facts) are added to the knowledge base.
5. The process repeats until no new facts can be derived.

The program displays:

* Initial facts
* Rules that fired
* Newly inferred conclusions
* Final eligible courses

---

# 4. Backward Chaining

Backward chaining is a **goal-driven reasoning method**.

Steps followed:

1. The system starts with a query (goal).
2. It searches for rules that could produce that goal.
3. The system then checks if the rule conditions are true.
4. If conditions are not known, the system attempts to prove them recursively.
5. The system finally returns:

* **PROVED** if the goal is satisfied
* **NOT PROVED** if the conditions cannot be satisfied

This process demonstrates how expert systems reason backwards from a goal.

---

# 5. Test Cases

The system was tested using three example students:

### Student 1

Name: **Galgalo Halake**
Courses: IST 2010, IST 1025, STA 2020
GPA: 3.4

### Student 2

Name: **John Kamau**
Courses: IST 2010, IST 1025, IST 2040
GPA: 3.3

### Student 3

Name: **Mary Wanjiku**
Courses: IST 2010
GPA: 2.2

Each test case demonstrates both forward chaining and backward chaining.

---

# 6. How to Run the Program

1. Clone the repository or download the files.
2. Open the project in **VS Code** or any Python environment.
3. Run the Python script using:

```
python course_expert_system.py
```

The program will automatically run all test cases and display the inference results.

---

# 7. Sample Output

Example execution of the expert system:

Student: Galgalo Halake
Completed Courses: IST 2010, IST 1025, STA 2020
GPA: 3.4

Forward Chaining Results:
Rule fired → Eligible for IST 4035

Final Eligible Courses:
- Eligible for IST 4035

Backward Chaining Query:
Is Galgalo Halake eligible for IST 4035?

Result: PROVED


Student: John Kamau
Completed Courses: IST 2010, IST 1025, IST 2040
GPA: 3.3

Forward Chaining Results:
Rule fired → Eligible for IST 3020
Rule fired → Eligible for IST 3030

Backward Chaining Query:
Is John Kamau eligible for IST 3030?

Result: PROVED

---

# 8. Conclusion

This project demonstrates how **rule-based expert systems** can be implemented using basic Python structures.

Both **forward chaining and backward chaining** were successfully implemented to simulate reasoning in a university course eligibility system.