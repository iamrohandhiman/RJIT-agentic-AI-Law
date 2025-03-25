import express from "express";

const API_URL = "https://api.bland.ai/v1/calls";
const AUTH_TOKEN = "org_dcfc26138fa927f0d050dbf1edcbdbecc8ac8572a4d3c24fe25687c6bf087923cb0c27d63b1cff5348e169"; // Direct API Key

/**
 * Makes an API call to Bland AI with a specified phone number and legal context.
 * @param {string} phoneNumber - The user's phone number.
 * @param {string} context - Custom legal guidance context for the AI task.
 * @returns {Promise<Object>} - The API response.
 */
export const makeLegalCall = async (phoneNumber, context) => {
  context= toString(context)
  console.log("I'm hit")
  const headers = {
    Authorization: `Bearer ${AUTH_TOKEN}`,
    "Content-Type": "application/json",
  };

  const data = {
    phone_number: phoneNumber,
    task: context,
    model: "enhanced",
    language: "hi",
    voice: "29d08f5f-a879-41b7-b438-23666c7ffe51",
    max_duration: 12,
  };

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers,
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(`API Request Failed: ${response.statusText}`);
    }

    const responseBody = await response.json();
    return responseBody;
  } catch (error) {
    console.error("Error making API call:", error.message);
    throw error;
  }
};