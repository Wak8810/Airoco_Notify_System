import { useSupabaseData } from './hooks/useSupabase'
import { useState, useMemo } from 'react'
import { Header } from './components/header'
import { Footer } from './components/footer'

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

// 教室の表示順序を定義
const CLASSROOM_ORDER = ['R3-301', 'R3-401', 'R3-403']

// 星を表示する関数
const renderStars = (score: number) => {
  return '★'.repeat(score) + '☆'.repeat(3 - score)
}

// 前日の日付を取得する関数
const getYesterday = () => {
  const date = new Date()
  date.setDate(date.getDate() - 1)
  return date.toISOString().split('T')[0]
}

function App() {
  const { data, loading, error } = useSupabaseData<DataItem>('classroom_scores')
  const [selectedDate, setSelectedDate] = useState<string>(getYesterday())

  // データが存在する日付のリストを作成
  const availableDates = useMemo(() => {
    if (!data) return []
    const dates = new Set(data.map(item => item.date.slice(0, 10)))
    return Array.from(dates).sort().reverse()
  }, [data])

  // 選択された日付のデータのみをフィルタリング
  const filteredData = data?.filter(item => 
    item.date.slice(0, 10) === selectedDate
  )

  const groupedData = filteredData?.reduce((acc, item) => {
    if (!acc[item.classroom]) acc[item.classroom] = []
    acc[item.classroom].push(item)
    return acc
  }, {} as Record<string, DataItem[]>)

  const displayDate = selectedDate

  return (
    <div>
      <Header />
      <div className="p-4">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-bold">教室環境データ</h1>
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

        {displayDate && (
          <p className="mb-4 text-gray-600">
            表示日: {new Date(displayDate).toLocaleDateString('ja-JP', {
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
            ))}
          </div>
        ) : (
          <div>データが見つかりません</div>
        )}
      </div>
      <Footer />
    </div>
  )
}

export default App