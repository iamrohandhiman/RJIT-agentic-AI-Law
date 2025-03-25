import sys
import json
from phi.agent import Agent
from phi.model.google import Gemini

def callAgent(summary):
    agent = Agent(
        model=Gemini(id="gemini-1.5-flash", api_key="AIzaSyAGFeTbVXzUe1yUTVOn1dxZOPdwsz-fhtc"),
        instructions=(
            "You are an expert in Indian law. Given the user's case details, identify the most relevant legal sections "
            "from the Indian Penal Code (IPC), Criminal Procedure Code (CrPC), Civil Procedure Code (CPC), Rent Control Acts, "
            "or any other applicable laws. \n"
            "Ensure the response is in structured JSON format, strictly following this schema:\n\n"
            "{\n"
            '  "sectionsApplicable": [\n'
            '    {\n'
            '      "sectionName": "Section eviction under Rent Control Act",\n'
            '      "reason": "The landlord seeks eviction due to non-payment of rent exceeding 6 months, as per the Rent Control Act applicable in the respective state."\n'
            '    },\n'
            '    {\n'
            '      "sectionName": "Section 420 IPC - Cheating",\n'
            '      "reason": "The tenant has deliberately issued false rental agreements and refused to pay, constituting fraud under Section 420 IPC."\n'
            '    }\n'
            "  ]\n"
            "}\n"
            "Only provide valid sections with proper justifications. Avoid irrelevant or excessive details."
        ),
    )


    formatted_prompt = f"""
    INCIDENT SUMMARY:
    {summary}

    INSTRUCTIONS:
    - Identify and list the most applicable legal sections.
    - Ensure sections are from IPC, CrPC, CPC, Rent Control Acts, or other Indian laws.
    - Clearly justify why each section applies.
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
