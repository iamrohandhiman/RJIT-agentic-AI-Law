import sys
import json
from phi.agent import Agent
from phi.model.google import Gemini

def callAgent(summary):
    agent = Agent(
        model=Gemini(id="gemini-1.5-flash", api_key="AIzaSyAGFeTbVXzUe1yUTVOn1dxZOPdwsz-fhtc"),
        instructions=(f""
        ),
    )


    formatted_prompt = f"""
    INCIDENT SUMMARY:
    {summary}

    INSTRUCTIONS:
    - Identify and list the most applicable legal sections.
    - Ensure sections are from IPC, CrPC, CPC, Rent Control Acts, or other Indian laws.
    - Clearly justify why each section applies.
    -explain why this is applicable in your case what in your case makes this applicable
    - Respond only in valid JSON format as per the schema.
    """

    answer = agent.run(formatted_prompt).content
    return answer  
if __name__ == "__main__":
    if len(sys.argv) > 1:
        summary = sys.argv[1]
        response = callAgent(summary)
        print(response)  
    else:
        print("No summary provided") 
