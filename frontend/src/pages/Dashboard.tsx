import { useEffect, useState } from "react";
import { getDocuments, retryJob } from "../api/api";

export default function Dashboard() {
  const [docs, setDocs] = useState<any[]>([]);

  const fetchDocs = async () => {
    const data = await getDocuments();
    setDocs(data);
  };

  useEffect(() => {
    fetchDocs();
    const interval = setInterval(fetchDocs, 3000);
    return () => clearInterval(interval);
  }, []);

  const getColor = (status: string) => {
    if (status === "completed") return "green";
    if (status === "processing") return "orange";
    if (status === "failed") return "red";
    return "gray";
  };

  return (
    <div>
      <h2>📄 Documents</h2>

      {docs.map((doc) => (
        <div key={doc.id} style={{ border: "1px solid #ccc", padding: 10, margin: 10 }}>
          <p><b>{doc.filename}</b></p>

          <p style={{ color: getColor(doc.status) }}>
            Status: {doc.status}
          </p>

          <button onClick={() => retryJob(doc.id)}>Retry</button>

          <br />

          <a href={`http://<YOUR-IP>:8000/export/${doc.id}`} target="_blank">
            Export JSON
          </a>
        </div>
      ))}
    </div>
  );
}