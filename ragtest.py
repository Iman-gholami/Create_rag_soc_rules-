from openai import OpenAI

client = OpenAI(api_key="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")

VECTOR_STORE_ID = "vs_697dca4c483c8191b3469c2539a40761"  

resp = client.responses.create(
    model="gpt-4.1",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [VECTOR_STORE_ID]
    }],
    input="""
From the IDS rules knowledge base, list 20 rules related to scanning.
Return: rule_id, title, classtype, and why it matches (keywords/pcre/content).
"""
)

print(resp.output_text)
