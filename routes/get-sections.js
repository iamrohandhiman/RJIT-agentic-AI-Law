import express from "express";
import { spawn } from "child_process";
import { parseLegalSectionsResponse } from "../utils/jsonRgxParser.js";
const router = express.Router();

router.post("/api/v1/user/get-legal-sections", (req, res) => {
    const { summary } = req.body;

    if (!summary) {
        return res.status(400).json({ error: "Summary is required" });
    }

    const pythonProcess = spawn("python", ["legal_ai.py", summary]);

    let output = "";

    pythonProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    pythonProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });

    pythonProcess.on("close", () => {
        const pO = parseLegalSectionsResponse(output)
        res.send(pO); 
    });
});

export default router;
