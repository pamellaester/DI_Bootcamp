import { useParams } from "react-router-dom";

const Shop = (props) => {
    const params = useParams()
    console.log(params);
    return (
        <div>
            <h2>Shop</h2>
        </div>
    )
}
export default Shop;