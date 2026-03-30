
from langchain_core.prompts import PromptTemplate

formatString="Rajat is a good Man {myvar}"
print(formatString.format(myvar="Best AI Engineer"))

langchain_template= PromptTemplate(
    input_variables=["topic"],
    template="tell me about {topic}"
)
langchain_result=langchain_template.format(topic="caching")
print(langchain_result)