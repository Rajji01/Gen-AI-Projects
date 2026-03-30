
from langchain_core.prompts import PromptTemplate

formatString="Rajat is a good Man {myvar}"
print(formatString.format(myvar="Best AI Engineer"))

langchain_template= PromptTemplate(
    input_variables=["topic"],
    template="tell me about {topic}"
)
langchain_result=langchain_template.format(topic="caching")
print(langchain_result)

template = PromptTemplate(
    input_variables=["topic"],
    template="What is {topic}?"
)
result = template.format(topic="Docker")
# Output: "What is Docker?"


chat = ChatPromptTemplate.from_messages([
    ("system", "Tu ek {role} hai"),    # AI ki personality
    ("human", "Bata {topic} ke baare mein")  # tera question
])
messages = chat.format_messages(role="interviewer", topic="Caching")


QUESTION_TEMPLATES = {} 
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

print("\n📘 LLD QUESTION:")
print("-" * 40)
print(QUESTION_TEMPLATES["lld"].format(
    component="Rate Limiter for Razorpay API Gateway",
    constraints="1 lakh requests/sec, distributed, multiple API keys"
))