from haystack.components.builders import PromptBuilder

template = """
There are some QAs in Context below that you can learn thease knowledge to answer question given below.
just simply answer the question in one line.

Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{question}}
Answer:
"""

prompt_builder = PromptBuilder(template=template)
