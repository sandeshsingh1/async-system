import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

type Doc = {
  id: number;
  filename: string;
  status: string;
};

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [docs, setDocs] = useState<Doc[]>([]);
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("all");

  const API = "http://localhost:8000";

  // 📥 Upload
  const uploadFile = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    await axios.post(`${API}/upload`, formData);
    fetchDocs();
  };

  // 📄 Fetch
  const fetchDocs = async () => {
    const res = await axios.get(`${API}/documents`);
    setDocs(res.data);
  };

  useEffect(() => {
    fetchDocs();
    const interval = setInterval(fetchDocs, 2000);
    return () => clearInterval(interval);
  }, []);

  // 🎨 Status style
  const getStatusClass = (status: string) => {
    switch (status) {
      case "completed":
        return "status completed";
      case "processing":
      case "parsing":
      case "extracting":
        return "status processing";
      case "failed":
        return "status failed";
      default:
        return "status pending";
    }
  };

  // 📊 Progress mapping
  const getProgress = (status: string) => {
    switch (status) {
      case "processing":
        return 30;
      case "parsing":
        return 50;
      case "extracting":
        return 75;
      case "completed":
        return 100;
      case "failed":
        return 100;
      default:
        return 10;
    }
  };

  // 🔍 Filter
  const filteredDocs = docs.filter((d) => {
    const matchSearch = d.filename
      .toLowerCase()
      .includes(search.toLowerCase());
    const matchFilter = filter === "all" || d.status === filter;
    return matchSearch && matchFilter;
  });

  // 🔁 Retry
  const retryDoc = async (id: number) => {
    await axios.post(`${API}/retry/${id}`);
  };

  // 📤 Export
  const exportDoc = async (id: number) => {
    const res = await axios.get(`${API}/export/${id}`);
    alert(JSON.stringify(res.data, null, 2));
  };

  return (
    <div className="container">
      <h1>📄 Async Document System</h1>

      {/* Upload */}
      <div className="card">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
        />
        <button onClick={uploadFile}>Upload</button>
      </div>

      {/* Search + Filter */}
      <div className="card">
        <input
          placeholder="Search filename..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select onChange={(e) => setFilter(e.target.value)}>
          <option value="all">All</option>
          <option value="pending">Pending</option>
          <option value="processing">Processing</option>
          <option value="parsing">Parsing</option>
          <option value="extracting">Extracting</option>
          <option value="completed">Completed</option>
          <option value="failed">Failed</option>
        </select>
      </div>

      {/* Table */}
      <div className="card">
        <h2>Documents</h2>

        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Filename</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {filteredDocs.map((d) => (
              <tr key={d.id}>
                <td>{d.id}</td>
                <td>{d.filename}</td>

                <td>
                  <span className={getStatusClass(d.status)}>
                    {d.status}
                  </span>

                  {/* Progress */}
                  <div className="progress-bar">
                    <div
                      className="progress-fill"
                      style={{ width: `${getProgress(d.status)}%` }}
                    />
                  </div>
                </td>

                <td>
                  <button onClick={() => retryDoc(d.id)}>Retry</button>
                  <button onClick={() => exportDoc(d.id)}>Export</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;