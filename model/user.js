import mongoose, { Schema } from "mongoose";

const userSchema = new Schema(
  {
    userName:String,
    phoneNumber:String,
    Address:String,
    summary:String,
    documentSummary:String
  }
)

export const User = mongoose.model("LawUser", userSchema);