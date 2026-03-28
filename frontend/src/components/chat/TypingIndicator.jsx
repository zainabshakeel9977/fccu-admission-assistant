export default function TypingIndicator() {
  return (
    <div className="flex items-center gap-1.5 p-4 bg-slate-100 dark:bg-slate-800 w-fit rounded-2xl rounded-bl-none ml-4 mb-4">
      <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
      <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce [animation-delay:-0.15s]"></div>
      <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></div>
    </div>
  );
}