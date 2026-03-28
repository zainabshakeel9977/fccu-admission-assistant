/** @type {import('tailwindcss').Config} */
export default {
  // Enables the class-based dark mode logic we implemented in App.jsx
  darkMode: 'class',
  
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  
  theme: {
    extend: {
      colors: {
        // Adding FCCU branding directly into your theme for easier use
        fccu: {
          blue: "#1F3C88",
          gold: "#FFB800",
          navy: "#162a61",
        }
      },
      // Custom scrollbar styling (used in Sidebar and ChatWindow)
      animation: {
        'fade-in': 'fadeIn 0.3s ease-out',
        'slide-up': 'slideUp 0.4s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  
  plugins: [
    // Recommended: run 'npm install tailwindcss-animate' for professional transitions
    require("tailwindcss-animate"),
  ],
};