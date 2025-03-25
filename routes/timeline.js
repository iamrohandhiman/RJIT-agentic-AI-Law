import express from "express"
import { spawn } from "child_process";
import { parseLegalSectionsResponse } from "../utils/jsonRgxParser.js";
import { User } from "../model/user.js";

const router = express.Router();

router.post("/api/v1/user/get-timeline", async(req, res) => {
    const { chargesPressed ,phoneNumber} = req.body;
    const user = await User.findOne({phoneNumber:phoneNumber})
   
    const summary = user.summary

    if (!summary) {
        return res.status(400).json({ error: "Summary is required." });
    }

    const pythonProcess = spawn("python", ["timeline_ai.py", summary,chargesPressed]);

    let responseData = "";

    pythonProcess.stdout.on("data", (data) => {
        responseData += data.toString();
    });

    pythonProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });

    pythonProcess.on("close", (code) => {
        if (code === 0) {
            responseData = parseLegalSectionsResponse(responseData)
            res.send(responseData);
        } else {
            res.status(500).json({ error: "Python script execution failed." });
        }
    });
});



export default router;