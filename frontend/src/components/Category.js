import { Link } from "react-router-dom"
import useFetchCategories from "../hooks/useFetchCategories"


export const Category = () => {

    const { categories, setCategories } = useFetchCategories()


    return (
        <>
            <div className="dropdown">
                <button className="btn btn-success dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Categories
                </button>
                <ul className="dropdown-menu">
                    {categories.map(cate => {
                        return (
                            <li key={cate.id}><Link className="dropdown-item" to={`/category/${cate.id}`}>{cate.title}</Link></li>
                        )
                    })}
                </ul>
            </div>
        </>
    )
}