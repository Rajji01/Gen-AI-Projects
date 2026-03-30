# ArchMaster - Phase 1 Learning Notes (Hinglish)

## Step 1: Prompt Templates ✅

### Kya Sikha?

**Prompt Template** = Ek reusable saancha (mold) jisme variables daalke
AI ke liye instructions banate hain.

### 3 Types of Templates:

| Type | Kab Use Kare | Example |
|------|-------------|---------|
| `PromptTemplate` | Simple, single prompt | Question generate karna |
| `ChatPromptTemplate` | Chat format (system + human msg) | Jab AI ko role dena ho |
| `Template Library` | Multiple templates ek jagah | LLD, HLD, Pattern questions |

### Key Takeaways:
1. **Ache prompt = Acha output** — GenAI mein prompt engineering KING hai
2. **Variables use karo** — Hardcoded prompts mat likho, dynamic banao
3. **System message important hai** — AI ko clearly role do
4. **Format specify karo** — AI ko batao output kaisa chahiye

### Code Quick Reference:
```python
# Simple template
template = PromptTemplate(
    input_variables=["topic"],
    template="Question about {topic}"
)
result = template.format(topic="Microservices")

# Chat template (modern way)
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are {role}"),
    ("human", "Question about {topic}")
])
messages = chat_template.format_messages(role="Architect", topic="Caching")
```

### Tere App Mein Kaise Use Hoga:
- LLD questions ke liye → `lld` template
- HLD questions ke liye → `hld` template  
- Design patterns ke liye → `design_pattern` template
- Answer evaluate karne ke liye → `evaluate_answer` template

---

## Next: Step 2 — LLM Connection (AI se actually baat karna)
- Templates ko AI model se connect karenge
- FREE mein — bina API key ke (Ollama / HuggingFace)
- Tab REAL questions generate honge!
