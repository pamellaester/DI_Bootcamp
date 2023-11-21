import { useParams } from "react-router-dom";

const Home = (props) => {
    const params = useParams()
    console.log(params);
    return (
        <div>
            <h2>Home</h2>
        </div>
    )
}

export default Home;