import { BrowserRouter as Router, Route, Routes } from "react-router-dom"
import { NavBar } from "./components/Navbar/NavBar"
import { Home } from "./components/Home/Home"
import { Footer } from "./components/Footer/Footer"

function App() {


  return (
    <>
      <Router>
        <NavBar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} exact />
            {/* <Route path="/category/:id" element={<CategoryProducts />} />
            <Route path="category/:id/product/:id" element={<ProductDetail />} /> */}
          </Routes>
        </main>
        <Footer />
      </Router>
    </>
  )
}

export default App
