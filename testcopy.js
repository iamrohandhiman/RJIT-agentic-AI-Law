import dotenv from "dotenv";

dotenv.config();

const AUTH_TOKEN = process.env.AUTH_TOKEN;

// Simple Test Function to Make a Call
async function testCall(phoneNumber) {
  const headers = {
    Authorization: "org_dcfc26138fa927f0d050dbf1edcbdbecc8ac8572a4d3c24fe25687c6bf087923cb0c27d63b1cff5348e169",
    "Content-Type": "application/json",
  };

  const data = {
    phone_number: phoneNumber,
    task:   `Act like a friendly normal consultant speaking in simple terms reassuring simple poliet care like and help the perople asking leagal quesitons , you may only refer to the mentioned question you can additionaly use related info from the web which is not inclided[
        {
          eventName: "Petition District Legal Services Authority (DLSA) for Free Lawyer",
          description: "Go to the DLSA and apply for free legal representation under the Legal Services Authorities Act, 1987.",
          date: "2025-03-28",
          costEstimate: "Free",
          requiredDocuments: [
            "Aadhar card (for identity verification)",
            "Property ownership documents",
            "Income certificate (to prove financial hardship)",
            "FIR copy (if already filed, optional)"
          ],
          extraTips: [
            "Mention financial hardship explicitly in your application—it strengthens your case.",
            "If rejected, file a written appeal to the State Legal Services Authority (SLSA)."
          ],
          potentialDelays: "Waiting time for Legal Aid lawyer assignment.",
          alternativeRoute: "Seek pro bono assistance from NGOs or individual lawyers."
        },
        {
          eventName: "Complaint to District Magistrate & Land Revenue Office",
          description: "Submit a formal complaint requesting an investigation into fraudulent land transactions.",
          date: "2025-04-01",
          costEstimate: "Minimal (Stamp paper, photocopies)",
          requiredDocuments: [
            "Property ownership documents",
            "Electricity bills",
            "FIR copy (if filed, optional)"
          ],
          extraTips: [
            "Use registered post for submission—this prevents claims of lost paperwork.",
            "If ignored, file an RTI asking for case status."  
          ],
          potentialDelays: "Bureaucratic delays; lack of responsiveness.",
          alternativeRoute: "File a PIL in the High Court if all other avenues fail."
        },
        {
          eventName: "Seek temporary shelter and support from NGOs",
          description: "Seek shelter and basic necessities from NGOs while legal proceedings continue.",
          date: "2025-03-28 - Ongoing",
          costEstimate: "Free or minimal contribution depending on NGO resources",
          requiredDocuments: ["Proof of identity and address (if possible, optional)"],
          extraTips: [
            "Contact several NGOs to find one that best fits your needs.",
            "Maintain open communication with your caseworker."
          ],
          potentialDelays: "Finding suitable shelter and support.",
          alternativeRoute: "Seek assistance from local religious institutions or community centers."
        }
      ];`,
    model: "enhanced",
    language: "hi",
    voice: "29d08f5f-a879-41b7-b438-23666c7ffe51",
    max_duration: 12,
  };

  try {
    const response = await fetch("https://api.bland.ai/v1/calls", {
      method: "POST",
      headers: headers,
      body: JSON.stringify(data),
    });

    const responseBody = await response.json();
    return responseBody;
  } catch (error) {
    console.error("Error making call:", error);
    throw error;
  }
}

// Example usage
testCall("+918433754692")
  .then(response => console.log("Call Response:", response))
  .catch(error => console.error(error));
