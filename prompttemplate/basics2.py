"""
=============================================================
PART 3: ChatPromptTemplate — AI se Baat Karne ka Modern Tarika
=============================================================

Pehle samjho CHAT format kya hai.

Jab tu ChatGPT ya Claude use karta hai, toh 2 cheezein hoti hain:
1. SYSTEM message — AI ko batao "tu kaun hai" (ye user ko nahi dikhta)
2. HUMAN message — tera actual question

Example:
  SYSTEM: "Tu ek strict interviewer hai"
  HUMAN:  "Mujhe caching ke baare mein question do"

AI system message ke hisaab se behave karega!
Agar system mein bolo "tu ek comedian hai" toh funny answers dega.
Agar bolo "tu strict interviewer hai" toh tough questions dega.

YEHI hai ChatPromptTemplate — system + human messages ko
template mein daal do.
"""

from langchain_core.prompts import ChatPromptTemplate

# ============================================
# STEP 1: Simple ChatPromptTemplate
# ============================================

# Sabse basic — ek system, ek human message
simple_chat = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful coding teacher."),   # AI ka role
    ("human", "Explain {topic} in simple words.")      # User ka question
])

# Messages banao
messages = simple_chat.format_messages(topic="REST API")

# Dekho kya bana
print("STEP 1: Simple Chat Template")
print("-" * 40)
for msg in messages:
    print(f"  [{msg.type}]: {msg.content}")
print()

# ============================================
# STEP 2: Variables DONO mein daal sakte ho
# ============================================

# System mein bhi variable, Human mein bhi variable
# Ye powerful hai — AI ka ROLE bhi dynamic ho sakta hai!

flexible_chat = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}. You have {exp} years of experience."),
    ("human", "Give me a {difficulty} question about {topic}.")
])

# Scenario 1: Strict interviewer
print("STEP 2a: Strict Interviewer")
print("-" * 40)
messages = flexible_chat.format_messages(
    role="strict technical interviewer",
    exp="15",
    difficulty="hard",
    topic="Microservices"
)
for msg in messages:
    print(f"  [{msg.type}]: {msg.content}")
print()

# Scenario 2: Friendly mentor
print("STEP 2b: Friendly Mentor")
print("-" * 40)
messages = flexible_chat.format_messages(
    role="friendly coding mentor",
    exp="10",
    difficulty="easy",
    topic="Microservices"
)
for msg in messages:
    print(f"  [{msg.type}]: {msg.content}")
print()

# SAME topic (Microservices) but DIFFERENT roles = DIFFERENT style questions!
# Ye samjh — system message se AI ka personality change hota hai.

# ============================================
# STEP 3: Apne ArchMaster App ke liye template
# ============================================

# Ab REAL template banate hain jo tere app mein use hoga

archmaster_chat = ChatPromptTemplate.from_messages([
    ("system", """You are ArchMaster — an AI architecture knowledge testing system.

Your job:
- Generate real-world architecture interview questions
- Adapt difficulty to candidate's experience
- Focus on practical scenarios, not textbook theory
- Give hints if candidate is stuck

Current mode: {mode}"""),

    ("human", """Generate a question for me.

My details:
- Experience: {years} years
- Topic: {topic}
- Difficulty: {difficulty}

I want a real scenario — jaise koi Indian tech company mein aata hai.
For example: Zomato, Paytm, Flipkart type scenarios.""")
])

# Self-test mode
print("STEP 3: ArchMaster Template")
print("-" * 40)
messages = archmaster_chat.format_messages(
    mode="Self Assessment",
    years="6",
    topic="Database Design",
    difficulty="Senior Level",
)
for msg in messages:
    print(f"\n  [{msg.type}]:")
    print(f"  {msg.content}")

print()
print("=" * 50)
print("PART 3 DONE! Ab Part 4 chalao — sab link up hoga.")
print("=" * 50)