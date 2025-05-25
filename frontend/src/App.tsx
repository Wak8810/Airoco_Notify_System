import { useSupabaseData } from './hooks/useSupabase'
import { useState, useMemo } from 'react'
import { Header } from './components/header' 
import { Footer } from './components/footer'
import './css/tailwind.css'

interface DataItem {
  classroom: string
  date: string
  day_of_week: string
  period: number
  co2_score: number
  temperature_score: number
  humidity_score: number
  co2_value: number
  temperature_value: number
  humidity_value: number
  created_at: string
}

const CLASSROOM_ORDER = ['R3-301', 'R3-401', 'R3-403']

const renderStars = (score: number) => {
  return '★'.repeat(score) + '☆'.repeat(3 - score)
}

const getYesterdayOrTodayJST = () => {
  const now = new Date();
  const jstOffset = 9 * 60 * 60 * 1000;
  const nowJST = new Date(now.getTime() + jstOffset);
  const currentHourJST = nowJST.getHours();
  const dateToSet = new Date(now);
  if (currentHourJST < 20) {
    dateToSet.setDate(dateToSet.getDate() - 1);
  }

  const dayOfWeek = dateToSet.getDay();
  if (dayOfWeek === 0) { // 日曜日
    dateToSet.setDate(dateToSet.getDate() - 2);
  } else if (dayOfWeek === 6) { // 土曜日
    dateToSet.setDate(dateToSet.getDate() - 1);
  }

  return dateToSet.toISOString().split('T')[0];
};

function App() {
  const { data, loading, error } = useSupabaseData<DataItem>('classroom_scores')
  const [selectedDate, setSelectedDate] = useState<string>(getYesterdayOrTodayJST())

  const availableDates = useMemo(() => {
    if (!data) return []
    const dates = new Set(data.map(item => item.date.slice(0, 10)))
    return Array.from(dates)
      .filter(date => {
        const dayOfWeek = new Date(date).getDay()
        return dayOfWeek !== 0 && dayOfWeek !== 6
      })
      .sort()
      .reverse()
  }, [data])

  const filteredData = data?.filter(item => 
    item.date.slice(0, 10) === selectedDate
  )

  const groupedData = filteredData?.reduce((acc, item) => {
    if (!acc[item.classroom]) acc[item.classroom] = []
    acc[item.classroom].push(item)
    return acc
  }, {} as Record<string, DataItem[]>)

  return (
    <>
      <Header />
      <div>
        <div className="p-4">
          <div className="flex justify-between items-center mb-6">
            <h1 className="text-3xl font-bold">教室環境データ</h1>
            <div className="flex items-center gap-2">
              <label htmlFor="date-select" className="text-sm font-medium text-gray-700">
                日付を選択
              </label>
              <input
                type="date"
                id="date-select"
                value={selectedDate}
                onChange={(e) => setSelectedDate(e.target.value)}
                min={availableDates[availableDates.length - 1]}
                max={availableDates[0]}
                className="px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500"
              />
            </div>
          </div>

          {selectedDate && (
            <p className="mb-4 text-gray-600">
              表示日: {new Date(selectedDate).toLocaleDateString('ja-JP', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                weekday: 'long'
              })}
            </p>
          )}

          {loading && <div>Loading...</div>}
          {error && <div className="text-red-500">Error: {error.message}</div>}

          {groupedData && Object.keys(groupedData).length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {CLASSROOM_ORDER.map(classroom => (
                groupedData[classroom] && ( // groupedDataに教室が存在する場合のみレンダリング
                  <div key={classroom} className="bg-white shadow-md rounded-lg p-4 border">
                    <h2 className="text-lg font-bold text-green-800 mb-3">{classroom}</h2>
                    {groupedData[classroom]
                      .sort((a, b) => a.period - b.period)
                      .map(item => (
                        <div key={item.period} className="mb-4 p-3 bg-green-50 rounded-md">
                          <h3 className="font-semibold text-gray-700 mb-2">第{item.period}限</h3>
                          <div className="text-blue-800">
                            CO2: <span className="text-yellow-500">{renderStars(item.co2_score)}</span>
                            <span className="ml-1 text-gray-600 text-xs">({item.co2_value} ppm)</span>
                          </div>
                          <div className="text-red-800">
                            温度: <span className="text-yellow-500">{renderStars(item.temperature_score)}</span>
                            <span className="ml-1 text-gray-600 text-xs">({item.temperature_value} ℃)</span>
                          </div>
                          <div className="text-green-800">
                            湿度: <span className="text-yellow-500">{renderStars(item.humidity_score)}</span>
                            <span className="ml-1 text-gray-600 text-xs">({item.humidity_value} %)</span>
                          </div>
                        </div>
                      ))}
                  </div>
                )
              ))}
            </div>
          ) : (
            <div>データが見つかりません</div>
          )}
        </div>
      </div>
      <Footer />
    </>
  );
};

export default App