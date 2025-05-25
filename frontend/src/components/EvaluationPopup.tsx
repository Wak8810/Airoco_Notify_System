import { useEffect } from 'react';

interface EvaluationPopupProps {
  isOpen: boolean;
  onClose: () => void;
}

const renderStars = (score: number) => {
  return '★'.repeat(score) + '☆'.repeat(3 - score);
};

export const EvaluationPopup = ({ isOpen, onClose }: EvaluationPopupProps) => {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }

    return () => {
      document.body.style.overflow = 'unset';
    };
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 max-w-lg w-full mx-4">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-bold text-gray-800">評価基準</h2>
          <button
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
        <div className="space-y-4">
          <div>
            <h3 className="font-semibold text-blue-800 mb-2">CO2濃度</h3>
            <div className="space-y-1">
              <p><span className="text-yellow-500">{renderStars(3)}</span>: 800ppm未満</p>
              <p><span className="text-yellow-500">{renderStars(2)}</span>: 800-1000ppm</p>
              <p><span className="text-yellow-500">{renderStars(1)}</span>: 1000ppm以上</p>
            </div>
          </div>
          <div>
            <h3 className="font-semibold text-red-800 mb-2">温度</h3>
            <div className="space-y-1">
              <p><span className="text-yellow-500">{renderStars(3)}</span>: 20-26℃</p>
              <p><span className="text-yellow-500">{renderStars(2)}</span>: 26-28℃ または 18-20℃</p>
              <p><span className="text-yellow-500">{renderStars(1)}</span>: 28℃以上 または 18℃未満</p>
            </div>
          </div>
          <div>
            <h3 className="font-semibold text-green-800 mb-2">湿度</h3>
            <div className="space-y-1">
              <p><span className="text-yellow-500">{renderStars(3)}</span>: 40-60%</p>
              <p><span className="text-yellow-500">{renderStars(2)}</span>: 60-70% または 30-40%</p>
              <p><span className="text-yellow-500">{renderStars(1)}</span>: 70%以上 または 30%未満</p>
            </div>
          </div>
          <p className="text-sm text-gray-500">参考: <a href="https://www.mhlw.go.jp/content/10900000/000616069.pdf" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">厚生労働省の基準</a></p>
        </div>
      </div>
    </div>
  );
}; 