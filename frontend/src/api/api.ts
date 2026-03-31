const BASE_URL = "http://<YOUR-IP>:8000";

export const uploadFile = async (file: File) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BASE_URL}/upload`, {
    method: "POST",
    body: formData,
  });

  return res.json();
};

export const getDocuments = async () => {
  const res = await fetch(`${BASE_URL}/documents`);
  return res.json();
};

export const retryJob = async (id: number) => {
  await fetch(`${BASE_URL}/retry/${id}`, { method: "POST" });
};