
import React, { useState } from "react";

const Card = () => {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse(null);
    try {
      const res = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      setResponse(
        data.type === "sql"
          ? Array.isArray(data.result) && data.result.length > 0
            ? (
                <table border="1" cellPadding="5" style={{ marginTop: 10 }}>
                  <thead>
                    <tr>
                      {Object.keys(data.result[0]).map((col) => (
                        <th key={col}>{col}</th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {data.result.map((row, idx) => (
                      <tr key={idx}>
                        {Object.values(row).map((val, i) => (
                          <td key={i}>{String(val)}</td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              )
            : <div>No records found.</div>
          : data.result
      );
    } catch (err) {
      setResponse("Error: " + err.message);
    }
    setLoading(false);
  };

  return (
    <div className="card">
      <h2>Chat Area</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Enter your question"
          style={{ width: "300px" }}
        />
        <button type="submit" disabled={loading} style={{ marginLeft: 8 }}>
          {loading ? "Loading..." : "Ask"}
        </button>
      </form>
      <div style={{ marginTop: 20 }}>{response && <div>{response}</div>}</div>
    </div>
  );
};

export default Card;
