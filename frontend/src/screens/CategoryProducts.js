import { Link } from "react-router-dom"
import { useParams } from "react-router-dom"
import { category } from "../category"
import { products } from "../products"
import { Rating } from "../components/Rating"
import "../assets/css/category_products.css"
import useFetchCategories from "../hooks/useFetchCategories"
export const CategoryProducts = () => {
    const { id } = useParams()
    const { categories, setCategories } = useFetchCategories()


    const veriCategory = categories.find((cate) => cate.id == id)
    // const categoryFind = category.find((cate) => cate._id == id)
    // const product = products.filter((produ) => produ.series == id)

    return (
        <>
            <h1>
                En categoria: {!veriCategory ? null : veriCategory.title}
            </h1>

            {/* <section className="section-1-category-products">
                <h1>{categoryFind.name}</h1>
                <ul className="content-category-products">
                    {product.map((prod) => (
                        <li key={prod._id}>

                            <div className="card" style={{ width: "18rem" }} key={prod._id}>
                                <Link to={`product/${prod._id}`}>
                                    <img src={prod.image} className="card-img-top" alt="..." />
                                </Link>
                                <div className="card-body">
                                    <h5 className="card-title">
                                        <Link to={`/product/${prod._id}`}>
                                            {prod.name}
                                        </Link>
                                    </h5>
                                    <div>
                                        <Rating value={prod.rating} text={`${prod.numReviews}`} color={'#f8e825'} />
                                    </div>
                                    <h2 className="text-center">$ {prod.price}</h2>
                                </div>
                            </div>
                        </li>
                    ))}
                </ul>
            </section> */}
        </>
    )
}