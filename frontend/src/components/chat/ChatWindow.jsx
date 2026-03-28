import React, { useEffect, useRef } from "react";
import { Info, MessageSquare } from "lucide-react";
import MessageBubble from "./MessageBubble";
import TypingIndicator from "./TypingIndicator";

export default function ChatWindow({ messages, loading, program }) {
  const scrollRef = useRef(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTo({
        top: scrollRef.current.scrollHeight,
        behavior: "smooth",
      });
    }
  }, [messages, loading]);

  return (
    <div ref={scrollRef} className="flex-1 overflow-y-auto bg-slate-50 px-4 py-8 custom-scrollbar">
      <div className="max-w-4xl mx-auto flex flex-col min-h-full">
        
        {/* Info Box */}
        <div className="flex items-start gap-3 p-4 mb-8 bg-blue-50 border border-blue-100 rounded-xl">
          <Info size={18} className="text-[#1F3C88] shrink-0 mt-0.5" />
          <p className="text-xs text-slate-600 leading-relaxed italic">
            <span className="font-bold text-[#1F3C88] capitalize">Disclaimer:</span> Responses are generated from official university content. For personalized or case-specific queries, please contact the FCCU Admissions Office directly.
            Currently assisting with <span className="font-bold text-[#1F3C88] capitalize">{program}</span> admissions.
          </p>
        </div>

        {/* Welcome State (Shows when messages array is empty) */}
        {messages.length === 0 && !loading && (
          <div className="flex-1 flex flex-col items-center justify-center text-center py-20 animate-in fade-in duration-700">
            <div className="w-16 h-16 bg-slate-200 rounded-full flex items-center justify-center mb-4">
              <MessageSquare size={32} className="text-slate-400" />
            </div>
            <h3 className="text-lg font-semibold text-slate-700">
              FCCU {program === 'bachelors' ? "Bachelors" : "Postgraduate"} Assistant
            </h3>
            <p className="text-sm text-slate-500 max-w-xs">
              How can I help you with your {program} admission process today?
            </p>
          </div>
        )}

        {/* Chat Bubbles */}
        <div className="flex-1">
          {messages.map((msg, i) => (
            <MessageBubble key={i} message={msg} />
          ))}
          {loading && <TypingIndicator />}
        </div>
      </div>
    </div>
  );
}