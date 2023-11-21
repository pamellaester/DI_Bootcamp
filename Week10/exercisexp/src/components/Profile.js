import { useParams } from "react-router-dom";

const Profile = (props) => {
    const params = useParams()
    console.log(params);
    return (
        <div>
            <h2>Profile</h2>
        </div>
    )
}

export default Profile;