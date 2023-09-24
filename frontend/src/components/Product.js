import products from "../products"
import "../assets/css/product.css"
import { Rating } from "./Rating"
import { Link } from "react-router-dom"




export const Product = () => {



    return (
        <>
            <ul className="content-products">
                {products.map(product => {
                    return (
                        <li key={product._id}>

                            <div className="card" style={{ width: "18rem" }} key={product._id}>
                                <Link to={`category/${product.series}/product/${product._id}`}>
                                    <img src={product.image} className="card-img-top" alt="..." />
                                </Link>
                                <div className="card-body">
                                    <h5 className="card-title">
                                        <Link to={`/product/${product._id}`}>
                                            {product.name}
                                        </Link>
                                    </h5>
                                    <div>
                                        <Rating value={product.rating} text={`${product.numReviews}`} color={'#f8e825'} />
                                    </div>
                                    <h2 className="text-center">$ {product.price}</h2>
                                </div>
                            </div>
                        </li>
                    )
                })}
            </ul>
        </>
    )
}