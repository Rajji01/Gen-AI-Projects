"""
=============================================================
PART 2: PromptTemplate — Deep Dive
=============================================================

Ab samjhte hain PromptTemplate ke andar kya hota hai.

Real life example:
Tu Zomato ka architect hai. Tujhe ek system design karna hai.
Tu apne junior se puchta hai:

  "Bhai {system_name} ka design bata, {users} users handle karna hai"

Har baar system_name aur users change hota hai, but PATTERN same hai.
YE hai PromptTemplate.
"""

from langchain_core.prompts import PromptTemplate

# ============================================
# STEP 1: Sabse simple template — 1 variable
# ============================================

# Template banao — sirf EK variable hai: topic
simple = PromptTemplate(
    input_variables=["topic"],         # ye list hai variables ki
    template="What is {topic}?"        # {topic} ki jagah value aayegi
)

# Ab use karo — .format() se value daal do
result = simple.format(topic="Docker")
print("Simple template:")
print(result)
# Output: What is Docker?
print()

# Kya hoga agar variable na de?
# simple.format()  ← ye ERROR dega! Kyunki topic dena zaroori hai.

# ============================================
# STEP 2: Multiple variables — 2 ya zyada
# ============================================

# Ab thoda complex — 3 variables
interview_template = PromptTemplate(
    input_variables=["topic", "difficulty", "years"],  # 3 variables
    template="""Topic: {topic}
Difficulty: {difficulty}
Candidate experience: {years} years

Generate one interview question."""
)

# Sab variables ki value deni padegi
result = interview_template.format(
    topic="Load Balancing",
    difficulty="Medium",
    years="6"
)
print("Multiple variables template:")
print(result)
print()

# ============================================
# STEP 3: Multiline template — Lamba prompt
# ============================================

# Real AI prompts lambe hote hain — multiline mein likhte hain
# Python mein triple quotes """ """ se multiline string banti hai

detailed_template = PromptTemplate(
    input_variables=["system_name", "daily_users", "country"],
    template="""You are a senior architect at a tech company.

Design a system: {system_name}
Expected daily users: {daily_users}
Target market: {country}

Please cover:
1. Main components
2. Database choice and why
3. Caching strategy
4. How to handle peak traffic"""
)

# Zomato jaisa scenario
result = detailed_template.format(
    system_name="Food Delivery App",
    daily_users="5 million",
    country="India"
)
print("Detailed template:")
print(result)
print()

# ============================================
# STEP 4: Template ko REUSE karna — Power!
# ============================================

# YEHI hai asli fayda — ek template, multiple scenarios
# Same template, different values = different questions

print("=" * 50)
print("SAME template, DIFFERENT inputs:")
print("=" * 50)

# Scenario 1: Paytm jaisa
print("\n--- Scenario 1: Paytm ---")
print(detailed_template.format(
    system_name="Digital Payments System",
    daily_users="50 million",
    country="India"
))

# Scenario 2: Uber jaisa
print("\n--- Scenario 2: Uber ---")
print(detailed_template.format(
    system_name="Ride Sharing Platform",
    daily_users="20 million",
    country="India"
))

# Dekh — ek template likha, 2 alag questions generate ho gaye!
# Kal 100 alag topics daalega toh 100 questions ban jaayenge.
# YE hai PromptTemplate ki power.

print()
print("=" * 50)
print("PART 2 DONE! Ab Part 3 chalao.")
print("=" * 50)