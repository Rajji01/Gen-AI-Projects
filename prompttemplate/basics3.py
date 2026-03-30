"""
=============================================================
PART 4: Sab Link Up — ArchMaster Template Library
=============================================================

Ab tak tu sikha:
  Part 1 → Import kya hai, PromptTemplate kya hai
  Part 2 → Variables, multiline, reuse
  Part 3 → ChatPromptTemplate (system + human)

Ab sab COMBINE karte hain — tere ArchMaster app ke liye
ek proper Template Library banate hain.

Soch aise — tu ek architect hai, tere paas 4 drawers hain:
  Drawer 1: LLD questions ke templates
  Drawer 2: HLD questions ke templates
  Drawer 3: Design Pattern questions ke templates
  Drawer 4: Answer evaluate karne ka template

Candidate aaye → drawer kholo → template use karo → question do!
"""

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# ============================================
# TEMPLATE LIBRARY — Dictionary mein store
# ============================================

# Python dictionary = key-value pairs
# Key = template ka naam
# Value = actual template object

QUESTION_TEMPLATES = {}  # khaali dictionary, ab isme templates daalenge

# --------------------------------
# DRAWER 1: LLD (Low Level Design)
# --------------------------------
# LLD mein kya puchte hain?
# → Classes banao, design patterns lagao, API design karo

QUESTION_TEMPLATES["lld"] = PromptTemplate(
    input_variables=["component", "constraints"],
    template="""Design a Low-Level Design for: {component}

Constraints: {constraints}

Your answer should cover:
1. Classes aur unke relationships (has-a, is-a)
2. Design patterns — kaunsa lagaoge aur KYU
3. API contracts (endpoints, request/response)
4. Error handling
5. Thread safety (agar zaroorat ho)"""
)

# --------------------------------
# DRAWER 2: HLD (High Level Design)
# --------------------------------
# HLD mein kya puchte hain?
# → System architecture, scaling, databases, trade-offs

QUESTION_TEMPLATES["hld"] = PromptTemplate(
    input_variables=["system", "scale", "requirements"],
    template="""Design a High-Level Architecture for: {system}

Scale: {scale}
Requirements: {requirements}

Your answer should cover:
1. System components aur unki responsibilities
2. Communication — sync ya async (REST, gRPC, Kafka?)
3. Database — SQL ya NoSQL? Kyu?
4. Scaling strategy — horizontal ya vertical?
5. Failure handling — kya hoga agar kuch crash ho?
6. Trade-offs — tumne kya choose kiya aur kya sacrifice kiya"""
)

# --------------------------------
# DRAWER 3: Design Patterns
# --------------------------------
# Pattern questions mein kya puchte hain?
# → Scenario do, pattern identify karo, trade-offs batao

QUESTION_TEMPLATES["design_pattern"] = PromptTemplate(
    input_variables=["scenario", "pattern_hint"],
    template="""Scenario: {scenario}

Hint: Think about {pattern_hint} pattern.

Questions:
1. Kaunsa design pattern lagaoge? Kyu?
2. Implementation kaise karoge? (pseudocode ok)
3. Trade-offs kya hain?
4. Kab ye pattern use NAHI karoge?"""
)

# --------------------------------
# DRAWER 4: Answer Evaluator
# --------------------------------
# Ye answer check karne ke liye hai
# Candidate ka answer do, AI evaluate karega

QUESTION_TEMPLATES["evaluate"] = PromptTemplate(
    input_variables=["question", "answer", "level"],
    template="""Evaluate this architecture answer:

QUESTION: {question}
ANSWER: {answer}
EXPECTED LEVEL: {level}

Score on (0-10 each):
1. Correctness — kya sahi hai?
2. Depth — kitna deep samjha hai?
3. Practical — real mein kaam karega?
4. Trade-offs — alternatives consider kiye?

Give: Overall score, kya acha tha, kya missing tha, kya padhe."""
)


# ============================================
# AB USE KARTE HAIN — Real Scenarios!
# ============================================

print("=" * 60)
print("  ARCHMASTER TEMPLATE LIBRARY — DEMO")
print("=" * 60)

# ----- LLD Question -----
print("\n📘 LLD QUESTION:")
print("-" * 40)
print(QUESTION_TEMPLATES["lld"].format(
    component="Rate Limiter for Razorpay API Gateway",
    constraints="1 lakh requests/sec, distributed, multiple API keys"
))

# ----- HLD Question -----
print("\n📗 HLD QUESTION:")
print("-" * 40)
print(QUESTION_TEMPLATES["hld"].format(
    system="Zomato Food Delivery Tracking",
    scale="10 lakh orders/day, 2 lakh delivery partners",
    requirements="Real-time location, ETA prediction, order status updates"
))

# ----- Design Pattern Question -----
print("\n📙 DESIGN PATTERN QUESTION:")
print("-" * 40)
print(QUESTION_TEMPLATES["design_pattern"].format(
    scenario="Paytm mein payment process karna hai — UPI, Card, Wallet sab support karna hai. Aage naye payment methods bhi add ho sakte hain.",
    pattern_hint="Strategy"
))

# ----- Answer Evaluation -----
print("\n📕 ANSWER EVALUATION:")
print("-" * 40)
print(QUESTION_TEMPLATES["evaluate"].format(
    question="Design a caching strategy for Flipkart product pages",
    answer="Redis use karenge as cache. TTL 5 min rakhenge. Cache miss pe DB se fetch karenge.",
    level="6 years experience — Senior"
))

# ============================================
# BONUS: Template select karna dynamically
# ============================================

print("\n" + "=" * 60)
print("  BONUS: Dynamic Template Selection")
print("=" * 60)

# User ne choose kiya kaunsa type chahiye
user_choice = "hld"  # ye baad mein UI se aayega

# Dictionary se template nikalo
selected_template = QUESTION_TEMPLATES[user_choice]

# Use karo
print(f"\nUser selected: {user_choice.upper()}")
print("-" * 40)
print(selected_template.format(
    system="OLA Ride Matching System",
    scale="5 lakh concurrent rides",
    requirements="< 30 sec match time, surge pricing, driver allocation"
))

print("\n" + "=" * 60)
print("🎉 COMPLETE! Ab tu samajh gaya:")
print("  ✅ Import kaise karte hain")
print("  ✅ PromptTemplate kya hai aur kyu use karte hain")
print("  ✅ Variables — single, multiple, multiline")
print("  ✅ ChatPromptTemplate — system + human messages")
print("  ✅ Template Library — organized templates")
print("  ✅ Dynamic selection — user choice se template pick")
print()
print("NEXT STEP: In templates ko REAL AI model se connect karenge!")
print("Tab AI actually questions generate karega — not just templates.")
print("=" * 60)