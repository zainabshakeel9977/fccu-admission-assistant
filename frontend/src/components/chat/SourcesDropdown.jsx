import { useState } from "react";
import { ChevronDown, FileText, ExternalLink } from "lucide-react";

export default function SourcesDropdown({ sources }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="mt-2">
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-1.5 text-[11px] font-bold uppercase tracking-wider text-[#1F3C88] dark:text-[#FFB800] hover:opacity-80 transition-opacity"
      >
        <ChevronDown size={14} className={`transition-transform duration-200 ${open ? 'rotate-180' : ''}`} />
        View Sources ({sources.length})
      </button>

      {open && (
        <div className="mt-2 space-y-2 animate-in fade-in slide-in-from-top-1 duration-200">
          {sources.map((src, i) => (
            <div key={i} className="flex items-start gap-2 p-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-sm">
              <FileText size={14} className="text-slate-400 mt-0.5" />
              <div className="flex flex-col">
                <span className="text-xs font-medium text-slate-700 dark:text-slate-200 truncate max-w-[200px]">
                  {src.source_name}
                </span>
                <span className="text-[10px] text-slate-500">Page {src.page_number}</span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}