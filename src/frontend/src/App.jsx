import React, { useState, useEffect } from 'react';
import { Send, User, Bot } from 'lucide-react';

export default function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  // Simulate fetching from your Python backend
  const fetchResponse = async (userMessage) => {
    setLoading(true);
    try {
      // Replace with actual backend call
      // Example: const res = await fetch(`/api/chat?msg=${userMessage}`);
      // const data = await res.json();
      const data = `Simulated response for: "${userMessage}"`;
      setMessages((prev) => [...prev, { type: 'user', text: userMessage }, { type: 'bot', text: data }]);
    } catch (err) {
      setMessages((prev) => [...prev, { type: 'bot', text: 'Error fetching response.' }]);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    fetchResponse(input.trim());
    setInput('');
  };

  return (
    <div className="chat-container">
      <header className="chat-header">
        <h1>PROTEC17 🔗 Ask the Contract Pro</h1>
        <p>Get expert advice on contracts</p>
      </header>

      <div className="chat-messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.type}`}>
            {msg.type === 'user' ? <User className="icon" /> : <Bot className="icon" />}
            <span>{msg.text}</span>
          </div>
        ))}
        {loading && <div className="message bot">Loading...</div>}
      </div>

      <form className="chat-input" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Type your question..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit"><Send /></button>
      </form>

      <footer className="chat-footer">
        Built by union members ❤️
      </footer>
    </div>
  );
}
