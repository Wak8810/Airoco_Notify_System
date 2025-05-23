import { useState, useEffect } from 'react'
import { supabase } from '../lib/supabase'

export function useSupabaseData<T>(tableName: string) {
  const [data, setData] = useState<T[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    async function fetchData() {
      try {
        const { data, error } = await supabase
          .from(tableName)
          .select('*')
        
        if (error) throw error
        
        setData(data)
      } catch (e) {
        setError(e as Error)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [tableName])

  return { data, loading, error }
}