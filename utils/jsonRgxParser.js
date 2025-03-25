export function parseLegalSectionsResponse(responseString) {
    try {
        // Extract JSON content inside code block if exists
        const jsonMatch = responseString.match(/```json\s*([\s\S]*?)\s*```/);
        const jsonString = jsonMatch ? jsonMatch[1] : responseString;

        // Parse JSON safely
        return JSON.parse(jsonString);
    } catch (error) {
        console.error("Failed to parse JSON:", error);
        return { error: "Invalid JSON format" };
    }
}