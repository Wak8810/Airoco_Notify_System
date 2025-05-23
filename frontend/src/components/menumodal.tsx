import type { ReactNode } from 'react';

interface MenuModalProps {
  isOpen: boolean;
  onClose: () => void;
  children: ReactNode;
}

export const MenuModal = ({ isOpen, onClose, children }: MenuModalProps) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-between">
        <div></div>
        <div
            className="fixed inset-0 bg-black/70 z-40"
            onClick={onClose}
        ></div>

        <div className="relative bg-white rounded-lg shadow-xl p-6 w-1/6 h-1/1 z-50">
            <button
            onClick={onClose}
            className="absolute top-2 right-2 p-1 text-gray-500 hover:text-gray-800 rounded-full"
            aria-label="閉じる"
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
            {children}
        </div>
    </div>
  );
};