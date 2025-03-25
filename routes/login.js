import express from "express"
import { User } from "../model/user.js"

const router = express.Router()

router.post("/api/v1/user/signup",async(req,res)=>{
  const data = req.body
  await User.create(data)
  res.send({msg:{
    status:"created",
    phoneNumber:data.phoneNumber
  }})
})

export default  router
