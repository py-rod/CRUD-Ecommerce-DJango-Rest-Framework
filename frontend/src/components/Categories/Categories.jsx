import { Link } from "react-router-dom";
import useFetchCategories from "../../hooks/useFetchCategories";


export const Categories = () => {
    const { categories, setCategories } = useFetchCategories()
    return (
        <>
            <div className="dropdown">
                <Link className="btn dropdown-toggle text-light" to="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Categories
                </Link>

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