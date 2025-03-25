import express from "express";
import { spawn } from "child_process";
import { User } from "../model/user.js";

const router = express.Router();

router.post("/api/v1/user/generate-legal-document", async (req, res) => {
    let { event, phoneNumber } = req.body;

    if (!event || !phoneNumber) {
        return res.status(400).json({ error: "Event and phoneNumber are required" });
    }

    try {
        console.log(`Searching for user with phone number: ${phoneNumber}`);
        const user = await User.findOne({ phoneNumber });

        if (!user) {
            return res.status(404).json({ error: "User not found" });
        }

        // Extract only relevant user details
        const information = JSON.stringify({
            name: user.name,
            address: user.address,
            phone: user.phoneNumber,
        });

        console.log("User found:", information);
        console.log("Event:", event);

        // Spawn Python process to generate the legal document
        const pythonProcess = spawn("python", ["callAgent.py", event, information]);

        let output = "";

        pythonProcess.stdout.on("data", (data) => {
            output += data.toString();
        });

        pythonProcess.stderr.on("data", (data) => {
            console.error(`Error: ${data}`);
        });

        pythonProcess.on("close", () => {
            try {
                console.log("Generated Legal Document:\n", output);
                res.setHeader("Content-Type", "text/markdown");
                res.send(output); // Send the Markdown text as response
            } catch (error) {
                console.error("Processing error:", error);
                res.status(500).json({ error: "Failed to generate document" });
            }
        });
    } catch (error) {
        console.error("Database error:", error);
        res.status(500).json({ error: "Internal server error" });
    }
});

export default router;
