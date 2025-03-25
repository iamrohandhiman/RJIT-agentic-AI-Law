import mongoose from "mongoose"

export const connectDb =async()=>{
   try {
     await mongoose.connect("mongodb://localhost:27017/",{dbName:"law-db"}).then(console.log({msg:"db Connected"}))
   } catch (error) {
      console.log(error)
   } 
}