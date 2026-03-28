import React from 'react';
import { 
  GraduationCap, 
  BookOpen, 
  Calendar, 
  Map, 
  Mail, 
  HelpCircle, 
  FileText,
  ChevronRight
} from 'lucide-react';

/**
 * Reusable component for Contact Links
 * Includes BOTH:
 * - mailto (default mail client)
 * - Gmail direct link (better UX)
 */
const ContactItem = ({ label, email, subject }) => {
  const mailtoLink = `mailto:${email}?subject=${encodeURIComponent(subject)}`;
  const gmailLink = `https://mail.google.com/mail/?view=cm&to=${email}&subject=${encodeURIComponent(subject)}`;

  return (
    <div className="flex flex-col gap-1 mb-4 last:mb-0">
      
      {/* Label */}
      <span className="text-xs font-semibold text-slate-700 dark:text-slate-300">
        {label}
      </span>

      {/* Email + Actions */}
      <div className="flex items-center gap-2 text-[11px] text-slate-500">
        
        {/* Mailto (default client) */}
        <a 
          href={mailtoLink}
          className="flex items-center gap-1 hover:text-[#1F3C88] dark:hover:text-[#FFB800] transition-colors"
        >
          <Mail size={12} />
          <span className="truncate">{email}</span>
        </a>

        {/* Divider */}
        <span className="text-slate-300">|</span>

        {/* Open in Gmail */}
        <a 
          href={gmailLink}
          target="_blank"
          rel="noopener noreferrer"
          className="text-[10px] text-blue-600 hover:underline"
        >
          Gmail
        </a>
      </div>
    </div>
  );
};

export default function Sidebar({ program, setProgram }) {
  
  const NavButton = ({ id, label, icon: Icon }) => (
    <button
      onClick={() => setProgram(id)}
      className={`group flex items-center justify-between w-full p-3 rounded-lg transition-all duration-200 mb-2 border ${
        program === id 
          ? "bg-[#1F3C88] text-white border-[#1F3C88] shadow-md" 
          : "bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border-slate-200 dark:border-slate-700 hover:border-[#FFB800] hover:bg-slate-50 dark:hover:bg-slate-700"
      }`}
    >
      <div className="flex items-center gap-3">
        <Icon 
          size={18} 
          className={program === id 
            ? "text-[#FFB800]" 
            : "text-slate-400 group-hover:text-[#1F3C88]"
          } 
        />
        <span className="font-medium text-sm">{label}</span>
      </div>
      <ChevronRight 
        size={14} 
        className={program === id 
          ? "opacity-100" 
          : "opacity-0 group-hover:opacity-100 transition-opacity"
        } 
      />
    </button>
  );

  const ResourceLink = ({ href, label, icon: Icon }) => (
    <li>
      <a 
        href={href} 
        target="_blank"
        rel="noopener noreferrer"
        className="flex items-center gap-3 p-2 rounded-md text-slate-600 dark:text-slate-400 hover:text-[#1F3C88] dark:hover:text-[#FFB800] hover:bg-blue-50 dark:hover:bg-slate-800 transition-colors text-sm"
      >
        <Icon size={16} className="shrink-0" />
        <span className="truncate">{label}</span>
      </a>
    </li>
  );

  return (
    <aside className="w-72 h-screen bg-slate-50 dark:bg-slate-900 border-r border-slate-200 dark:border-slate-800 flex flex-col sticky top-0">
      
      {/* Scrollable Content */}
      <div className="flex-1 overflow-y-auto custom-scrollbar">
        
        {/* Program Selection */}
        <div className="p-6">
          <h3 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-4">
            Admission Assistant
          </h3>
          <NavButton id="bachelors" label="Bachelor's" icon={GraduationCap} />
          <NavButton id="postgraduate" label="Postgraduate" icon={GraduationCap} />
        </div>

        <div className="h-px bg-slate-200 dark:bg-slate-800 mx-6" />

        {/* Resources */}
        <div className="p-6">
          <h3 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-4 flex items-center gap-2">
            <BookOpen size={14} /> Quick Resources
          </h3>
          <ul className="space-y-1">
            <ResourceLink href="https://www.fccollege.edu.pk/wp-content/uploads/2025/12/Bachelors-Catalog-2025-26-updated.pdf" label="Bachelors Catalog" icon={FileText} />
            <ResourceLink href="https://www.fccollege.edu.pk/wp-content/uploads/2025/12/PG-Catalog-25-26-dec.pdf" label="Postgraduate Catalog" icon={FileText} />
            <ResourceLink href="https://www.fccollege.edu.pk/wp-content/uploads/2025/09/List-of-majors-Bachelor-Admissions.pdf" label="List of Majors" icon={FileText} />
            <ResourceLink href="https://www.fccollege.edu.pk/academic-calendar/" label="Academic Calendar" icon={Calendar} />
            <ResourceLink href="https://www.youtube.com/watch?v=aAIlCqxXbtk" label="Campus Tour" icon={Map} />
          </ul>
        </div>

        {/* Contact Section */}
        <div className="p-6 border-t border-slate-200 dark:border-slate-800 bg-slate-100/50 dark:bg-slate-800/30">
          <h3 className="text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-4 flex items-center gap-2">
            <HelpCircle size={14} /> Need Help?
          </h3>
          
          <ContactItem 
            label="Admissions Office" 
            email="admissions@fccollege.edu.pk" 
            subject="Admission Inquiry"
          />
          <ContactItem 
            label="Financial Aid Office" 
            email="financialaid@fccollege.edu.pk" 
            subject="Financial Aid Inquiry"
          />
          <ContactItem 
            label="Accounts Office" 
            email="accounts@fccollege.edu.pk" 
            subject="Fee & Accounts Inquiry"
          />
          <ContactItem 
            label="Residential Life" 
            email="reslife@fccollege.edu.pk" 
            subject="Hostel & Housing Inquiry"
          />
        </div>
      </div>

      {/* Footer */}
      <div className="p-4 border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
        <p className="text-[10px] text-center text-slate-400">
          © 2026 Forman Christian College
        </p>
      </div>
    </aside>
  );
}