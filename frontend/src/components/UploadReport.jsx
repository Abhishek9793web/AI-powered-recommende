import React, { useState } from 'react';
import axios from 'axios';

const UploadReport = ({ onExtract }) => {
  const [reportText, setReportText] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://localhost:5000/parse-report', {
      report_text: reportText
    });
    onExtract(res.data);
  };

  return (
    <form onSubmit={handleSubmit} className="p-4">
      <textarea
        rows="6"
        className="w-full border p-2"
        placeholder="Paste transfusion report here..."
        value={reportText}
        onChange={(e) => setReportText(e.target.value)}
      />
      <button className="mt-2 px-4 py-2 bg-blue-600 text-white">Extract Info</button>
    </form>
  );
};

export default UploadReport;
