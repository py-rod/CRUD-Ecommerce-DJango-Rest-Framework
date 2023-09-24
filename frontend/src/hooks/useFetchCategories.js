import { useState, useEffect } from "react"
import axios from "axios"


export const useFetchCategories = () => {
    const [categories, setCategories] = useState([])

    const getCategories = async () => {
        const { data } = await axios.get("http://127.0.0.1:8000/api/category/")
        setCategories(data)
    }

    useEffect(() => {

        getCategories()

    }, [])

    return {
        categories,
        setCategories
    }
}

export default useFetchCategories;