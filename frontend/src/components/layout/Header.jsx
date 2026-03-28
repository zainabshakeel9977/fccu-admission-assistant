import React from 'react';
import { GraduationCap } from 'lucide-react';

export default function Header() {
  return (
    <header className="bg-[#1F3C88] text-white shadow-lg z-10">
      <div className="max-w-[1920px] mx-auto px-6 py-3 flex items-center justify-between">
        
        {/* Brand/Logo Section */}
        <div className="flex items-center gap-4">
          <div className="relative group">
            {/* Logo Placeholder */}
            <div className="w-12 h-12 bg-white rounded-lg flex items-center justify-center shadow-inner group-hover:scale-105 transition-transform duration-200">
               <GraduationCap className="text-[#1F3C88]" size={28} />
            </div>
            {/* Subtle glow effect behind logo */}
            <div className="absolute inset-0 bg-white/20 blur-md rounded-lg -z-10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
          </div>

          <div className="flex flex-col">
            <h1 className="font-bold text-xl tracking-tight leading-none uppercase">
              Forman Christian College
            </h1>
            <span className="text-[10px] text-blue-200 font-medium tracking-[0.2em] uppercase mt-1">
              A Chartered University
            </span>
          </div>
        </div>

        {/* Action Section - Buttons removed for a cleaner look */}
        <div className="flex items-center gap-4">
          {/* Optional: You could place a Search icon or University Link here later */}
        </div>

      </div>
      
      {/* Decorative Gold Accent Bar */}
      <div className="h-1 w-full bg-[#FFB800]"></div>
    </header>
  );
}