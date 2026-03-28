import { useState } from "react";
import Header from "./components/layout/Header";
import Sidebar from "./components/layout/Sidebar";
import ChatWindow from "./components/chat/ChatWindow";
import ChatInput from "./components/chat/ChatInput";
import { useChat } from "./hooks/useChat";

function App() {
  // 1. Program Selection State
  const [program, setProgram] = useState("bachelors");

  // 2. Custom Hook for Chat Logic
  const { messages, sendMessage, loading } = useChat(program);

  return (
    /* Main wrapper with fixed height and overflow control */
    <div className="h-screen flex flex-col overflow-hidden bg-white">
      
      {/* Header component (DarkMode props removed) */}
      <Header />

      <div className="flex flex-1 overflow-hidden bg-slate-50">
        
        {/* Sidebar for navigation and resources */}
        <Sidebar program={program} setProgram={setProgram} />

        {/* Main Content Area */}
        <main className="flex flex-col flex-1 relative min-w-0 bg-white">
          <ChatWindow 
            messages={messages} 
            loading={loading} 
            program={program} 
          />
          
          <ChatInput 
            onSend={sendMessage} 
            isLoading={loading} 
          />
        </main>
      </div>
    </div>
  );
}

export default App;