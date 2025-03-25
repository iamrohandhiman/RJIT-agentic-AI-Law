import express from  "express"
import dotenv from "dotenv"
import cookieParser from "cookie-parser"
import mongoose from "mongoose"
import cors from "cors"
import { connectDb } from "./utils/db.js"
import loginRoute from "./routes/login.js"
import legalSections from "./routes/get-sections.js"
import getTimeline from "./routes/timeline.js"
import callevent from "./routes/help-call.js"
import genDoc from "./generateDoc.js"
connectDb()
dotenv.config()

const app = express()
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(cors());

app.use(callevent)
app.use(genDoc)
app.use(legalSections)
app.use(loginRoute)
app.use(getTimeline)

const port = process.env.MONGO_URI || 5000

app.get("/api/v1/user/test",(req,res,next)=>{
  res.json({msg:"Working"})
})



app.listen(port,()=>{
  console.log(`server running on port ${port}`)
})