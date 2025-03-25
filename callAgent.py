import sys
from phi.agent import Agent
from phi.model.google import Gemini

def callAgent(event, information):
    print(information)
    agent = Agent(
        model=Gemini(id="gemini-1.5-flash", api_key="AIzaSyAGFeTbVXzUe1yUTVOn1dxZOPdwsz-fhtc"),
        instructions=""
    )

    formatted_prompt = f"""
    INCIDENT SUMMARY:
    The user is facing the following issue: {event}. and here is information about person writing {information}
    
    Below is the **user’s provided information**, including **name, address, and phone number**, as well as any supporting documents: {information}

    TASK:
    - Write a **formal legal letter** addressed to the **appropriate authority** (e.g., Police Commissioner, Consumer Forum, Rent Tribunal, Municipal Corporation, Court).
    - Ensure that the letter follows **Indian legal frameworks**, referencing **IPC, CrPC, CPC, Rent Control Act, Consumer Protection Act, or other relevant laws**.
    - Extract the **user's name, address, and phone number** from the provided information and include them in the letter.
    - Clearly reference the **most applicable legal sections** and provide a **strong but concise justification** for why these laws apply.
    - Maintain a **polite yet firm tone**, emphasizing the urgency and seriousness of the matter.
    - Conclude with a **clear request for legal action, resolution, or investigation**.
    - **Ensure the response is in plain text formatted as Markdown** (no JSON, only a properly structured legal letter).
    
    RESPONSE FORMAT:
    - Return **only the full legal letter** as a **string in Markdown format**.
    - Ensure the letter follows **a proper legal format**, including **date, recipient, subject, body, and closing signature**.
    """

    answer = agent.run(formatted_prompt).content
    return answer  

if __name__ == "__main__":
    if len(sys.argv) > 2:
        event = sys.argv[1]
        information = sys.argv[2]
        response = callAgent(event, information)
        print(response)  
    else:
        print("Error: Missing required inputs (event, information)")
