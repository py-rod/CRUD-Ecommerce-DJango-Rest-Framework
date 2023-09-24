import { Header } from "./components/Header";
import { Footer } from "./components/Footer";
import { Home } from "./screens/Home";
import { ProductDetail } from "./screens/ProductDetail";
import { CategoryProducts } from "./screens/CategoryProducts";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"


function App() {
  return (
    <>
      <Router>
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<Home />} exact />
            <Route path="/category/:id" element={<CategoryProducts />} />
            <Route path="category/:id/product/:id" element={<ProductDetail />} />
          </Routes>
        </main>
        <Footer />
      </Router>
    </>
  );
}

export default App;