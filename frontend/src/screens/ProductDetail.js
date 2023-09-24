import { Link } from "react-router-dom"
import { Rating } from "../components/Rating"
import { products } from "../products"
import { useParams } from "react-router-dom"
import "../assets/css/product_detail.css"



export const ProductDetail = () => {

    const { id } = useParams()

    const product = products.find((pro) => pro._id === id)
    return (
        <>
            <section className="section-1-detail">
                <div className="content-detail-product">
                    <img src={product.image} alt={product.name} />
                    <div>
                        <h3>
                            {product.name}
                        </h3>
                        <p>
                            Description: {product.description}
                        </p>
                        <Rating value={product.rating} text={`${product.numReviews}`} color={"#eee600"} />
                        <h4>$ {product.price}</h4>
                        <p>
                            {product.countInStock !== 0 ? "In stock" : "Out stock"}
                        </p>
                        <button className="butto-add-cart" disabled={product.countInStock === 0}>Add to cart</button>
                    </div>
                </div>
            </section>
        </>
    )
}