import {
    useQuery,
    useMutation,
  } from '@tanstack/react-query'
import axios from 'axios'

export const useGetResult = () => {
    return useQuery({
        queryKey: ["results"],
        queryFn: async () => {
            const res = await axios.get("http://localhost:8000/api/lstm/")
            return res.data
        },
        refetchOnWindowFocus: false,
        refetchInterval: 3000,
        refetchIntervalInBackground: false
    })
}