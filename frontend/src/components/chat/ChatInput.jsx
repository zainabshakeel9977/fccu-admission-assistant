import React, { useState } from "react";
import { SendHorizontal } from "lucide-react";

export default function ChatInput({ onSend, isLoading }) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (!text.trim() || isLoading) return;
    onSend(text);
    setText("");
  };

  // Allows user to press 'Enter' to send, but Shift+Enter for new lines if you switch to textarea later
  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="p-4 bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 shadow-[0_-4px_10px_rgba(0,0,0,0.03)]">
      <div className="max-w-4xl mx-auto">
        <div className="relative flex items-center">
          <input
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={isLoading}
            placeholder="Ask about admissions, fee structure, or eligibility..."
            className="w-full bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-slate-100 text-sm rounded-xl pl-4 pr-14 py-3 border-2 border-transparent focus:border-[#1F3C88] dark:focus:border-[#FFB800] focus:bg-white dark:focus:bg-slate-900 transition-all outline-none disabled:opacity-50"
          />
          
          <button
            onClick={handleSend}
            disabled={!text.trim() || isLoading}
            className={`absolute right-2 p-2 rounded-lg transition-all duration-200 ${
              !text.trim() || isLoading
                ? "text-slate-400 bg-transparent"
                : "text-white bg-[#1F3C88] hover:bg-[#162a61] shadow-md hover:scale-105 active:scale-95"
            }`}
          >
            <SendHorizontal size={20} />
          </button>
        </div>
        
        <p className="text-[10px] text-center text-slate-400 mt-3 italic">
          FCCU Admission Assistant can make mistakes. Verify important dates and fees on the official website.
        </p>
      </div>
    </div>
  );
}