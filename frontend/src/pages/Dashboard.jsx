import React, { useState } from 'react';
import UploadReport from '../components/UploadReport';
import PatientForm from '../components/PatientForm';

const Dashboard = () => {
  const [patientData, setPatientData] = useState(null);

  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Smart Blood Matching Dashboard</h1>
      <UploadReport onExtract={setPatientData} />
      {patientData && <PatientForm patient={patientData} />}
    </div>
  );
};

export default Dashboard;
