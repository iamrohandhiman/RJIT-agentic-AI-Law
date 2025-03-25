import mongoose, { Schema } from "mongoose";

const userSchema = new Schema(
  {
    userName:String,
    phoneNumber:String,
    Address:String
  }
)

export const User = mongoose.model("LawUser", userSchema);