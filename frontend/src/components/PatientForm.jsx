import React, { useState } from 'react';
import axios from 'axios';
import RecommendationCard from './RecommendationCard';

const dummyDonors = [
  {
    unit_id: "U1", blood_type: "B+", minor_antigens: ["K"], availability: true, is_fresh: true
  },
  {
    unit_id: "U2", blood_type: "B+", minor_antigens: ["E"], availability: true, is_fresh: true
  },
  {
    unit_id: "U3", blood_type: "B+", minor_antigens: [], availability: true, is_fresh: false
  }
];

const PatientForm = ({ patient }) => {
  const [recommendations, setRecommendations] = useState([]);

  const getMatches = async () => {
    const res = await axios.post('http://localhost:5000/recommend-units', {
      patient,
      donors: dummyDonors
    });
    setRecommendations(res.data.recommendations);
  };

  return (
    <div className="p-4">
      <h3 className="text-lg font-semibold">Extracted Patient Data:</h3>
      <pre className="bg-gray-200 p-2 rounded">{JSON.stringify(patient, null, 2)}</pre>
      <button className="bg-green-600 text-white px-4 py-2 mt-3" onClick={getMatches}>
        Get Recommendations
      </button>

      <div className="mt-4">
        {recommendations.map((unit, idx) => (
          <RecommendationCard key={idx} unit={unit} />
        ))}
      </div>
    </div>
  );
};

export default PatientForm;
