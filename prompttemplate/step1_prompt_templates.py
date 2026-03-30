"""
=============================================================
ARCHMASTER - Phase 1, Step 1: Prompt Templates
=============================================================

CONCEPT: Prompt Template
------------------------
Socho tum ek architect ho aur interview le rahe ho.
Tumhara question pattern hamesha same hota hai:

    "Mujhe {topic} ke baare mein {difficulty} level ka question do"

LangChain ka PromptTemplate yehi kaam karta hai:
- Variables define karo (topic, difficulty)
- Template likho
- Runtime pe values daalke final prompt banao

Ye GenAI ka PEHLA aur SABSE IMPORTANT concept hai.
Ache prompts = Ache results. Bura prompt = Bakwas output.
"""

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# ============================================
# 1. BASIC PROMPT TEMPLATE
# ============================================
# Sabse simple template — ek variable, ek output

basic_template = PromptTemplate(
    input_variables=["topic"],
    template="""You are a senior software architect with 15 years of experience.
Generate one technical interview question about {topic}.
The question should test deep understanding, not just bookish knowledge.

Question:"""
)

# Isko use kaise karein:
prompt = basic_template.format(topic="Microservices")
print("=" * 60)
print("1. BASIC TEMPLATE OUTPUT:")
print("=" * 60)
print(prompt)
print()

# ============================================
# 2. ADVANCED TEMPLATE - Multiple Variables
# ============================================
# Real app mein tujhe multiple variables chahiye honge

architecture_question_template = PromptTemplate(
    input_variables=["topic", "difficulty", "experience_years", "context"],
    template="""You are a principal software architect conducting a technical interview.

Candidate Profile:
- Experience: {experience_years} years
- Difficulty Level: {difficulty}

Generate ONE architecture interview question about: {topic}
Context/Scenario: {context}

Requirements for the question:
- Must be a real-world scenario, not theoretical
- Should have multiple valid approaches
- Must test system design thinking
- Include constraints (scale, latency, cost)

Format your response as:
QUESTION: [The actual question]
HINTS: [2-3 hints to guide thinking]
KEY_POINTS: [What a good answer should cover]
"""
)

prompt = architecture_question_template.format(
    topic="Database Sharding",
    difficulty="Senior",
    experience_years="6",
    context="E-commerce platform handling 10M daily orders"
)

print("=" * 60)
print("2. ADVANCED TEMPLATE OUTPUT:")
print("=" * 60)
print(prompt)
print()

# ============================================
# 3. CHAT PROMPT TEMPLATE (Important!)
# ============================================
# Modern LLMs chat format mein kaam karte hain:
# - System message: AI ko role do
# - Human message: User ka question
# - AI message: AI ka response
#
# Ye ChatGPT/Claude jaisa format hai

chat_template = ChatPromptTemplate.from_messages([
    # System message — AI ka role define karo
    ("system", """You are ArchMaster, an AI-powered architecture knowledge testing system.
Your role is to generate challenging but fair technical questions.
You adapt questions based on the candidate's experience level.
You focus on practical, real-world scenarios.
You are conducting this test for: {test_purpose}"""),
    
    # Human message — actual instruction
    ("human", """Generate a {difficulty} level question about {topic}.
    
The candidate has {experience_years} years of experience.
Focus area: {focus_area}

Remember: Real scenarios only. No textbook questions.""")
])

# Chat template se messages banao
messages = chat_template.format_messages(
    test_purpose="Self-assessment for architecture role",
    difficulty="Advanced",
    topic="Event-Driven Architecture",
    experience_years="6",
    focus_area="Handling eventual consistency in distributed systems"
)

print("=" * 60)
print("3. CHAT TEMPLATE OUTPUT:")
print("=" * 60)
for msg in messages:
    print(f"\n[{msg.type.upper()}]:")
    print(msg.content)
print()

# ============================================
# 4. TEMPLATE LIBRARY — Tere App ke liye
# ============================================
# Different types ke questions ke liye alag templates

TEMPLATES = {
    "lld": PromptTemplate(
        input_variables=["component", "constraints"],
        template="""Design a Low-Level Design for: {component}

Constraints: {constraints}

Your response should include:
1. Class diagram (describe classes and relationships)
2. Key design patterns used and WHY
3. API contracts
4. Error handling strategy
5. Thread safety considerations (if applicable)"""
    ),
    
    "hld": PromptTemplate(
        input_variables=["system", "scale", "requirements"],
        template="""Design a High-Level Architecture for: {system}

Scale: {scale}
Key Requirements: {requirements}

Your response should include:
1. System components and their responsibilities
2. Communication patterns (sync/async)
3. Data storage strategy
4. Scalability approach
5. Failure handling and recovery
6. Trade-offs in your design"""
    ),
    
    "design_pattern": PromptTemplate(
        input_variables=["scenario", "pattern_hint"],
        template="""Given this scenario: {scenario}

Suggested pattern to explore: {pattern_hint}

Questions:
1. Which design pattern(s) would you apply and why?
2. Show the implementation approach
3. What are the trade-offs?
4. When would you NOT use this pattern?"""
    ),
    
    "evaluate_answer": PromptTemplate(
        input_variables=["question", "answer", "experience_level"],
        template="""As a senior architect, evaluate this answer:

QUESTION: {question}
CANDIDATE'S ANSWER: {answer}
EXPECTED LEVEL: {experience_level}

Evaluate on:
1. Correctness (0-10)
2. Depth of understanding (0-10)
3. Practical applicability (0-10)
4. Trade-off awareness (0-10)

Provide:
- Overall score
- What was good
- What was missing
- Suggested improvements
- Resources to study"""
    )
}

# Template library use karo
print("=" * 60)
print("4. TEMPLATE LIBRARY DEMO:")
print("=" * 60)

# LLD question
lld_prompt = TEMPLATES["lld"].format(
    component="Rate Limiter for API Gateway",
    constraints="Must handle 100K requests/sec, distributed across 5 data centers"
)
print("\n[LLD QUESTION]:")
print(lld_prompt)

# HLD question
hld_prompt = TEMPLATES["hld"].format(
    system="Real-time Notification System like WhatsApp",
    scale="500M daily active users, 50B messages/day",
    requirements="< 100ms delivery, message ordering, offline support"
)
print("\n[HLD QUESTION]:")
print(hld_prompt)

print("\n" + "=" * 60)
print("NEXT STEP: Step 2 mein in templates ko AI model se connect karenge!")
print("Tab AI actually questions generate karega.")
print("=" * 60)
