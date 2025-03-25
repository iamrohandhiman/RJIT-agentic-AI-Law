import express from "express"
const router = express.Router();
import {makeLegalCall} from "../utils/callEvent.js"
router.post("/api/v1/user/make-call", async (req, res) => {
  const { context } = req.body;
  let phoneNumber = "+918433754692"
  if (!phoneNumber || !context) {
    return res.status(400).json({ error: "Phone number and context are required." });
  }

  try {
    const result = await makeLegalCall(phoneNumber, context);
    res.json({ success: true, data: result });
  } catch (error) {
    res.status(500).json({ error: "Failed to make call", details: error.message });
  }
});

export default router;