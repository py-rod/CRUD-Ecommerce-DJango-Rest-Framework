import { Link } from "react-router-dom"
import { Category } from "./Category"
export const Header = () => {
    return (
        <>
            <header>
                <nav className="navbar navbar-expand-lg bg-primary navbar-dark">
                    <div className="container-fluid">
                        <Link className="navbar-brand" to="/">Ecommerce</Link>
                        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                            <span className="navbar-toggler-icon"></span>
                        </button>
                        <div className="collapse navbar-collapse" id="navbarNav">
                            <Category />
                            <ul className="navbar-nav ms-auto">
                                <li className="nav-item d-flex">
                                    <Link className="nav-link active" aria-current="page" to="/cart">
                                        <i className="fa-solid fa-cart-shopping"></i>
                                    </Link>
                                    <Link className="nav-link active" aria-current="page" to="/account">
                                        <i className="fa-solid fa-user"></i>
                                    </Link>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </header>
        </>
    )
}