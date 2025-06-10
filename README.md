# NyayConnect: Your AI-Powered Legal Assistance Platform

**NyayConnect** is an innovative backend platform designed to democratize access to legal assistance in India. By leveraging cutting-edge AI and seamless integrations, it empowers users with tools to navigate complex legal scenarios, generate essential documents, understand applicable laws, and plan strategic legal action. This platform aims to bridge the gap between legal complexities and the common person, making initial legal support more accessible and understandable.

## Overview

Navigating the Indian legal system can be daunting, often requiring specialized knowledge and significant resources. NyayConnect addresses this challenge by providing an intelligent, automated, and user-friendly suite of services. Whether it's drafting a formal complaint, identifying relevant legal sections for a case, or strategizing the next steps, NyayConnect offers a crucial first line of support.

**This project is ideal for:**
*   Individuals seeking preliminary legal guidance.
*   Organizations looking to provide automated legal assistance.
*   Developers building comprehensive legal-tech solutions.

## Core Features

NyayConnect offers a robust set of features, all accessible via a well-defined API:

1.  **AI-Powered Legal Document Generation:**
    *   Dynamically generates formal legal letters (e.g., complaints to authorities) tailored to user-provided event descriptions and personal information.
    *   Ensures documents adhere to Indian legal frameworks and maintain a professional tone.
    *   Output is provided in easy-to-use Markdown format.

2.  **Intelligent Legal Section Identification:**
    *   Analyzes user-provided case summaries and supporting document details.
    *   Identifies the most applicable legal sections from IPC, CrPC, CPC, and other relevant Indian laws.
    *   Provides justifications for why each section applies, offering clarity to the user.

3.  **Strategic Legal Timeline Planning:**
    *   Generates multiple alternative legal timelines (e.g., Standard Path, Cheapest Option, Bureaucratic Pressure Tactics) based on the user's situation and charges they wish to press.
    *   Each timeline includes:
        *   Sequenced events with estimated dates.
        *   Detailed descriptions of each step.
        *   Cost estimates (highlighting low-cost/free options).
        *   Lists of required documents (specifying if templates are needed or if documents are optional).
        *   Actionable "insider tips" for navigating the legal system efficiently.

4.  **Automated Legal Assistance Calls:**
    *   Integrates with Bland AI to initiate automated calls providing legal guidance or information based on a given context.
    *   Supports Hindi language and customizable voice options for broader accessibility.

5.  **Secure User Management:**
    *   Provides a simple signup mechanism to store user details securely.
    *   User information (name, address, phone number) is used to personalize generated documents and services.

6.  **Database Integration:**
    *   Utilizes MongoDB to persist user data and relevant case information, ensuring continuity and personalized experiences.

## Technology Stack

*   **Backend:** Node.js, Express.js
*   **Database:** MongoDB with Mongoose ODM
*   **AI & NLP:** Python scripts leveraging Google's Gemini AI (via `phi-agent`) for:
    *   Legal Document Drafting
    *   Legal Clause Analysis
    *   Procedural Timeline Generation
*   **External API Integration:** Bland AI for automated telephonic assistance.
*   **Communication:** RESTful APIs
*   **Utilities:** `nodemailer` for potential email functionalities (e.g., sending generated documents).

## System Architecture

NyayConnect operates through a modular architecture:

1.  **Client (User Interface - not part of this backend project):** Interacts with the Node.js API.
2.  **Node.js (Express.js) API Server:**
    *   Handles incoming HTTP requests.
    *   Authenticates and authorizes requests (basic user lookup).
    *   Manages user data via MongoDB.
    *   Orchestrates AI tasks by spawning dedicated Python scripts.
    *   Communicates with external services like Bland AI.
3.  **Python AI Modules:**
    *   Receive specific tasks (e.g., document generation, section analysis) and data from the Node.js server.
    *   Utilize the Gemini Large Language Model to process information and generate intelligent, context-aware responses.
    *   Return structured output (JSON or Markdown) to the Node.js server.
4.  **MongoDB Database:** Stores user profiles, case summaries, and potentially other relevant data.
5.  **Bland AI Service:** External service invoked for making automated calls based on provided context.

   ## API Endpoints

All endpoints are prefixed with `/api/v1/user`.

---

### 1. User Signup

*   **Endpoint:** `POST /signup`
*   **Description:** Registers a new user in the system.
*   **Request Body:**
    ```json
    {
      "userName": "John Doe",
      "phoneNumber": "91XXXXXXXXXX",
      "address": "123 Main St, Anytown, India",
      "summary": "Initial case summary (optional)",
      "documentSummary": "Summary of documents (optional)"
    }
    ```
*   **Response:**
    ```json
    {
      "msg": {
        "status": "created",
        "phoneNumber": "91XXXXXXXXXX"
      }
    }
    ```

---

### 2. Generate Legal Document

*   **Endpoint:** `POST /generate-legal-document`
*   **Description:** Generates a formal legal document (e.g., a letter to an authority) based on an event and user's details.
*   **Request Body:**
    ```json
    {
      "event": "Description of the legal issue or event requiring a document.",
      "phoneNumber": "91XXXXXXXXXX" // User's registered phone number
    }
    ```
*   **Response:**
    *   **Content-Type:** `text/markdown`
    *   **Body:** Raw Markdown text of the generated legal letter.
    *   Example (structure):
        ```markdown
        [Your Name]
        [Your Address]
        [Your Phone Number]

        [Date]

        To,
        The [Appropriate Authority],
        [Address of Authority]

        Subject: [Subject of the Letter related to the 'event']

        Respected Sir/Madam,

        [Body of the letter detailing the issue, referencing relevant user information and legal context based on the 'event' and Indian law.]

        [Request for action or resolution.]

        Sincerely,
        [Your Name]
        ```

---

### 3. Get Legal Sections

*   **Endpoint:** `POST /get-legal-sections`
*   **Description:** Identifies and explains relevant Indian legal sections based on a case summary and document summary.
*   **Request Body:**
    ```json
    {
      "summary": "Detailed summary of the legal case/incident.",
      "phoneNumber": "91XXXXXXXXXX", // User's registered phone number
      "documentSummary": "Summary of any supporting documents provided by the user."
    }
    ```
*   **Response:**
    *   **Content-Type:** `application/json`
    *   **Body:** A JSON object detailing applicable legal sections and their justifications. (The exact structure depends on the `legal_ai.py` script's output format, typically a list of sections with explanations).
    *   Example (conceptual):
        ```json
        {
          "identifiedSections": [
            {
              "section": "IPC Section 420 (Cheating)",
              "justification": "This section is applicable because...",
              "relevanceToCase": "In your case, the act of [...] falls under this section."
            },
            // ... other sections
          ]
        }
        ```

---

### 4. Get Legal Timeline

*   **Endpoint:** `POST /get-timeline`
*   **Description:** Generates alternative legal timelines with steps, costs, documents, and tips for a given situation.
*   **Request Body:**
    ```json
    {
      "chargesPressed": "Specific charges the user wants to press or explore (e.g., 'fraud, property dispute').",
      "phoneNumber": "91XXXXXXXXXX" // User's registered phone number (to fetch their case summary)
    }
    ```
*   **Response:**
    *   **Content-Type:** `application/json`
    *   **Body:** A JSON object containing different timelines, each with a series of steps.
    *   Example (structure based on `timeline_ai.py` prompt):
        ```json
        {
          "Timelines": {
            "StandardLegalPath": [
              {
                "eventName": "File an FIR & Seek Urgent Legal Aid",
                "description": "Detailed steps...",
                "date": "YYYY-MM-DD",
                "costEstimate": "Minimal; Legal Aid - Free",
                "requiredDocuments": [
                  {"document": "Original property papers", "templateNeeded": false, "isOptional": false}
                  // ... more documents
                ],
                "extraTips": ["Bring a witness...", "File an RTI..."]
              }
              // ... more events
            ],
            "CheapestLegalOption": [ /* ... similar structure ... */ ],
            "BureaucraticPressureTactic": [ /* ... similar structure ... */ ]
          }
        }
        ```

---

### 5. Make Automated Call

*   **Endpoint:** `POST /make-call`
*   **Description:** Initiates an automated call via Bland AI to provide guidance based on the given context.
*   **Request Body:**
    ```json
    {
      "context": "The specific legal guidance or information to be conveyed in the call. This will be the task for the AI."
      // "phoneNumber": "The target phone number for the call." (Note: Currently hardcoded in the example, but ideally part of the request or fetched from user profile)
    }
    ```
*   **Response:**
    *   **Content-Type:** `application/json`
    *   **Body:** JSON response from the Bland AI API, indicating call status or details.
    *   Example (conceptual, actual response from Bland AI may vary):
        ```json
        {
          "success": true,
          "data": {
            "call_id": "c_xxxxxxxxxxxx",
            "status": "queued",
            // ... other details from Bland AI
          }
        }
        // Or error:
        {
          "error": "Failed to make call",
          "details": "Error message from Bland AI or internal error."
        }
        ```

---

### 6. Test Route

*   **Endpoint:** `GET /test`
*   **Description:** A simple test route to check if the server is running.
*   **Response:**
    ```json
    {
      "msg": "Working"
    }
    ```

---

## Getting Started

To set up and run this project locally, follow these general steps:

### Prerequisites

*   **Node.js:** Version 16.x or higher.
*   **npm:** (Usually comes with Node.js).
*   **MongoDB:** A running instance of MongoDB.
*   **Python:** Version 3.x, with `pip` for installing packages.
*   **API Keys:**
    *   **Gemini API Key:** For the Python AI scripts.
    *   **Bland AI Auth Token:** For the automated call feature.

### Installation

1.  **Clone the repository (if applicable):**
    ```bash
    # git clone <repository-url>
    # cd <project-directory>
    ```
2.  **Install Node.js dependencies:**
    ```bash
    npm install
    ```
3.  **Install Python dependencies:**
    The Python scripts use the `phi-agent` library and its dependencies (like `google-generativeai`). Ensure these are installed in your Python environment.
    ```bash
    # Example:
    # pip install phidata google-generativeai
    ```

### Configuration

1.  **Environment Variables:**
    Create a `.env` file in the root of the project directory and add the following variables:
    ```env
    MONGO_URI=mongodb://localhost:27017/law-db # Your MongoDB connection string
    PORT=5000 # Port for the Node.js server

    # For utils/callEvent.js (Bland AI) - Ideally, move this to .env
    BLAND_AI_AUTH_TOKEN=your_bland_ai_auth_token

    # For Python scripts (Gemini AI) - These should be accessed by Python scripts via os.environ, not hardcoded.
    GEMINI_API_KEY=your_gemini_api_key
    ```
    *Note: The current Python scripts and `callEvent.js` might have API keys hardcoded. It is strongly recommended to modify them to read keys from environment variables for security.*

2.  **Database Connection:**
    Ensure your MongoDB server is running and accessible at the `MONGO_URI` specified. The application will create the `law-db` database if it doesn't exist.

### Running the Server

1.  **Start the Node.js application:**
    ```bash
    npm start # Or your configured script, e.g., node index.js
    ```
    The server should start, and you'll see a console message indicating it's running on the configured port (e.g., `server running on port 5000`).

## Python AI Modules

The core intelligence of NyayConnect resides in its Python scripts, which interface with Google's Gemini AI:

*   **`callAgent.py` (for Document Generation):**
    *   Takes an `event` description and user `information` (name, address, phone).
    *   Prompts Gemini to draft a formal legal letter in Markdown, adhering to Indian legal standards.
*   **`legal_ai.py` (for Legal Section Identification):**
    *   Receives a case `summary` and `documentSummary`.
    *   Instructs Gemini to identify and justify relevant Indian legal sections (IPC, CrPC, etc.).
    *   Designed to output in a structured JSON format.
*   **`timeline_ai.py` (for Legal Timeline Generation):**
    *   Accepts a case `summary` and `chargesPressed`.
    *   Prompts Gemini to generate three distinct legal timelines (Standard, Cheapest, Bureaucratic Pressure).
    *   Each timeline is detailed with events, dates, costs, required documents, and strategic tips, formatted as JSON.

These scripts are invoked as child processes by the Node.js backend, allowing for seamless integration of Python's AI capabilities into the JavaScript environment.

## Project Impact & Future Vision

**NyayConnect** stands as a testament to how technology, particularly AI, can be harnessed to address real-world challenges. By simplifying access to preliminary legal information and tools, this platform has the potential to:

*   **Empower Individuals:** Provide users with a better understanding of their legal standing and options.
*   **Increase Accessibility:** Offer initial legal support to those who might otherwise lack resources or knowledge.
*   **Streamline Processes:** Automate the generation of common legal documents and provide strategic planning tools.
*   **Serve as a Foundation:** Act as a robust backend for more comprehensive legal-tech applications.

**Future Enhancements could include:**

*   **Multilingual Support:** Expanding AI interactions and document generation to more Indian languages.
*   **Advanced Document Customization:** Allowing users more granular control over document content.
*   **Integration with Legal Professionals:** Creating pathways for users to connect with lawyers after initial AI-assisted guidance.
*   **Case Management Features:** Basic tools for users to track their legal journey.
*   **Enhanced AI Reasoning:** Utilizing more advanced AI models for deeper legal analysis and prediction.
*   **Email Notifications:** Integrating the `sendEmail.js` utility to send generated documents or important updates to users.

This project showcases a practical application of AI in the legal domain, offering a valuable service with significant potential for growth and impact.
