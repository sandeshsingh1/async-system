import { useState } from "react";
import { uploadFile } from "../api/api";

export default function Upload() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    await uploadFile(file);
    alert("Uploaded!");
    setLoading(false);
  };

  return (
    <div>
      <h2>⬆ Upload</h2>

      <input type="file" onChange={(e) => setFile(e.target.files![0])} />

      <button onClick={handleUpload}>
        {loading ? "Uploading..." : "Upload"}
      </button>
    </div>
  );
}