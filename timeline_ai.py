import sys
import json
from datetime import datetime, timedelta
from phi.agent import Agent
from phi.model.google import Gemini

sys.stdout.reconfigure(encoding='utf-8')

def callAgent(summary):
    agent = Agent(
        model=Gemini(id="gemini-1.5-flash", api_key="AIzaSyAGFeTbVXzUe1yUTVOn1dxZOPdwsz-fhtc"),
        instructions=(
            "You are an expert in Indian law. Given the user's case details, generate three alternative legal timelines "
            "for resolving the issue. Each timeline should include events with realistic dates, a clear description of steps, "
            "cost estimates, required documents, and insider tips for navigating the legal system efficiently."
        ),
    )
    
    today = datetime.now()
    date1 = (today + timedelta(days=3)).strftime('%Y-%m-%d')
    date2 = (today + timedelta(days=7)).strftime('%Y-%m-%d')
    date3 = (today + timedelta(days=14)).strftime('%Y-%m-%d')
    date4 = (today + timedelta(days=30)).strftime('%Y-%m-%d')
    
    formatted_prompt = f"""
    INCIDENT SUMMARY:
    {summary}
    INSTRUCTIONS:
    - Generate three alternative legal timelines, starting from today's date ({today.strftime('%Y-%m-%d')}).
    - Each timeline should be structured as a JSON list under respective timeline categories.
    - Events must be **logically sequenced** based on real-life legal timelines in India.
    - Provide a **clear and tactical breakdown** at each step, covering:
      - **Cost estimates** (highlight free/low-cost options)
      - **Required documents** (listed under 'requiredDocuments' with 'templateNeeded' boolean for templatable items and 'isOptional' boolean for necessity: false for necessary, true for optional)
      - **Insider strategies** under 'extraTips' to overcome legal barriers
      - **Potential delays and how to counteract them**
      - **Alternative routes if a step faces resistance**
    - The response must be formatted as a **structured JSON**:
    {{
      "Timelines": {{
        "StandardLegalPath": [
          {{
            "eventName": "File an FIR & Seek Urgent Legal Aid",
            "description": "Go to the police station and file a **detailed** FIR citing IPC Sections 420, 467, 468, 471, 120B. Do NOT settle for a mere complaint—demand an FIR and insist on an acknowledgment receipt. If the police refuse, escalate the matter to the DCP or file a complaint with the Magistrate under CrPC 156(3). Meanwhile, approach a Legal Aid Society for immediate assistance to strengthen your case.",
            "date": "{date1}",
            "costEstimate": "Minimal (photocopying, transport); Legal Aid - Free",
            "requiredDocuments": [
              {{"document": "Original property registration papers", "templateNeeded": false, "isOptional": false}},
              {{"document": "Father's death certificate", "templateNeeded": false, "isOptional": true}},
              {{"document": "Electricity bills (as proof of long-term residence)", "templateNeeded": false, "isOptional": true}},
              {{"document": "Witness statements from neighbors", "templateNeeded": true, "isOptional": true}},
              {{"document": "Copies of fraudulent sale deed", "templateNeeded": false, "isOptional": false}}
            ],
            "extraTips": [
              "Bring a witness (NGO member, journalist, or community leader) for added pressure.",
              "If the police delay, send a written complaint via registered post for documentation.",
              "If still ignored, file an RTI request asking for case updates—this forces accountability."
            ]
          }},
          {{
            "eventName": "File a Civil Suit for Injunction & Possession",
            "description": "Without waiting, file a **civil suit under the Specific Relief Act, 1963**, requesting an injunction against any sale or alteration of the property. Seek immediate legal assistance to draft a solid affidavit proving your case. If necessary, apply for a waiver of court fees under the Legal Services Authorities Act, 1987.",
            "date": "{date2}",
            "costEstimate": "₹2,000 - ₹5,000 (Court fees, unless waived)",
            "requiredDocuments": [
              {{"document": "FIR copy", "templateNeeded": false, "isOptional": false}},
              {{"document": "Property registration documents", "templateNeeded": false, "isOptional": false}},
              {{"document": "Electricity bills", "templateNeeded": false, "isOptional": true}},
              {{"document": "Witness statements", "templateNeeded": true, "isOptional": true}},
              {{"document": "Fraudulent sale deed", "templateNeeded": false, "isOptional": false}}
            ],
            "extraTips": [
              "Use an **urgent hearing request** to speed up proceedings.",
              "Ensure the **suit is properly served** to all accused parties—this prevents delays.",
              "Keep track of hearing dates—courts often delay cases if petitioners are absent."
            ]
          }}
        ],
        "CheapestLegalOption": [
          {{
            "eventName": "Petition District Legal Services Authority (DLSA) for Free Lawyer",
            "description": "Go to the **District Legal Services Authority (DLSA)** and submit an application for **free legal representation** under the Legal Services Authorities Act, 1987. Ensure you carry all property-related documents. Legal Aid lawyers can assist in filing police complaints, civil suits, and injunctions at zero cost.",
            "date": "{date1}",
            "costEstimate": "Free",
            "requiredDocuments": [
              {{"document": "Aadhar card (for identity verification)", "templateNeeded": false, "isOptional": false}},
              {{"document": "Property ownership documents", "templateNeeded": false, "isOptional": false}},
              {{"document": "FIR copy (if already filed)", "templateNeeded": false, "isOptional": true}},
              {{"document": "Income certificate (if required for eligibility)", "templateNeeded": false, "isOptional": true}}
            ],
            "extraTips": [
              "Mention **financial hardship** in your application—it strengthens your case.",
              "If rejected, file a written appeal to the **State Legal Services Authority (SLSA)**.",
              "Legal aid lawyers can also file **RTIs & PILs** on your behalf."
            ]
          }},
          {{
            "eventName": "Complaint to District Magistrate & Land Revenue Office",
            "description": "Submit a formal complaint to the **District Magistrate & Revenue Office**, requesting an immediate investigation into the fraudulent transaction. Demand the **cancellation of illegal land records** and insist on a freeze on property transfers until legal resolution.",
            "date": "{date2}",
            "costEstimate": "Minimal (Stamp paper, photocopies)",
            "requiredDocuments": [
              {{"document": "Property ownership documents", "templateNeeded": false, "isOptional": false}},
              {{"document": "Electricity bills", "templateNeeded": false, "isOptional": true}},
              {{"document": "FIR copy", "templateNeeded": false, "isOptional": true}}
            ],
            "extraTips": [
              "Use **registered post** for submission—this prevents claims of lost paperwork.",
              "If ignored, file an **RTI** asking for case status—this forces them to act."
            ]
          }}
        ],
        "BureaucraticPressureTactic": [
          {{
            "eventName": "File a Complaint with the Anti-Corruption Bureau (ACB)",
            "description": "Suspect bribery in land record alterations? **File a complaint with the ACB**, requesting an internal investigation into potential corruption. This raises pressure on officials handling your case, increasing the likelihood of quicker action.",
            "date": "{date1}",
            "costEstimate": "Free",
            "requiredDocuments": [
              {{"document": "Land records showing alteration", "templateNeeded": false, "isOptional": false}},
              {{"document": "FIR copy (if filed)", "templateNeeded": false, "isOptional": true}},
              {{"document": "Complaint details", "templateNeeded": true, "isOptional": false}}
            ],
            "extraTips": [
              "Corruption complaints can be filed **anonymously** if you fear retaliation.",
              "Attach **any proof of bribery**—this speeds up action.",
              "If ignored, escalate to the **State Vigilance Commission**."
            ]
          }},
          {{
            "eventName": "File an RTI to Pressure Authorities",
            "description": "Submit an **RTI (Right to Information) request** to the Revenue Department asking for records of all land transactions, title changes, and survey modifications. Government officials **must respond within 30 days**, forcing them to disclose if fraud has taken place.",
            "date": "{date2}",
            "costEstimate": "₹10 (RTI filing fee)",
            "requiredDocuments": [
              {{"document": "Property ownership details", "templateNeeded": false, "isOptional": false}},
              {{"document": "FIR copy (if available)", "templateNeeded": false, "isOptional": true}}
            ],
            "extraTips": [
              "Request specific names of officers involved in land transactions—this creates accountability.",
              "If they refuse information, file an appeal with the **State Information Commission**."
            ]
          }},
          {{
            "eventName": "Expose the Fraud Through Local Media & NGOs",
            "description": "If authorities are slow to act, **contact local media and NGOs** to expose the issue. Fraudulent land deals often get fast-tracked once public pressure mounts.",
            "date": "{date3}",
            "costEstimate": "Free",
            "requiredDocuments": [
              {{"document": "Documents proving ownership", "templateNeeded": false, "isOptional": false}},
              {{"document": "FIR copy (if available)", "templateNeeded": false, "isOptional": true}},
              {{"document": "Evidence of legal inaction", "templateNeeded": true, "isOptional": true}}
            ],
            "extraTips": [
              "Focus on newspapers, TV news channels, and social media campaigns.",
              "Involve **local activist groups**—they often push authorities to act faster.",
              "If corruption is suspected, connect with the **Lokayukta Office** for action."
            ]
          }}
        ]
      }}
    }}
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