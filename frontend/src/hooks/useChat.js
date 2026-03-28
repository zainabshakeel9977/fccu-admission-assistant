import { useState, useEffect } from "react";
import { sendQuery } from "../services/api";

export const useChat = (program) => {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  /**
   * Effect: Reset Chat History
   * This triggers whenever the 'program' (bachelors/postgraduate) changes.
   */
  useEffect(() => {
    setMessages([]);
  }, [program]);

  const sendMessage = async (text) => {
    // Prevent empty messages or sending while a request is already in progress
    if (!text.trim() || loading) return;

    const userMessage = { role: "user", content: text };
    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const data = await sendQuery(text, program);

      const botMessage = {
        role: "assistant",
        content: data.answer || "I'm sorry, I couldn't process that request.",
        sources: data.sources || [],
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      console.error("Chat API Error:", err);
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Error connecting to server. Please try again later.",
        },
      ]);
    } finally {
      // Using finally ensures loading is set to false even if an error occurs
      setLoading(false);
    }
  };

  return { messages, sendMessage, loading };
};