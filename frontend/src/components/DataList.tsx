// src/components/DataList.tsx
import { useSupabaseData } from '../hooks/useSupabase'

interface DataItem {
  id: number
  name: string
  // その他の必要なフィールド
}

export function DataList() {
  const { data, loading, error } = useSupabaseData<DataItem>('class_rooms_score')

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <div>
      {data.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  )
}