import React, { useState } from "react";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const customerProfile = {
    name: "John Doe",
    devices: ["Laptop", "Smartphone"],
    current_plan: "Basic Internet",
    location: "New York, USA",
    issue: "Slow connection",
  };

  const handleSubmit = async () => {
    try {
      const res = await fetch("http://localhost:5000/api/recommendations", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ customer_profile: customerProfile, question: input }),
      });
      const data = await res.json();

      if (data.recommendation) {
        setResponse(data.recommendation);
      } else {
        setResponse("Error: " + (data.error || "Unknown error"));
      }
    } catch (error) {
      console.error("Error:", error);
      setResponse("Failed to fetch recommendation.");
    }
  };

  return (
    <div>
      <nav className="navbar background">
        <h1>Product Recommendation System</h1>
      </nav>
      <section className="section">
        <div className="box-main">
          <h1>Ask Your Question</h1>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your question..."
          />
          <button onClick={handleSubmit}>Submit</button>
          <div>
            <h2>Response:</h2>
            <p>{response}</p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default App;