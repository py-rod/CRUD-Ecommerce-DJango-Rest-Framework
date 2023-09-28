import { useFetchLimitProducts } from "../../hooks/useFetchProducts"
import "./limitproducts.css"

export const LimitProducts = () => {

    const { limitProducts, setLimitProducts } = useFetchLimitProducts()


    return (
        <>
            <section className="section-2-limit-all-products">
                <h2>All Products</h2>
                <ul>
                    {limitProducts.map(product => {
                        return (
                            <li key={product.id}>
                                {!product.image
                                    ?
                                    null
                                    :
                                    console.log(product.image)}
                            </li>
                        )
                    })}
                </ul>
            </section>
        </>
    )
}