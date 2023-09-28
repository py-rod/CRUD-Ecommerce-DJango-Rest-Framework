import { Link } from "react-router-dom"
import { Categories } from "../Categories/Categories"
export const NavBar = () => {
    return (
        <>
            <header>
                <nav className="navbar navbar-expand-lg bg-primary navbar-dark">
                    <div className="container-fluid">
                        <Link className="navbar-brand" to="/">Ecommerce</Link>
                        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                            <span className="navbar-toggler-icon"></span>
                        </button>

                        {/* CATEGORIES */}
                        <Categories />

                        <div className="collapse navbar-collapse" id="navbarNav">
                            <ul className="navbar-nav ms-auto">
                                <li className="nav-item">
                                    <Link className="nav-link active" aria-current="page" to="/cart">Cart</Link>
                                </li>
                                <li className="nav-item">
                                    <Link className="nav-link active" aria-current="page" to="/account">Acoount</Link>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </header>
        </>
    )
}