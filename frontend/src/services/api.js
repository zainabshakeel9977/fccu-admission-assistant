const API_URL = "http://127.0.0.1:8000/query";

export const sendQuery = async (question, program) => {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question,
      program,
    }),
  });

  if (!response.ok) {
    throw new Error("API Error");
  }

  return response.json();
};