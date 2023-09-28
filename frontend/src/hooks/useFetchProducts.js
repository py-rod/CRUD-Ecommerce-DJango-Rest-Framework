import { useState, useEffect } from "react"
import axios from "axios"


export const useFetchAllProducts = () => {
    const [products, setAllProducts] = useState([])

    const getAllProducts = async () => {
        const { data } = await axios.get("http://127.0.0.1:8000/api/products/")
        setAllProducts(data)
    }

    useEffect(() => {

        getAllProducts()

    }, [])

    return {
        products,
        setAllProducts
    }
}




export const useFetchLimitProducts = () => {
    const [limitProducts, setLimitProducts] = useState([])

    const getLimitProducts = async () => {
        const { data } = await axios.get("http://127.0.0.1:8000/api/products/")
        const limit = data.slice(0, 6)
        setLimitProducts(limit)
    }

    useEffect(() => {
        getLimitProducts()
    }, [])

    return {
        limitProducts,
        setLimitProducts
    }
}