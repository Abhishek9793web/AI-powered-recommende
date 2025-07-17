import React from 'react';

const RecommendationCard = ({ unit }) => {
  return (
    <div className="border rounded p-3 mb-3 shadow-md bg-gray-100">
      <p><strong>Unit ID:</strong> {unit.unit_id}</p>
      <p><strong>Blood Type:</strong> {unit.blood_type}</p>
      <p><strong>Score:</strong> {unit.score}</p>
      <p>
        <strong>Risk:</strong>{' '}
        <span className={unit.risk_level === 'Low Risk' ? 'text-green-600' : 'text-red-600'}>
          {unit.risk_level}
        </span>
      </p>
    </div>
  );
};

export default RecommendationCard;
