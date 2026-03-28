import { useState } from "react";
import { Copy, Check, Info } from "lucide-react";
import SourcesDropdown from "./SourcesDropdown";

export default function MessageBubble({ message }) {
  const isUser = message.role === "user";
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(message.content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className={`flex flex-col mb-6 ${isUser ? "items-end" : "items-start"}`}>
      {/* Bubble */}
      <div
        className={`relative group max-w-[85%] sm:max-w-xl p-4 shadow-sm transition-all ${
          isUser
            ? "bg-[#FFB800] text-[#1F3C88] rounded-2xl rounded-tr-none font-medium"
            : "bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-100 dark:border-slate-700 rounded-2xl rounded-tl-none"
        }`}
      >
        <div className="text-sm leading-relaxed whitespace-pre-wrap">
          {message.content}
        </div>

        {/* Copy Button - appears on hover for cleaner UI */}
        {!isUser && (
          <button
            onClick={handleCopy}
            className="absolute -right-10 top-0 p-2 text-slate-400 hover:text-[#1F3C88] dark:hover:text-[#FFB800] opacity-0 group-hover:opacity-100 transition-opacity"
            title="Copy response"
          >
            {copied ? <Check size={16} className="text-green-500" /> : <Copy size={16} />}
          </button>
        )}
      </div>

      {/* Footer Info (Sources & Actions) */}
      {!isUser && (
        <div className="ml-1 mt-1">
          {message.sources && message.sources.length > 0 && (
            <SourcesDropdown sources={message.sources} />
          )}
        </div>
      )}
    </div>
  );
}