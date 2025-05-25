import { useState } from 'react';
import { EvaluationPopup } from './EvaluationPopup';

export const Header = () => {
  const [isPopupOpen, setIsPopupOpen] = useState(false);

  return (
    <>
      <header className="bg-green-600 text-white shadow-md">
        <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
          <h1 className="text-xl font-bold">R3環境チェック</h1>
          <button 
            className="bg-green-700 text-white px-4 py-2 rounded-md hover:bg-green-800 transition-colors"
            onClick={() => setIsPopupOpen(true)}
          >
            評価基準
          </button>
        </div>
      </header>
      <EvaluationPopup 
        isOpen={isPopupOpen}
        onClose={() => setIsPopupOpen(false)}
      />
    </>
  );
};
